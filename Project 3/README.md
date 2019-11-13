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

Set up the Lambda function in AWS either directly from the code in `./server/dataVsAlert_lambda.py` or by uploading the `./server/dataVsAlert_AWSLambda_deploypkg.zip` deployment package.

Run `./server/sensor_AWS.py` to start the sensor readings and AWS connection.

### Client Installation:

Download the [`client` folder](./client) and open `index.html` for the HTML interface.

## Project Work

We created a [Work Breakdown Structure](https://github.com/SMITHABHASKAR/EID_ECEN5783_Fall19/blob/master/Project%203/WBS.pdf) for this project. We color-coded the various parts, with blue corresponding to Smitha Bhaskar's work and red corresponding to Shanel Wu's work.

The end result is a cloud-based temperature/humidity sensor system managed through AWS services. Maintaining the sensor GUI from Project 1, we added an additional interface through HTML so that a remote user can access sensor readings.

## Project Additions
- Added a button for number of records in the queue
- Added two of these devices onto the same console, through the oragnization option on AWS
- Added error handling in AWS connection by providing a field for the queue URL if it was incorrect in the backend.


## Project Issues:

- **Connecting to MQTT:** Because we originally set up MQTT on one of our Pi's, but later ported it to the other Pi, we realized that we had not completely changed over the security credentials so that AWS would recognize the other PI.
- **Setting up the Lambda function:** Lambda functions have many runtime options: Node.JS, Python 3.7, Python 2.7, and many more. When we incorrectly generated a Lambda in Node.JS and then tried to switch it over to Python, there were many small formatting errors because of AWS's template generation, like in the filenames, handler names, etc. It was easier to delete the Lambda and start from scratch. In retrospect, it might have been easier to use Node.JS for the Lambda function, as the function parsed JSON's. Since we were already fairly accustomed with JSON functions in Node.JS, we had to re-learn the function names for Python.
- **Configuring Roles, Permissions, Policies:** There were a lot of permissions- and authentication-related forms to match up between AWS services, devices accessing AWS services, and our own accounts.

## References
- [AWS IoT Greengrass "Getting Started" Guide](https://docs.aws.amazon.com/greengrass/latest/developerguide/module3-II.html)
- [AWS Greengrass SDK for the Raspberry Pi's as IoT Cores](https://github.com/aws/aws-greengrass-core-sdk-python/)
- [AWS Greengrass installation through Pip](https://pypi.org/project/greengrasssdk/)
- [Publishing to SNS through AWS Lambda](https://stackoverflow.com/questions/31484868/can-you-publish-a-message-to-an-sns-topic-using-an-aws-lambda-function-backed-by)
- [Troubleshooting Pi AWS IoT Connection](https://github.com/aws/aws-iot-device-sdk-python/issues/154)
- [Sending Sensor Reading from Pi to AWS IoT](https://github.com/pdeolankar/Raspberry-pi-Temperature-sensor-AWS-IoT/blob/master/egrun.py)
