$(document).ready(function(){
    footer = $("#post-fixed-footer");
    breakpoint = 700;
    footer.hide();

    $(window).scroll(function() {

        scroll = $(window).scrollTop();
        console.log(scroll);

        if (scroll >= breakpoint) { 
            footer.show();
        }
        else {
            footer.hide();
        }
    }); 
});