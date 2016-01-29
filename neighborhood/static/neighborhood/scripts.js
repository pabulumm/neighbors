/**
 * Created by tuck on 1/29/16.
 */

var main = function() {

	$('.nav-tabs a').click(function(){
        $(this).tab('show');
    });
}

$(document).ready(main);