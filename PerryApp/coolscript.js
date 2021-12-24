$(document).ready(function(){
    console.log('JQuery loaded!');
    $("#button").click(function(){
        var str = $("#whatTitle").val();
        $('#CardTitle').text(str);
        var str = $("#whatText").val();
        $('#CardText').text(str);  
        var str = $("#whatImage").val();
        $("#myCoolImage").attr("src",str);
    });
});  