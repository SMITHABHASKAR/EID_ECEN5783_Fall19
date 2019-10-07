
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

      // source: https://www.w3schools.com/php/php_ajax_database.asp
      // function showTable(str) {
      //   if (str == "") {
      //     document.getElementById("network").innerHTML = "";
      //     return;
      //   } else {
      //     if (window.XMLHttpRequest) {
      //         // code for IE7+, Firefox, Chrome, Opera, Safari
      //         xmlhttp = new XMLHttpRequest();
      //     } else {
      //         // code for IE6, IE5
      //         xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
      //     }
      //     xmlhttp.onreadystatechange = function() {
      //         if (this.readyState == 4 && this.status == 200) {
      //             document.getElementById("network").innerHTML = this.responseText;
      //         }
      //     };
      //     xmlhttp.open("GET","tables.php?q="+str,true);
      //     xmlhttp.send();
      //   }
      // }

      function loadXMLDoc()
        {
        var xmlhttp;
        if (window.XMLHttpRequest)
          {// code for IE7+, Firefox, Chrome, Opera, Safari
          xmlhttp=new XMLHttpRequest();
          }
        else
          {// code for IE6, IE5
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
          }
        xmlhttp.onreadystatechange=function()
          {
          if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
            document.getElementById("network").innerHTML=xmlhttp.responseText;
            }
          }
        xmlhttp.open("GET","128.138.189.237:8081",true);
        xmlhttp.send();
        }
 
      $(document).ready(function () {
        $("div#connected").hide()

        //https://medium.com/programmers-developers/convert-blob-to-string-in-javascript-944c15ad7d52
        const reader = new FileReader();
 
        var ws, ws2;
        var wsopen = false;
        var ws2open = false;
        var mode = "F";

        $("div#units").html("Displaying temp in degrees " + mode);

        function startTable() {
          var html = ''
            for (var i = 0; i < data.length; i++){
                // We store html as a var then add to DOM after for efficiency
                html += '<li>' + data[i].note + '</li>'
            }
            $('#network').html(html)
          }
 
        $("#open").click(function(evt) {
          evt.preventDefault();
 
          var host = $("#host").val();
          var port = $("#port").val();
          var uri = "/ws";
 
          // create websocket instance
          ws = new WebSocket("ws://" + host + ":" + port + uri);
           
          // Handle incoming websocket message callback
          ws.onmessage = function(evt) {
            log("Message Received: " + evt.data.toString());
            };
 
          // Close Websocket callback
          ws.onclose = function(evt) {
            log("***Connection Closed***");
            alert("Connection close");
            $("#host").css("background", "#ff0000"); 
            $("#port").css("background", "#ff0000"); 
            $("#uri").css("background",  "#ff0000");
            $("div#connected").empty();
            $("#open").attr("disabled", false);
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
          var uri = "/ws";
 
          // create websocket instance
          ws2 = new WebSocket("ws://" + host + ":" + port + uri);
           
          // Handle incoming websocket message callback
          ws2.onmessage = function(evt) {
            log("Message Received: " + evt.data.toString());

            //if (typeof evt.data == "Blob") {
            //   console.log("Received image, converting...");
            //   // Use createObjectURL to make a URL for the blob
            //   var image = new Image();
            //   image.src = URL.createObjectURL(evt.data);
            //   document.getElementById('graph').appendChild(image);
            // //}
            };
 
          // Close Websocket callback
          ws2.onclose = function(evt) {
            log("***Connection Closed***");
            alert("Connection close");
            $("#host2").css("background", "#ff0000"); 
            $("#port2").css("background", "#ff0000"); 
            $("#uri2").css("background",  "#ff0000");
            //$("div#message_details").empty();
            $("#open2").attr("disabled", false);
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

        // Switch units between F and C
        $("#switch").click(function(evt) {
          console.log("converting");
          //ws.send("switch");
          //ws2.send("switch");
          if (mode == "F") {
            mode = "C";
          } else if (mode == "C") {
            mode = "F";
          }
          $("div#units").html("Displaying temp in degrees " + mode);
        });
 
        // Test network latency
        $("#network").click(function(evt) {
          //ws.send("network");
          ws2.send("network");
          loadWholePage("128.138.189.237:8081");
          //$.get("128.138.189.237:8081",function(data){ $("div#network").html(data); });
          //$.ajax({ url: '128.138.189.237:8081', success: function(data) { $("div#network").html(data); } });
          //loadXMLDoc();
        });
      });


/**
  responseHTML
  (c) 2007-2008 xul.fr    
  Licence Mozilla 1.1
*/  


/**
  Searches for body, extracts and return the content
  New version contributed by users
*/


function getBody(content) 
{
   test = content.toLowerCase();    // to eliminate case sensitivity
   var x = test.indexOf("<body");
   if(x == -1) return "";

   x = test.indexOf(">", x);
   if(x == -1) return "";

   var y = test.lastIndexOf("</body>");
   if(y == -1) y = test.lastIndexOf("</html>");
   if(y == -1) y = content.length;    // If no HTML then just grab everything till end

   return content.slice(x + 1, y);   
} 

/**
  Loads a HTML page
  Put the content of the body tag into the current page.
  Arguments:
    url of the other HTML page to load
    id of the tag that has to hold the content
*/    

function loadHTML(url, fun, storage, param)
{
  var xhr = createXHR();
  xhr.onreadystatechange=function()
  { 
    if(xhr.readyState == 4)
    {
      //if(xhr.status == 200)
      {
        storage.innerHTML = getBody(xhr.responseText);
        fun(storage, param);
      }
    } 
  }; 

  xhr.open("GET", url , true);
  xhr.send(null); 

} 

  /**
    Callback
    Assign directly a tag
  */    


  function processHTML(temp, target)
  {
    target.innerHTML = temp.innerHTML;
  }

  function loadWholePage(url)
  {
    var y = document.getElementById("storage");
    var x = document.getElementById("displayed");
    loadHTML(url, processHTML, x, y);
  } 


  /**
    Create responseHTML
    for acces by DOM's methods
  */  
  
  function processByDOM(responseHTML, target)
  {
    target.innerHTML = "Extracted by id:<br />";

    // does not work with Chrome/Safari
    //var message = responseHTML.getElementsByTagName("div").namedItem("two").innerHTML;
    var message = responseHTML.getElementsByTagName("div").item(1).innerHTML;
    
    target.innerHTML += message;

    target.innerHTML += "<br />Extracted by name:<br />";
    
    message = responseHTML.getElementsByTagName("form").item(0);
    target.innerHTML += message.dyn.value;
  }
  
  function accessByDOM(url)
  {
    //var responseHTML = document.createElement("body");  // Bad for opera
    var responseHTML = document.getElementById("storage");
    var y = document.getElementById("displayed");
    loadHTML(url, processByDOM, responseHTML, y);
  } 
