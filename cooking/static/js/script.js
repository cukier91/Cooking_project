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

data = fetch('http://127.0.0.1:8000/api/calories/')
  .then(response => response.json())
  .then(data => data);



button.addEventListener('click', function (e){
    let clone = item.cloneNode(true);
    document.getElementById('section_test').appendChild(clone)

})

check.addEventListener('click', function (e){
    console.log(data)
})