$(function ($) {
  $('DIV#add_item').on('click', function (event) {
    $('UL.my_list').append($('<li></li>').text('item'));
  });
  $('DIV#remove_item').on('click', function (event) {
    $('UL.my_list :last-child').remove();
  });
  $('DIV#clear_list').on('click', function (event) {
    $('UL.my_list').empty();
  });
});
