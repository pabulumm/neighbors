/**
 * Created by tuck on 4/3/16.
 */
$(document).ready(function() {
    $.ajax({
        url: "/neighborhood/current-calendar/",
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken
        },
        dataType: "json",
        success: function (data) {
            //alert("Successfully retrieved event calendar for month "+data.month);
            var event_teasers = data.event_teasers;
            var days = data.days;
            get_event(event_teasers[0].id);
            $('#calendar-head').append('<button id="calendar-month-prev" class="btn btn-default">'
                +'<span id="left-arrow" class="glyphicon glyphicon-chevron-left"></span></button>'
                +'<h1>'+data.month+'</h1><button id="calendar-month-next" class="btn btn-default">'
                +'<span id="right-arrow" class="glyphicon glyphicon-chevron-right"></span></button>');
            $.each(days, function (index, value) {
                $('#event-calendar').append('<div id="day'+value+'" class="day"><p class="day-counter">'
                    + value + '</p></div>');
                $.each(event_teasers, function(index, event) {
                    if (event.day == value) {
                        $('#day'+value).append('<p class="event-link">'+event.title+'</p><br />');
                    }
                })
            });
        },
        error: function (xhr, errmsg, err) {
            alert('ID requested was: ' + id + 'ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});



function get_event(id) {
    $.ajax({
        url: "/neighborhood/get-event/",
        type: 'GET',
        data: {
            id: id,
            csrfmiddlewaretoken: csrftoken
        },
        dataType: "json",
        success: function (data) {
            //alert("Successfully retrieved event with id:" + id);
            var event = data.event;
            $('#event-title').html(event.title);
            $('#time').append('Starts: '+event.start+'   |   Ends: '+event.end);
            $('#location').append(event.location);
            $('#description').html(event.description);

        },
        error: function (xhr, errmsg, err) {
            alert('ID requested was: ' + id + 'ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}