// Author(s): Smitha Bhaskar and Shanel Wu

const WebSocket = require('ws');
var mysql = require('mysql');

const wss = new WebSocket.Server({ port: 8080 });

var con = mysql.createConnection({
    host: "localhost",
    user: "EID",
    password: "EID",
    database: 'TEMP'
});

wss.on('connection', function connection(ws) {
    ws.on('message', function incoming(message) {
        console.log('received: %s', message);
    });

    con.connect(function(err) {
        if (err) throw err;
        console.log("Connected!");

        con.query("SELECT * FROM Sensor LIMIT 10 ;", function (err, result) {
            if (err) throw err;
            ws.send(result); //Send 10 latest tabular values
            console.log("Result: " + JSON.stringify(result));
        });

    });

    ws.send('something');
    //ws.send(JSON.stringify({topic:'test', data:'tst2'}));
});