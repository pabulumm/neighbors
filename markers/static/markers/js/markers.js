/**
 * Created by tuck on 4/11/16.
 */

var marker_list = [];

var post_marker_id = -1;    // to be returned when a marker is created
var post_marker;            // the marker to add to the map upon successful feed post

var can_place_marker = false;

function newMarker(title, lat, lon, type_of_marker) {
    $.ajax({
        url: "/markers/new_marker/",
        type: "Post",
        data: {
            title: title,
            lat: pin_latlng.lat,
            lon: pin_latlng.lng,
            type_of_marker: type_of_marker,
            csrfmiddlewaretoken: csrftoken
        },
        success: function (json) {
            pin.closePopup();
            alert('Created a ' + type_of_marker + ' marker at latitude:' + json['lat'] + ' and longitude:' + json['lon']);
            post_marker = L.marker([pin_latlng.lat, pin_latlng.lng]).setIcon(getIconType(type_of_marker));
            post_marker_id = json['marker_id'];
            pin = null;

        },
        error: function (xhr, errmsg, err) {
            alert('ERROR: ' + xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    })
}


function getAllMarkers() {
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
                    .setIcon(getIconType(marker.type_of_marker, false))
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
}
