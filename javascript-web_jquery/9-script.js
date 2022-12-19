$(function ($) {
  const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
  const lang = $('html')[0].lang;
  const newUrl = url.replace(url.slice(38), 'lang=' + lang);
  $.get(newUrl, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
});
