/**
 * Created by tuck on 4/4/16.
 */



function colorPost(elem_id) {
    $(elem_id).css({
        'background': "rgba(158, 236, 255, 1)",
        'background': "-moz-linear-gradient(left, rgba(158, 236, 255, 1) 0%, rgba(189, 215, 255, 1) 100%",
        'background': "-webkit-gradient(left top, right top, color-stop(0%, rgba(158, 236, 255, 1)), color-stop(100%, rgba(189, 215, 255, 1))",
        'background': "-webkit-linear-gradient(left, rgba(158, 236, 255, 1) 0%, rgba(189, 215, 255, 1) 100%",
        'background': "-o-linear-gradient(left, rgba(158, 236, 255, 1) 0%, rgba(189, 215, 255, 1) 100%",
        'background': "-ms-linear-gradient(left, rgba(158, 236, 255, 1) 0%, rgba(189, 215, 255, 1) 100%",
        'background': "linear-gradient(to right, rgba(158, 236, 255, 1) 0%, rgba(189, 215, 255, 1) 100%",
        'filter': "progid:DXImageTransform.Microsoft.gradient(startColorstr='#9eecff', endColorstr='#bdd7ff', GradientType=1"
    });
}
//
//
//$(function () {
//    alert('coloring');
//    $.each(post_ids, function (index, id) {
//        //$(id).css({
//        //
//        //$(id).addClass('blue-gradient');
//    });
//
//
//});