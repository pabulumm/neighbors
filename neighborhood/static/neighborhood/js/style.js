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
        case 'ORANGE':
            break;
        default:
            $(elem_id).css({
                '-webkit-box-shadow': '0 0 4px 2px rgba(50,50,50,50.42)',
                '-moz-box-shadow': '0 0 4px 2px rgba(50,50,50,50.42)',
                'box-shadow': '0 0 4px 2px rgba(50,50,50,50.42)'
            });
            break;

    }
}

