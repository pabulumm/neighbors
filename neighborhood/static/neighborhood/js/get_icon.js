/**
 * Created by tuck on 3/28/16.
 */

function getIconType(type, url_only) {
    var url = "";
    switch (type) {
        case 'HOUSE':
            url = "/static/markers/png/house-38-64.png";
            break;
        case 'YARD_SALE':
            url = "/static/markers/png/sale-28-48.png";
            break;
        case 'CONSTRUCTION':
            url = "/static/markers/png/construction-28-48.png";
            break;
        case 'THEFT':
            url = "/static/markers/png/crime-28-48.png";
            break;
        case 'EVENT':
            url = "/static/markers/png/event-28-48.png";
            break;
        case 'TRASH':
            url = "/static/markers/png/trash-32.png";
            break;
        default:
            return new L.Icon.Default;
            break;
    }
    if (url_only) {
        return url;
    }
    else {
        return new L.icon({
            iconUrl: url,
            iconSize: [38, 64],
            iconAnchor: [0, 16],
            popupAnchor: [0, -16]
        });
    }
}