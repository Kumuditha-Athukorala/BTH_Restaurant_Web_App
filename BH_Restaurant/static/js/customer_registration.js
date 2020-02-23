function checkCustomerRegistration() {

    alert("customer");
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
            "confirmpassword": conpswd,
        }
        // var lgdata = JSON.stringify(regiseterData);
        $.ajax({
            type: "POST",
            url: "/register",
            data: regiseterData,
            success: function (result) {

            }
        });

    }

}