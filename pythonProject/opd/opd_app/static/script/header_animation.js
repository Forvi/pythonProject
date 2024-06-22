const headerEl = document.getElementById("header")
const logo = document.getElementById("logo");
const paths = logo.querySelectorAll("path");

window.addEventListener("scroll", function () {
    const scrollPos = window.scrollY

    if (scrollPos > 80) {
        headerEl.classList.add("header_effects");
        paths.forEach(path => {
            path.style.fill = "#222222";
        });
    } else {
        headerEl.classList.remove("header_effects")
        paths.forEach(path => {
            path.style.fill = "white";
        });
    }
})