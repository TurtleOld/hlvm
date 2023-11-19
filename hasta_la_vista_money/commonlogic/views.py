from django.contrib import messages
from django.db.models import Count, QuerySet, Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from hasta_la_vista_money.account.models import Account
from hasta_la_vista_money.users.models import User


def build_category_tree(categories, parent_id=None, depth=2, current_depth=1):
    """Формирование дерева категория для отображения на сайте."""
    tree = []
    for category in categories:
        if category['parent_category'] == parent_id:
            children = []
            if current_depth < depth:
                children = build_category_tree(
                    categories,
                    category['id'],
                    depth,
                    current_depth + 1,
                )
            category_copy = category.copy()
            if children:
                category_copy['children'] = children
            tree.append(category_copy)
    return tree


def collect_info_receipt(user: User) -> QuerySet:
    """
    Сбор информации о чеках для отображения на страницах сайта.

    :param user: User
    :return: QuerySet
    """
    return (
        user.receipt_users.annotate(
            month=TruncMonth('receipt_date'),
        )
        .values(
            'month',
            'account__name_account',
        )
        .annotate(
            count=Count('id'),
            total_amount=Sum('total_sum'),
        )
        .order_by('-month')
    )


class IncomeExpenseCreateViewMixin(CreateView):
    depth_limit = None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['depth'] = self.depth_limit
        return kwargs


def create_object_view(form, model, request, message) -> dict[str, bool]:
    """
    Создание объектов для внесения данных по платежам кредита, расхода и дохода.

    :param form:
    :param model:
    :param request:
    :param message:
    :return: JsonResponse
    """
    form_instance = form.save(commit=False)
    cd = form.cleaned_data
    amount = cd.get('amount')
    account = cd.get('account')
    category = cd.get('category')

    selected_account = get_object_or_404(Account, id=account.id)
    selected_category = get_object_or_404(model, name=category)

    if selected_account.user == request.user:
        change_account_balance(account, request, amount)
        form_instance.user = request.user
        form_instance.category = selected_category

        form_instance.save()
        messages.success(
            request,
            message,
        )
        return {'success': True}
    return {'success': False, 'errors': form.errors}


def change_account_balance(account, request, amount):
    """Изменение баланса счёта."""
    if 'income' in request.path:
        account.balance += amount
    else:
        account.balance -= amount
    account.save()
