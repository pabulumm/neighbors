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


function pollVote(poll_id, vote) {
    console.log('Vote: ' + vote + ' for poll: ' + poll_id + ' staged for submission.');
    $.ajax({
        url: '/polls/poll-vote/',
        type: 'POST',
        dataType: 'json',
        data: {
            vote: vote,
            poll_id: poll_id,
            csrfmiddlewaretoken: csrftoken
        },
        success: function (data) {
            console.log('AJAX: pollVote returned SUCCESSFUL');
            if (data.vote_id > 0) {
                alert('Your vote has been submitted!');
            }
            else {
                alert('Only one vote per user is permitted for each Decision.');
            }
        },
        error: function (xhr, errmsg, err) {
            alert('ID requested was: ' + id + 'ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

var selected_poll =

$(document).ready(function() {
    $('.poll-item-container').click(function() {
        if ($(this).hasClass('selected-poll')) {
            $(this).animate({"height": '100px'}).removeClass('selected-poll');
        }
        else {
            $('.selected-poll').animate({"height": '100px'}).removeClass('selected-poll');
            $(this).animate({"height": '300px'}).addClass('selected-poll');
        }
    })
});