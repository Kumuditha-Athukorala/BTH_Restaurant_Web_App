$(document).ready(function () {


  $("div.blog-post").hover(
    function () {
      $(this).find("div.content-hide").slideToggle("fast");
    },
    function () {
      $(this).find("div.content-hide").slideToggle("fast");
    }
  );

  $('.flexslider').flexslider({
    prevText: '',
    nextText: ''
  });

  $('.testimonails-slider').flexslider({
    animation: 'slide',
    slideshowSpeed: 5000,
    prevText: '',
    nextText: '',
    controlNav: false
  });

  $(function () {

    // Instantiate MixItUp:

    $('#Container').mixItUp();



    $(document).ready(function () {
      $(".fancybox").fancybox();
    });

  });


});


function scrollToElement(selector, callback) {

  var animation = {
    scrollTop: $(selector).offset().top
  };
  $('html,body').animate(animation, 'slow', 'swing', function () {
    if (typeof callback == 'function') {
      callback();
    }
    callback = null;
  });
}


function preventBack() {
  window.history.forward();
}
setTimeout("preventBack()", 0);
window.onunload = function () {
  null
};