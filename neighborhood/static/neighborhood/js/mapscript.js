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
                    '<button class="popup-button" id=house>House</button><button class="popup-button" id=event>Event</button><br />' +
                    '<button class="popup-button" id=const>Construction</button><button class="popup-button" id=trash>Trash</button><br />' +
                    '<button class="popup-button" id=theft>Theft</button><button class="popup-button" id=yard>Yard Sale</button><br />' +
                    '<button class=save>SAVE</button>')
                .openPopup();
        }
    }
});

// Getting all markers in db and loading to map


$('#marker-post-button').click(function(event) {
    event.preventDefault();
    if ($('#marker-post-button').hasClass('marker-active')) {
        $('#marker-post-button').removeClass('marker-active');
        can_place_marker = false;
    }
    else {
        $('#marker-post-button').addClass('marker-active');
        can_place_marker = true;
    }
    toggleMarkerInfo();
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
    //$.ajax({
    //    url: "/markers/new_marker/",
    //    type: "Post",
    //    data: {
    //        title: title,
    //        lat: pin_latlng.lat,
    //        lon: pin_latlng.lng,
    //        type_of_marker: type_of_marker,
    //        csrfmiddlewaretoken: csrftoken
    //    },
    //    success: function (json) {
    //        pin.closePopup();
    //        alert('Created a ' + type_of_marker + ' marker at latitude:' + json['lat'] + ' and longitude:' + json['lon']);
    //        L.marker([pin_latlng.lat, pin_latlng.lng]).setIcon(getIconType(type_of_marker)).addTo(map);
    //        pin = null;
    //
    //    },
    //    error: function (xhr, errmsg, err) {
    //        alert('ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    //    }
    //})
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
