var TOTAL_IMG = 0;
var CURRENT_IMG = 0;


$(document).ready(function(){
    var productListingContainer  = $("ul.product-listing-container");
    var productRowWidth = productListingContainer.width();
    var productList = $("li.booking-card");
    var totalProducts = productList.length;
    var firstProduct = productList.first();
    var eachProductWidth = firstProduct.width();
    var productsEachRow = Math.min(Number.parseInt(productRowWidth / eachProductWidth) , 3);
    
    var neededProducts = productsEachRow - (totalProducts % productsEachRow);
    for(var i = 0; i< neededProducts; i++){
        var fake = $(firstProduct).clone();
        fake.addClass("fake");
        productListingContainer.append(fake)
    }
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

