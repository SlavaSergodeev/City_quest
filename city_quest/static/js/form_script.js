function check_quest() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url: "check_quest/", // the endpoint
        type: "POST", // http method
        data: {the_post: $('#id_result').val()}, // data sent with the post request

        // handle a successful response
        success: function (json) {
            $('#id_result').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            if ('result' in json) {
                window.location.assign(json['result']);
            }
            else {
                $('#errors').text('Неправильный ответ');
                $('#errors').show();
                setTimeout(function () {
                    $('#errors').fadeOut('fast')
                }, 3000);
            }
        }
        //
        // // handle a non-successful response
        // error : function(xhr,errmsg,err) {
        //     $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
        //         " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        //     console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        // }
    });
}

$('#post-form').on('submit', function (event) {
    event.preventDefault();
    console.log("form submitted!");  // sanity check
    check_quest();
});

$(document).ready(function () {
    $("#myModalBox").modal('show');
});
function scr() {
    event.preventDefault();
    console.log("create post is working!")
    $('#modal-1').modal();}

function input() {
    console.log("create post is working!")

    $.ajax({
        url: "/custom_auth/login/", // the endpoint
        type: "POST", // http method
        data: {username: $('#username').val(), password: $('#password').val()},
        // data sent with the post request


        success: function (json) {
            console.log("create post is working!");
            event.preventDefault();
            console.log("Yes");
            // $('#username').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            if ('username' in json) {
                console.log("succsafdfgdhgfhess");
                // another sanity check
                window.location.assign(json['user'])

                // $("modal-1").modal   .hide()
                // window.location.assign();
            }
            event.href('/');
        },
        error:function (data) {
            debugger;
            console.log("create post is working!")
        }
            // else {
            //     $('#username').text('Неправильный ответ');
            //     $('#username').show();
            //     setTimeout(function () {
            //         $('#username').fadeOut('fast')
            //     }, 3000);
            // }

    })
}