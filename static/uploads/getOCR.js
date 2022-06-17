const formSubmit = document.querySelector('.submit-btn');
const hideContainer = document.querySelector('.hide-container');
const okayBtn = document.querySelector('.okay-btn');
const inputImage = document.querySelector('#image_input1');
const form = document.querySelector("form");



console.log(inputImage);
formSubmit.addEventListener('click', (e) => {
    if (inputImage.value != "") {
        console.log("file uploaded")
    }
    hideContainer.style.display = "flex";
})

okayBtn.addEventListener('click', (e) => {
    console.log("done");
    hideContainer.style.display = "none";
    window.location.href = "http://127.0.0.1:5000/services/";
})