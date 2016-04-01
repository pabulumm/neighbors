/**
 * Created by tuck on 3/28/16.
 */

function getIconType(type, url_only) {
    var url = "";
    switch (type) {
        case 'HOUSE':
            url = "/static/markers/png/house-32.png";
            break;
        case 'YARD_SALE':
            url = "/static/markers/png/shopping-tag-32.png";
            break;
        case 'CONSTRUCTION':
            url = "/static/markers/png/bulldozer-32.png";
            break;
        case 'THEFT':
            url = "/static/markers/png/burglar-32.png";
            break;
        case 'EVENT':
            url = "/static/markers/png/event-32.png";
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
            iconSize: [32, 32],
            iconAnchor: [16, 16],
            popupAnchor: [0, -16]
        });
    }
}

