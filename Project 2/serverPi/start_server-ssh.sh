#!/bin/bash
python3 tornado_websocket.py &
ssh -p 22 -R swpi:80:localhost:22 serveo.net &
