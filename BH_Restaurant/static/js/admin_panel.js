$(document).ready(function () {

    console.log("view all customers")

    $.ajax({
        type: "POST",
        url: "/viewallcustomers",
        success: function (result) {
            console.log(result)
        }
    });

    $(document).ready(function () {
        console.log("view all bookings")
        $.ajax({
            type: "POST",
            url: "/viewallbookings",
            success: function (result) {
                console.log(result)
            }
        });
    });

    $(document).ready(function () {
        console.log("view all categories")
        $.ajax({
            type: "POST",
            url: "/allCategories",
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
            window.location.reload();
        }
    });
}


function processOrder(purpose, orderId) {


    alert("cancel or Process");
    alert(purpose);
    alert(orderId);

    var customerName = document.getElementById("cusName").innerHTML;
    var orderDate = document.getElementById("orderDate").innerHTML;
    var orderTime = document.getElementById("orderTime").innerHTML;
    var headCount = document.getElementById("headCount").innerHTML;
    var orderEmail = document.getElementById("orderEmail").innerHTML;

    console.log(customerName, orderDate, orderTime, headCount, orderEmail);
    orderData = {
        "o_purpose": purpose,
        "o_id": orderId,
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

            window.location.reload();
        }
    });

}



function addNewCategory() {
    alert("cat");

    document.getElementById("cat-message").innerHTML = "";
    var category = document.getElementById("category").value;


    if (category == "" || category == null) {
        document.getElementById("cat-message").innerHTML = "Please Enter the New Food Category ...!";
        return false;
    } else if (category.length >= 46) {
        document.getElementById("cat-message").innerHTML = "Category Name is too long...!";
        return false;
    } else {

        catData = {
            "catName": category
        }

        $.ajax({
            type: "POST",
            url: "/addNewCategory",
            data: catData,
            success: function (result) {
                if (result == 'None') {

                    window.location.href = "/";
                } else {
                    document.getElementById("change-pw-message").innerHTML = "Category Adding Cancelled..!";
                }

            }
        });
    }



}

function cancelCat() {
    alert("cancle");
    window.location.href = "/";

}




function cancelMenuItem() {
    alert("cancle");
    window.location.href = "/";
}