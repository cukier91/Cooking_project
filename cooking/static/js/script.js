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

button.addEventListener('click', function (e){
    let clone = item.cloneNode(true);
    document.getElementById('section_test').appendChild(clone)

})

const productsArray = []
function catchList(){

    const quantityProduct = document.querySelectorAll('#selector')
    quantityProduct.forEach(element =>{
        productsArray.push(element.value)
        console.log(productsArray)
    })
    fetch('http://127.0.0.1:8000/api/calories').then(async response => {
        return response.json();
    }).then(data => {
        products.innerHTML = data.map(product => {
                return `
                <tr>
                <td class="product_name">${product.name}</td>
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
        const pass = document.querySelectorAll("td.product_name")
    pass.forEach(element =>{
      if(productsArray.includes(`${element.innerHTML}`) !== true ){
          element.parentElement.hidden = true
      }
    })

    })


}
check.addEventListener('click',catchList)





