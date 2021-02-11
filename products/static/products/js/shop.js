// Sort trigger button
$("#sort-container").hide()
$( "#sort-trigger").click(function() {     
    if($('#sort-container:visible').length)
        $('#sort-container').hide("slide", { direction: "right" }, 1000);
    else
        $('#sort-container').show("slide", { direction: "right" }, 1000);        
});