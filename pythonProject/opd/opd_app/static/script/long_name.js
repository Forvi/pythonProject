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