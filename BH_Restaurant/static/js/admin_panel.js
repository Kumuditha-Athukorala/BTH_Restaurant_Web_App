function viewAllCustomers() {

    alert("viewAllCustomers");

    $.ajax({
        type: "POST",
        url: "/viewallcustomers",
        success: function (result) {
            console.log(result)
        }
    });


}