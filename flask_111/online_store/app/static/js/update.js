var inputId;
var inputName;
var inputCategory;
var inputPrice;
var inputStock;
var inputImage;

var data_json;

function ID() {
    // Math.random should be unique because of its seeding algorithm.
    // Convert it to base 36 (numbers + letters), and grab the first 9 characters
    // after the decimal.
    return '_' + Math.random().toString(36).substr(2, 9);
};

function init() {
    inputId = document.getElementById("id");
    inputName = document.getElementById("name");
    inputCategory = document.getElementById("category");
    inputPrice = document.getElementById("price");
    inputStock = document.getElementById("stock");
    inputImage = document.getElementById("image");

    inputId.value = ID();

    populateInputs();
}

function verifyInputs(){
    var text = inputName.value;
    if(text == "") {
        alert("Insert the Name of the product.");
        return false;
    }
    text = inputCategory.value;
    if(text == "") {
        alert("Insert the Category of the product.");
        return false;
    }
    text = inputPrice.value;
    if(text == "" || text == 0 || text == "0") {
        alert("Insert the Price of the product.");
        return false;
    }
    text = inputStock.value;
    if(text == "" || text == 0 || text == "0") {
        alert("Insert the stock of the product.");
        return false;
    }
    text = inputImage.value;
    if(text == "") {
        alert("Insert the Image of the product.");
        return false;
    }
    return true;
}

function setValues(data) {
    if(data) {
        data_json = JSON.parse(data);
    }
}

function populateInputs(){
    if(data_json) {
        inputId.value = data_json.data[0];
        inputName.value = data_json.data[1];
        inputCategory.value = data_json.data[2];
        inputPrice.value = data_json.data[3];
        inputStock.value = data_json.data[4];
        inputImage.value = data_json.data[5];
        if(data_json.status && ("updated" == data_json.status || "ok" == data_json.status)){
            return;
        } else {
            alert("** Error: " + data_json.status + " **");
        }
    }
}

window.onload = init