/**
 * Created by tuck on 4/8/16.
 */

function checkPostViewed(feed_post_id) {
    $.ajax({
        url: '/feed/get-viewed/',
        type: 'GET',
        data: {
            feed_post_id: feed_post_id,
            csrfmiddlewaretoken: csrftoken
        },
        dataType: "json",
        success: function (data) {
            if (data.viewed == 1) { // add the date that the user viewed the post
                $('#feed-post' + feed_post_id).append('<small>Viewed on:' + data.date + '</small>');
            }
            else { // add unseen post animation to div
                $('#feed-post' + feed_post_id).append('<div id="flag' + feed_post_id + '" class="flag"><p>!</p></div>');
            }
        },
        error: function (xhr, errmsg, err) {
            alert('ERROR: ' + xhr.status + ": " + xhr.responseText + "\n\n" +
                errmsg, + "\n\n" + err);
        }
    });
}

function viewPost(post_id) {
    $.ajax({
        url: '/feed/view-post/',
        type: 'POST',
        data: {
            post_id: post_id,
            csrfmiddlewaretoken: csrftoken
        },
        dataType: 'json',
        success: function (data) {
            if (data.post_viewed == true) {
                $('#flag' + post_id).hide();
            }
        },
        error: function (xhr, errmsg, err) {
            alert('ERROR: ' + xhr.status + ": " + xhr.responseText);
        }
    });
}

function submitPost() {
    $.ajax({
        url: '/feed/submit-post/',
        type: 'POST',
        data: {
            csrfmiddlewaretoken: csrftoken
        },
        dataType: 'json',
        success: function(data) {

        },
        error: function (xhr, errmsg, err) {
            alert('ERROR: ' + xhr.status + ": " + xhr.responseText);
        }
    })

}

function createMarkerFeedPost(marker_type, post_username, post_id,
                              marker_id, marker_lat, marker_lon) {
    //alert('Received parameters: '+ marker_type + post_username+post_id+marker_id+marker_lat+marker_lon);
    var post_statement = getMarkerPostStatement(marker_type);
    var full_post_id = "#feed-post"+post_id;
    //changeElemBorderColor(full_post_id, getPostColor(marker_type));
    var src = getIconType(marker_type, true);
    var icon_img = $("<img>", {class: 'feed-post-icon', src: src});
    $(full_post_id + " .feed-item-body").append(icon_img);
    $(full_post_id + " .feed-item-body").append('<p>' + post_statement + '</p>');
    $(full_post_id).on('click', function () {
        viewPost(post_id);
        // center map on clicked post designated marker
        centerMarker([marker_lat, marker_lon]);
        // open popup descriptor
        openPop(marker_id);
    });
}

/**
 * Returns the user icon image for feed posts
 * ----- TODO should use ajax to get the specific image for the user.
 * @param post_id
 */
function getUserImage(post_id) {

    var src = '/static/markers/png/user2.png';
    var icon_img = $("<img>", {class: 'feed-post-icon', src: src});
    $(post_id + " .feed-item-body").append(icon_img);
}

function getMarkerPostStatement(type) {
    var post_statement = "Placed a new marker!";
    switch (type) {
        case 'HOUSE':
            post_statement = "A new friendly neighbor has joined the neighborhood!";
            break;
        case 'EVENT':
            post_statement = " has invited you to an event.";
            break;
        case 'YARD_SALE':
            post_statement = " is going to have a yard sale... with invaluable treasures.";
            break;
        case 'TRASH':
            post_statement = " found a piece of trash.... why? WHY?!";
            break;
        case 'CONSTRUCTION':
            post_statement = "Be cautious of new construction project.";
            break;
        case 'THEFT':
            post_statement = " has reported a crime in the area!";
            break;
        default:
            break;
    }
    return post_statement;
}

// TODO - IMPLEMENT FEED POST REFRESH WITH AJAX
$(function() {
    $('#refresh-feed').click()
});