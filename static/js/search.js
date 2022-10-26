function searchFunction() {
    var input, filter, cards, cardContainer, h5, title, i;
    input = document.getElementById("searchBox");
    filter = input.value.toUpperCase();
    cardContainer = document.getElementById("keywords");
    cards = cardContainer.getElementsByClassName("card");
    for (i = 0; i < cards.length; i++) {
        title = cards[i].querySelector(".card-body h1.card-title");
        if (title.innerText.toUpperCase().indexOf(filter) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none !important";
        }
    }
}

