var data_json;
var container;
function init() {
    container = document.getElementById("container");
    if(data_json) {
        if(data_json.status == "ok") {
            data_json.body.forEach(item => {
                document.getElementById("itemId").value = item.id;
                document.getElementById("itemImg").src = item.image;
                document.getElementById("itemName").innerText = item.name;
                document.getElementById("itemPrice").innerText = "Price: $" + item.price;
                
                var itemView  = document.getElementById("item");
                itemView.style.display = "block";
                container.appendChild(itemView.cloneNode(true));
                itemView.style.display = "none";
            });
        } else {
            var h = document.createElement("H1"); 
            var t = document.createTextNode("** Data not Found! **");
            h.appendChild(t);
            document.getElementById("message").appendChild(h);
        }
    }
}

function setValues(data) {
    if(data) {
        data_json = JSON.parse(data);
    }
}

window.onload = init;