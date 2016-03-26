$(document).ready(function () {
    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').focus()
    });
    //$("#announcement").click(function () {
    //    alert('happening');
    //    $("#announcement-form").fadeIn();
    //    $("#announcement-form").css({"visibility": "visible", "display": "block"});
    //});
    //$("#close_login").click(function () {
    //    $("#announcement-form").fadeOut();
    //    $("#announcement-form").css({"visibility": "hidden", "display": "none"});
    //});
});
