/*
This is a separate file because Bootstrap documents that there are performance problems
with including it on all pages. We wil only include this js file on pages that need to
use the tooltip
*/
$(function () {
    $("[data-toggle='tooltip']").tooltip({container: 'body'});
});