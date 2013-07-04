$(document).ready(function() {
    // Testing code
    (function () {
        console.log("javaScript loaded");
        var $search = $("#search");

        $search.keyup(function () {
            $.ajax({
                type: 'POST',
                url: '/stories/',
                data: {
                    'search': $search.val()
                },
                success: function(data) {
                    console.log(data);
                    $("div .stuff").html(data);
                },
                error : function(data) {
                    console.log("Operation failed");
                }
            });
        });
    })();
});