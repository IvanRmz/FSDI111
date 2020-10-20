
var item;
var amount = 1;

function setTotal() {
    document.getElementById("total").innerText = "Total: $" + item["price"] * amount;
}

function init() {
    if(item) {
        document.getElementById("id").value = item["id"];
        document.getElementById("name").innerText = item["name"];
        document.getElementById("image").src = item["image"];
        document.getElementById("stock").innerText = "Currently in the stock: " + item["stock"];
        document.getElementById("price").innerText = "Price per unit: $" + item["price"];
        document.getElementById("pickerDecrease").onclick = function(){
            if(amount > 1) {
                amount--;
                document.getElementById("pickerAmount").value = amount;
                setTotal();
            }
        };
        document.getElementById("pickerIncrease").onclick = function(){
            if(amount < item["stock"]) {
                amount++;
                document.getElementById("pickerAmount").value = amount;
                setTotal();
            }
        };
        setTotal()
    }
}



function setData(data) {
    if(data) {
        item = JSON.parse(data);
        console.log(typeof(item));
    }
}

window.onload = init;