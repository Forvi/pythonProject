$(document).ready(function () {
    $("#createpath").click(function () {
        $.ajax({
            type: "POST",
            url: "/check_user/",
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function (response) {
                if (response.is_authenticated) {
                    window.location.href = "/redactor";
                } else {
                    let errorMessageParagraph = document.getElementById("error-message");
                    errorMessageParagraph.textContent = response.error_message;
                }
            },
            error: function (xhr, textStatus, errorThrown) {
                // позже сделать обработчик ошибок
            }
        });
    });
});