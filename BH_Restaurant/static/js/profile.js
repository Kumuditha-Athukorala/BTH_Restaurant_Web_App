$(document).ready(function () {

    console.log("my bookings");

    $.ajax({
        type: "POST",
        url: "/mybookings",
        success: function (result) {
            console.log(result);

        }
    });
});