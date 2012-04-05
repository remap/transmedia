 
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
}