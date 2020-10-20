
Polymer({
    is: "custom_item",
    properties: {
        item: {
            type:String
        }
    }
});

var amount = 0;
var localItem;
function init(){
    console.log("item::init");
    // localItem = JSON.parse(this.item);
    // document.getElementById("itemImg").src = localItem.image;
    // document.getElementById("itemName").innerText = localItem.name;
    // document.getElementById("itemPrice").innerText = "Price: $" + localItem.price;
    // document.getElementById("pickerAmount").innerText = amount;
    // document.getElementById("pickerDecrease").onclick = function(){
    //     console.log("Decrease");
    //     if(amount > 2) {
    //         amount--;
    //         document.getElementById("pickerAmount").innerText = amount;
    //     }
    // };
    // document.getElementById("pickerIncrease").onclick = function(){
    //     console.log("Increase");
    //     if(amount <= localItem.stock) {
    //         amount++;
    //         document.getElementById("pickerAmount").innerText = amount;
    //     }
    // };
}

window.onload = init