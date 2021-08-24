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

const productsDict = {}
function catchList(){

    const quantityProduct = document.querySelectorAll('#selector')
    quantityProduct.forEach(element =>{
        productsDict[`${element.value}`] = element.parentElement.children[1].value
        console.log(productsDict)
    })
    fetch('http://127.0.0.1:8000/api/calories').then(async response => {
        return response.json();
    }).then(data => {
        products.innerHTML = data.map(product => {
                if(`${product.name}` in productsDict){
                    let productWeight = parseFloat(productsDict[product.name])/100
                    return `
                    <tr>
                    <td class="product_name">${product.name}</td>
                    <td>${(product.energy * productWeight).toFixed(2) }</td>
                    <td>${(product.fat * productWeight.toFixed(2))}</td>
                    <td>${(product.carbohydrates * productWeight).toFixed(2)}</td>
                    <td>${(product.fiber * productWeight).toFixed(2)}</td>
                    <td>${(product.protein * productWeight).toFixed(2)}</td>
                    <td>${(product.salt * productWeight).toFixed(2)}</td>
                    <td>${(product.sugar * productWeight).toFixed(2)}</td>
                    </tr>
                `;}
            }).join("")
        const pass = document.querySelectorAll("td.product_name")
    pass.forEach(element =>{
      if(!(`${element.innerHTML}` in productsDict) ){
          element.parentElement.hidden = true
      }
    })

    })


}
check.addEventListener('click',catchList)





