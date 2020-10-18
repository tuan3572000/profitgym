var WINDOW_HEIGHT = "900px";
var TOTAL_SECTIONS = 0;
var CURRENT_SECTION = 1;




$(document).ready(function(){
    TOTAL_SECTIONS = $(".section.fp-section").length;
    WINDOW_HEIGHT = $(window).height() + "px";
    responsiveImage();
    verticalScrollImage();
    populateSectionSelectionBar();
    activeSection();
})


function responsiveImage(){
    adjustBgImgHeight();
    window.addEventListener('resize', function(){
        WINDOW_HEIGHT = $(window).height() + "px";
        adjustBgImgHeight();
    });

    function adjustBgImgHeight(){
        $('img.lazy-bg').css("height", WINDOW_HEIGHT);
    }

    $("#fp-nav ul").on('click', "li" , function() {
        adjustBgImgHeight();
        var sectionIndex = $(this).index();
        CURRENT_SECTION = sectionIndex + 1;
        activeSection();
    });
}

function activeSection(){
    $(".fp-section").removeClass("active");
    $("#section" + CURRENT_SECTION).addClass("active");
    $("#fp-nav ul li a").removeClass("active");
    $("#fp-nav ul li a.section"+ CURRENT_SECTION).addClass("active");
    $("#fp-nav .fixed-tooltip").text($("#section" + CURRENT_SECTION).attr("data-title"));

}


function populateSectionSelectionBar(){
    for(var sectionIndex = 1; sectionIndex <= TOTAL_SECTIONS; sectionIndex ++){
        $("#fp-nav ul").append(
            $('<li><a class="section' + sectionIndex + '"><span></span></a><div class="fp-tooltip right">Welcome</div></li>')
        )
    }
}



function verticalScrollImage(){
    $('.section').bind('DOMMouseScroll',
        _.debounce(function(e) {
            scrollEventOnSection(e);
          }, 400)
    );
}


function scrollEventOnSection(e){
    if(e.originalEvent.detail > 0) {
       if(CURRENT_SECTION < TOTAL_SECTIONS){
            CURRENT_SECTION = CURRENT_SECTION + 1;
       }else{
            CURRENT_SECTION = TOTAL_SECTIONS - 1;
       }
     }else {
        if(CURRENT_SECTION > 1 ){
            CURRENT_SECTION = CURRENT_SECTION - 1;
       }else{
            CURRENT_SECTION = 1;
       }
     }
     activeSection();
     return false;
}

