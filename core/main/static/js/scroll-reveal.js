var slideUp = {
    distance: '150%',
    origin: 'bottom',
    opacity: null
};
var slideLeft = {
    distance: '100%',
    origin: 'left',
    opacity: null,
};
var slideBottom = {
    distance: '100%',
    origin: 'bottom',
    opacity: null,
};
ScrollReveal().reveal('.event__slider', slideBottom);
ScrollReveal().reveal('.about', slideBottom , { delay: 250 });
ScrollReveal().reveal('.services', slideBottom , { delay: 250 });
ScrollReveal().reveal('.youtube', slideBottom , { delay: 250 });
ScrollReveal().reveal('.tours', slideBottom , { delay: 250 });
ScrollReveal().reveal('.blog', slideBottom , { delay: 250 });
ScrollReveal().reveal('.discography', slideBottom , { delay: 250 });
ScrollReveal().reveal('.contact', slideUp , { delay: 250 });
ScrollReveal().reveal('.skills', slideLeft , { delay: 250 });