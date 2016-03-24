/**
 * Created by tuck on 3/23/16.
 */
$(document).ready(function() {
    $('#report').click(function () {
        $('#content').animate({
            'marginTop': "200px" //moves Down
        });
    });

    $('#cancel').click(function () {
        $('#content').animate({
            'marginTop': "0" //moves Up
        });
    });
});