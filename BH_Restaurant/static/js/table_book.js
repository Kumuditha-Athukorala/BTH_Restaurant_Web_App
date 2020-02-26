function checkTableBookingForm() {

    alert("booking");

    document.getElementById("booking-message").innerHTML = "";

    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    var phone = document.getElementById("cnumber").value;
    var email = document.getElementById("email").value;
    var adult = document.getElementById("adult").value;
    var children = document.getElementById("children").value;
    var book_date = document.getElementById("book_date").value;
    var book_time = document.getElementById("time").value;
    var comment = document.getElementById("comment").value;

    console.log(fname, lname, phone, email, adult, children, book_date, book_time, comment);
    console.log(book_date);

    if (fname == null || fname == "" || lname == null || lname == "" || phone == null || phone == "" ||
        email == null || email == "" || adult == null || adult == "" || children == null || children == "" ||
        book_date == null || book_date == "" || book_time == null || book_time == "" || comment == null || comment == "") {

        document.getElementById("booking-message").innerHTML = "Please Fill All the Details...!";
        return false;
    } else if (fname.length > 25) {
        document.getElementById("booking-message").innerHTML = "First name is too long...!";
        return false;
    } else if (lname.length > 25) {
        document.getElementById("booking-message").innerHTML = "Last name is too long...!";
        return false;
    } else if (!validatePhoneNumber(phone)) {
        document.getElementById("booking-message").innerHTML = "Invalied Phone Number...!";
        return false;
    } else if (!validateEmail(email)) {
        document.getElementById("booking-message").innerHTML = "Invalied Email Address...!";
        return false;
    } else if (adult < 0 || adult > 20) {
        document.getElementById("booking-message").innerHTML = "Adults head count must be in between 0-20 ...!";
        return false;
    } else if (children < 0 || children > 20) {
        document.getElementById("booking-message").innerHTML = "Chidren head Count must be in between 0-20 ...!";
        return false;
    } else if (!checkDate(book_date)) {

        document.getElementById("booking-message").innerHTML = "Selected Date is invalied...!";
        return false;

    } else if (!checkBookingTime(book_time)) {

        document.getElementById("booking-message").innerHTML = "Please Select a proper booking date-time slot...!";
        return false;
    } else {
        //Ajax call here.
    }

}

function checkDate(bookdate) {

    var selectedDate = new Date(bookdate);
    var today = new Date();
    today.setHours(0, 0, 0, 0);
    if (selectedDate >= today) {
        return true;
    } else {
        return false;
    }
}

function checkBookingTime(time) {
    var today = new Date();
    var current_hour = today.getHours();
    var current_hour_12 = current_hour - 12;

    var booking_date = document.getElementById("book_date").value;
    var selected_date = new Date(booking_date);
    today.setHours(0, 0, 0, 0);

    if (selected_date < today) {
        alert("one");
        return false;
    } else if (selected_date > today) {
        alert("two");
        return true;
    } else {
        alert("sameeeee");
        if (time == current_hour_12 || time < current_hour_12) {
            alert("timeeeee");
            return false;
        } else {
            return true;
        }
    }

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


function cancelBooking() {
    alert("cancle");
    window.location.href = "/";
}