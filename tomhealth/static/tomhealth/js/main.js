const showMenu = (toggleBtn, navBar) =>{

    const toggle = document.getElementById(toggleBtn),
    nav = document.getElementById(navBar)

    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show-menu')
        })
    }
}
showMenu('m-toggle','nav-menu')


const navLink = document.querySelectorAll('.list-item')

const linkAction = () => {
    const menu = document.querySelector('#nav-menu')

    menu.classList.remove('show-menu')
}

navLink.forEach(n => n.addEventListener('click',linkAction));


const scrollHeader = () => {
    const headerNav = document.querySelector('header')

    if (this.scrollY >= 200 ) 
        headerNav.classList.add('scroll-header'); else headerNav.classList.remove('scroll-header');
}
window.addEventListener('scroll', scrollHeader)


const scrollTop = () => {
    const scroll_top = document.getElementById('scroll-top')

    if (this.scrollY >= 200 ) 
    scroll_top.classList.add('scroll-top'); else scroll_top.classList.remove('scroll-top');
}
window.addEventListener('scroll', scrollTop)
