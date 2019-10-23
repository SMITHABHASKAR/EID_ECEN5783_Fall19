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



## Project Issues:

## References
