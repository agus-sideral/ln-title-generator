let container = document.getElementsByClassName("div-col")
container.getElementByTagName("a")

// novelupdates.com
let container = document.getElementsByClassName("search_title")
let contArray = Array.from(container);
let res = contArray.map(a => a.innerText + "\n");
res.join("");

