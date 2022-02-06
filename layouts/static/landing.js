let header = document.getElementById('header')
let scrollBefore = 0
window.addEventListener("scroll", (event) => {
    let scroll = this.scrollY;
    console.log(scroll)
    if (scroll == 0 || scrollBefore == 0){
        header.classList.toggle('on-top')
    }
    scrollBefore = scroll
});