 
$(document).ready(function(){
   setInterval ( "loadData()", 200 );
 });



function loadData() {   
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', 'js/status.json', true);
    xobj.onreadystatechange = function () {
        if (xobj.readyState == 4) {
            var jsonData = xobj.responseText;
            processData(jsonData);
        }
    }
    xobj.send(null);
}


function processData(data){
	var status = eval('(' + data + ')');
	$(year).html(status.year);
   	$(category).html(status.category);
	$(categorydescription).html(status.categorydescription);
}




function sendData(keyVal) {   
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', 'http://localhost:8082/?key='+keyVal, true);
    xobj.onreadystatechange = function () {
        if (xobj.readyState == 4) {
            var jsonData = xobj.responseText;
        }
    }
    xobj.send(null);
}

document.onkeypress=function(e){
	var e=window.event || e
	var keyunicode=e.charCode || e.keyCode
	sendData(e.keyCode)
}