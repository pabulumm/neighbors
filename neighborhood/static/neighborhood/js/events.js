/**
 * Created by tuck on 4/3/16.
 */

var days = [];
var event_teasers;
var curr_month;
var curr_year;

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$.ajax({
    url: "/neighborhood/current-calendar/",
    type: 'GET',
    data: {
        csrfmiddlewaretoken: csrftoken
    },
    dataType: "json",
    success: function (data) {
        //alert("Successfully retrieved event calendar for month "+data.month);
        event_teasers = data.event_teasers;
        var days = data.days;
        curr_month = data.month_int;
        curr_year = data.year;
        get_event(event_teasers[0].id);
        $('#calendar-head').append('<button id="calendar-month-prev" class="btn btn-default">'
            + '<span id="left-arrow" class="glyphicon glyphicon-chevron-left"></span></button>'
            + '<h1>' + data.month + ' ~ ' + data.year + '</h1><button id="calendar-month-next" class="btn btn-default">'
            + '<span id="right-arrow" class="glyphicon glyphicon-chevron-right"></span></button>');
        $.each(days, function (index, value) {
            $('#event-calendar').append('<div id="' + value + '" class="day"><p id="' + value + '" class="day-counter">'
                + value + '</p></div>');
            $.each(event_teasers, function (index, event) {
                if (event.day == value) {
                    $('#' + value).append('<p id="' + value + '" class="event-link">' + event.title + '</p><br />');
                }
            })
        });
    },
    error: function (xhr, errmsg, err) {
        alert('ID requested was: ' + id + 'ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
});

function reloadCalendar(direction) {
    if (direction == 'LEFT') {
        if (curr_month == 1) {
            curr_month = 12;
            curr_year--;
        }
        else {
            curr_month--;
        }
    }
    else if (direction == 'RIGHT') {
        if (curr_month == 12) {
            curr_month = 1;
            curr_year++;
        }
        else {
            curr_month++;
        }
    }
    alert('reloading calendar for month: ' + curr_month + ' year: ' + curr_year);

    $.ajax({
        url: "/neighborhood/specific-calendar/",
        type: 'GET',
        data: {
            month: curr_month,
            year: curr_year,
            csrfmiddlewaretoken: csrftoken
        },
        dataType: "json",
        success: function (data) {
            alert("Retrieval Success!");
            // clear last calendar html
            $('#event-calendar').html('<div id=calendar-head"></div><div id="calendar-body"></div>');
            //alert("Successfully retrieved event calendar for month "+data.month);
            event_teasers = data.event_teasers;
            var days = data.days;
            get_event(event_teasers[0].id);
            $('#calendar-head').append('<button id="calendar-month-prev" class="btn btn-default">'
                + '<span id="left-arrow" class="glyphicon glyphicon-chevron-left"></span></button>'
                + '<h1>' + data.month + ' ~ ' + data.year + '</h1><button id="calendar-month-next" class="btn btn-default">'
                + '<span id="right-arrow" class="glyphicon glyphicon-chevron-right"></span></button>');
            $.each(days, function (index, value) {
                $('#event-calendar').append('<div id="' + value + '" class="day"><p id="' + value + '" class="day-counter">'
                    + value + '</p></div>');
                $.each(event_teasers, function (index, event) {
                    if (event.day == value) {
                        $('#' + value).append('<p id="' + value + '" class="event-link">' + event.title + '</p><br />');
                    }
                })
            });
        },
        error: function (xhr, errmsg, err) {
            alert('ID requested was: ' + id + 'ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
    alert('finished reloading');
}

function isValidCalendarBox(id) {
    var elem_id = '#' + id;
    var id_num;
    if ($(elem_id).hasClass('day')) {
        id_num = +id;
    }
    else if ($(elem_id).hasClass('event-link')
        || $(elem_id).hasClass('day-counter')) {
        id_num = +$(elem_id).parent().attr('id');
    }
    else {
        id_num = -1
    }
    return id_num;
}

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
            $('#time').append('Starts: ' + event.start + '   |   Ends: ' + event.end);
            $('#location').append(event.location);
            $('#description').html(event.description);

        },
        error: function (xhr, errmsg, err) {
            alert('ID requested was: ' + id + 'ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function loadDayListeners() {
    $('#event-calendar').click(function (event) {
        var id = event.target.id;
        if (id == "calendar-month-prev" || id == "left-arrow") {
            return reloadCalendar('LEFT');
        }
        else if (id == "calendar-month-next" || id == "right-arrow") {
            return reloadCalendar('RIGHT');
        }
        else {
            var id_as_num = isValidCalendarBox(event.target.id);
            var id = '#' + id_as_num;
            if (id_as_num > 0
                && (!($(id).hasClass('highlight')))) {

                // highlight the selected calendar day div
                $('.highlight').removeClass('highlight');
                $(id).addClass('highlight');

                // load the event teasers for the side panel list - clear it first
                $('#event-list-day').html('');
                $.each(event_teasers, function (index, event) {
                    if (event.day == id_as_num) {
                        $('#event-list-day').append('<p>' + event.title + '</p>');
                    }
                });
            }
        }
    });
}


loadDayListeners();



