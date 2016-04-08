/**
 * Created by tuck on 4/4/16.
 */
function changeElemBorderColor(elem_id, color) {
    switch (color) {
        case 'GREEN':
            $(elem_id).css({
                '-webkit-box-shadow': '0 0 4px 2px rgba(22,234,156,1)',
                '-moz-box-shadow': '0 0 4px 2px rgba(22,234,156,1)',
                'box-shadow': '0 0 4px 2px rgba(22,234,156,1)'
            });
            break;
        case 'RED':
            $(elem_id).css({
                '-webkit-box-shadow': '0 0 4px 2px rgba(201,78,80,1)',
                '-moz-box-shadow': '0 0 4px 2px rgba(201,78,80,1)',
                'box-shadow': '0 0 4px 2px rgba(201,78,80,1)'
            });
            break;
        case 'BLUE':
            $(elem_id).css({
                '-webkit-box-shadow': '0 0 4px 2px rgba(10,104,245,1)',
                '-moz-box-shadow': '0 0 4px 2px rgba(10,104,245,1)',
                'box-shadow': '0 0 4px 2px rgba(10,104,245,1)'
            });
            break;
        case 'LIGHT-BLUE':
            $(elem_id).css({
                '-webkit-box-shadow': '0 0 4px 2px rgba(94,236,255,1)',
                '-moz-box-shadow': '0 0 4px 2px rgba(94,236,255,1)',
                'box-shadow': '0 0 4px 2px rgba(94,236,255,1)'
            });
            break;
        case 'YELLOW':
            $(elem_id).css({
                '-webkit-box-shadow': '0 0 4px 2px rgba(241,247,153,1)',
                '-moz-box-shadow': '0 0 4px 2px rgba(241,247,153,1)',
                'box-shadow': '0 0 4px 2px rgba(241,247,153,1)'
            });
            break;
        case 'ORANGE':
            $(elem_id).css({
                '-webkit-box-shadow': '0 0 4px 2px rgba(255,177,94,1)',
                '-moz-box-shadow': '0 0 4px 2px rgba(255,177,94,1)',
                'box-shadow': '0 0 4px 2px rgba(255,177,94,1)'
            });
            break;
        default:
            $(elem_id).css({
                '-webkit-box-shadow': '0 0 4px 2px rgba(50,50,50,1)',
                '-moz-box-shadow': '0 0 4px 2px rgba(50,50,50,1)',
                'box-shadow': '0 0 4px 2px rgba(50,50,50,1)'
            });
            break;

    }
}

function getPostColor(marker_type) {
    var color = 'DEFAULT';
    switch (marker_type) {
        case 'HOUSE':
            color = 'LIGHT-BLUE';
            break;
        case 'EVENT':
            color = 'RED';
            break;
        case 'YARD_SALE':
            color = 'YELLOW';
            break;
        case 'TRASH':
            break;
        default:
            break;
    }
    return color;
}

function getMarkerPostStatement(username, type) {
    var post_statement = "<strong>" + username + "</strong>" + " placed a new marker!";
    switch (type) {
        case 'HOUSE':
            post_statement = "A new friendly neighbor has joined the neighborhood!";
            break;
        case 'EVENT':
            post_statement = "<strong>" + username + "</strong>" + " has invited you to an event.";
            break;
        case 'YARD_SALE':
            post_statement = "<strong>" + username + "</strong>" + " is going to have a yard sale... with invaluable treasures.";
            break;
        case 'TRASH':
            post_statement = "<strong>" + username + "</strong>" + " found a piece of trash.... why? WHY?!";
            break;
        case 'CONSTRUCTION':
            post_statement = "Be cautious of new construction project.";
            break;
        case 'THEFT':
            post_statement = "<strong>" + username + "</strong>" + "has reported a crime in the area!";
            break;
        default:
            break;
    }
    return post_statement;
}


$(function () {
    alert('coloring');
    $.each(post_ids, function (index, id) {
        //$(id).css({
        //    'background': "rgba(158, 236, 255, 1)",
        //    'background': "-moz-linear-gradient(left, rgba(158, 236, 255, 1) 0%, rgba(189, 215, 255, 1) 100%",
        //    'background': "-webkit-gradient(left top, right top, color-stop(0%, rgba(158, 236, 255, 1)), color-stop(100%, rgba(189, 215, 255, 1))",
        //    'background': "-webkit-linear-gradient(left, rgba(158, 236, 255, 1) 0%, rgba(189, 215, 255, 1) 100%",
        //    'background': "-o-linear-gradient(left, rgba(158, 236, 255, 1) 0%, rgba(189, 215, 255, 1) 100%",
        //    'background': "-ms-linear-gradient(left, rgba(158, 236, 255, 1) 0%, rgba(189, 215, 255, 1) 100%",
        //    'background': "linear-gradient(to right, rgba(158, 236, 255, 1) 0%, rgba(189, 215, 255, 1) 100%",
        //    'filter': "progid:DXImageTransform.Microsoft.gradient(startColorstr='#9eecff', endColorstr='#bdd7ff', GradientType=1"
        //})
        $(id).addClass('blue-gradient');
    });


});