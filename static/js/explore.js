/*
Loaded only on the explore page
*/

$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    var breakpoint = 247
    var fixed_class = "fixed-top"
    var padding_class = "explore-search-padding"
    var sticky_obj = $("#explore-search-box-row")
    var container_obj = $("#explore-container")
    //console.log(scroll)

    if (scroll >= breakpoint) {
        // perform tasks to stick the search bar
        sticky_obj.addClass(fixed_class);
        container_obj.addClass(padding_class);
    }
    else if (scroll < breakpoint) {
        // perform tasks to unstick the search bar
        sticky_obj.removeClass(fixed_class);
        container_obj.removeClass(padding_class);
    }
});