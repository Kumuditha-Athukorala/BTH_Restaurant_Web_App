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

    } else if (password.length <= 8) {
        document.getElementById("register-message").innerHTML = "Password must be 8 characters long...!";
        return false;
    } else if (password != conpswd) {
        document.getElementById("register-message").innerHTML = "Passwords are not mactching...!";
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

    function registerCustomer(regiseterData) {
        alert("2222")
        $.ajax({
            type: "POST",
            url: "/registerCustomer",
            data: regiseterData
        });

    }


    function cancelRegisterForm() {
        window.location.href = "/";
    }

}