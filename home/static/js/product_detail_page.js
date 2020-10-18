var TOTAL_IMG = 0;
var CURRENT_IMG = 0;


$(document).ready(function(){
    TOTAL_IMG = $(".img-large-wrap").length;
    displayImage();
})


function displayImage(){
    handleSelectedImage();
    $(".img-small-wrap").on('click', ".item-gallery" , function() {
        CURRENT_IMG = $(this).index();
        handleSelectedImage();

    });
}

function handleSelectedImage(){
    $(".img-large-wrap").addClass("d-none");
    $(".img-large-wrap").eq(CURRENT_IMG).removeClass("d-none");
}

