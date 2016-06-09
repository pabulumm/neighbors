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


function toggleMarkerInfo() {
    if (!$('#marker-post-button').hasClass('marker-active')) {
        $('#new-marker-info').hide();
    }
    else {
        $('#new-marker-info').show();
    }
}


var marker_list = [];

var can_place_marker = false;

function newMarker(name, callback) {
    var post_marker_id = -1;
    var title = name;
    console.log('New Marker called.');
    if (name.length > 45) {
        title = name.substring(0, 45);
    }
    $.ajax({
        url: "/markers/new-marker/",
        type: "Post",
        data: {
            title: title,
            description: name,
            lat: pin_latlng.lat,
            lon: pin_latlng.lng,
            type_of_marker: type_of_marker,
            csrfmiddlewaretoken: csrftoken
        },
        success: function (json) {
            console.log('AJAX newMarker returned SUCCESSFUL');
            pin.closePopup();
            console.log('Created a ' + type_of_marker + ' marker at latitude:' +
                pin_latlng.lat + ' and longitude:' + pin_latlng.lng);
            L.marker([pin_latlng.lat, pin_latlng.lng]).setIcon(getIconType(type_of_marker)).addTo(map);
            console.log(json['marker_id']);
            pin = null;
            callback(json['marker_id']);
        },
        error: function (xhr, errmsg, err) {
            alert('ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
    return post_marker_id;
}

function getAllMarkers() {
    $.ajax({
        url: "/markers/get-markers/",
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken
        },
        dataType: "json",
        success: function (data) {
            $.each(data.markers, function (markerIndex, marker) {


                var popup_str =
                    '<div class="popup-container"><h4>' + marker.title + '</h4>'+
                    '<span class="underline-fade"></span><p>' + marker.description +
                    '</p><br/><p class="mark-type-popup">' + marker.type_of_marker +
                    '</p><small>' + marker.create_date + '</small></div>';

                // create a new L.marker for each retrieved model instance
                var mark = L.marker([marker.lat, marker.lon])
                    .setIcon(getIconType(marker.type_of_marker, false))
                    // creating the popup for our marker
                    .bindPopup(popup_str).addTo(map);
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
}


L.mapbox.accessToken = 'pk.eyJ1IjoicGFidWx1bSIsImEiOiIwZTUwZmViZjQxZjYyMDJmNTQ0ZDY3YTdkNDE5ZjM0ZCJ9.MZqD7DtnmRFQfWLMGRMP_w';
var map = L.mapbox.map('map', 'mapbox.streets', {
    legendControl: {
        position: 'topleft'
    },
    zoomControl: false
}).setView([37.67.6670, -119.418438], 16);

// move zoom control location to top right corner
new L.Control.Zoom({position: 'topright'}).addTo(map);
//map.legendControl.addLegend(document.getElementById('legend').innerHTML);

// Create holders for new marker info
var name = "Sample Marker Name";
var lat, lon;
var pin;
var type_of_marker = "DEFAULT";
var pin_latlng;

getAllMarkers();
toggleMarkerInfo();

// create new custom icon


map.on('click', function (e) {
    if (can_place_marker) {
        if (pin != null) { // pin placed already, move it
            pin.setLatLng(e.latlng).openPopup();
            pin_latlng = e.latlng;
        }
        else { // no pin yet, make new pin
            pin_latlng = e.latlng;
            pin = new L.marker(pin_latlng).addTo(map)
                .bindPopup(
                    '<button class="popup-button" id=comment>Comment</button>' +
                    '<button class="popup-button" id=event>Event</button><br />' +
                    '<button class="popup-button" id=const>Construction</button>' +
                    '<button class="popup-button" id=trash>Trash</button><br />' +
                    '<button class="popup-button" id=theft>Theft</button>' +
                    '<button class="popup-button" id=yard>Yard Sale</button><br />'
                )
                .openPopup();
        }
    }
});

// Getting all markers in db and loading to map


$('#marker-post-button').click(function (event) {
    event.preventDefault();
    if ($('#marker-post-button').hasClass('marker-active')) {
        $('#marker-post-button').removeClass('marker-active');
        $('#new-marker-info').hide();
        if (pin) {
            map.removeLayer(pin);
        }
        can_place_marker = false;
    }
    else {
        $('#marker-post-button').addClass('marker-active');
        $('#new-marker-info').show();
        can_place_marker = true;
    }
    toggleMarkerInfo();
});


$('#map').on('click', '#comment', function () {
    type_of_marker = "COMMENT";
    pin.setIcon(getIconType(type_of_marker));
    pin.closePopup();
});
$('#map').on('click', '#yard', function () {
    type_of_marker = "YARD_SALE";
    pin.setIcon(getIconType(type_of_marker));
    pin.closePopup();
});
$('#map').on('click', '#const', function () {
    type_of_marker = "CONSTRUCTION";
    pin.setIcon(getIconType(type_of_marker));
    pin.closePopup();
});
$('#map').on('click', '#theft', function () {
    type_of_marker = "THEFT";
    pin.setIcon(getIconType(type_of_marker));
    pin.closePopup();
});
$('#map').on('click', '#event', function () {
    type_of_marker = "EVENT";
    pin.setIcon(getIconType(type_of_marker));
    pin.closePopup();
});
$('#map').on('click', '#trash', function () {
    type_of_marker = "TRASH";
    pin.setIcon(getIconType(type_of_marker));
    pin.closePopup();
});
$('#map').on('click', '#default', function () {
    type_of_marker = "TRASH";
    pin.setIcon(getIconType(type_of_marker));
    pin.closePopup();
});
//$('#map').on('click', '.save', function () {
//    newMarker(name, pin_latlng.lat, pin_latlng.lng, type_of_marker);
//});

function centerUserMap(lat, lng) {
    //console.log('centering user map to ' + lat + ', ' + lng);
    //new L.marker([lat, lng]).setIcon(getIconType("HOUSE", false)).addTo(map2);
    //map2.setView([lat, lng], 17);
}

function centerEventMap(latlng) {
    //new L.marker(latlng).setIcon(getIconType("EVENT", false)).addTo(map3);
    //map3.setView(latlng, 17);
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
