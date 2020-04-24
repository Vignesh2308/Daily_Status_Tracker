document.getElementById('cur_date').valueAsDate = new Date();
var dd = new Date();
var cur_date = dd.getFullYear()+"-"+0+(dd.getMonth()+1)+"-"+dd.getDate();
document.getElementById('cur_date').setAttribute("min",cur_date);
document.getElementById('completion_date').setAttribute("min",cur_date);

$('#assess_comp').hide();
$('#data').hide();
$('#source_others').hide();
$('#submit').hide();

$("#assessment").change(function(){

        var status=$(this).children("option:selected").val();
        if(status==='Yes')
            $('#assess_comp').show();
        else
            $('#assess_comp').hide();
});

$("#source").change(function(){

    var status=$(this).children("option:selected").val();
    if(status==='others')
        $('#source_others').show();
    else
        $('#source_others').hide();

});


$('#hours_spent').keyup(function(){
    var hours = $(this).val();
    document.getElementById("ttl_hours").value=hours;
})






