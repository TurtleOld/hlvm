let productForm = document.querySelectorAll(".form-product")
let container = document.querySelector("#form-create-receipt")
let addButton = document.querySelector("#add-form")
let removeButton = document.querySelector("#remove-form")
let totalForms = document.querySelector("#id_form-TOTAL_FORMS")

document.addEventListener('DOMContentLoaded', function() {
    onClickRemoveObject();
    exchangeAccountShow();
});

let formNum = productForm.length-1
addButton.addEventListener('click', addForm)
removeButton.addEventListener('click', removeForm)

function addForm(e) {
    e.preventDefault()

    let newForm = productForm[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
    container.insertBefore(newForm, addButton)

    totalForms.setAttribute('value', `${formNum+1}`)
    newForm.querySelector('.price').addEventListener('input', amountUpdate);
    newForm.querySelector('.quantity').addEventListener('input', amountUpdate);
}

function removeForm(e) {
    e.preventDefault()

    productForm = document.querySelectorAll(".form-product")
    let lastForm = productForm[productForm.length - 1]

    let formRegex = RegExp(`form-(\\d){1}-`,'g')
    lastForm.innerHTML = lastForm.innerHTML.replace(formRegex, `form-${productForm.length - 1}-`);

    if (productForm.length > 1) {
        lastForm.remove();
    }

    totalForms.setAttribute('value', `${productForm.length}`)

}


function toggleNewSellerField() {

    const existingSeller = document.getElementById('id_existing_seller');
    const newSeller = document.getElementById('form-create-receipt').getElementsByClassName('row')[1];
    const addNewSellerBtn = document.getElementById('add-new-seller-btn');
    const addNewSellerCheckBox = document.getElementById('id_add_new_seller');

    if (existingSeller.value === 'other') {
        newSeller.style.display = 'flex';
        addNewSellerBtn.style.display = 'block';
        addNewSellerCheckBox.checked = true;
    } else {
        newSeller.style.display = 'none';
        addNewSellerBtn.style.display = 'none'
        addNewSellerCheckBox.checked = false;
    }
}

$(document).ready(function() {
  toggleNewSellerField();
  $('#id_existing_seller').on('change', function() {
    toggleNewSellerField();
  });
});


function amountUpdate() {
    let formInputs = container.querySelectorAll('.form-product');
    formInputs.forEach( formInput => {
        let priceInput = formInput.querySelector('.price');
        let quantityInput = formInput.querySelector('.quantity');
        let amountInput = formInput.querySelector('.amount');
        if (priceInput && quantityInput && amountInput) {
            let price = parseFloat(priceInput.value);
            let quantity = parseFloat(quantityInput.value);
            let amount = price * quantity;
            amountInput.value = amount.toFixed(2);
        }
    });
}

productForm.forEach(form => {
    form.querySelector('.price').addEventListener('input', amountUpdate);
    form.querySelector('.quantity').addEventListener('input', amountUpdate);
});


function totalSum() {
    let total_sum = 0;
    let formInputs = container.querySelectorAll('.form-product');  
    let totalSumInput = document.querySelector('.total-sum');
    formInputs.forEach(formInput => {  
        let amountInputs = formInput.querySelectorAll('.amount');
        amountInputs.forEach(amountInput => { 
            if (amountInput) {  
                total_sum += parseFloat(amountInput.value);
            }  
        }); 
    });  
    totalSumInput.value = total_sum.toFixed(2);
} 

container.addEventListener('click', function(event) {
  if (event.target.matches('.amount[readonly]') || event.target.matches('.total-sum[readonly]')) {
    totalSum();
  }
});

const addNewSellerBtn = document.getElementById('add-new-seller-btn');
addNewSellerBtn.addEventListener('click', () => {
    const existingSellerField = document.querySelector('#id_existing_seller');
    existingSellerField.value = '--';
    existingSellerField.disabled = true;

    const newSellerField = document.querySelector('#id_new_seller');
    newSellerField.required = true;
    newSellerField.disabled = false;

    addNewSellerBtn.style.display = 'none';
});

const formCheck = document.querySelector('.form-check');
formCheck.closest('.row').style.display = 'none';


function exchangeAccountShow() {
    const exchangeAccountElement = document.getElementById('exchange-account');
    const bodyElement = document.body;

    if (exchangeAccountElement.classList.contains('show')) {
        exchangeAccountElement.style.display = 'block';
        exchangeAccountElement.ariaModal = 'true'
        exchangeAccountElement.role = 'dialog'
        bodyElement.classList.add('modal-open')
        bodyElement.style.overflow = 'hidden';
        bodyElement.style.paddingRight = '0';
    }

    document.addEventListener('click', function(event) {
        if (event.target.matches('[data-bs-dismiss="modal"]')) {
            exchangeAccountElement.style.display = 'none';
            exchangeAccountElement.setAttribute('aria-modal', 'false');
            bodyElement.classList.remove('modal-open');
            bodyElement.style.overflow = 'auto';
            bodyElement.style.paddingRight = '0';
        }
    });
}

function onClickRemoveObject() {
    const removeObjectButton = document.querySelectorAll('.remove-object-button')
    removeObjectButton.forEach((button) => {
        button.addEventListener('click', (event) => {
            const confirmed_button_category = confirm('Вы уверены?')
            if (!confirmed_button_category) {
                event.preventDefault()
            }
        });
    });
}

window.setTimeout(function() {
    $(".alert").fadeTo(400, 0).slideUp(400, function(){
        $(this).remove();
    });
}, 4000);
