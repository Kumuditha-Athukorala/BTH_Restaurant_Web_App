function viewAllCustomers() {

    $.ajax({
        type: "POST",
        url: "/viewallcustomers",
        success: function (result) {
            console.log(result)
        }
    });


}

function viewAllBookings() {

    $.ajax({
        type: "POST",
        url: "/viewallbookings",
        success: function (result) {
            console.log(result)
        }
    });


}