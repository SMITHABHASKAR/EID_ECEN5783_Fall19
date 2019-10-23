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
  startTable();

  $("h4#units").html("Displaying temp in degrees " + mode);

  function SQSRead() {
    // create JSON parameters for receiving messages from AWS SQS
    var readParams = {
      QueueUrl: 'STRING_VALUE', // required
      AttributeNames: [], // array [ name1 | name 2 | ... ]
      MaxNumberOfMessages: 1,
      MessageAttributeNames: [],
      ReceiveRequestAttemptId: 'STRING_VALUE',
      VisibilityTimeout: 100,
      WaitTimeSeconds: 15
    };

    // fill in params from user input

    // create the SQS service object
    var sqs = new AWS.SQS();

    // get data from SQS and display it on the webpage
    sqs.receiveMessage(params, function(err, data) {
      if (err) {
        console.log(err, err.stack);  // error occured
        connected = false;
      } else {
        console.log(data);            // success
        connected = true;
    }});

    // if doing extra credit, use queue get attributes?
  }

  function startTable() {
    var html = '<table><tr><th>Date/Time</th><th>Temperature in C</th><th>Temperature in F</th><th>Humidity</th></tr>';
    for (var i = 0; i < 20; i++){
        // We store html as a var then add to DOM after for efficiency
        html += '<tr><td>' + 0 + '</td><td>' + 0 + '</td><td>' + 0 + '</td><td>' + 0 + '</td></tr>';
    }
    html += '</table>';
    $('#feed').html(html);
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
    
  });

  // Get all SQS records in queue
  $("#getAll").click(function(evt) {
    
  });

  // Switch units between F and C
  $("#switch").click(function(evt) {
    $("button#switch").html("Switch to " + mode);
    if (mode == "F") {
      mode = "C";
    } else if (mode == "C") {
      mode = "F";
    }
    $("h4#units").html("Displaying temp in degrees " + mode);
  });
});
