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


function checkCustomerUpdates() {
    alert("update");

    document.getElementById("update-message").innerHTML = "";
    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    var gender = document.getElementById("sel1").value;
    var phone = document.getElementById("cnumber").value;
    var address = document.getElementById("address").value;


    console.log(fname, lname, gender, phone, address);

    if (fname == null || fname == "" || lname == null || lname == "" || gender == null || gender == "" || phone == null || phone == "" ||
        address == null || address == "") {

        document.getElementById("update-message").innerHTML = "Please Fill All the Details...!";
        return false;

    } else if (fname.length > 25) {
        document.getElementById("update-message").innerHTML = "First name is too long...!";
        return false;
    } else if (lname.length > 25) {
        document.getElementById("update-message").innerHTML = "Last name is too long...!";
        return false;
    } else if (address.length > 250) {
        document.getElementById("update-message").innerHTML = "Address is too long...!";
        return false;
    } else if (!validateNewPhoneNumber(phone)) {
        document.getElementById("update-message").innerHTML = "Invalied Phone Number...!";
        return false;
    } else {
        updateData = {
            "firstName": fname,
            "lastName": lname,
            "gender": gender,
            "phone": phone,
            "address": address,

        }

        $.ajax({
            type: "POST",
            url: "/updateCustomer",
            data: updateData,
            success: function (result) {
                if (result == 'None') {
                    alert("Your Details Updated Successfully...!!!");
                    window.location.href = "/";
                } else {
                    document.getElementById("update-message").innerHTML = "Something Went Wrong...!";
                }

            }
        });

    }
}



function validateNewPhoneNumber(phone) {
    var phoneno = /^\+?([0-9]{2})\)?[-. ]?([0-9]{4})[-. ]?([0-9]{4})$/;
    if (phoneno.test(phone)) {
        return true;
    } else {
        return false;
    }
}


function cancelUpdateForm() {
    alert("cancle");
    window.location.href = "/";
}


function changePassword() {

    alert("change pw");

    document.getElementById("change-pw-message").innerHTML = "";
    var email = document.getElementById("email").value;
    var password = document.getElementById("pwd").value;
    var conpswd = document.getElementById("repwd").value;



    if (email == "" || password == "" || email == null || password == null) {
        document.getElementById("change-pw-message").innerHTML = "Please Enter the New User Login Credentials...!";
        return false;
    } else if (password.length <= 7 || password.length >= 17) {
        document.getElementById("change-pw-message").innerHTML = "Password must be 8-16 characters long...!";
        return false;
    } else if (password != conpswd) {
        document.getElementById("change-pw-message").innerHTML = "Passwords are not matching...!";
        return false;
    } else {

        newLoginData = {
            "username": email,
            "password": password
        }

        $.ajax({
            type: "POST",
            url: "/changePassword",
            data: newLoginData,
            success: function (result) {
                if (result == 1) {

                    window.location.href = "/";
                } else {
                    document.getElementById("change-pw-message").innerHTML = "Login credentials Changing is Invalied";
                }

            }
        });
    }

}

function cancelChangePassword() {
    alert("cancle");
    window.location.href = "/";
}


function addNewCategory() {
    alert("cat");

    document.getElementById("cat-message").innerHTML = "";
    var category = document.getElementById("category").value;


    if (category == "" || category == null) {
        document.getElementById("cat-message").innerHTML = "Please Enter the New Food Category ...!";
        return false;
    } else if (password.length <= 46) {
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
                if (result == 1) {

                    window.location.href = "/";
                } else {
                    document.getElementById("change-pw-message").innerHTML = "Category Adding Cancelled..!";
                }

            }
        });
    }



}

function cancelCat() {

}