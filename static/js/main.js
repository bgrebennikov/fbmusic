

$(document).ready(function(){

    

    
    // sign up

    $('.signup_btn').click(function(){
        $('.mw-overlay').css({'display': 'block'});
        $('.signup-window').css({'display': 'block'});
        setTimeout(function(){
            $('.mw-overlay').css({'opacity': 0.5});
            $('.signup-window').css({'opacity': 1, 'top': '50vh'});
        }, 200)
    });
  

    $('.mw_submit').click(function(){
        $.ajax({
            type: "POST",
            url: "/account/signup/",
            data: {
                'username': $('.mw_username').val(),
                'email': $('.mw_email').val(),
                'password': $('.mw_password').val(),
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            },
            success: function( data, textStatus, jQxhr ){
                $('.err_messages').text("");
                $('.smw_content').hide();
                $('.success_auth_message').css({'display': 'block'});
            },
            error: function( jqXhr, textStatus, errorThrown ){
                $('.err_messages').text("Проверьте правильность введенных данных!")
            }
        })
    })

    $('.close_window_btn').click(function(){
        closeMW();
    })

    // All Modal Windows

    $(".mw-overlay").click(function(){
        closeMW();
    });

    function closeMW(){
        $(".mw").css({'top': '40vh',
                     'opacity': '0'});
        $(".mw-overlay").css({'opacity': '0'});
        setTimeout(function(){
            $(".mw").css({'display': 'none'});
            $(".mw-overlay").css({'display': 'none'});
        }, 200)
    }

})


// sign in

$('.signin_btn').click(function(){
    $.ajax({
        type: "POST",
        url: "/account/login/",
        data: {
            'username': $('.auth_login').val(),
            'password': $('.auth_password').val(),
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
        },
        success: function( data, textStatus, jQxhr ){
            if (data == "success"){
                window.location.reload();
            }
            else if (data == "wrong_data"){
                alert("Не верный логин или пароль!")
            }
        },
        error: function( jqXhr, textStatus, errorThrown ){
            console.log(errorThrown);
        }
    })
})

var track = document.querySelectorAll('.track');
var playBtn = document.querySelectorAll('.playTrack');
var player = document.querySelectorAll('.audiofile');


function playAudio(id){
    console.log(id);
    
}

function readableDuration(seconds) {
    sec = Math.floor( seconds );    
    min = Math.floor( sec / 60 );
    min = min >= 10 ? min : '0' + min;    
    sec = Math.floor( sec % 60 );
    sec = sec >= 10 ? sec : '0' + sec;    
    return min + ':' + sec;
}