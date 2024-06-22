addfavorite = async (pk) => {
    event.stopPropagation();
    const res = await fetch(`/add_fav/${pk}`).then(res => res.json());
    location.reload();
}

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
                console.log(errorThrown)
            }
        });
    });
});

const profile = document.getElementById('header');
const list = document.getElementById('menu__navigate');

list.addEventListener('click', () => {
    if (list.classList.contains('disp')) {
        list.classList.remove('disp');
    } else {
        list.classList.add('disp');
    }
});