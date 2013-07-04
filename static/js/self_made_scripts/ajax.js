$(document).ready(function() {

    // Getting cookie function
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = $.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

    // Getting the CSRF cookie
    var csrftoken = getCookie('csrftoken');

    function ajaxCall() {
        $.ajax({
            type: 'POST',
            url: '/stories/ajax/',
            data: {'value_to_be_taken': 10},
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(data) {
                $(".stuff-goes-here").append(data)
            }
        });
    }

    (function () {
        $(".click-here").click(function (event) {
            ajaxCall();
            console.log(event);
        });
    }());

});

