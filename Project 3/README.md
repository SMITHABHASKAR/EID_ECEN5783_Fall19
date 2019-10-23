Installation Instructions:

sudo apt-get update
sudo apt-get upgrade
pip install aws-sdk-python
  --> unzip the folder
  --> python3 install setup.py 
  
  The project has been divided into server and client.
  Server: AWS integration + GUI+ sensor python code
  Client: HTML webserver
  
  RUN: 
  --> The sensor_aws.py on server side.
  --> html code on client side. 



Project Work:
Work breakdown Structure: https://github.com/SMITHABHASKAR/EID_ECEN5783_Fall19/blob/master/Project%203/WBS.pdf

Here the various moving parts are split and are color coordinated. 
Blue- Smitha Bhaskar
Red- Shanel Wu

Project 3 is based on integrating the AWS cloud network with the exisiting project buildup. The PyQT GUI from Project 1 and tornado Server from Project 2 are interfaced with the AWS functionalities. The AWS functionalities :
          1. AWS Lambda
          2. AWS SQS
          3. AWS SNS
The Lambda functions as a 

Project Additions:

--> Included a button on HTML to display the number of records in the Queue
--> Integrated two cloud platforms onto one device console.


Project Issues:

--> Integrating all the moving parts of AWS
--> Faced issues with the MQTT client setup on AWS


Citations:

https://learn.adafruit.com/dht?view=all#dht-circuitpython-code
https://aws.amazon.com/articles/getting-started-with-aws-and-python/
https://github.com/aws/aws-iot-device-sdk-python/issues/154
https://github.com/aws/aws-iot-device-sdk-python
https://github.com/pdeolankar/Raspberry-pi-Temperature-sensor-AWS-IoT/blob/master/egrun.py

