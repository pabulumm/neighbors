$(document).ready(function() {
    //For getting CSRF token
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');


    L.mapbox.accessToken = 'pk.eyJ1IjoicGFidWx1bSIsImEiOiIwZTUwZmViZjQxZjYyMDJmNTQ0ZDY3YTdkNDE5ZjM0ZCJ9.MZqD7DtnmRFQfWLMGRMP_w';
    var map = L.mapbox.map('map', 'mapbox.streets').setView([34.220912, -119.055079], 16);
    L.marker([34.221542, -119.055518]).addTo(map);

    var name;
    var lat,lon;

    map.on('click', function(e) {
        // create a variable to hold to new marker
        var marker = L.marker(e.latlng).addTo(map);
        marker.bindPopup('<button id="save" class="save">Save</button>').openPopup();// +
            //'<button class="cancel">Cancel</button>').openPopup();

        // grab the position of the click
        name = "Test Name";
        lat = e.latlng.lat;
        lon = e.latlng.lng;
    });

    //$('#map').on('click', '.cancel', function() {

    //});

    $('#map').on('click', '.save', function() {
        // AJAX call to save new marker as GeoDjango model
        $.ajax({
            url: "{% url 'world:new_marker' %}",
            type: "Post",
            data : {
                name: name,
                lat: lat,
                lon: lon,
                csrfmiddlewaretoken: csrftoken
            },
            success : function(json) {
                console.log(json);
                alert('Created a House marker at latitude:' + json['lat'] + ' and longitude:' + json['lon'])
            },
            error : function(xhr,errmsg,err) {
                alert('ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        })
    });
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});
