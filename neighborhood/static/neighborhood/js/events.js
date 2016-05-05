/**
 * Created by tuck on 4/3/16.
 */

var days = [];
var event_teasers;
var curr_month;
var month;
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
        month = data.month;
        curr_month = data.month_int;
        curr_year = data.year;
        if (event_teasers.length > 0) {
            console.log(event_teasers[0].id);
            get_event(event_teasers[0].id);
        }
        $('#calendar-head').append('<button id="calendar-month-next" class="btn btn-default">'
            + '<span id="right-arrow" class="glyphicon glyphicon-chevron-right"></span></button>'
            + '<h1 id="month-label">' + data.month + ' ~ ' + data.year + '</h1><button id="calendar-month-prev" class="btn btn-default">'
            + '<span id="left-arrow" class="glyphicon glyphicon-chevron-left"></span></button>');
        // creating the header labels for the days of the week
        $('#calendar-body').append(
            '<div class="day-label">Monday</div>' +
            '<div class="day-label">Tuesday</div>' +
            '<div class="day-label">Wednesday</div>' +
            '<div class="day-label">Thursday</div>' +
            '<div class="day-label">Friday</div>' +
            '<div class="day-label">Saturday</div>' +
            '<div class="day-label">Sunday</div>');
        $.each(days, function (index, value) {
            $('#calendar-body').append('<div id="' + value + '" class="day"><p id="' + value + '" class="day-counter">'
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
    console.log('reloading calendar for month: ' + curr_month + ' year: ' + curr_year);

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
            console.log("AJAX: specific-calendar returned SUCCESSFUL");
            // clear last calendar html
            $('#calendar-body').html('');
            console.log("Successfully retrieved event calendar for month "+data.month);
            event_teasers = data.event_teasers;
            var days = data.days;


            $('#month-label').html(data.month + ' ~ ' + data.year);
            $.each(days, function (index, value) {
                $('#calendar-body').append('<div id="' + value + '" class="day"><p id="' + value + '" class="day-counter">'
                    + value + '</p></div>');
                $.each(event_teasers, function (index, event) {
                    if (event.day == value) {
                        $('#' + value).append('<p id="' + value + '" class="event-link">' + event.title + '</p><br />');
                    }
                })
            });

            if (event_teasers.length > 0) {
                get_event(event_teasers[0].id);
            }
        },
        error: function (xhr, errmsg, err) {
            alert('ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
    console.log('Completed event calendar switch');
}


function get_event(event_id) {
    $.ajax({
        url: "/neighborhood/get-event/",
        type: 'GET',
        data: {
            event_id: event_id,
            csrfmiddlewaretoken: csrftoken
        },
        dataType: "json",
        success: function (data) {
            console.log("Successfully retrieved event with id:" + event_id);
            var event = data.event;
            $('#event-title').html(event.title);
            $('#starttime').append(event.start);
            $('#endtime').append(event.end);
            $('#location').append(event.location);
            $('#event-description').html(event.description);
            console.log("Current event: " +event.description);
        },
        error: function (xhr, errmsg, err) {
            alert('ID requested was: ' + event_id + 'ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}


function isValidCalendarBox(id) {
    id_num = id;
    if (isNaN(id_num)) {
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
    }
    return id_num;
}

/**
 *
 */
function loadDayListeners() {
    $('#event-calendar').click(function (event) {
        var event_id = event.target.id;
        if (event_id == "calendar-month-prev" || event_id == "left-arrow") {
            return reloadCalendar('LEFT');
        }
        else if (event_id == "calendar-month-next" || event_id == "right-arrow") {
            return reloadCalendar('RIGHT');
        }
        else {
            console.log("Clicked element id: " + event_id);
            var id_as_num = isValidCalendarBox(event_id);
            var id = '#' + id_as_num;
            console.log("Clicked element id_as_num: " + id_as_num);
            if (id_as_num > 0
                && (!($(id).hasClass('highlight')))) {
                console.log("Element before class: " +$(id).attr("class"));
                // highlight the selected calendar day div
                $('.highlight').removeClass('highlight');
                $(id).addClass('highlight');

                console.log("Element before class: " +$(id).attr("class"));

                // clear event items list
                $('#event-list-items').html('');
                $('#event-list-header-text').html(month+' '+id_as_num);

                var empty = true; // boolean to determine if any events were added to the list
                $.each(event_teasers, function (index, event) {
                    if (event.day == id_as_num) {
                        empty = false;
                        $('#event-list-items').append('<p>' + event.title + '</p>');
                    }
                });
                if (empty) {
                    $('#event-list-items').append('<p id="empty-list-tag">No Events.</p>');
                }
            }
        }
    });
}


loadDayListeners();



