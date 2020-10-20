
var data_json;
var table;


function setValues(data) {
    if(data) {
        data_json = JSON.parse(data);
    }
}

function addHeaders() {
    var headers = ["Product","Category","Price","Stock",""];
    var headingRow = document.createElement('tr')
    headers.forEach(header=>{
    

        var headingCell = document.createElement('td');
        var headingText = document.createTextNode(header);
        headingCell.appendChild(headingText);
        headingRow.appendChild(headingCell);
    });
    table.appendChild(headingRow);
}

function addRow(product){
    var tr = document.createElement('tr');
    var td1 = document.createElement('td');
    var td2 = document.createElement('td');
    var td3 = document.createElement('td');
    var td4 = document.createElement('td');
    var td5 = document.createElement('td');

    var text1 = document.createTextNode(product.name);
    var text2 = document.createTextNode(product.category);
    var text3 = document.createTextNode(product.price);
    var text4 = document.createTextNode(product.stock);
    // var text5 = document.createTextNode(product.id);

    var inputId1=document.createElement('INPUT');
    inputId1.type='hidden';
    inputId1.name='id';
    inputId1.value=product.id;

    var inputId2=document.createElement('INPUT');
    inputId2.type='hidden';
    inputId2.name='id';
    inputId2.value=product.id;
    

    var deleteBtn = document.createElement('button');
    deleteBtn.type = "submit";
    deleteBtn.innerHTML = "Delete";

    var deleteForm = document.createElement("form");
    deleteForm.setAttribute("method","POST");
    deleteForm.setAttribute("action","/products?method=DELETE");

   deleteForm.appendChild(inputId1);
   deleteForm.appendChild(deleteBtn);

   var editBtn = document.createElement('button');
    editBtn.type = "submit";
    editBtn.innerHTML = "Edit";

   var editForm = document.createElement("form");
   editForm.setAttribute("method","POST");
   editForm.setAttribute("action","/products?method=CHANGE");

   editForm.appendChild(inputId2);
   editForm.appendChild(editBtn);

   td5.appendChild(deleteForm);
   td5.appendChild(editForm);


    td1.appendChild(text1);
    td2.appendChild(text2);
    td3.appendChild(text3);
    td4.appendChild(text4);
    // td5.appendChild(text5);

    tr.appendChild(td1)
    tr.appendChild(td2)
    tr.appendChild(td3)
    tr.appendChild(td4)
    tr.appendChild(td5)

    table.appendChild(tr);
}


function init() { 
    table = document.getElementById("productsTable");
    if(data_json) {
        if(data_json.status == "empty"){
            var h = document.createElement("H1"); 
            var t = document.createTextNode("** Data not Found! **");
            h.appendChild(t);
            document.getElementById("message").appendChild(h);
        } else {
            addHeaders();
            data_json.body.forEach(product=>addRow(product));

            if(data_json.status != "ok") {
                alert("** Error: " + data_json.status + " **");
            }
        }
    }
}

window.onload = init