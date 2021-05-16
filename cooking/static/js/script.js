
const checkee = document.querySelectorAll('input');
const lab = document.querySelectorAll('label')

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

