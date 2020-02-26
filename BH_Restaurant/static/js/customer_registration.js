function checkCustomerRegistration() {

    document.getElementById("register-message").innerHTML = "";
    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    var gender = document.getElementById("sel1").value;
    var phone = document.getElementById("cnumber").value;
    var address = document.getElementById("address").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("pwd").value;
    var conpswd = document.getElementById("repwd").value;

    console.log(fname, lname, gender, phone, address, email,
        password, conpswd);

    if (fname == null || fname == "" || lname == null || lname == "" || gender == null || gender == "" || phone == null || phone == "" ||
        address == null || address == "" || email == null || email == "" || password == null || password == "" || conpswd == null || conpswd == "") {

        document.getElementById("register-message").innerHTML = "Please Fill All the Details...!";
        return false;

    } else if (fname.length > 25) {
        document.getElementById("register-message").innerHTML = "First name is too long...!";
        return false;
    } else if (lname.length > 25) {
        document.getElementById("register-message").innerHTML = "Last name is too long...!";
        return false;
    } else if (address.length > 250) {
        document.getElementById("register-message").innerHTML = "Address is too long...!";
        return false;
    } else if (!validatePhoneNumber(phone)) {
        document.getElementById("register-message").innerHTML = "Invalied Phone Number...!";
        return false;
    } else if (!validateEmail(email)) {
        document.getElementById("register-message").innerHTML = "Invalied Email Address...!";
        return false;
    } else if (password.length <= 7 || password.length >= 17) {
        document.getElementById("register-message").innerHTML = "Password must be 8-16 characters long...!";
        return false;
    } else if (password != conpswd) {
        document.getElementById("register-message").innerHTML = "Passwords are not matching...!";
        return false;
    } else {
        regiseterData = {
            "firstName": fname,
            "lastName": lname,
            "gender": gender,
            "phone": phone,
            "address": address,
            "email": email,
            "password": password,
            "conpassword": conpswd
        }
        // var lgdata = JSON.stringify(regiseterData);
        $.ajax({
            type: "POST",
            url: "/checkEmail",
            data: regiseterData,
            success: function (result) {
                if (result == 0) {
                    alert('before')
                    registerCustomer(regiseterData);
                } else {
                    document.getElementById("register-message").innerHTML = "Email is already existed...!";
                }

            }
        });

    }
}

function registerCustomer(regiseterData) {
    alert("2222")
    $.ajax({
        type: "POST",
        url: "/registerCustomer",
        data: regiseterData,
        success: function (result) {

            if (result == 'None') {
                alert("You Have Successfully Registerd...!!!");
                window.location.href = "/";
            }

        }
    });

}

function validatePhoneNumber(phone) {
    var phoneno = /^\+?([0-9]{2})\)?[-. ]?([0-9]{4})[-. ]?([0-9]{4})$/;
    if (phoneno.test(phone)) {
        return true;
    } else {
        return false;
    }
}

function validateEmail(mail) {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail)) {
        return true;
    }
    return false;
}

function cancelRegisterForm() {
    alert("cancle");
    window.location.href = "/";
}