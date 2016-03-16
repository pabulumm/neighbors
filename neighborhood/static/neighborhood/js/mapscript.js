$(document).ready(function() {
    L.mapbox.accessToken = 'pk.eyJ1IjoicGFidWx1bSIsImEiOiIwZTUwZmViZjQxZjYyMDJmNTQ0ZDY3YTdkNDE5ZjM0ZCJ9.MZqD7DtnmRFQfWLMGRMP_w';
    var map = L.mapbox.map('map', 'mapbox.streets', {
        legendControl: {
            position: 'topleft'
        },
        zoomControl: false
    }).setView([34.220912, -119.055079], 16);

    // move zoom control location to top right corner
    new L.Control.Zoom({ position: 'topright' }).addTo(map);

    map.legendControl.addLegend(document.getElementById('legend').innerHTML);
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
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});
