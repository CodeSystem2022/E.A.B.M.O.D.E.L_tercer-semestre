"use strict";

// Capture html element
let first_article_section = document.getElementById("second_section_row_first");
let second_article_section = document.querySelector(".second_section_row_second");
let third_article_section = document.querySelector(".second_section_row_third");

// Create the initial div for graphics
let div_graphics = document.createElement("div");
div_graphics.style.display = "none";
div_graphics.innerHTML = "lorem ipsum blaaaaaaaaaaaaaaaaaaaaaa bla";
div_graphics.classList.add("graphics-div");

let currentDiv = null;

// Function to toggle div visibility
function toggleDiv(articleSection) {
    if (currentDiv === articleSection.divGraphics) {
        articleSection.divGraphics.style.display = "none";
        currentDiv = null;
    } else {
        if (currentDiv) {
            currentDiv.style.display = "none";
        };
        articleSection.divGraphics.style.display = "block";
        currentDiv = articleSection.divGraphics;
    };
};

first_article_section.insertAdjacentElement("afterend", div_graphics.cloneNode(true));
second_article_section.insertAdjacentElement("afterend", div_graphics.cloneNode(true));
third_article_section.insertAdjacentElement("afterend", div_graphics.cloneNode(true));

first_article_section.divGraphics = first_article_section.nextElementSibling;
second_article_section.divGraphics = second_article_section.nextElementSibling;
third_article_section.divGraphics = third_article_section.nextElementSibling;

// Execute click event
first_article_section.addEventListener("click", function() {
    toggleDiv(first_article_section);
});
second_article_section.addEventListener("click", function() {
    toggleDiv(second_article_section);
});
third_article_section.addEventListener("click", function() {
    toggleDiv(third_article_section);
});
