function checkLoginForm() {

    document.getElementById("login-message").innerHTML = "";
    var uname = document.getElementById("email").value;
    var pswd = document.getElementById("pwd").value;



    if (uname == "" || pswd == "" || uname == null || pswd == null) {
        alert("if");
        document.getElementById("login-message").innerHTML = "Please Enter the User Login Credentials...!";
        return false;
    } else {
        alert("done");
    }
}