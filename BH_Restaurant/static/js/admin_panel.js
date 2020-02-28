$(document).ready(function () {

    $.ajax({
        type: "POST",
        url: "/viewallcustomers",
        success: function (result) {
            console.log(result)
        }
    });

    $(document).ready(function () {
        $.ajax({
            type: "POST",
            url: "/viewallbookings",
            success: function (result) {
                console.log(result)
            }
        });
    });



});

function changeCustomerStatus(id) {
    alert(id);
    userData = {
        "userId": id
    }

    $.ajax({
        type: "POST",
        url: "/changecustomerstatus",
        data: userData,
        success: function (result) {
            console.log(result);
            allCustomers();
            window.location.reload();
        }
    });
}


function allCustomers() {

    $.ajax({
        type: "POST",
        url: "/viewallcustomers",
        success: function (result) {
            console.log(result)
        }
    });
}