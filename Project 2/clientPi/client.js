
      // log function
      log = function(data) {
        $("div#terminal").prepend("</br>" +data);
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
        $("div#connected").hide()
 
        var ws, ws2;
        var wsopen = false;
        var ws2open = false;
        var mode = "F";

 
        $("#open").click(function(evt) {
          evt.preventDefault();
 
          var host = $("#host").val();
          var port = $("#port").val();
          var uri = $("#uri").val();
 
          // create websocket instance
          ws = new WebSocket("ws://" + host + ":" + port + uri);
           
          // Handle incoming websocket message callback
          ws.onmessage = function(evt) {
            log("Message Received: " + evt.data)
            alert("message received: " + evt.data);
            };
 
          // Close Websocket callback
          ws.onclose = function(evt) {
            log("***Connection Closed***");
            alert("Connection close");
            $("#host").css("background", "#ff0000"); 
            $("#port").css("background", "#ff0000"); 
            $("#uri").css("background",  "#ff0000");
            $("div#connected").empty();
 
            };
 
          // Open Websocket callback
          ws.onopen = function(evt) { 
            $("#host").css("background", "#00ff00"); 
            $("#port").css("background", "#00ff00"); 
            $("#uri").css("background", "#00ff00");
            log("***Connection 1 Opened***");
            $("#open").attr("disabled", true);

            wsopen = true;
            if (ws2open) {
              $("div#connected").show();
              log("**Both Connections Now Available**");
            }
          };
        });

        $("#open2").click(function(evt) {
          evt.preventDefault();
 
          var host = $("#host2").val();
          var port = $("#port2").val();
          var uri = $("#uri2").val();
 
          // create websocket instance
          ws2 = new WebSocket("ws://" + host + ":" + port + uri);
           
          // Handle incoming websocket message callback
          ws2.onmessage = function(evt) {
            log("Message Received: " + evt.data)
            alert("message received: " + evt.data);
            };
 
          // Close Websocket callback
          ws2.onclose = function(evt) {
            log("***Connection Closed***");
            alert("Connection close");
            $("#host2").css("background", "#ff0000"); 
            $("#port2").css("background", "#ff0000"); 
            $("#uri2").css("background",  "#ff0000");
            //$("div#message_details").empty();
 
            };
 
          // Open Websocket callback
          ws2.onopen = function(evt) { 
            $("#host2").css("background", "#00ff00"); 
            $("#port2").css("background", "#00ff00"); 
            $("#uri2").css("background", "#00ff00");
            log("***Connection 2 Opened***");
            $("#open2").attr("disabled", true);

            ws2open = true;
            if (wsopen) {
              $("div#connected").show();
              log("**Both Connections Now Available**"); 
            }
          };
        });
 
        // Send websocket message function
        $("#send").click(function(evt) {
            log("Sending Message to WS 1: "+$("#message").val());
            ws.send($("#message").val());
        });

        $("#send2").click(function(evt) {
            log("Sending Message to WS 2: " +$("#message").val());
            ws2.send($("#message").val());
        })

        // Poll sensor
        $("#read").click(function(evt) {
        	ws.send("read");
        	//log("Sensor reads nonsense");
        });

        // Get latest MySQL entry
        $("#get").click(function(evt) {
          ws2.send("get");
        });

        // Get latest MySQL entry
        $("#switch").click(function(evt) {
          ws.send("switch");
          ws2.send("switch");
        });
 
        // Get latest MySQL entry
        $("#network").click(function(evt) {
          ws.send("network");
          ws2.send("network");
        });
      });