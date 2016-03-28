$(document).ready(function(){
        $('#map-container').animate({
            'right':"0"
        }).addClass('visible');

        $('#feed').animate({
            'bottom':"0"
        }).addClass('side-visible');


    $('#status-button').click(function(){
        //$('.feed').animate({
        //    'marginLeft':"-100%"
        //});
        $('.visible').animate({
            'right':"-100%"
        }).removeClass('visible');

        $('#status').animate({
            'right': "0"
        }, "slow").addClass('visible');
    });
    $('#map-button').click(function(){

        $('.visible').animate({
            'right':"-100%"
        }).removeClass('visible');

        $('.side-visible').animate({
            'bottom':"-100%"
        }).removeClass('side-visible');


        $('#map-container').animate({
            'right':"0"
        }).addClass('visible');

        $('#feed').animate({
            'bottom':"0"
        }).addClass('side-visible');

    });

    $('#account-button').click(function(){
        $('.visible').animate({
            'right':"-100%"
        }).removeClass('visible');

        $('.side-visible').animate({
            'bottom':"-100%"
        }).removeClass('side-visible');

        $('#account').animate({
            'right':"0"
        }).addClass('visible');

        $('#account-options').animate({
            'bottom':"0"
        }).addClass('side-visible');
    });

    $('#poll-select').click(function(){
        $('.visible').animate({
            'right':"-100%"
        }).removeClass('visible');

        $('.side-visible').animate({
            'bottom':"-100%"
        }).removeClass('side-visible');

        $('#poll-detail').animate({
            'right':"0"
        }).addClass('visible');

        $('#poll-menu').animate({
            'bottom':"0"
        }).addClass('side-visible');
    });

    $('#poll-header').click(function(e) {
        e.preventDefault();
        $('.visible').animate({
            'right':"-100%"
        }).removeClass('visible');

        $('.side-visible').animate({
            'bottom':"-100%"
        }).removeClass('side-visible');

        window.location = "http://localhost:8000/polls/8/";
    })
});
















