/**
 * Created by manuel on 5/8/38.
 */

// Load the Visualization API and the piechart package.
google.charts.load('current', {'packages': ['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

function reformatData3(jsonData){
    var temp = jsonData.LikesDate;
    console.log("temp: " + JSON.stringify(temp));
    var result = [];
    var i;
    var row;
    for (i=0; i < temp.length; ++i){
        row= temp[i]
        dataElement = [];
        dataElement.push(row.date);
        dataElement.push(row.count);
        result.push(dataElement);
    }
    console.log("Data: " + JSON.stringify(result));
    return result;
}

function drawChart() {
    var jsonData = $.ajax({
        url: "http://chatapp.us-east-1.elasticbeanstalk.com/ChatApp/likes/date",
        dataType: "json",
        async: false
    }).responseText;

    console.log("jsonData: " + JSON.parse(jsonData));

    // Create our data table out of JSON data loaded from server.
    var data3 = new google.visualization.DataTable();
    data3.addColumn('string', 'Parts');
    data3.addColumn('number', 'Stock');
    data3.addRows(reformatData3(JSON.parse(jsonData)));

    var options3 = {
        title: 'Likes per day last 7 days',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Total Number',
            minValue: 0
        },
        vAxis: {
            title: 'Part'
        }
    };

    var chart3 = new google.visualization.PieChart(document.getElementById('chart3_div'));

    chart3.draw(data3, options3);

}


google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawChart);


