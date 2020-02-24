function checkLoginForm() {

  document.getElementById("login-message").innerHTML = "";
  var uname = document.getElementById("email").value;
  var pswd = document.getElementById("pwd").value;



  if (uname == "" || pswd == "" || uname == null || pswd == null) {
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
          // myprofile();
          window.location.href = "/profile";
        } else {
          document.getElementById("login-message").innerHTML = "Invalied Login Credentials...!";
        }

      }
    });
  }
}

function cancelLoginForm() {
  window.location.href = "/";
}

function myprofile() {
  $.ajax({
    type: "POST",
    url: "/myprofile"
  });
}