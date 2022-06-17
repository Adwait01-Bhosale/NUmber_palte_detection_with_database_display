const setTimeBtn = document.querySelector('.set-btn');
const hideContainer = document.querySelector('.hide-container');
const submitBtn = document.querySelector('.submit');


setTimeBtn.addEventListener('click', (e) => {
    hideContainer.style.display = "flex";
})

submitBtn.addEventListener('click', (e) => {
    console.log("done");
    hideContainer.style.display = "none";
})