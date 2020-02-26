function viewAllCustomers() {

    alert("viewAllCustomers");

    $.ajax({
        type: "POST",
        url: "/viewallcustomers",
        success: function (result) {
            if (result == 1) {
                alert('fine')

            }

        }
    });


}