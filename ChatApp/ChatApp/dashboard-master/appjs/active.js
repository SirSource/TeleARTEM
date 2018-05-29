/**
 * Created by manuel on 5/8/58.
 */

// Load the Visualization API and the piechart package.
google.charts.load('current', {'packages': ['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

function reformatData5(jsonData){
    var temp = jsonData.TopUsers;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        dataElement.push(row.id);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function drawChart() {
    var jsonData = $.ajax({
        url: "http://127.0.0.1:5000/ChatApp/messages/topusers",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data5 = new google.visualization.DataTable();
    data5.addColumn('string', 'Parts');
    data5.addColumn('number', 'Stock');
    data5.addRows(reformatData5(JSON.parse(jsonData)));

    var options5 = {
        title: 'Top 10 Users last 7 days',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Number',
            minValue: 0
        },
        vAxis: {
            title: 'Part'
        }
    };

    var chart5 = new google.visualization.PieChart(document.getElementById('chart5_div'));

    chart5.draw(data5, options5);

}


google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawChart);


