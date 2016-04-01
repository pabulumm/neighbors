


function showMap() {

    $('.visible').animate({'right': "-100%"}).removeClass('visible');
    $('#map-container').animate({'right': "0"}).addClass('visible');
    if (!($('#feed').hasClass('side-visible'))) {
        loadFeed();
    }
}

function loadFeed() {
    $.each(post_ids, function (index, post_id) {
        $(post_id).css('left', "-100%");
    });
    $('.side-visible').animate({'bottom': "-100%"}).removeClass('side-visible');
    $('#feed').animate({'bottom': "0"}).addClass('side-visible');

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
}

function hideListMenu() {
    $('.visible').animate({'right': "0"});
    $('.side-visible').animate({'left': "0"});
    $('#list-menu').animate({'left':"-20%"});
}


$(document).ready(function () {
    showMap();
    $('.nav-tabs a').click(function () {
        $(this).tab('show');
    });

    $('#status-button').click(function () {
        //$('.feed').animate({
        //    'marginLeft':"-100%"
        //});
        $('.visible').animate({
            'right': "-100%"
        }).removeClass('visible');

        $('#status').animate({
            'right': "0"
        }, "slow").addClass('visible');
    });
    $('#map-button').click(function () {
        showMap();
    });

    $('#account-button').click(function () {
        $('.visible').animate({
            'right': "-100%"
        }).removeClass('visible');

        $('.side-visible').animate({
            'bottom': "-100%"
        }).removeClass('side-visible');

        $('#account').animate({
            'right': "0"
        }).addClass('visible');

        $('#account-options').animate({
            'bottom': "0"
        }).addClass('side-visible');
    });

    $('#poll-select').click(function () {
        $('.visible').animate({
            'right': "-100%"
        }).removeClass('visible');

        $('.side-visible').animate({
            'bottom': "-100%"
        }).removeClass('side-visible');

        $('#poll-detail').animate({
            'right': "0"
        }).addClass('visible');

        $('#poll-menu').animate({
            'bottom': "0"
        }).addClass('side-visible');
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
















