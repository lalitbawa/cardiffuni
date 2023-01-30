// Mobile navbar toggle

const toggle_button = document.getElementById("toggle-button")
const nav_link = document.getElementsByClassName("navbar-links1")[0]

toggle_button.addEventListener('click',()=>{
    nav_link.classList.toggle('active')
})