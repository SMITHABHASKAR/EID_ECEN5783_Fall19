# EID Project 3 - Cloud-Based Temperature/Humidity System

Developers: Smitha Bhaskar and Shanel Wu
Instructor: Bruce Montgomery
Fall 2019, University of Colorado Boulder

## Installation Instructions

### Hardware Requirements:
- Raspberry Pi (server and AWS IoT Greengrass Core)
- Another computer (client)
- DHT22 temperature/humidity sensor and circuit

### Server Installation:

Install the following software packages/libraries:
- `apt-get`: mysql (from Projects 1 & 2)
- `pip`: mysql, adafruit_DHT, pyqt5 (from Projects 1 & 2)
- `npm`: aws-sdk

Follow the instructions from Amazon Web Services (AWS) to [set up AWS IoT Greengrass on the Raspberry Pi.](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-gs.html) (Modules 1-3)

### Client Installation:

Download the [`client` folder](./client) and open `index.html` for the HTML interface.

## Project Work

We created a [Work Breakdown Structure](https://github.com/SMITHABHASKAR/EID_ECEN5783_Fall19/blob/master/Project%203/WBS.pdf) for this project. We color-coded the various parts, with blue corresponding to Smitha Bhaskar's work and red corresponding to Shanel Wu's work.

The end result is a cloud-based temperature/humidity sensor system managed through AWS services. Maintaining the sensor GUI from Project 1, we added an additional interface through HTML so that a remote user can access sensor readings.

## Project Additions
--> Added a button for no. of records in the queue
--> Added two of these devices onto the same console, through the oragnization option on AWS


## Project Issues:

--> Had issues in connecting the MQTT
--> Setting up the Lambda rule

## References
https://docs.aws.amazon.com/greengrass/latest/developerguide/module3-II.html
https://github.com/aws/aws-greengrass-core-sdk-python/
https://pypi.org/project/greengrasssdk/
https://stackoverflow.com/questions/31484868/can-you-publish-a-message-to-an-sns-topic-using-an-aws-lambda-function-backed-by
https://stackoverflow.com/questions/31484868/can-you-publish-a-message-to-an-sns-topic-using-an-aws-lambda-function-backed-by
https://github.com/aws/aws-iot-device-sdk-python/issues/154
https://github.com/pdeolankar/Raspberry-pi-Temperature-sensor-AWS-IoT/blob/master/egrun.py
