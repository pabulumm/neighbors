/**
 * Created by tuck on 4/1/16.
 */



$.each(poll_ids, function (index, poll_id) {
    //if (index == 0) {
    //    get_poll(poll_id);
    //}
    $("#poll" + poll_id.toString()).click(function () {
        get_poll(poll_id);
    })
});

function get_poll(id) {
    $.ajax({
        url: "/polls/fetch-poll/",
        type: 'GET',
        data: {
            id: id,
            csrfmiddlewaretoken: csrftoken
        },
        dataType: "json",
        success: function (data) {
            //alert("Successfully retrieved poll with id:" + id);
            var poll = data.poll;
            $('#poll-detail').html('<h1>' + poll.question_text + '</h1><small>'
                + poll.pub_date + '</small><p>' + poll.description + '</p>');

        },
        error: function (xhr, errmsg, err) {
            alert('ID requested was: ' + id + 'ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}


function loadFirstPoll() {
    get_poll(poll_ids[0]);
}
