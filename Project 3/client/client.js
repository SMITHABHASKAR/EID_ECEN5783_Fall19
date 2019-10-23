/// <reference types="aws-sdk" />
/*  
Code sources: 
-   WebSockets Server example - https://os.mbed.com/cookbook/Websockets-Server
-   SQS API for JavaScript - https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SQS.html
-   AWS Browser Script w/ JS, unauth users, and 1 other service - https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started-browser.html
Modified by: Shanel Wu
*/

// Initialize the Amazon Cognito credentials provider
AWS.config.region = 'us-west-2'; // Region
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
    IdentityPoolId: 'us-west-2:d4b53238-567d-4e08-88cf-724393cf23cd',
});

var queueURL = 'https://sqs.us-west-2.amazonaws.com/729220473028/Test1';

// log function
log = function(data) {
  $("div#terminal").prepend("</br>" + data);
  console.log(data);
};

// temperature converting functions
FtoC = function(temp_f) {
  return (temp_f - 32)*5/9
}
CtoF = function(temp_c) {
  return temp_c*9/5 + 32
}

$(document).ready(function () {
  //$("div#connected").hide()

  var connected = false;
  var mode = "F";
  var sqs;
  var queueShow = false;

  // tabular display data
  var header = "";
  var rows = [];
  var count = 0;

  var params = {
        QueueUrl: queueURL, // required
        AttributeNames: [ "All" ], // array [ name1 | name 2 | ... ]
        MaxNumberOfMessages: 10,
        MessageAttributeNames: [ "All" ],
        WaitTimeSeconds: 0
      };
  
  // create JSON parameters for receiving messages from AWS SQS
  SQSConnect();
  startTable();

  //$("h4#units").html("Displaying temp in degrees " + mode);

  function SQSConnect() {
    // create the SQS service object
    sqs = new AWS.SQS();

    // get data from SQS and display it on the webpage
    sqs.receiveMessage(params, function(err, data) {
      if (err) {
        log( [err, err.stack] );  // error occured
        connected = false;
        $("#aws").css("background", "#ff0000");
        $("#aws").attr("readonly", "false");
        $("#open").attr("disabled", "false");
      } else {
        log(data);            // success
        connected = true;
        $("#aws").css("background", "#00ff00");
        $("#aws").attr("value", "Connected!");
        $("#aws").attr("readonly", "true");
        $("#open").attr("disabled", "true");

        log(parseMessage(data));
    }});

    // if doing extra credit, use getQueueAttributes
    // queue attribute (also available from received messages) - ApproximateNumberOfMessages
    sqs.getQueueAttributes()
  }

  function parseMessage(data) {
    var message = data.Messages[0];
    var contents = {
      body: message.Body
    };
    return contents.body;
  }

  function startTable() {
    header = '<table><tr><th>Date/Time</th><th>Temperature in C</th><th>Temperature in F</th><th>Humidity</th></tr>';
    for (var i = 0; i < 20; i++){
        // We store html as a var then add to DOM after for efficiency
        rows.push('<tr><td>' + '-' + '</td><td>' + '' + '</td><td>' + '' + '</td><td>' + '' + '</td></tr>');
    }
    $('#feed').html(header + rows.join('') + '</table>');
  }

  function updateTable() {
    count++;
    var newRow = '<tr><td>' + count + '</td><td>' + '0' + '</td><td>' + '' + '</td><td>' + '' + '</td></tr>';
    
    if (count <= 20) {
      rows[count-1] = newRow; // keep filling the table
    } else {
      rows.shift(); // remove oldest entry
      rows.push(newRow);
    }
    $('#feed').html(header + rows.join('') + '</table>');
  }

  $("#open").click(function(evt) {
    evt.preventDefault();

    // var host = $("#host").val();
    // var port = $("#port").val();
    // var uri = "/ws";

    // // create websocket instance
    // ws = new WebSocket("ws://" + host + ":" + port + uri);
     
    // // Handle incoming websocket message callback
    // ws.onmessage = function(evt) {
    //   log("Message Received: " + evt.data.toString());
    //   };

    // // Close Websocket callback
    // ws.onclose = function(evt) {
    //   log("***Connection Closed***");
    //   alert("Connection close");
    //   $("#host").css("background", "#ff0000"); 
    //   $("#port").css("background", "#ff0000"); 
    //   $("#uri").css("background",  "#ff0000");
    //   $("div#connected").empty();
    //   $("#open").attr("disabled", false);
    //   };

    // // Open Websocket callback
    // ws.onopen = function(evt) { 
    //   $("#host").css("background", "#00ff00"); 
    //   $("#port").css("background", "#00ff00"); 
    //   $("#uri").css("background", "#00ff00");
    //   log("***Connection 1 Opened***");
    //   $("#open").attr("disabled", true);
    // };
  });

  // Send message function (should be disabled with permissions for unauth user)
  $("#send").click(function(evt) {
    
  });

  // Get one SQS record
  $("#getOne").click(function(evt) {
    updateTable();
  });

  // Get all SQS records in queue
  $("#getAll").click(function(evt) {
    
  });

  // Show number of records in SQS Queue
  $("#queue").click(function(evt) {
    queueShow = !queueShow;

    if (queueShow) {
      $("span#queueCount").html(
        '<label for="queueNum">Queue: </label>' +
        '<input id="queueNum" type="text" readonly="true" value="0 records">')
      $("span#queueCount").show()
      $("button#queue").html("Hide Queue Count");
    } else {
      $("span#queueCount").hide()
      $("button#queue").html("Show Queue Count");
    }
  })

  // Switch units between F and C
  $("#switch").click(function(evt) {
    $("button#switch").html("Switch to " + mode);
    if (mode == "F") {
      mode = "C";
    } else if (mode == "C") {
      mode = "F";
    }
    $("input#currTemp").attr("value", '0 \xB0' + mode);
  });
});
