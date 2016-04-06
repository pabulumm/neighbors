/**
 * Created by tuck on 4/3/16.
 */

var days = [];
var event_teasers;
var curr_month;
var curr_year;

$(document).ready(function () {


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

    loadDayListeners();

    $('#left-arrow').click(function () {
        alert('left-arrow click');
        if (curr_month == 1) {
            curr_month = 12;
            curr_year--;
        }
        else {
            curr_month--;
        }
        reloadCalendar(curr_month, curr_year);
        loadDayListeners();
    });

    $('#right-arrow').click(function () {
        alert('right-arrow click');

        if (curr_month == 12) {
            curr_month = 1;
            curr_year++;
        }
        else {
            curr_month++;
        }
        reloadCalendar(curr_month, curr_year);
        loadDayListeners();
    });
});

function reloadCalendar(month, year) {
    alert('reloading calendar');
    $.ajax({
        url: "/neighborhood/specific-calendar/",
        type: 'GET',
        data: {
            month: month,
            year: year,
            csrfmiddlewaretoken: csrftoken
        },
        dataType: "json",
        success: function (data) {
            // clear last calendar html
            $('#calendar-head').html('');
            $('#calendar-body').html('');
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
}


function loadDayListeners() {
    $('#event-calendar').click(function (event) {
        alert(event.target.id);
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
    });
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