const checkee = document.querySelectorAll('#checkbox_list');

for (const check of checkee) {
    check.addEventListener('change',

    function () {

        if (check.checked) {
            check.parentElement.style = "text-decoration: line-through"
        } else {
            check.parentElement.style = "text-decoration-line"
        }

    }

)
}

const button = document.querySelector('#button_add')
const item = document.querySelector('#div_test')
const dict = document.getElementById('dictionary')
const check = document.getElementById('check')
const products = document.getElementById('products')

function catchList(){
    fetch('http://127.0.0.1:8000/api/calories').then(async response => {
        return response.json();
    }).then(data => {
        products.innerHTML = data.map(product => {
            return `
            <tr>
            <td>${product.name}</td>
            <td>${product.energy}</td>
            <td>${product.fat}</td>
            <td>${product.carbohydrates}</td>
            <td>${product.fiber}</td>
            <td>${product.protein}</td>
            <td>${product.salt}</td>
            <td>${product.sugar}</td>
            </tr>
            `;
        }).join("")
    })


}

check.addEventListener('click',catchList)

button.addEventListener('click', function (e){
    let clone = item.cloneNode(true);
    document.getElementById('section_test').appendChild(clone)

})

