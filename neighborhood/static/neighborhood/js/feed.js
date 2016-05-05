/**
 * Created by tuck on 4/8/16.
 */


var poll_ids = [];
var post_ids = [];

function newPostId(id) {
    post_ids.push(id);
    return id;
}

function newPollId(id) {
    poll_ids.push(id);
    return id;
}

// adds a decorative banner strip to the top of the post
// div if it is of special type. i.e. ANNOUNCEMENT or POLL
function addPostBanner(post_id, post_type) {
    if (post_type == 'ANNOUNCEMENT') {
        $('#feed-post'+post_id).append(
            '<div class="post-tag-container">' +
            '<p class="post-tag">announcement</p></div>'
        )
    }
    else if (post_type == 'POLL') {
        $('#feed-post'+post_id).append(
            '<div class="post-tag-container" style="background:#c94e50">' +
            '<p class="post-tag">pending decision</p></div>'
        );
    }
}

var confirm_post_phrase = "Are you sure the marker you've chosen is of the correct type and in the correct place?";
function submitPost() {
    console.log('Called submit post!');
    if (can_place_marker && confirm(confirm_post_phrase)) {
        var text = $('#post-text').val();
        newMarker(text, function(result) {
            if (result > 0) {
                console.log('newMarker returned marker id: ' + result);
                $.ajax({
                    url: '/feed/submit-post/',
                    type: 'POST',
                    data: {
                        'text': text,
                        'has_marker': 1,
                        'marker_id': result,
                        'post_type': 'POST-MARKER',
                        csrfmiddlewaretoken: csrftoken
                    },
                    dataType: 'json',
                    success: function (data) {
                        if (!data.success) {
                            console.log('AJAX: New Feed creation successful');
                            $('#post-text').val('');
                            location.reload();
                        }
                    },
                    error: function (xhr, errmsg, err) {
                        alert('ERROR: ' + xhr.status + ": " + xhr.responseText);
                    }
                });
            }
        });

    }
    else {
        $.ajax({
            url: '/feed/submit-post/',
            type: 'POST',
            data: {
                'text': $('#post-text').val(),
                'has_marker': 0,
                'marker_id': -1,
                'post_type': 'POST-NORMAL',
                csrfmiddlewaretoken: csrftoken
            },
            dataType: 'json',
            success: function (data) {
                if (!data.success) {
                    console.log('AJAX: New Feed creation successful');
                    $('#post-text').val('');
                    location.reload();
                }
            },
            error: function (xhr, errmsg, err) {
                alert('ERROR: ' + xhr.status + ": " + xhr.responseText);
            }
        });
    }

}


