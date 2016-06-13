var nav_visible;

function setDemoSettings(memberStatus) {
    if (memberStatus == 'demo') {
        $('.add-content-button').each(function() {
            $(this).css('data-target', '#demoModal');
        })
    }
}

function showMap() {
    swapMainWindow($('#map-container'));
    if (!($('#feed').hasClass('side-visible'))) {
        //refresh-feed();
        loadFeed();
    }
}

function loadFeed() {
    console.log('Loading FeedPosts');
    $.each(post_ids, function (index, post_id) {
        $(post_id).css('left', "-100%");
    });
    swapSideBar($('#feed'));
    $.each(post_ids, function (index, post_id) {
        $('#feed-post' + post_id).delay(200 * index + 500).animate({
            'left': "5%"
        })
    });
}

function showListMenu() {
    $('.visible').animate({'right': "0", 'width': "55%"});
    $('.side-visible').animate({'left': "20%", 'width': "25%"});
    $('#list-menu').animate({'left': "0"});
    nav_visible = true;
}

function hideListMenu() {
    $('.visible').animate({'right': "0", 'width': "75%"});
    $('.side-visible').animate({'left': "0", 'width': "25%"});
    $('#list-menu').animate({'left': "-20%"});
    nav_visible = false;
}


/**
 * swapMainWindow -
 * Swaps the current main window with the new window to display.
 * The main window is the detail/list section of the display occupying
 * the right 75% of the screen with site-nav hidden and 55% when visible.
 * @param id
 */
function swapMainWindow(id) {
    if (!(id.hasClass('visible'))) {
        $('.visible').animate({'right': "-100%"}).removeClass('visible');
        if (nav_visible) {
            id.animate({'margin-right': "0", 'width': "55%"});
        }
        else {
            id.animate({'margin-right': "0", 'width': "75%"});
        }
        id.show().animate({'right': "0"}).addClass('visible');
    }
}


/**
 * swapSideBar -
 * Swaps the current side bar div with the new sidebar div to display based
 * on user nav selection.
 * Always uses 25% of screen to left of main window div.
 * @param id
 */
function swapSideBar(id) {
    if (!(id.hasClass('side-visible'))) {
        $('.side-visible').animate({'bottom': "-100%"}).hide().removeClass('side-visible');
        if (nav_visible) {
            id.css({'left': "20%", 'width': "25%"});
        }
        else {
            id.css({'left': "0", 'width': "25%"});
        }
        id.show().animate({'bottom': "0"}).addClass('side-visible');
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

$('#toggle-user-post').click(function () {
    var toggle = $('#toggle-post-icon');
    if (toggle.hasClass('glyphicon-menu-up')) {
        $('#feed-header').animate({height: 70});
        $('#user-post').hide().addClass('user-post-invis');
    }
    else {
        $('#feed-header').animate({'height': "260px"}, 'slow');
        $('#user-post').show().removeClass('user-post-invis');
    }

    toggle.toggleClass("glyphicon-menu-up glyphicon-menu-down");
});


$(document).ready(function () {
    nav_visible = false;
    showMap();

    $('.nav-tabs a').click(function () {
        $(this).tab('show');
    });

    $('.menu-option button').hover(function () {
        $(this).stop().animate({
            'opacity': 1,
            'font-size': "25px"
        }, 300);
    }, function () {
        $(this).stop().animate({
            'opacity': 0.6,
            "font-size": '20px'
        }, 100);
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
        toggleListMenu();
    });

    $('#account-select').click(function () {
        swapMainWindow($('#account'));
        swapSideBar($('#account-options'));
        toggleListMenu();
    });

    $('#poll-select').click(function () {
        swapMainWindow($('#poll-main'));
        swapSideBar($('#poll-sidebar'));
        toggleListMenu();

    });

    $('#info-select').click(function () {
        swapMainWindow($('#info-main'));
        swapSideBar($('#info-sidebar'));
        toggleListMenu();
    });
    $('#event-select').click(function () {
        swapMainWindow($('#event-calendar'));
        swapSideBar($('#event-detail-sidebar'));
        toggleListMenu();
    });

    $('#announce-index').click(function () {
        //getAnnouncements();
        swapMainWindow($('#announcement-main'));
        swapSideBar($('#announcement-sidebar'));
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

    $('#list-menu-button').click(function () {
        var menu_icon = $('#menu-icon');
        if (menu_icon.hasClass('glyphicon-remove')) {
            hideListMenu();
        }
        else {
            showListMenu();
        }
        menu_icon.toggleClass("glyphicon-list glyphicon-remove");
    });

    $('.info-section-pill').click(function () {
        if (!$(this).hasClass('info-active')) {
            $('.info-active').removeClass('info-active');
            $(this).addClass('info-active');
            //$(this).tab('show');
        }
    });

    $('.info-section-pill a').click(function () {
        if (!$(this).parent().hasClass('info-active')) {
            $(this).tab('show');
        }
    });

// When new poll is created we reload the home page and
// swap the page to the events section
    $('#new-poll-form').bind('ajax:complete', function () {
        swapMainWindow($('#poll-main'));
        swapSideBar($('#poll-sidebar'));
    });

    $('#datetimepicker1').datetimepicker({
        format: "YY-MM-DD HH:mm:ss",
        defaultDate: "2016-01-01 00:00:00",
    });
    $('#datetimepicker2').datetimepicker({
        useCurrent: false, //Important! See issue #1075
        format: "YY-MM-DD HH:mm:ss",
        defaultDate: "2016-01-02 00:00:00"
    });
    $("#datetimepicker1").on("dp.change", function (e) {
        $('#datetimepicker2').data("DateTimePicker").minDate(e.date);
    });
    $("#datetimepicker2").on("dp.change", function (e) {
        $('#datetimepicker1').data("DateTimePicker").maxDate(e.date);
    });

});












