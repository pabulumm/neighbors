/**
 * Created by tuck on 3/28/16.
 */

function getIconType(type, url_only) {
    var url = "";
    switch (type) {
        case 'HOUSE':
            url = "/static/markers/png/house-28-48-cust1.png";
            break;
        case 'YARD_SALE':
            url = "/static/markers/png/sale-28-48-cust1.png";
            break;
        case 'CONSTRUCTION':
            url = "/static/markers/png/construction-28-48-cust1.png";
            break;
        case 'THEFT':
            url = "/static/markers/png/crime-28-48-cust1.png";
            break;
        case 'EVENT':
            url = "/static/markers/png/event-28-48-cust1.png";
            break;
        case 'COMMENT':
            url = "/static/markers/png/comment-location-28-48.png";
            break;
        case 'TRASH':
            url = "/static/markers/png/trash-24.png";
            if (!url_only) {
                return new L.icon({
                    iconUrl: url,
                    iconSize: [24, 24],
                    iconAnchor: [12, 12],
                    popupAnchor: [0, -12]
                });
            }
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
            iconSize: [28, 48],
            iconAnchor: [14, 48],
            popupAnchor: [0, -48]
        });
    }
}