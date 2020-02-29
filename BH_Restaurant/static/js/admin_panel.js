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

function processOrder(purpose, orderId) {

    alert("cancel or Process");
    alert(purpose, orderId);

    var customerName = document.getElementById("cusName").innerHTML;
    var orderDate = document.getElementById("orderDate").innerHTML;
    var orderTime = document.getElementById("orderTime").innerHTML;
    var headCount = document.getElementById("headCount").innerHTML;
    var orderEmail = document.getElementById("orderEmail").innerHTML;

    console.log(customerName, orderDate, orderTime, headCount, orderEmail);
    orderData = {
        "o_purpose": purpose,
        "O_id": orderId,
        "o_name": customerName,
        "o_date": orderDate,
        "o_time": orderTime,
        "o_count": headCount,
        "o_email": orderEmail
    }

    $.ajax({
        type: "POST",
        url: "/cancel_or_process_order",
        data: orderData,
        success: function (result) {
            console.log(result);
            // window.location.reload();
        }
    });

}