/**
 * Created by tuck on 4/8/16.
 */
//var colors = [
//    [62, 35, 255],
//    [60, 255, 60],
//    [255, 35, 98],
//    [45, 175, 230],
//    [255, 0, 255],
//    [255, 128, 0]
//];

var colors = [
    [255,41,95], // #ff295f - red
    [133,34,214], //# #b940ff - purple
    [10,104,245], // #0a68f5 - blue
    [0,174,255] // #00aeff - light blue
];



var step = 0;
//color table indices for:
// current color left
// next color left
// current color right
// next color right
var colorIndices = [0, 1, 2, 3];

//transition speed
var gradientSpeed = 0.002;

function updateGradient() {

    if ($ === undefined) return;

    var c0_0 = colors[colorIndices[0]];
    var c0_1 = colors[colorIndices[1]];
    var c1_0 = colors[colorIndices[2]];
    var c1_1 = colors[colorIndices[3]];

    var istep = 1 - step;
    var r1 = Math.round(istep * c0_0[0] + step * c0_1[0]);
    var g1 = Math.round(istep * c0_0[1] + step * c0_1[1]);
    var b1 = Math.round(istep * c0_0[2] + step * c0_1[2]);
    var color1 = "rgb(" + r1 + "," + g1 + "," + b1 + ")";

    var r2 = Math.round(istep * c1_0[0] + step * c1_1[0]);
    var g2 = Math.round(istep * c1_0[1] + step * c1_1[1]);
    var b2 = Math.round(istep * c1_0[2] + step * c1_1[2]);
    var color2 = "rgb(" + r2 + "," + g2 + "," + b2 + ")";

    $('.flag').css({
        background: "-webkit-gradient(linear, left top, right top, from(" + color1 + "), to(" + color2 + "))"
    }).css({
        background: "-moz-linear-gradient(left, " + color1 + " 0%, " + color2 + " 100%)"
    });

    step += gradientSpeed;
    if (step >= 1) {
        step %= 1;
        colorIndices[0] = colorIndices[1];
        colorIndices[2] = colorIndices[3];

        //pick two new target color indices
        //do not pick the same as the current one
        colorIndices[1] = ( colorIndices[1] + Math.floor(1 + Math.random() * (colors.length - 1))) % colors.length;
        colorIndices[3] = ( colorIndices[3] + Math.floor(1 + Math.random() * (colors.length - 1))) % colors.length;

    }
}

setInterval(updateGradient, 5);

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
