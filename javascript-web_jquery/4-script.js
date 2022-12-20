$(function ($) {
  $('DIV#toggle_header').on('click', function (event) {
      $('header').toggleClass('green').addClass('red');
  });
});
/*$(function ($) {
  $('DIV#toggle_header').on('click', function (event) {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green').addClass('red');
    } else {
      $('header').removeClass('red').addClass('green');
    }
  });
});*/
