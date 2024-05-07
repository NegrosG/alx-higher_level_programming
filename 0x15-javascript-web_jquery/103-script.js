$(document).ready(function () {
  function getTranslation() {
    const language = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/?lang=${language}`;
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(getTranslation);

  $('#language_code').keypress(function (e) {
    if (e.which == 13) { // Enter key pressed
      getTranslation();
    }
  });
});
