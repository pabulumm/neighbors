/**
 * Created by tuck on 3/27/16.
 */
google.charts.load('current', {'packages': ['corechart']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {

    var data1 = google.visualization.arrayToDataTable([
        ['Type', 'Cost per Month'],
        ['Landscaping', 1200.00],
        ['Improvements', 4000.00],
        ['Labor', 2000.00],
        ['Repair', 600.00],
        ['Maintenance', 1700.00]
    ]);

    var options1 = {
        title: 'Neighborhood Expenses'
    };

    var data2 = google.visualization.arrayToDataTable([
        ['Year', 'Sales', 'Expenses'],
        ['2004', 1000, 400],
        ['2005', 1170, 460],
        ['2006', 660, 1120],
        ['2007', 1030, 540]
    ]);

    var options2 = {
        title: 'Company Performance',
        curveType: 'function',
        legend: {position: 'bottom'}
    };

    var chart1 = new google.visualization.PieChart(document.getElementById('piechart'));
    var chart2 = new google.visualization.LineChart(document.getElementById('linechart'));

    function selectHandler() {
      var selectedItem = chart1.getSelection()[0];
      if (selectedItem) {
        var category = data.getValue(selectedItem.row, 0);
        alert('The user selected ' + category);
      }
    }

    function readyHandler() {

    }

    google.visualization.events.addListener(chart1, 'select', selectHandler);
    google.visualization.events.addListener(chart1, 'ready', readyHandler);

    chart1.draw(data1, options1);
    chart2.draw(data2, options2);
}



$(document).ready(function() {
    $('#linechart').hide();
    $('#piechart').show();

    function toggle_visibility(id1, id2) {
        var e = document.getElementById(id1);
        var e2 = document.getElementById(id2);
        if (e.style.display == 'block') {
            e.style.display = 'block';
            e2.style.display = 'none';
        }
        else {
            e.style.display = 'none';
            e2.style.display = 'block';
        }
    }
    $('#history-chart').on('click', function() {
        toggle_visibility('piechart', 'linechart');
    });

    $('#expense-chart').on('click', function() {
        toggle_visibility('piechart', 'linechart');
    });
})