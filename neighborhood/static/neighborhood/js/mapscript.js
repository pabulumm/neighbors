/**
 * CUSTOM ICON INSTANTIATION
 *
 * Types of Markers -
 *
 HOUSE = 'HOU'
 EVENT = 'EVE'
 TRASH = 'TRA'
 CONSTRUCTION = 'CON'
 POOL = 'POL'
 SPA = 'SPA'
 THEFT = 'THF'
 YARD_SALE = 'YAR'
 */

/**
 * MARKER TYPE SELECTION POPUP
 */


function getIconType(type, url_only) {
    var url = "";
    switch (type) {
        case 'HOUSE':
            url = "/static/markers/png/house-38-64.png";
            break;
        case 'YARD_SALE':
            url = "/static/markers/png/sale-28-48.png";
            break;
        case 'CONSTRUCTION':
            url = "/static/markers/png/construction-28-48.png";
            break;
        case 'THEFT':
            url = "/static/markers/png/crime-28-48.png";
            break;
        case 'EVENT':
            url = "/static/markers/png/event-28-48.png";
            break;
        case 'TRASH':
            url = "/static/markers/png/trash-32.png";
            break;
        default:
            return new L.Icon.Default;
            break;
    }
    if (url_only) {
        return url;
    }
    else {
        return new L.icon({
            iconUrl: url,
            iconSize: [38, 64],
            iconAnchor: [0, 16],
            popupAnchor: [0, -16]
        });
    }
}




L.mapbox.accessToken = 'pk.eyJ1IjoicGFidWx1bSIsImEiOiIwZTUwZmViZjQxZjYyMDJmNTQ0ZDY3YTdkNDE5ZjM0ZCJ9.MZqD7DtnmRFQfWLMGRMP_w';
var map = L.mapbox.map('map', 'mapbox.streets', {
    legendControl: {
        position: 'topleft'
    },
    zoomControl: false
}).setView([34.220912, -119.055079], 16);

// move zoom control location to top right corner
new L.Control.Zoom({position: 'topright'}).addTo(map);
//map.legendControl.addLegend(document.getElementById('legend').innerHTML);

// create profile map
var map2 = L.mapbox.map('map2', 'mapbox.streets').setView([34.220912, -119.055079], 16);
var map3 = L.mapbox.map('map3', 'mapbox.streets').setView([34.220912, -119.055079], 16);

// Create holders for new marker info
var name = "Sample Marker Name";
var lat, lon;
var pin;
var type_of_marker = "DEFAULT";
var mark_latlng;

var marker_list = [];

// create new custom icon


map.on('click', function (e) {
    if (pin != null) { // pin placed already, move it
        pin.setLatLng(e.latlng).openPopup();
        mark_latlng = e.latlng;
    }
    else { // no pin yet, make new pin
        mark_latlng = e.latlng;
        pin = new L.marker(mark_latlng).addTo(map)
            .bindPopup(
                '<button class="popup-button" id=house>House</button><button class="popup-button" id=event>Event</button><br />' +
                '<button class="popup-button" id=const>Construction</button><button class="popup-button" id=trash>Trash</button><br />' +
                '<button class="popup-button" id=theft>Theft</button><button class="popup-button" id=yard>Yard Sale</button><br />' +
                '<button class=save>SAVE</button>')
            .openPopup();
    }
});

// Getting all markers in db and loading to map


$.ajax({
    url: "/markers/get_markers/",
    type: 'GET',
    data: {
        csrfmiddlewaretoken: csrftoken
    },
    dataType: "json",
    success: function (data) {
        $.each(data.markers, function (markerIndex, marker) {

            // create a new L.marker for each retrieved model instance
            var mark = L.marker([marker.lat, marker.lon])
                .setIcon(getIconType(
                    marker.type_of_marker, false))
                // creating the popup for our marker
                .bindPopup(
                    '<h3>' + marker.title + '</h3><p>' + marker.description +
                    '<br/><strong>' + marker.type_of_marker +
                    '</strong><br/><small>' + marker.create_date + '</small>'
                ).addTo(map);
            // create a marker variable reference
            var marker_reference = {
                'id': marker.id,
                'lat': marker.lat,
                'lon': marker.lon,
                'type': marker.type_of_marker,
                'title': marker.title,
                'marker': mark
            };
            // add the loaded marker to the reference list
            marker_list.push(marker_reference);
        });
    },
    error: function (xhr, errmsg, err) {
        alert('ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
});


$('#map').on('click', '#house', function () {
    type_of_marker = "HOUSE";
    pin.setIcon(getIconType(type_of_marker));
});
$('#map').on('click', '#yard', function () {
    type_of_marker = "YARD_SALE";
    pin.setIcon(getIconType(type_of_marker));
});
$('#map').on('click', '#const', function () {
    type_of_marker = "CONSTRUCTION";
    pin.setIcon(getIconType(type_of_marker));
});
$('#map').on('click', '#theft', function () {
    type_of_marker = "THEFT";
    pin.setIcon(getIconType(type_of_marker));
});
$('#map').on('click', '#event', function () {
    type_of_marker = "EVENT";
    pin.setIcon(getIconType(type_of_marker));
});
$('#map').on('click', '#trash', function () {
    type_of_marker = "TRASH";
    pin.setIcon(getIconType(type_of_marker));
});
$('#map').on('click', '#default', function () {
    type_of_marker = "TRASH";
    pin.setIcon(getIconType(type_of_marker));
});
$('#map').on('click', '.save', function () {
    // AJAX call to save new marker as GeoDjango model
    $.ajax({
        url: "/markers/new_marker/",
        type: "Post",
        data: {
            title: title,
            lat: mark_latlng.lat,
            lon: mark_latlng.lng,
            type_of_marker: type_of_marker,
            csrfmiddlewaretoken: csrftoken
        },
        success: function (json) {
            pin.closePopup();
            alert('Created a ' + type_of_marker + ' marker at latitude:' + json['lat'] + ' and longitude:' + json['lon']);
            L.marker([mark_latlng.lat, mark_latlng.lng]).setIcon(getIconType(type_of_marker)).addTo(map);
            pin = null;

        },
        error: function (xhr, errmsg, err) {
            alert('ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    })
});

function centerUserMap(latlng) {
    new L.marker(latlng).setIcon(getIconType("HOUSE", false)).addTo(map2);
    map2.setView(latlng, 18);
}

function centerEventMap(latlng) {
    new L.marker(latlng).setIcon(getIconType("EVENT", false)).addTo(map3);
    map3.setView(latlng, 17);
}

function openPop(marker_id) {
    $.each(marker_list, function (markerIndex, marker) {
        if (marker_id == marker.id) {
            marker.marker.openPopup();
        }
    })
}

function centerMarker(latlng) {
    map.panTo(latlng);
}
