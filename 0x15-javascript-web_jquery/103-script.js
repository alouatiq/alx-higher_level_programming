$(document).ready(function () {
    function fetchTranslation() {
        const langCode = $("#language_code").val();
        if (langCode) {
            $.get(`https://www.fourtonfish.com/hellosalut/?lang=${langCode}`, function (data) {
                $("#hello").text(data.hello);
            });
        }
    }

    $("#btn_translate").click(fetchTranslation);

    $("#language_code").keypress(function (event) {
        if (event.which === 13) { // ENTER key
            fetchTranslation();
        }
    });
});
