function checkLoginForm() {

  document.getElementById("login-message").innerHTML = "";
  var uname = document.getElementById("email").value;
  var pswd = document.getElementById("pwd").value;



  if (uname == "" || pswd == "" || uname == null || pswd == null) {
    document.getElementById("login-message").innerHTML = "Please Enter the User Login Credentials...!";
    return false;
  } else if (!validateEmail(uname)) {
    document.getElementById("login-message").innerHTML = "Invalied Email Address...!";
    return false;
  } else if (pswd.length <= 7 || pswd.length >= 17) {
    document.getElementById("login-message").innerHTML = "Password must be 8-16 characters long...!";
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
          window.location.href = "/";
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


function validateEmail(mail) {
  if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail)) {
    return true;
  }
  return false;
}

function myprofile() {
  $.ajax({
    type: "POST",
    url: "/myprofile"
  });
}


function fgpwProcess() {

  document.getElementById("fgpw-message").innerHTML = "";

  var fgemail = document.getElementById("fgemail").value;

  if (fgemail == "" || fgemail == null) {
    document.getElementById("fgpw-message").innerHTML = "Please Enter the Registerd Email...!";
    return false;
  } else if (!validateEmail(fgemail)) {
    document.getElementById("fgpw-message").innerHTML = "Invalied Email Address...!";
    return false;
  } else {
    emlData = {
      "email": fgemail
    }

    $.ajax({
      type: "POST",
      url: "/checkEmail",
      data: emlData,
      success: function (result) {
        if (result == 0) {
          document.getElementById("fgpw-message").innerHTML = "Please Enter the Registered Email...!";
        } else {

          sendpw(emlData);
        }

      }
    });

  }
}


function sendpw(emlData) {


  $.ajax({
    type: "POST",
    url: "/forgotemail",
    data: emlData,
    success: function (result) {

      if (result == '0') {
        document.getElementById("login-message").innerHTML = "Please Check Your Registered Email..!!";

      } else {
        document.getElementById("fgpw-message").innerHTML = "Please Enter the Registerd Email...!";
      }

    }
  });

}