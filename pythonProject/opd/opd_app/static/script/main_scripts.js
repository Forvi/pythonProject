    const headerEl = document.getElementById("header")
    const logo = document.getElementById("logo");
    const paths = logo.querySelectorAll("path");

    window.addEventListener("scroll", function () {
        const scrollPos = window.scrollY

        if (scrollPos > 80) {
            headerEl.classList.add("header_effects");
            paths.forEach(path => {
                path.style.fill = "black";
            });
        } else {
            headerEl.classList.remove("header_effects")
            paths.forEach(path => {
                path.style.fill = "white";
            });
        }
    })

function longText() {
    let textElements = document.getElementsByClassName("cardName_text");
    for (let textElement of textElements) {
        let text = textElement.innerText;
        if (text.length > 12) {
            let cutText = text.substring(0, 12) + "...";
            textElement.innerText = cutText;
        }
    }
}
longText();

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

menu__navigate.addEventListener('click' () => {
    if(list.classList.contains('disp') == true) {
        list.classList.remove('disp');
    } else {
        list.classList.add('disp');
    }
});
