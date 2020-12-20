let slides = document.querySelectorAll('.slides .li-item')
let currentSlide = 0;
let slideInterval = setInterval(nextSlide, 5000)


function nextSlide () {
    slides[currentSlide].className = 'li-item'
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].className = 'li-item show'
}