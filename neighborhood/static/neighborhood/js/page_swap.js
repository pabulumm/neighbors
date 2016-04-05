
var nav_visible;



function showMap() {
    swapMainWindow($('#map-container'));
    if (!($('#feed').hasClass('side-visible'))) {
        loadFeed();
    }
}

function loadFeed() {
    $.each(post_ids, function (index, post_id) {
        $(post_id).css('left', "-100%");
    });
    swapSideBar($('#feed'));
    $.each(post_ids, function (index, post_id) {
        $(post_id).delay(200 * index + 500).animate({
            'left': "5%"
        })
    });
}

function showListMenu() {
    $('.visible').animate({'right': "-20%"});
    $('.side-visible').animate({'left': "20%"});
    $('#list-menu').animate({'left':"0"});
    nav_visible = true;
}

function hideListMenu() {
    $('.visible').animate({'right': "0"});
    $('.side-visible').animate({'left': "0"});
    $('#list-menu').animate({'left':"-20%"});
    nav_visible = false;
}

function swapMainWindow(id) {
    if (!(id.hasClass('visible'))) {
        $('.visible').animate({'right': "-100%"}).removeClass('visible');
        if (nav_visible) {
            id.animate({'right': "-20%"}).addClass('visible');
        }
        else {
            id.animate({'right': "0"}).addClass('visible');
        }
    }
}

function swapSideBar(id) {
    if (!(id.hasClass('side-visible'))) {
        $('.side-visible').animate({'bottom': "-100%"}).removeClass('side-visible');
        if (nav_visible) {
            id.css('left', "20%");
        }
        else {
            id.css('left', "0");
        }
        id.animate({'bottom': "0"}).addClass('side-visible');
    }
}

function toggleListMenu() {
    var menu_icon = $('#menu-icon');
    if (menu_icon.hasClass('glyphicon-remove')) {
        hideListMenu();
    }
    else {
        showListMenu();
    }
   menu_icon.toggleClass("glyphicon-list glyphicon-remove");
}

$(document).ready(function () {
    nav_visible = false;
    showMap();
    $('.nav-tabs a').click(function () {
        $(this).tab('show');
    });

    $('#status-button').click(function () {
        swapMainWindow($('#status'));
        if (!($('#feed').hasClass('side-visible'))) {
            loadFeed();
        }
    });
    $('#map-button').click(function () {
        showMap();
    });
    $('#home-select').click(function () {
        showMap();
    });

    $('#account-button').click(function () {
        swapMainWindow($('#account'));
        swapSideBar($('#account-options'));
    });

    $('#poll-select').click(function () {
        swapMainWindow($('#poll-detail'));
        swapSideBar($('#poll-menu'));
        loadFirstPoll();
    });

    $('#event-select').click(function () {
        swapMainWindow($('#event-calendar'));
        swapSideBar($('#event-detail'));
        toggleListMenu();
    });

    $('#poll-header').click(function (e) {
        e.preventDefault();
        $('.visible').animate({
            'right': "-100%"
        }).removeClass('visible');

        $('.side-visible').animate({
            'bottom': "-100%"
        }).removeClass('side-visible');

        window.location = "http://localhost:8000/polls/8/";
    });

    $('#list-menu-button').click(function() {
        var menu_icon = $('#menu-icon');
        if (menu_icon.hasClass('glyphicon-remove')) {
            hideListMenu();
        }
        else {
            showListMenu();
        }
       menu_icon.toggleClass("glyphicon-list glyphicon-remove");
    })
});
