function createMarkerFeedPost(marker_type, post_id, post_text,
                              marker_id, marker_lat, marker_lon) {
    console.log('createMarkerFeedPost: Received parameters: '+ marker_type+post_id+marker_id+marker_lat+marker_lon);
    var post_statement;
    //if (post_text.length < 1 ) {
    //    post_statement = getMarkerPostStatement(marker_type);
    //}
    //else {
    //    post_statement = post_text;
    //}
    //
    console.log(post_text);
    post_statement = post_text;
    var full_post_id = "#feed-post" + post_id;
    //changeElemBorderColor(full_post_id, getPostColor(marker_type));
    var src = getIconType(marker_type, true);
    var icon_img = $("<img>", {class: 'feed-post-icon', src: src});
    $(full_post_id + " .feed-item-body").append(icon_img);
    console.log('appending post statment: ' + post_statement);
    $(full_post_id + " .feed-item-body").append('<p>' + post_statement + '</p>');
    console.log('Appended statement to: '+full_post_id + " .feed-item-body");
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
    var icon_img = $("<img>", {class: 'feed-post-user-icon', src: src});
    $(post_id+' .feed-item-body').append(icon_img);
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

function getAnnouncements() {
    $('#accouncement-main').html('');
    $.ajax({
        url: '/feed/get-announcements/',
        type: 'GET',
        data: {
            csrfmiddlewaretoken: csrftoken
        },
        dataType: 'json',
        success: function(data) {
            console.log('AJAX: FeedPosts received from server');
            if (!data.announcements) {
                $('#accouncement-main').append('<p>No posts to display :(</p>');
            }
            else {
                $.each(data.announcements, function(index, post) {
                    console.log('Appending announcement with date ' + post.date
                        + ' and user' + post.user + ' and text ' + post.text);
                    $('#accouncement-main').append(
                        '<div class="announcement-item-container">'
                        + '<div class="announcement-item"><h1>'
                        + post.text + '</h1><small>' + post.date
                        + '</small><strong>' + post.user
                        + '</strong></div></div>'
                    );
                })
            }
        },
        error: function (xhr, errmsg, err) {
            alert('ERROR: ' + xhr.status + ": " + xhr.responseText);
        }
    });
}


$(document).ready(function() {
    $('.vote-confirm').click(function() {
        var poll_id = +this.id;
        if (confirm("AGREE: Are you sure?")) {
            console.log("CONFIRM VOTE for poll: " + poll_id);
            pollVote(poll_id, "CONFIRM");
        }
    });
    $('.vote-deny').click(function() {
        var poll_id = +this.id;
        if (confirm("DISAGREE: Are you sure?")) {
            console.log("DENY VOTE for poll: " + poll_id);
            pollVote(poll_id, "DENY");
        }
    })
});


//
//function checkPostViewed(feed_post_id) {
//    $.ajax({
//        url: '/feed/get-viewed/',
//        type: 'GET',
//        data: {
//            feed_post_id: feed_post_id,
//            csrfmiddlewaretoken: csrftoken
//        },
//        dataType: "json",
//        success: function (data) {
//            if (data.viewed == 1) { // add the date that the user viewed the post
//                $('#feed-post' + feed_post_id).append('<small class="viewed-date">Viewed on:' + data.date + '</small>');
//            }
//            else { // add unseen post animation to div
//                //$('#feed-post' + feed_post_id).append('<div id="flag' + feed_post_id + '" class="flag"><p>!</p></div>');
//            }
//        },
//        error: function (xhr, errmsg, err) {
//            alert('ERROR: ' + xhr.status + ": " + xhr.responseText + "\n\n" +
//                errmsg, +"\n\n" + err);
//        }
//    });
//}
//
//function viewPost(post_id) {
//    $.ajax({
//        url: '/feed/view-post/',
//        type: 'POST',
//        data: {
//            post_id: post_id,
//            csrfmiddlewaretoken: csrftoken
//        },
//        dataType: 'json',
//        success: function (data) {
//            if (data.post_viewed == true) {
//                $('#flag' + post_id).hide();
//            }
//        },
//        error: function (xhr, errmsg, err) {
//            alert('ERROR: ' + xhr.status + ": " + xhr.responseText);
//        }
//    });
//}

//function replaceFeedPost(post_id_val, post_id_lab, post_type, user_name, text, date) {
//
//    // add post id to the current list
//    newPostId(post_id_val);
//
//    // check if the post has already been viewed or not to determine unseen flag state.
//    checkPostViewed(post_id_val);
//    console.log('preparing to append.');
//    // create the div w/ contents
//    $(post_id_lab).append(
//        + '<small id="time-stamp">' + date + '</small>'
//        + '<div class="feed-item-body">'
//        + '<small class="feed-post-name"><strong>' + user_name + '</strong></small>'
//        + '<small> on '+date+'</small>'
//        + '<p id="text">' + text + '</p>'
//        + '</div>'
//    );
//    console.log('Shoulda been did bout now');
//    if (post_type == 'POLL') {
//        $(post_id_lab).append(
//            '<button id="" class="vote-yes">Yes</button>',
//            '<button id="" class="vote-no">No</button>'
//        )
//    }
//    $(post_id_lab).on('click', function () {
//        viewPost(post_id_val);
//    });
//    $(post_id_lab).css({
//        'left': "5%"
//    });
//    console.log('Replaced display div for feed post div ID: ' + post_id_lab);
//}