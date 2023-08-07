$("#newsletter-form").submit(function (e) {
    let loader_divs = document.querySelector('.spin-loader-newsletter');
        for(let i = 0; i < loader_divs.length; i++){
            loader_divs[i].style.display= "inline-block"
        }
        loader_divs.style.display = "flex"
    e.preventDefault();
    var serializedData = $(this).serialize();
    var getAlert = document.querySelector('.alert-control-newsletter');
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/post/ajax/newsletter',
        data: serializedData,
        success: function (response) {
            $(loader_divs).fadeOut()
            $("#newsletter-form").trigger('reset');
            getAlert.setAttribute('class' , 'alert alert-success mt-4')
            getAlert.setAttribute('id' , 'success')
            getAlert.innerText = 'Thanks For Subscribe Us'
        },
        error: function (response) {
            $(loader_divs).fadeOut()
            getAlert.setAttribute('class' , 'alert alert-danger mt-4')
            getAlert.setAttribute('id' , 'error')
            getAlert.innerText = 'There is accured any error'
        }
    })
})

$("#newsletter-form-detail").submit(function (e) {
    let loader_divs = document.querySelector('.spin-loader-newsletter-detail');
        for(let i = 0; i < loader_divs.length; i++){
            loader_divs[i].style.display= "inline-block"
        }
        loader_divs.style.display = "flex"
    e.preventDefault();
    var serializedData = $(this).serialize();
    var getAlert = document.querySelector('.alert-control-newsletter-detail');
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/post/ajax/newsletter',
        data: serializedData,
        success: function (response) {
            $(loader_divs).fadeOut()
            $("#newsletter-form").trigger('reset');
            getAlert.setAttribute('class' , 'alert alert-success mt-4')
            getAlert.setAttribute('id' , 'success')
            getAlert.innerText = 'Thanks For Subscribe Us'
        },
        error: function (response) {
            $(loader_divs).fadeOut()
            getAlert.setAttribute('class' , 'alert alert-danger mt-4')
            getAlert.setAttribute('id' , 'error')
            getAlert.innerText = 'There is accured any error'
        }
    })
})

$("#contact-form").submit(function (e) {
    let loader_divs = document.querySelector('.spin-loader-contact');
    for(let i = 0; i < loader_divs.length; i++){
        loader_divs[i].style.display= "inline-block"
    }
    loader_divs.style.display = "flex"
    e.preventDefault();
    var serializedData = $(this).serialize();
    var getAlert = document.querySelector('.alert-control-contact');
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/post/ajax/message',
        data: serializedData,
        success: function (response) {
           $(loader_divs).fadeOut()
            $("#contact-form").trigger('reset');
            getAlert.setAttribute('class' , 'alert alert-success w-100 text-center')
            getAlert.setAttribute('id' , 'success')
            getAlert.innerText = 'Thanks For Message , We Will Contact With You !'
            getAlert.fadeIn()
        },
        error: function (response) {
           $(loader_divs).fadeOut()
           getAlert.setAttribute('class' , 'alert alert-danger w-100 text-center')
           getAlert.setAttribute('id' , 'error')
           getAlert.innerText = 'There is accured any error'
           getAlert.fadeIn()
        }
    })
})