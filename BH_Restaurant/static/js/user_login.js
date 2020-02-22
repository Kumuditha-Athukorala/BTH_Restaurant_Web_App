function checkLoginForm() {

  document.getElementById("login-message").innerHTML = "";
  var uname = document.getElementById("email").value;
  var pswd = document.getElementById("pwd").value;



  if (uname == "" || pswd == "" || uname == null || pswd == null) {
    alert("if");
    document.getElementById("login-message").innerHTML = "Please Enter the User Login Credentials...!";
    return false;
  } else {

    loginData = {
      "username": uname,
      "password": pswd
    }
    var lgdata = JSON.stringify(loginData);
    $.ajax({
      type: "POST",
      url: "/checklogin",
      data: loginData,
      success: function (result) {
        if (result == 1) {
          window.location.href = '/';
        } else {

          document.getElementById("login-message").innerHTML = "Invalied Login Credentials...!";
        }

      }
    });

  }
}