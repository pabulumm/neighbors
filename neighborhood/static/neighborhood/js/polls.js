/**
 * Created by tuck on 4/1/16.
 */
$(document).ready(function() {

    $.each(poll_ids, function (index, poll_id) {
        $(poll_id).click(function() {
            get_poll(poll_id.id);
        })
    });

    function get_poll(id) {
        $.ajax({
            url: "/polls/id/",
            type: 'GET',
            data: {
                csrfmiddlewaretoken: csrftoken
            },
            dataType: "json",
            success: function (poll) {
                alert("Successfully retrieved poll with id:" + id);

            },
            error: function (xhr, errmsg, err) {
                alert('ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

});