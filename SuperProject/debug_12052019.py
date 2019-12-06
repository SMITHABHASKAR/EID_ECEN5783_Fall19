Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py 
ready to connect
connecting to fake loom
making connection request
connecting to loom at  127.0.0.1 : 1337
1
2
connection successful! enabling functions
sending connect packets to loom
LoomControl: sending  b'\x04\x0e'
GUI: connection successful
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
pattern row: [True, True, True, False]
LoomControl: sending  bytearray(b'\x05\x02\x00\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 0
placing marker on row 0
created marker at 60
<class 'AttributeError'> 'NoneType' object has no attribute 'height' <traceback object at 0x000001E3CE72C348>
Traceback (most recent call last):
  File "C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py", line 354, in updateLoomState
    self.advance()
  File "C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py", line 386, in advance
    self.sendToLoom()
  File "C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py", line 409, in sendToLoom
    self.ui.project.placeMarker(self.lineNumber)
  File "C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\weavingWidgets.py", line 183, in placeMarker
    ym = (self.design.height() - row - 1) * self.blockSize # rows are numbered from bottom to top, marker should start on bottom of image
AttributeError: 'NoneType' object has no attribute 'height'

=============================== RESTART: Shell ===============================
>>> 
 RESTART: C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py 
ready to connect
connecting to fake loom
making connection request
connecting to loom at  127.0.0.1 : 1337
1
2
connection successful! enabling functions
sending connect packets to loom
LoomControl: sending  b'\x04\x0e'
GUI: connection successful
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
pattern row: [True, True, False]
LoomControl: sending  bytearray(b'\x05\x02\x00\x00\x06\x01\x06\x01\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x04\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x02oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x05\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x03\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x06oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd')
sent pick 0
placing marker on row 0
created marker at 40
<class 'AttributeError'> 'NoneType' object has no attribute 'height' <traceback object at 0x0000020F5C41A1C8>
Traceback (most recent call last):
  File "C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py", line 354, in updateLoomState
    self.advance()
  File "C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py", line 386, in advance
    self.sendToLoom()
  File "C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py", line 409, in sendToLoom
    self.ui.project.placeMarker(self.lineNumber)
  File "C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\weavingWidgets.py", line 183, in placeMarker
    ym = (self.design.height() - row - 1) * self.blockSize # rows are numbered from bottom to top, marker should start on bottom of image
AttributeError: 'NoneType' object has no attribute 'height'

=============================== RESTART: Shell ===============================
>>> 
 RESTART: C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py 
ready to connect
connecting to fake loom
making connection request
connecting to loom at  127.0.0.1 : 1337
1
2
connection successful! enabling functions
sending connect packets to loom
LoomControl: sending  b'\x04\x0e'
GUI: connection successful
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x00\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
created marker at 20
0
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x01\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 1
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x02\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 2
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x03\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 3
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x04\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 4
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x05\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 5
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x06\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 6
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x07\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 7
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x08\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 8
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\t\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 9
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\n\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 10
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x0b\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 11
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x0c\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 12
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02\r\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 12
placing marker on row 0
created marker at 60
pattern row: [0, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x0e\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 13
placing marker on row 1
ym = 40
marker y = -20
scene y =  60.0
pattern row: [0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02\x0f\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 14
placing marker on row 2
ym = 20
marker y = -40
scene y =  60.0
pattern row: [1, 0, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02\x10\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 15
placing marker on row 3
ym = 0
marker y = -60
scene y =  60.0
pattern row: [0, 0, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x11\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 16
placing marker on row 0
ym = 60
marker y = 0
scene y =  60.0
pattern row: [0, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x12\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 17
placing marker on row 1
ym = 40
marker y = -20
scene y =  60.0
pattern row: [0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02\x13\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 18
placing marker on row 2
ym = 20
marker y = -40
scene y =  60.0
pattern row: [1, 0, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02\x14\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 19
placing marker on row 3
ym = 0
marker y = -60
scene y =  60.0
pattern row: [0, 0, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x15\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 20
placing marker on row 0
ym = 60
marker y = 0
scene y =  60.0

 RESTART: C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py 
ready to connect
('C:/Users/Shanel Wu/Documents/GitHub/EID_ECEN5783_Fall19/SuperProject/testFiles/2_doubleweaving_SCRIPT.bmp', 'Image files (*.bmp *.tif)')
user loaded file
connecting to fake loom
making connection request
connecting to loom at  127.0.0.1 : 1337
1
2
connection successful! enabling functions
sending connect packets to loom
LoomControl: sending  b'\x04\x0e'
GUI: connection successful
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\x00\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 0
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x01\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 1
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\x02\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 2
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x03\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 3
advance progress marker
0
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\x04\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 4
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x05\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 5
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\x06\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 6
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x07\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 7
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\x08\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 8
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\t\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 9
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\n\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 10
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x0b\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 11
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\x0c\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 10
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\r\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 9
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\x0e\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 8
advance progress marker
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02\x0f\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 8
placing marker on row 0
created marker at 40
pattern row: [True, True, False]
LoomControl: sending  bytearray(b'\x05\x02\x10\x00\x06\x01\x06\x01\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x04\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x02oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x05\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x03\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x06oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd')
sent pick 9
placing marker on row 0
ym = 40
marker y = 0
scene y =  40.0
pattern row: [True, False, True]
LoomControl: sending  bytearray(b'\x05\x02\x11\x00\x06\x01\x06\x01oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x04\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x02\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x05oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x03\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x06\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck')
sent pick 10
placing marker on row 1
ym = 20
marker y = -20
scene y =  40.0
pattern row: [False, True, True]
LoomControl: sending  bytearray(b'\x05\x02\x12\x00\x06\x01\x06\x01\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x04oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x02\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x05\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x03oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x06\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6')
sent pick 11
placing marker on row 2
ym = 0
marker y = -40
scene y =  40.0
pattern row: [True, True, False]
LoomControl: sending  bytearray(b'\x05\x02\x13\x00\x06\x01\x06\x01\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x04\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x02oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x05\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x03\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x06oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd')
sent pick 12
placing marker on row 0
ym = 40
marker y = 0
scene y =  40.0
pattern row: [True, False, True]
LoomControl: sending  bytearray(b'\x05\x02\x14\x00\x06\x01\x06\x01oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x04\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x02\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x05oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x03\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x06\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck')
sent pick 13
placing marker on row 1
ym = 20
marker y = -20
scene y =  40.0
pattern row: [False, True, True]
LoomControl: sending  bytearray(b'\x05\x02\x15\x00\x06\x01\x06\x01\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x04oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x02\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x05\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x03oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x06\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6')
sent pick 14
placing marker on row 2
ym = 0
marker y = -40
scene y =  40.0
pattern row: [True, True, False]
LoomControl: sending  bytearray(b'\x05\x02\x16\x00\x06\x01\x06\x01\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x04\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x02oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x05\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x03\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x06oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd')
sent pick 15
placing marker on row 0
ym = 40
marker y = 0
scene y =  40.0
pattern row: [True, False, True]
LoomControl: sending  bytearray(b'\x05\x02\x17\x00\x06\x01\x06\x01oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x04\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x02\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x05oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x03\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x06\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck')
sent pick 16
placing marker on row 1
ym = 20
marker y = -20
scene y =  40.0
pattern row: [False, True, True]
LoomControl: sending  bytearray(b'\x05\x02\x18\x00\x06\x01\x06\x01\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x04oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x02\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x05\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x03oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x06\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6')
sent pick 17
placing marker on row 2
ym = 0
marker y = -40
scene y =  40.0
pattern row: [True, True, False]
LoomControl: sending  bytearray(b'\x05\x02\x19\x00\x06\x01\x06\x01\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x04\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x02oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x05\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x03\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x06oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd')
sent pick 18
placing marker on row 0
ym = 40
marker y = 0
scene y =  40.0
pattern row: [True, False, True]
LoomControl: sending  bytearray(b'\x05\x02\x1a\x00\x06\x01\x06\x01oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x04\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x02\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x05oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x03\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x06\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck')
sent pick 19
placing marker on row 1
ym = 20
marker y = -20
scene y =  40.0
pattern row: [False, True, True]
LoomControl: sending  bytearray(b'\x05\x02\x1b\x00\x06\x01\x06\x01\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x04oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x02\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x05\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x03oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x06\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6')
sent pick 20
placing marker on row 2
ym = 0
marker y = -40
scene y =  40.0
pattern row: [True, True, False]
LoomControl: sending  bytearray(b'\x05\x02\x1c\x00\x06\x01\x06\x01\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x04\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x02oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x05\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x03\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x06oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd')
sent pick 21
placing marker on row 0
ym = 40
marker y = 0
scene y =  40.0
pattern row: [True, False, True]
LoomControl: sending  bytearray(b'\x05\x02\x1d\x00\x06\x01\x06\x01oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x04\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x02\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x05oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x03\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x06\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck')
sent pick 22
placing marker on row 1
ym = 20
marker y = -20
scene y =  40.0
pattern row: [False, True, True]
LoomControl: sending  bytearray(b'\x05\x02\x1e\x00\x06\x01\x06\x01\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x04oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x02\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x05\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x03oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x06\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6')
sent pick 23
placing marker on row 2
ym = 0
marker y = -40
scene y =  40.0
pattern row: [True, True, False]
LoomControl: sending  bytearray(b'\x05\x02\x1f\x00\x06\x01\x06\x01\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x04\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x02oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x05\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x03\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x06oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd')
sent pick 24
placing marker on row 0
ym = 40
marker y = 0
scene y =  40.0
pattern row: [True, False, True]
LoomControl: sending  bytearray(b'\x05\x02 \x00\x06\x01\x06\x01oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x04\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x02\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x05oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x03\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x06\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck')
sent pick 25
placing marker on row 1
ym = 20
marker y = -20
scene y =  40.0
pattern row: [False, True, True]
LoomControl: sending  bytearray(b'\x05\x02!\x00\x06\x01\x06\x01\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x04oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x02\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x05\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x03oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x06\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6')
sent pick 26
placing marker on row 2
ym = 0
marker y = -40
scene y =  40.0
pattern row: [True, True, False]
LoomControl: sending  bytearray(b'\x05\x02"\x00\x06\x01\x06\x01\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x04\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x02oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x05\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x03\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x06oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd')
sent pick 27
placing marker on row 0
ym = 40
marker y = 0
scene y =  40.0
pattern row: [True, False, True]
LoomControl: sending  bytearray(b'\x05\x02#\x00\x06\x01\x06\x01oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x04\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x02\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x05oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x03\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x06\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck')
sent pick 28
placing marker on row 1
ym = 20
marker y = -20
scene y =  40.0
pattern row: [False, True, True]
LoomControl: sending  bytearray(b'\x05\x02$\x00\x06\x01\x06\x01\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x04oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x02\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x05\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x03oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x06\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6')
sent pick 29
placing marker on row 2
ym = 0
marker y = -40
scene y =  40.0
pattern row: [True, True, False]
LoomControl: sending  bytearray(b'\x05\x02%\x00\x06\x01\x06\x01\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x04\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x02oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x05\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x03\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x06oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd')
sent pick 30
placing marker on row 0
ym = 40
marker y = 0
scene y =  40.0
pattern row: [True, False, True]
LoomControl: sending  bytearray(b'\x05\x02&\x00\x06\x01\x06\x01oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x04\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x02\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x05oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x03\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x06\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck')
sent pick 31
placing marker on row 1
ym = 20
marker y = -20
scene y =  40.0
pattern row: [False, True, True]
LoomControl: sending  bytearray(b"\x05\x02\'\x00\x06\x01\x06\x01\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x04oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x02\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x05\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x03oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x06\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6")
sent pick 32
placing marker on row 2
ym = 0
marker y = -40
scene y =  40.0
pattern row: [True, True, False]
LoomControl: sending  bytearray(b'\x05\x02(\x00\x06\x01\x06\x01\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x04\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x02oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x05\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x03\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x06oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd')
sent pick 33
placing marker on row 0
ym = 40
marker y = 0
scene y =  40.0
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
('', '')
user cancelled
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02)\x00\x06\x01\x06\x01\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf?\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x04\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x02oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd\x05\xf6\xbf\x99\xd9o6\x9b\xffv\xb3\xfb\xddfo\xbf\xcdf\xbf\xd6\xff\xc3\xbd\xc3\xbdk\xcf\xbf\xc6?\xd6\x03\x99\xdf\x7ff\xf6\xdbmo\xbb\xdd\xccn\xbf\x9f\xd9~\x9b\xf9k\xcf?\xd6?\xd6\xbd?\xdc;\xfck\x06oo\xe6\xbf\x99\xed\xf6\x9f\xcdn7\xb3\xd9\xfff\xb3\xfd\xc6\xbd?\xfck\xfck\xd6\xffc\xfd\xc3\xbd')
sent pick 33
placing marker on row 0
created marker at 140
pattern row: [0, 1, 0, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02*\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$')
sent pick 34
placing marker on row 2
ym = 100
marker y = -40
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 1, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02+\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 35
placing marker on row 3
ym = 80
marker y = -60
scene y =  140.0
pattern row: [0, 1, 1, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02,\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 36
placing marker on row 4
ym = 60
marker y = -80
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02-\x00\x06\x01\x06\x01Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 37
placing marker on row 5
ym = 40
marker y = -100
scene y =  140.0
pattern row: [0, 1, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02.\x00\x06\x01\x06\x01~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 38
placing marker on row 6
ym = 20
marker y = -120
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02/\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 39
placing marker on row 7
ym = 0
marker y = -140
scene y =  140.0
pattern row: [0, 0, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x020\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 40
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x021\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd')
sent pick 41
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
pattern row: [0, 1, 0, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x022\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$')
sent pick 42
placing marker on row 2
ym = 100
marker y = -40
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 1, 1, 0]
LoomControl: sending  bytearray(b'\x05\x023\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 43
placing marker on row 3
ym = 80
marker y = -60
scene y =  140.0
pattern row: [0, 1, 1, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x024\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 44
placing marker on row 4
ym = 60
marker y = -80
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x025\x00\x06\x01\x06\x01Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 45
placing marker on row 5
ym = 40
marker y = -100
scene y =  140.0
pattern row: [0, 1, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x026\x00\x06\x01\x06\x01~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 46
placing marker on row 6
ym = 20
marker y = -120
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 0, 0]
LoomControl: sending  bytearray(b'\x05\x027\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 47
placing marker on row 7
ym = 0
marker y = -140
scene y =  140.0
pattern row: [0, 0, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x028\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 48
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x029\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd')
sent pick 49
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
pattern row: [0, 1, 0, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02:\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$')
sent pick 50
placing marker on row 2
ym = 100
marker y = -40
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 1, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02;\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 51
placing marker on row 3
ym = 80
marker y = -60
scene y =  140.0
pattern row: [0, 1, 1, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02<\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 52
placing marker on row 4
ym = 60
marker y = -80
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02=\x00\x06\x01\x06\x01Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 53
placing marker on row 5
ym = 40
marker y = -100
scene y =  140.0
pattern row: [0, 1, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02>\x00\x06\x01\x06\x01~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 54
placing marker on row 6
ym = 20
marker y = -120
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02?\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 55
placing marker on row 7
ym = 0
marker y = -140
scene y =  140.0
pattern row: [0, 0, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02@\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 56
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02A\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd')
sent pick 57
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
pattern row: [0, 1, 0, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02B\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$')
sent pick 58
placing marker on row 2
ym = 100
marker y = -40
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 1, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02C\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 59
placing marker on row 3
ym = 80
marker y = -60
scene y =  140.0
pattern row: [0, 1, 1, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02D\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 60
placing marker on row 4
ym = 60
marker y = -80
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02E\x00\x06\x01\x06\x01Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 61
placing marker on row 5
ym = 40
marker y = -100
scene y =  140.0
pattern row: [0, 1, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02F\x00\x06\x01\x06\x01~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 62
placing marker on row 6
ym = 20
marker y = -120
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02G\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 63
placing marker on row 7
ym = 0
marker y = -140
scene y =  140.0
pattern row: [0, 0, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02H\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 64
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02I\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd')
sent pick 65
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
pattern row: [0, 1, 0, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02J\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$')
sent pick 66
placing marker on row 2
ym = 100
marker y = -40
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 1, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02K\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 67
placing marker on row 3
ym = 80
marker y = -60
scene y =  140.0
pattern row: [0, 1, 1, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02L\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 68
placing marker on row 4
ym = 60
marker y = -80
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02M\x00\x06\x01\x06\x01Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 69
placing marker on row 5
ym = 40
marker y = -100
scene y =  140.0
pattern row: [0, 1, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02N\x00\x06\x01\x06\x01~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 70
placing marker on row 6
ym = 20
marker y = -120
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02O\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 71
placing marker on row 7
ym = 0
marker y = -140
scene y =  140.0
pattern row: [0, 0, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02P\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 72
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02Q\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd')
sent pick 73
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
pattern row: [0, 1, 0, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02R\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$')
sent pick 74
placing marker on row 2
ym = 100
marker y = -40
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 1, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02S\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 75
placing marker on row 3
ym = 80
marker y = -60
scene y =  140.0
pattern row: [0, 1, 1, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02T\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 76
placing marker on row 4
ym = 60
marker y = -80
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02U\x00\x06\x01\x06\x01Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 77
placing marker on row 5
ym = 40
marker y = -100
scene y =  140.0
pattern row: [0, 1, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02V\x00\x06\x01\x06\x01~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 78
placing marker on row 6
ym = 20
marker y = -120
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02W\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 79
placing marker on row 7
ym = 0
marker y = -140
scene y =  140.0
pattern row: [0, 0, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02X\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 80
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02Y\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd')
sent pick 81
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
pattern row: [0, 1, 0, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02Z\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$')
sent pick 82
placing marker on row 2
ym = 100
marker y = -40
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 1, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02[\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 83
placing marker on row 3
ym = 80
marker y = -60
scene y =  140.0
pattern row: [0, 1, 1, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02\\\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 84
placing marker on row 4
ym = 60
marker y = -80
scene y =  140.0
pattern row: [1, 0, 1, 1, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02]\x00\x06\x01\x06\x01Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 85
placing marker on row 5
ym = 40
marker y = -100
scene y =  140.0
pattern row: [0, 1, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02^\x00\x06\x01\x06\x01~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 86
placing marker on row 6
ym = 20
marker y = -120
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02_\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 87
placing marker on row 7
ym = 0
marker y = -140
scene y =  140.0
pattern row: [0, 0, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02`\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 88
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
pattern row: [0, 0, 1, 0, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02a\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd')
sent pick 89
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
('C:/Users/Shanel Wu/Documents/GitHub/EID_ECEN5783_Fall19/SuperProject/testFiles/3_pressureSensor_SCRIPT.bmp', 'Image files (*.bmp *.tif)')
user loaded file
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02b\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd')
sent pick 89
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02c\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 90
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02d\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 91
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02e\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 92
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02f\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 93
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02g\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 94
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02h\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 95
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02i\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 96
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02j\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 97
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02k\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 98
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02l\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 99
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02m\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 100
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02n\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 101
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02o\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 102
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02p\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf')
sent pick 103
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02q\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6mf?3\x99\xccf\x99\xcfl63\x99\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 104
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02r\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x02$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x05\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99\x03$\x9f4m\xdb\xe6\xd9O\x86a8\x9em\xbfm\x8eI\x92\x99\xcf\xccf3\x99f?\x93\xc9\xccf\x06\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7a\x92O\x92q\xb6\xedf?3\x99\xccf\x99\xcfl63\x99')
sent pick 105
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02s\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9eGk\x92O\x92q\x16\xcff?3\x99\xccl\x99\xcfl63\x1b\x04\xdbo\xcb\x92$\x19&\xbfy\x9eGA\x92O\x92q\x14\xc5f?3\x99\xccD\x99\xcfl63\x11\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x8b\x7f\xcb\x92$\x19r\xbfy\x9e\xc7a\x92O\x92q\xb6m\'?3\x99\xccf\xc9\xcfl63\x99\x06\x8a/\xca\x92$\x19"\xafy\x9e\xc7a\x92O\x92q\xb6\xed"?3\x99\xccf\x88\xcfl63\x99')
sent pick 106
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02t\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 107
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02u\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x10\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7k\x92O\x92q\xb6\xeff?3\x99\xccn\x99\xcfl63\x9b\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x03 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf\x06\xdb\x7f\xcb\x92$\x19v\xbfy\x9e\xc7a\x92O\x92q\xb6\xedg?3\x99\xccf\xd9\xcfl63\x99')
sent pick 108
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02v\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x80*\x00\x0f\x00\x00\xa2\xaa\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x00\x8a\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06Q_\x01\x00\x00\x00T\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80E\x0f\x00\x00\x00\x00Q\x0f\x00\x00\x00\x00')
sent pick 109
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02w\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18\x1em\xbfm\x8eA\x92\x99\xcf\xccf3\x19f?\x93\xc9\xccF\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05 \x1f \x05Z\xa0P\x0f\x02!\x10\n\x05\xaf\x05\n\x01\x92\t\xcf\xc0B\x03\tB?\x90\xc0\xc0B\x03\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6mw?3\x99\xccf\xdd\xcfl63\x99\x06 \x9f0m\xdb\xe6\xd8\x0f\x86a8\x9em\xbfm\x8eI\x92\x89\xcf\xccf3\x99b?\x93\xc9\xccf')
sent pick 110
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02x\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\n\x00\x0f\x00\x00\x00\x82\x00\x0f\x00\x00\x00\x08\x00\x0f\x00\x00\x00\x02\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05 \x1f \x05Z\xa0P\x0f\x02!\x10\n\x05\xaf\x05\n\x01\x92\t\xcf\xc0B\x03\tB?\x90\xc0\xc0B\x03U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00\x06\x00\x1f\x00\x00\x00\x00P\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x01\x0f\x00\x00\x00\x00@\x0f\x00\x00\x00\x00')
sent pick 111
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02y\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18>m\xbfm\x8eC\x9a\x99\xcf\xccf39f?\x93\xc9\xccN\x04$\x9f4m\xdb\xe6\xd9O\x86a\xb8\xbem\xbfm\x8e\xeb\xba\x99\xcf\xccf3\xbbf?\x93\xc9\xcc\xee\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03!\xdf1m\xdb\xe6\xd8\x1f\x86a8\x9em\xbfm\x8eI\x92\x8d\xcf\xccf3\x99c?\x93\xc9\xccf\x06u\xdf5m\xdb\xe6\xdd_\x86a8\x9em\xbfm\x8eI\x92\xdd\xcf\xccf3\x99w?\x93\xc9\xccf')
sent pick 112
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02z\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00\x06U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00')
sent pick 113
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b"\x05\x02{\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x04\xdbo\xcb\x92$\x19&\xbfy\x9eGk\x92O\x92q\x16\xcff?3\x99\xccl\x99\xcfl63\x1b\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6mw?3\x99\xccf\xdd\xcfl63\x99\x06\x8b\x7f\xcb\x92$\x19r\xbfy\x9e\xc7a\x92O\x92q\xb6\xed\'?3\x99\xccf\xc9\xcfl63\x99")
sent pick 114
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02|\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00\x06\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00')
sent pick 115
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02}\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x184m\xbfm\x8eC\x18\x99\xcf\xccf31f?\x93\xc9\xccL\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x02\x81o\x81\x12 \x11"\x1f)\x94B!\x12\x0f\x12!\x16H$\x0f\x03\t\x0c$\t\xcf@\x02\x03\t\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03!\xcf1m\xdb\xe6\x88\x1f\x86a8\x9em\xbfm\x8eI\x92\x8c\xcf\xccf3\x99#?\x93\xc9\xccf\x06\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6\xedw?3\x99\xccf\xdd\xcfl63\x99')
sent pick 116
advance progress marker
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02~\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x184m\xbfm\x8eC\x18\x99\xcf\xccf31f?\x93\xc9\xccL\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x02\x81o\x81\x12 \x11"\x1f)\x94B!\x12\x0f\x12!\x16H$\x0f\x03\t\x0c$\t\xcf@\x02\x03\t\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03!\xcf1m\xdb\xe6\x88\x1f\x86a8\x9em\xbfm\x8eI\x92\x8c\xcf\xccf3\x99#?\x93\xc9\xccf\x06\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6\xedw?3\x99\xccf\xdd\xcfl63\x99')
sent pick 116
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x7f\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00 \x00\x0f\x00\x00\x02\x08\x00\x0f\x00\x00\x00 \x00\x0f\x00\x00\x00\x08\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x02\x81o\x81\x12 \x11"\x1f)\x94B!\x12\x0f\x12!\x16H$\x0f\x03\t\x0c$\t\xcf@\x02\x03\t\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x01O\x01\x00\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x0f\x00\x00\x00\x00\x01\x0f\x00\x00\x00\x00\x06U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00')
sent pick 117
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02\x80\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9eg\xeb\x92O\x92q\x1e\xcff?3\x99\xcc\xec\x99\xcfl63;\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x90\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x02\xa5\xff\xb5\x7f\xfb\xf7\xfb_\xaf\xf5z\xbf\x7f\xbf\x7f\xaf_\xda\xbd\xcf\xcfo?\xbdo\xff\xd3\xcb\xcfo\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x8f\x7f\xcf\x92$\x19s\xffy\x9e\xc7a\x92O\x92q\xb6m7?3\x99\xccf\xcd\xcfl63\x99\x06 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf')
sent pick 118
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x81\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00 \xaa\x00\x0f\x00\x00\n\x8a\x00\x0f\x00\x00\x00\xa8\x00\x0f\x00\x00\x00*\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xa5\xff\xb5\x7f\xfb\xf7\xfb_\xaf\xf5z\xbf\x7f\xbf\x7f\xaf_\xda\xbd\xcf\xcfo?\xbdo\xff\xd3\xcb\xcfo\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x05_\x05\x00\x00\x00Q_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x15\x0f\x00\x00\x00\x00E\x0f\x00\x00\x00\x00\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 119
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x82\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x10\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18>m\xbfm\x8eC\x9a\x99\xcf\xccf39f?\x93\xc9\xccN\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf\x06!\xdf1m\xdb\xe6\xd8\x1f\x86a8\x9em\xbfm\x8eI\x92\x8d\xcf\xccf3\x99c?\x93\xc9\xccf')
sent pick 120
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x83\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00')
sent pick 121
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\x84\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9eGk\x92O\x92q\x16\xcff?3\x99\xccl\x99\xcfl63\x1b\x04\xdbo\xcb\x92$\x19&\xbfy\x9eGA\x92O\x92q\x14\xc5f?3\x99\xccD\x99\xcfl63\x11\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x8b\x7f\xcb\x92$\x19r\xbfy\x9e\xc7a\x92O\x92q\xb6m\'?3\x99\xccf\xc9\xcfl63\x99\x06\x8a/\xca\x92$\x19"\xafy\x9e\xc7a\x92O\x92q\xb6\xed"?3\x99\xccf\x88\xcfl63\x99')
sent pick 122
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x85\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 123
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02\x86\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x10\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7k\x92O\x92q\xb6\xeff?3\x99\xccn\x99\xcfl63\x9b\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x03 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf\x06\xdb\x7f\xcb\x92$\x19v\xbfy\x9e\xc7a\x92O\x92q\xb6\xedg?3\x99\xccf\xd9\xcfl63\x99')
sent pick 124
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x87\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x80*\x00\x0f\x00\x00\xa2\xaa\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x00\x8a\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06Q_\x01\x00\x00\x00T\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80E\x0f\x00\x00\x00\x00Q\x0f\x00\x00\x00\x00')
sent pick 125
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02\x88\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18\x1em\xbfm\x8eA\x92\x99\xcf\xccf3\x19f?\x93\xc9\xccF\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05 \x1f \x05Z\xa0P\x0f\x02!\x10\n\x05\xaf\x05\n\x01\x92\t\xcf\xc0B\x03\tB?\x90\xc0\xc0B\x03\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6mw?3\x99\xccf\xdd\xcfl63\x99\x06 \x9f0m\xdb\xe6\xd8\x0f\x86a8\x9em\xbfm\x8eI\x92\x89\xcf\xccf3\x99b?\x93\xc9\xccf')
sent pick 126
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x89\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\n\x00\x0f\x00\x00\x00\x82\x00\x0f\x00\x00\x00\x08\x00\x0f\x00\x00\x00\x02\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05 \x1f \x05Z\xa0P\x0f\x02!\x10\n\x05\xaf\x05\n\x01\x92\t\xcf\xc0B\x03\tB?\x90\xc0\xc0B\x03U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00\x06\x00\x1f\x00\x00\x00\x00P\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x01\x0f\x00\x00\x00\x00@\x0f\x00\x00\x00\x00')
sent pick 127
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x8a\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18>m\xbfm\x8eC\x9a\x99\xcf\xccf39f?\x93\xc9\xccN\x04$\x9f4m\xdb\xe6\xd9O\x86a\xb8\xbem\xbfm\x8e\xeb\xba\x99\xcf\xccf3\xbbf?\x93\xc9\xcc\xee\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03!\xdf1m\xdb\xe6\xd8\x1f\x86a8\x9em\xbfm\x8eI\x92\x8d\xcf\xccf3\x99c?\x93\xc9\xccf\x06u\xdf5m\xdb\xe6\xdd_\x86a8\x9em\xbfm\x8eI\x92\xdd\xcf\xccf3\x99w?\x93\xc9\xccf')
sent pick 128
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x8b\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00\x06U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00')
sent pick 129
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b"\x05\x02\x8c\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x04\xdbo\xcb\x92$\x19&\xbfy\x9eGk\x92O\x92q\x16\xcff?3\x99\xccl\x99\xcfl63\x1b\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6mw?3\x99\xccf\xdd\xcfl63\x99\x06\x8b\x7f\xcb\x92$\x19r\xbfy\x9e\xc7a\x92O\x92q\xb6\xed\'?3\x99\xccf\xc9\xcfl63\x99")
sent pick 130
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x8d\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00\x06\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00')
sent pick 131
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02\x8e\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x184m\xbfm\x8eC\x18\x99\xcf\xccf31f?\x93\xc9\xccL\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x02\x81o\x81\x12 \x11"\x1f)\x94B!\x12\x0f\x12!\x16H$\x0f\x03\t\x0c$\t\xcf@\x02\x03\t\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03!\xcf1m\xdb\xe6\x88\x1f\x86a8\x9em\xbfm\x8eI\x92\x8c\xcf\xccf3\x99#?\x93\xc9\xccf\x06\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6\xedw?3\x99\xccf\xdd\xcfl63\x99')
sent pick 132
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x8f\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00 \x00\x0f\x00\x00\x02\x08\x00\x0f\x00\x00\x00 \x00\x0f\x00\x00\x00\x08\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x02\x81o\x81\x12 \x11"\x1f)\x94B!\x12\x0f\x12!\x16H$\x0f\x03\t\x0c$\t\xcf@\x02\x03\t\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x01O\x01\x00\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x0f\x00\x00\x00\x00\x01\x0f\x00\x00\x00\x00\x06U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00')
sent pick 133
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02\x90\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9eg\xeb\x92O\x92q\x1e\xcff?3\x99\xcc\xec\x99\xcfl63;\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x90\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x02\xa5\xff\xb5\x7f\xfb\xf7\xfb_\xaf\xf5z\xbf\x7f\xbf\x7f\xaf_\xda\xbd\xcf\xcfo?\xbdo\xff\xd3\xcb\xcfo\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x8f\x7f\xcf\x92$\x19s\xffy\x9e\xc7a\x92O\x92q\xb6m7?3\x99\xccf\xcd\xcfl63\x99\x06 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf')
sent pick 134
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x91\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00 \xaa\x00\x0f\x00\x00\n\x8a\x00\x0f\x00\x00\x00\xa8\x00\x0f\x00\x00\x00*\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xa5\xff\xb5\x7f\xfb\xf7\xfb_\xaf\xf5z\xbf\x7f\xbf\x7f\xaf_\xda\xbd\xcf\xcfo?\xbdo\xff\xd3\xcb\xcfo\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x05_\x05\x00\x00\x00Q_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x15\x0f\x00\x00\x00\x00E\x0f\x00\x00\x00\x00\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 135
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x92\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x10\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18>m\xbfm\x8eC\x9a\x99\xcf\xccf39f?\x93\xc9\xccN\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf\x06!\xdf1m\xdb\xe6\xd8\x1f\x86a8\x9em\xbfm\x8eI\x92\x8d\xcf\xccf3\x99c?\x93\xc9\xccf')
sent pick 136
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x93\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00')
sent pick 137
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\x94\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9eGk\x92O\x92q\x16\xcff?3\x99\xccl\x99\xcfl63\x1b\x04\xdbo\xcb\x92$\x19&\xbfy\x9eGA\x92O\x92q\x14\xc5f?3\x99\xccD\x99\xcfl63\x11\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x8b\x7f\xcb\x92$\x19r\xbfy\x9e\xc7a\x92O\x92q\xb6m\'?3\x99\xccf\xc9\xcfl63\x99\x06\x8a/\xca\x92$\x19"\xafy\x9e\xc7a\x92O\x92q\xb6\xed"?3\x99\xccf\x88\xcfl63\x99')
sent pick 138
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x95\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 139
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02\x96\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x10\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7k\x92O\x92q\xb6\xeff?3\x99\xccn\x99\xcfl63\x9b\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x03 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf\x06\xdb\x7f\xcb\x92$\x19v\xbfy\x9e\xc7a\x92O\x92q\xb6\xedg?3\x99\xccf\xd9\xcfl63\x99')
sent pick 140
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x97\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x80*\x00\x0f\x00\x00\xa2\xaa\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x00\x8a\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06Q_\x01\x00\x00\x00T\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80E\x0f\x00\x00\x00\x00Q\x0f\x00\x00\x00\x00')
sent pick 141
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02\x98\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18\x1em\xbfm\x8eA\x92\x99\xcf\xccf3\x19f?\x93\xc9\xccF\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05 \x1f \x05Z\xa0P\x0f\x02!\x10\n\x05\xaf\x05\n\x01\x92\t\xcf\xc0B\x03\tB?\x90\xc0\xc0B\x03\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6mw?3\x99\xccf\xdd\xcfl63\x99\x06 \x9f0m\xdb\xe6\xd8\x0f\x86a8\x9em\xbfm\x8eI\x92\x89\xcf\xccf3\x99b?\x93\xc9\xccf')
sent pick 142
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x99\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\n\x00\x0f\x00\x00\x00\x82\x00\x0f\x00\x00\x00\x08\x00\x0f\x00\x00\x00\x02\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05 \x1f \x05Z\xa0P\x0f\x02!\x10\n\x05\xaf\x05\n\x01\x92\t\xcf\xc0B\x03\tB?\x90\xc0\xc0B\x03U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00\x06\x00\x1f\x00\x00\x00\x00P\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x01\x0f\x00\x00\x00\x00@\x0f\x00\x00\x00\x00')
sent pick 143
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x9a\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18>m\xbfm\x8eC\x9a\x99\xcf\xccf39f?\x93\xc9\xccN\x04$\x9f4m\xdb\xe6\xd9O\x86a\xb8\xbem\xbfm\x8e\xeb\xba\x99\xcf\xccf3\xbbf?\x93\xc9\xcc\xee\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03!\xdf1m\xdb\xe6\xd8\x1f\x86a8\x9em\xbfm\x8eI\x92\x8d\xcf\xccf3\x99c?\x93\xc9\xccf\x06u\xdf5m\xdb\xe6\xdd_\x86a8\x9em\xbfm\x8eI\x92\xdd\xcf\xccf3\x99w?\x93\xc9\xccf')
sent pick 144
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x9b\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00\x06U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00')
sent pick 145
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b"\x05\x02\x9c\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x04\xdbo\xcb\x92$\x19&\xbfy\x9eGk\x92O\x92q\x16\xcff?3\x99\xccl\x99\xcfl63\x1b\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6mw?3\x99\xccf\xdd\xcfl63\x99\x06\x8b\x7f\xcb\x92$\x19r\xbfy\x9e\xc7a\x92O\x92q\xb6\xed\'?3\x99\xccf\xc9\xcfl63\x99")
sent pick 146
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x9d\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00\x06\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00')
sent pick 147
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02\x9e\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x184m\xbfm\x8eC\x18\x99\xcf\xccf31f?\x93\xc9\xccL\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x02\x81o\x81\x12 \x11"\x1f)\x94B!\x12\x0f\x12!\x16H$\x0f\x03\t\x0c$\t\xcf@\x02\x03\t\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03!\xcf1m\xdb\xe6\x88\x1f\x86a8\x9em\xbfm\x8eI\x92\x8c\xcf\xccf3\x99#?\x93\xc9\xccf\x06\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6\xedw?3\x99\xccf\xdd\xcfl63\x99')
sent pick 148
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\x9f\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00 \x00\x0f\x00\x00\x02\x08\x00\x0f\x00\x00\x00 \x00\x0f\x00\x00\x00\x08\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x02\x81o\x81\x12 \x11"\x1f)\x94B!\x12\x0f\x12!\x16H$\x0f\x03\t\x0c$\t\xcf@\x02\x03\t\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x01O\x01\x00\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x0f\x00\x00\x00\x00\x01\x0f\x00\x00\x00\x00\x06U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00')
sent pick 149
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02\xa0\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9eg\xeb\x92O\x92q\x1e\xcff?3\x99\xcc\xec\x99\xcfl63;\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x90\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x02\xa5\xff\xb5\x7f\xfb\xf7\xfb_\xaf\xf5z\xbf\x7f\xbf\x7f\xaf_\xda\xbd\xcf\xcfo?\xbdo\xff\xd3\xcb\xcfo\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x8f\x7f\xcf\x92$\x19s\xffy\x9e\xc7a\x92O\x92q\xb6m7?3\x99\xccf\xcd\xcfl63\x99\x06 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf')
sent pick 150
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xa1\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00 \xaa\x00\x0f\x00\x00\n\x8a\x00\x0f\x00\x00\x00\xa8\x00\x0f\x00\x00\x00*\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xa5\xff\xb5\x7f\xfb\xf7\xfb_\xaf\xf5z\xbf\x7f\xbf\x7f\xaf_\xda\xbd\xcf\xcfo?\xbdo\xff\xd3\xcb\xcfo\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x05_\x05\x00\x00\x00Q_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x15\x0f\x00\x00\x00\x00E\x0f\x00\x00\x00\x00\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 151
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xa2\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x10\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18>m\xbfm\x8eC\x9a\x99\xcf\xccf39f?\x93\xc9\xccN\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf\x06!\xdf1m\xdb\xe6\xd8\x1f\x86a8\x9em\xbfm\x8eI\x92\x8d\xcf\xccf3\x99c?\x93\xc9\xccf')
sent pick 152
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xa3\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00')
sent pick 153
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\xa4\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9eGk\x92O\x92q\x16\xcff?3\x99\xccl\x99\xcfl63\x1b\x04\xdbo\xcb\x92$\x19&\xbfy\x9eGA\x92O\x92q\x14\xc5f?3\x99\xccD\x99\xcfl63\x11\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x8b\x7f\xcb\x92$\x19r\xbfy\x9e\xc7a\x92O\x92q\xb6m\'?3\x99\xccf\xc9\xcfl63\x99\x06\x8a/\xca\x92$\x19"\xafy\x9e\xc7a\x92O\x92q\xb6\xed"?3\x99\xccf\x88\xcfl63\x99')
sent pick 154
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xa5\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 155
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02\xa6\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x10\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7k\x92O\x92q\xb6\xeff?3\x99\xccn\x99\xcfl63\x9b\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x03 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf\x06\xdb\x7f\xcb\x92$\x19v\xbfy\x9e\xc7a\x92O\x92q\xb6\xedg?3\x99\xccf\xd9\xcfl63\x99')
sent pick 156
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xa7\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x80*\x00\x0f\x00\x00\xa2\xaa\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x00\x8a\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06Q_\x01\x00\x00\x00T\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80E\x0f\x00\x00\x00\x00Q\x0f\x00\x00\x00\x00')
sent pick 157
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02\xa8\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18\x1em\xbfm\x8eA\x92\x99\xcf\xccf3\x19f?\x93\xc9\xccF\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05 \x1f \x05Z\xa0P\x0f\x02!\x10\n\x05\xaf\x05\n\x01\x92\t\xcf\xc0B\x03\tB?\x90\xc0\xc0B\x03\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6mw?3\x99\xccf\xdd\xcfl63\x99\x06 \x9f0m\xdb\xe6\xd8\x0f\x86a8\x9em\xbfm\x8eI\x92\x89\xcf\xccf3\x99b?\x93\xc9\xccf')
sent pick 158
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xa9\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\n\x00\x0f\x00\x00\x00\x82\x00\x0f\x00\x00\x00\x08\x00\x0f\x00\x00\x00\x02\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05 \x1f \x05Z\xa0P\x0f\x02!\x10\n\x05\xaf\x05\n\x01\x92\t\xcf\xc0B\x03\tB?\x90\xc0\xc0B\x03U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00\x06\x00\x1f\x00\x00\x00\x00P\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x01\x0f\x00\x00\x00\x00@\x0f\x00\x00\x00\x00')
sent pick 159
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xaa\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18>m\xbfm\x8eC\x9a\x99\xcf\xccf39f?\x93\xc9\xccN\x04$\x9f4m\xdb\xe6\xd9O\x86a\xb8\xbem\xbfm\x8e\xeb\xba\x99\xcf\xccf3\xbbf?\x93\xc9\xcc\xee\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03!\xdf1m\xdb\xe6\xd8\x1f\x86a8\x9em\xbfm\x8eI\x92\x8d\xcf\xccf3\x99c?\x93\xc9\xccf\x06u\xdf5m\xdb\xe6\xdd_\x86a8\x9em\xbfm\x8eI\x92\xdd\xcf\xccf3\x99w?\x93\xc9\xccf')
sent pick 160
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xab\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00\x06U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00')
sent pick 161
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b"\x05\x02\xac\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x04\xdbo\xcb\x92$\x19&\xbfy\x9eGk\x92O\x92q\x16\xcff?3\x99\xccl\x99\xcfl63\x1b\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6mw?3\x99\xccf\xdd\xcfl63\x99\x06\x8b\x7f\xcb\x92$\x19r\xbfy\x9e\xc7a\x92O\x92q\xb6\xed\'?3\x99\xccf\xc9\xcfl63\x99")
sent pick 162
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xad\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00\x06\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00')
sent pick 163
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02\xae\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x184m\xbfm\x8eC\x18\x99\xcf\xccf31f?\x93\xc9\xccL\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x02\x81o\x81\x12 \x11"\x1f)\x94B!\x12\x0f\x12!\x16H$\x0f\x03\t\x0c$\t\xcf@\x02\x03\t\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03!\xcf1m\xdb\xe6\x88\x1f\x86a8\x9em\xbfm\x8eI\x92\x8c\xcf\xccf3\x99#?\x93\xc9\xccf\x06\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6\xedw?3\x99\xccf\xdd\xcfl63\x99')
sent pick 164
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xaf\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00 \x00\x0f\x00\x00\x02\x08\x00\x0f\x00\x00\x00 \x00\x0f\x00\x00\x00\x08\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x02\x81o\x81\x12 \x11"\x1f)\x94B!\x12\x0f\x12!\x16H$\x0f\x03\t\x0c$\t\xcf@\x02\x03\t\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x01O\x01\x00\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x0f\x00\x00\x00\x00\x01\x0f\x00\x00\x00\x00\x06U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00')
sent pick 165
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02\xb0\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9eg\xeb\x92O\x92q\x1e\xcff?3\x99\xcc\xec\x99\xcfl63;\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x90\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x02\xa5\xff\xb5\x7f\xfb\xf7\xfb_\xaf\xf5z\xbf\x7f\xbf\x7f\xaf_\xda\xbd\xcf\xcfo?\xbdo\xff\xd3\xcb\xcfo\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x8f\x7f\xcf\x92$\x19s\xffy\x9e\xc7a\x92O\x92q\xb6m7?3\x99\xccf\xcd\xcfl63\x99\x06 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf')
sent pick 166
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xb1\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00 \xaa\x00\x0f\x00\x00\n\x8a\x00\x0f\x00\x00\x00\xa8\x00\x0f\x00\x00\x00*\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xa5\xff\xb5\x7f\xfb\xf7\xfb_\xaf\xf5z\xbf\x7f\xbf\x7f\xaf_\xda\xbd\xcf\xcfo?\xbdo\xff\xd3\xcb\xcfo\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x05_\x05\x00\x00\x00Q_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x15\x0f\x00\x00\x00\x00E\x0f\x00\x00\x00\x00\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 167
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xb2\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x10\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18>m\xbfm\x8eC\x9a\x99\xcf\xccf39f?\x93\xc9\xccN\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf\x06!\xdf1m\xdb\xe6\xd8\x1f\x86a8\x9em\xbfm\x8eI\x92\x8d\xcf\xccf3\x99c?\x93\xc9\xccf')
sent pick 168
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xb3\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00')
sent pick 169
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b'\x05\x02\xb4\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9eGk\x92O\x92q\x16\xcff?3\x99\xccl\x99\xcfl63\x1b\x04\xdbo\xcb\x92$\x19&\xbfy\x9eGA\x92O\x92q\x14\xc5f?3\x99\xccD\x99\xcfl63\x11\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x8b\x7f\xcb\x92$\x19r\xbfy\x9e\xc7a\x92O\x92q\xb6m\'?3\x99\xccf\xc9\xcfl63\x99\x06\x8a/\xca\x92$\x19"\xafy\x9e\xc7a\x92O\x92q\xb6\xed"?3\x99\xccf\x88\xcfl63\x99')
sent pick 170
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xb5\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 171
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02\xb6\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18\x14m\xbfm\x8eA\x10\x99\xcf\xccf3\x11f?\x93\xc9\xccD\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xc7k\x92O\x92q\xb6\xeff?3\x99\xccn\x99\xcfl63\x9b\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x03 \x8f0m\xdb\xe6\x88\x0f\x86a8\x9em\xbfm\x8eI\x92\x88\xcf\xccf3\x99"?\x93\xc9\xccf\x06\xdb\x7f\xcb\x92$\x19v\xbfy\x9e\xc7a\x92O\x92q\xb6\xedg?3\x99\xccf\xd9\xcfl63\x99')
sent pick 172
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xb7\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x80*\x00\x0f\x00\x00\xa2\xaa\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x00\x8a\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06Q_\x01\x00\x00\x00T\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80E\x0f\x00\x00\x00\x00Q\x0f\x00\x00\x00\x00')
sent pick 173
advance progress marker
got row with width 1320
[  0 255 255 ... 255 255   0]
LoomControl: sending  bytearray(b'\x05\x02\xb8\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x04$\x9f4m\xdb\xe6\xd9O\x86a\x18\x1em\xbfm\x8eA\x92\x99\xcf\xccf3\x19f?\x93\xc9\xccF\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05 \x1f \x05Z\xa0P\x0f\x02!\x10\n\x05\xaf\x05\n\x01\x92\t\xcf\xc0B\x03\tB?\x90\xc0\xc0B\x03\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6mw?3\x99\xccf\xdd\xcfl63\x99\x06 \x9f0m\xdb\xe6\xd8\x0f\x86a8\x9em\xbfm\x8eI\x92\x89\xcf\xccf3\x99b?\x93\xc9\xccf')
sent pick 174
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xb9\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\n\x00\x0f\x00\x00\x00\x82\x00\x0f\x00\x00\x00\x08\x00\x0f\x00\x00\x00\x02\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05 \x1f \x05Z\xa0P\x0f\x02!\x10\n\x05\xaf\x05\n\x01\x92\t\xcf\xc0B\x03\tB?\x90\xc0\xc0B\x03U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00\x06\x00\x1f\x00\x00\x00\x00P\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x01\x0f\x00\x00\x00\x00@\x0f\x00\x00\x00\x00')
sent pick 175
advance progress marker
got row with width 1320
[  0   0 255 ...   0 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xba\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x18>m\xbfm\x8eC\x9a\x99\xcf\xccf39f?\x93\xc9\xccN\x04$\x9f4m\xdb\xe6\xd9O\x86a\xb8\xbem\xbfm\x8e\xeb\xba\x99\xcf\xccf3\xbbf?\x93\xc9\xcc\xee\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03!\xdf1m\xdb\xe6\xd8\x1f\x86a8\x9em\xbfm\x8eI\x92\x8d\xcf\xccf3\x99c?\x93\xc9\xccf\x06u\xdf5m\xdb\xe6\xdd_\x86a8\x9em\xbfm\x8eI\x92\xdd\xcf\xccf3\x99w?\x93\xc9\xccf')
sent pick 176
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xbb\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x02\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00\x06U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00')
sent pick 177
advance progress marker
got row with width 1320
[255 255   0 ... 255   0   0]
LoomControl: sending  bytearray(b"\x05\x02\xbc\x00\x06\x01\x06\x01\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x04\xdbo\xcb\x92$\x19&\xbfy\x9eGk\x92O\x92q\x16\xcff?3\x99\xccl\x99\xcfl63\x1b\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6mw?3\x99\xccf\xdd\xcfl63\x99\x06\x8b\x7f\xcb\x92$\x19r\xbfy\x9e\xc7a\x92O\x92q\xb6\xed\'?3\x99\xccf\xc9\xcfl63\x99")
sent pick 178
advance progress marker
got row with width 1320
[255 255 255 ... 255 255 255]
LoomControl: sending  bytearray(b'\x05\x02\xbd\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\xa0\xaa\x00\x0f\x00\x00\xaa\xaa\x00\x0f\x00\x00\x00\xaa\x00\x0f\x00\x00\x00\xaa\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00*\x00\x0f\x00\x00\x02\x8a\x00\x0f\x00\x00\x00(\x00\x0f\x00\x00\x00\n\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\xa1\x7f\xa1\x17z\xb1r\x1f+\xb5R+\x17\xaf\x17+\x17\xda-\xcf\xc3K\x0f-K\xff\xd0\xc2\xc3K\x03U_\x05\x00\x00\x00U_\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00U\x0f\x00\x00\x00\x00\x06\x01_\x01\x00\x00\x00P\x1f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x05\x0f\x00\x00\x00\x00A\x0f\x00\x00\x00\x00')
sent pick 179
advance progress marker
got row with width 1320
[255   0   0 ...   0   0 255]
LoomControl: sending  bytearray(b'\x05\x02\xbe\x00\x06\x01\x06\x01$\x9f4m\xdb\xe6\xd9O\x86a\x184m\xbfm\x8eC\x18\x99\xcf\xccf31f?\x93\xc9\xccL\x04\xdbo\xcb\x92$\x19&\xbfy\x9e\xe7\xeb\x92O\x92q\xbe\xeff?3\x99\xcc\xee\x99\xcfl63\xbb\x02\x81o\x81\x12 \x11"\x1f)\x94B!\x12\x0f\x12!\x16H$\x0f\x03\t\x0c$\t\xcf@\x02\x03\t\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03!\xcf1m\xdb\xe6\x88\x1f\x86a8\x9em\xbfm\x8eI\x92\x8c\xcf\xccf3\x99#?\x93\xc9\xccf\x06\xdf\x7f\xcf\x92$\x19w\xffy\x9e\xc7a\x92O\x92q\xb6\xedw?3\x99\xccf\xdd\xcfl63\x99')
sent pick 180
advance progress marker
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'

 RESTART: C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py 
ready to connect
connecting to real loom at  192.168.7.20 : 62000
making connection request
connecting to loom at  192.168.7.20 : 62000
1
2
connection successful! enabling functions
sending connect packets to loom
LoomControl: sending  b'\x04\x0e'
GUI: connection successful
3
data available to read
b'\x07\x06\x01\x0b\x0c\x07\x03\x05\t\x03\x03\x02\x03\n5\t\x03\r\r\x03\x0e\x03\x03\x15\x01\x03\x17\xa4\x01\x03\x1b\x02\x03\x1d\xd0\x07\x03\x1f\x01\x00\x01\x03!\x01\x01\x03#\x01\x01\x03$\xff\x03+\x01\x01\x03-\x01\x01\x01\x02\x01\x04\x06\xd8\x809\xec\xfd\x1f\x01\x06\x15d\x00\t\t\x01\t\x0e.\x00\x00\x00\x00\t\x0e/\x00\x00\x00\x00\x02\r?\x00\x00\x00\x00\x00?\x00\x00\x00\x00\x00\x03,\x00\x00\x14\x07\xa8\xc0\x00\xff\xff\xff\x01\x07\xa8\xc0'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd1\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd1\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xcf\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
pattern row: [0, 0, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02\x00\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
created marker at 140
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x01\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x01\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 0, 1, 0, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x02\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd')
sent pick 1
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x02\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1, 0, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x03\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$')
sent pick 2
placing marker on row 2
ym = 100
marker y = -40
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x03\x00\x01\x04\x03\xe0\x00\x01\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0, 1, 1, 1, 1, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x04\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 3
placing marker on row 3
ym = 80
marker y = -60
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x04\x00\x01\x04\x03\xe3\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1, 1, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x05\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 4
placing marker on row 4
ym = 60
marker y = -80
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x05\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0, 1, 1, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x06\x00\x06\x01\x06\x01Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03Z\x0fJ\x80\x04\x08\x04\xafP\n\x85@\x80O\x80P\xa0%B?0\x90\xc0B\x90\x0f,40\x90\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 5
placing marker on row 5
ym = 40
marker y = -100
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x06\x00\x01\x04\x03\xe3\x00\x01\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02\x07\x00\x06\x01\x06\x01~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03~\x9f~\xed\xdf\xee\xdd\xef\xd6k\xbd\xde\xed\xff\xed\xde\xe9\xb7\xdb\xff\xfc\xf6\xf3\xdb\xf6?\xbf\xfd\xfc\xf6\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 6
placing marker on row 6
ym = 20
marker y = -120
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x07\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 0, 1, 0, 1, 0, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02\x08\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8\xa5\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4')
sent pick 7
placing marker on row 7
ym = 0
marker y = -140
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x08\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 0, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02\t\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 8
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\t\x00\x01\x04\x03\xdc\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 0, 1, 0, 1, 0, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02\n\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xdf\xef\xdf\xfa\xa5_\xaf\xff\xfd\xde\xef\xf5\xfa_\xfa\xf5\xfe\xed\xf6??\xbd\xfc\xf6\xbd\xcfo??\xbd')
sent pick 9
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
updated cell at 4 , 3 to False
updated cell at 4 , 2 to False
updated cell at 3 , 3 to False
updated cell at 3 , 4 to False
updated cell at 7 , 2 to False
data available to read
b'\x05\x03\n\x00\x01\x04\x03\xdc\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1, 0, 1, 1, 1, 0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x0b\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x80\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$')
sent pick 10
placing marker on row 2
ym = 100
marker y = -40
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x0b\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0, 1, False, False, 1, 1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x0c\x00\x06\x01\x06\x01\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x00\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x04\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x02\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x00\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x05\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb\x03\x04\x8f\x14h\x81F\x89O\x84@(\x94h\x1fh\x84H\x00\x90\x0f\x0c$0\x90$\x0f\x03\t\x0c$\x06\xfb\x7f\xeb\x97~\xb9v\xbf{\xbf\xd7k\x97\xef\x97{\xb7\xffo\xff\xf3\xdb\xcfo\xdb\xff\xfc\xf6\xf3\xdb')
sent pick 11
placing marker on row 3
ym = 80
marker y = -60
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
data available to read
b'\x01\x01\x01\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
updated cell at 2 , 2 to True
updated cell at 1 , 1 to False
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
updated cell at 3 , 1 to True
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
('C:/Users/Shanel Wu/Documents/GitHub/EID_ECEN5783_Fall19/SuperProject/testFiles/2_doubleweaving_SCRIPT.bmp', 'Image files (*.bmp *.tif)')
user loaded file
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd5\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd5\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd5\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd5\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd5\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd5\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd5\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd5\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd5\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd5\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
>>> data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal

 RESTART: C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py 
ready to connect
>>> 
 RESTART: C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py 
ready to connect
connecting to real loom at  192.168.7.20 : 62000
making connection request
connecting to loom at  192.168.7.20 : 62000
1
2
connection successful! enabling functions
sending connect packets to loom
LoomControl: sending  b'\x04\x0e'
GUI: connection successful
3
data available to read
b'\x07\x06\x01\x0b\x0c\x07\x03\x05\t\x03\x03\x02\x03\n5\t\x03\r\x10\x03\x0e\x03\x03\x15\x01\x03\x17\xa4\x01\x03\x1b\x02\x03\x1d\xd0\x07\x03\x1f\x01\x00\x01\x03!\x01\x01\x03#\x01\x01\x03$\xff\x03+\x01\x01\x03-\x01\x01\x01\x02\x01\x04\x06\xd8\x809\xec\xfd\x1f\x01\x06\x15d\x00\t\t\x01\t\x0e.\x00\x00\x00\x00\t\x0e/\x00\x00\x00\x00\x02\r?\x00\x00\x00\x00\x00?\x00\x00\x00\x00\x00\x03,\x00\x00\x14\x07\xa8\xc0\x00\xff\xff\xff\x01\x07\xa8\xc0'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x00\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
created marker at 20
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x01\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x01\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x02\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 1
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x02\x00\x01\x04\x03\xe3\x00\x01\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x03\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 2
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x03\x00\x01\x04\x03\xe3\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x04\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 3
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x04\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x05\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 4
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x05\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x06\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 5
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x06\x00\x01\x04\x03\xe3\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x07\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 6
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x07\x00\x01\x04\x03\xe3\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x08\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 7
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x08\x00\x01\x04\x03\xe3\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\t\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 8
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\t\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\n\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 9
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\n\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x0b\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 10
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x0b\x00\x01\x04\x03\xe3\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x0c\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 11
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x0c\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\r\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 12
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\r\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x0e\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x0e\x00\x01\x04\x03\xe0\x00\x01\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x0f\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 14
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x0f\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x10\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 15
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x10\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x11\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 16
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x11\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x12\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 17
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x12\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x13\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 18
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x13\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x14\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 19
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x14\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x15\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 20
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x15\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x16\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 21
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x16\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x17\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 22
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x17\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x18\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 23
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x18\x00\x01\x04\x03\xe0\x00\x01\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x19\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 24
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x19\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x1a\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 25
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x1a\x00\x01\x04\x03\xe0\x00\x01\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x1b\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 26
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x1b\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x1c\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 27
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x1c\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x1d\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 28
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x1d\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x1e\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 29
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
data available to read
b'\x01\x01\x01\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xe6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd5\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xdc\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd3\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd4\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x04'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xdc\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd9\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
>>> data available to read
b'\x04\x03\xd9\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal

 RESTART: C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py 
ready to connect
connecting to real loom at  192.168.7.20 : 62000
making connection request
connecting to loom at  192.168.7.20 : 62000
1
2
connection successful! enabling functions
sending connect packets to loom
LoomControl: sending  b'\x04\x0e'
GUI: connection successful
3
data available to read
b'\x07\x06\x01\x0b\x0c\x07\x03\x05\t\x03\x03\x02\x03\n5\t\x03\r\x10\x03\x0e\x03\x03\x15\x01\x03\x17\xa4\x01\x03\x1b\x02\x03\x1d\xd0\x07\x03\x1f\x01\x00\x01\x03!\x01\x01\x03#\x01\x01\x03$\xff\x03+\x01\x01\x03-\x01\x01\x01\x02\x01\x04\x06\xd8\x809\xec\xfd\x1f\x01\x06\x15d\x00\t\t\x01\t\x0e.\x00\x00\x00\x00\t\x0e/\x00\x00\x00\x00\x02\r?\x00\x00\x00\x00\x00?\x00\x00\x00\x00\x00\x03,\x00\x00\x14\x07\xa8\xc0\x00\xff\xff\xff\x01\x07\xa8\xc0'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x00\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
created marker at 20
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x01\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x01\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x02\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 1
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x02\x00\x01\x04\x03\xe3\x00\x01\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x03\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 2
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x03\x00\x01\x04\x03\xe3\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x04\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 3
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x04\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x05\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 4
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x05\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x06\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 5
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x06\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [0, 1]
LoomControl: sending  bytearray(b'\x05\x02\x07\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 6
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x07\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [1, 0]
LoomControl: sending  bytearray(b'\x05\x02\x08\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 7
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
data available to read
b'\x01\x01\x01\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02\t\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 7
placing marker on row 1
created marker at 0
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\n\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 7
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\n\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [False, True]
LoomControl: sending  bytearray(b'\x05\x02\x0b\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 8
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x0b\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [True, False]
LoomControl: sending  bytearray(b'\x05\x02\x0c\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 9
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x0c\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [False, True]
LoomControl: sending  bytearray(b'\x05\x02\r\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 10
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\r\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [True, False]
LoomControl: sending  bytearray(b'\x05\x02\x0e\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 11
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x0e\x00\x01\x04\x03\xe0\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [False, True]
LoomControl: sending  bytearray(b'\x05\x02\x0f\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 12
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x03\x0f\x00\x01\x04\x03\xe1\x00\x00\x00'
checking if received message is a pick request
a request!
pattern row: [True, False]
LoomControl: sending  bytearray(b'\x05\x02\x10\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
data available to read
b'\x01\x01\x01\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02\x11\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
pattern row: [False, True]
LoomControl: sending  bytearray(b'\x05\x02\x12\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 14
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
pattern row: [True, False]
LoomControl: sending  bytearray(b'\x05\x02\x13\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 15
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
pattern row: [False, True]
LoomControl: sending  bytearray(b'\x05\x02\x14\x00\x06\x01\x06\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 14
placing marker on row 0
ym = 20
marker y = 0
scene y =  20.0
pattern row: [True, False]
LoomControl: sending  bytearray(b'\x05\x02\x15\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
data available to read
b'\x01\x01\x04\x01\x05\x02\x04\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x02\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x16\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x02\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x17\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x02\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x18\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x05\x02\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x19\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
data available to read
b'\x05\x02\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02\x1a\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x01\x01\x01\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x1b\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 0
marker y = -20
scene y =  20.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02\x1c\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
created marker at 120
data available to read
b'\x01\x01\x01\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x01\x01\x01\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02\x1d\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x1e\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
data available to read
b'\x01\x01\x01\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02\x1f\x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02 \x00\x06\x01\x06\x01\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x04\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x02\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x06\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
sent pick 13
placing marker on row 1
ym = 120
marker y = -20
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
>>> 
 RESTART: C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py 
ready to connect
connecting to real loom at  192.168.7.20 : 62000
making connection request
connecting to loom at  192.168.7.20 : 62000
1
2
connection successful! enabling functions
sending connect packets to loom
LoomControl: sending  b'\x04\x0e'
GUI: connection successful
3
data available to read
b'\x07\x06\x01\x0b\x0c\x07\x03\x05\t\x03\x03\x02\x03\n5\t\x03\r\x10\x03\x0e\x03\x03\x15\x01\x03\x17\xa4\x01\x03\x1b\x02\x03\x1d\xd0\x07\x03\x1f\x01\x00\x01\x03!\x01\x01\x03#\x01\x01\x03$\xff\x03+\x01\x01\x03-\x01\x01\x01\x02\x01\x04\x06\xd8\x809\xec\xfd\x1f\x01\x06\x15d\x00\t\t\x01\t\x0e.\x00\x00\x00\x00\t\x0e/\x00\x00\x00\x00\x02\r?\x00\x00\x00\x00\x00?\x00\x00\x00\x00\x00\x03,\x00\x00\x14\x07\xa8\xc0\x00\xff\xff\xff\x01\x07\xa8\xc0'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
pattern row: [0, 0, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02\x00\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
created marker at 140
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02\x01\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x01\x01\x01\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x02\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
>>> 
 RESTART: C:\Users\Shanel Wu\Documents\GitHub\EID_ECEN5783_Fall19\SuperProject\pyqt_weaving.py 
ready to connect
connecting to real loom at  192.168.7.20 : 62000
making connection request
connecting to loom at  192.168.7.20 : 62000
1
2
connection successful! enabling functions
sending connect packets to loom
LoomControl: sending  b'\x04\x0e'
GUI: connection successful
3
data available to read
b'\x07\x06\x01\x0b\x0c\x07\x03\x05\t\x03\x03\x02\x03\n5\t\x03\r\x10\x03\x0e\x03\x03\x15\x01\x03\x17\xa4\x01\x03\x1b\x02\x03\x1d\xd0\x07\x03\x1f\x01\x00\x01\x03!\x01\x01\x03#\x01\x01\x03$\xff\x03+\x01\x01\x03-\x01\x01\x01\x02\x01\x04\x06\xd8\x809\xec\xfd\x1f\x01\x06\x15d\x00\t\t\x01\t\x0e.\x00\x00\x00\x00\t\x0e/\x00\x00\x00\x00\x02\r?\x00\x00\x00\x00\x00?\x00\x00\x00\x00\x00\x03,\x00\x00\x14\x07\xa8\xc0\x00\xff\xff\xff\x01\x07\xa8\xc0'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
pattern row: [0, 0, 0, 1, 0, 1, 0, 0]
LoomControl: sending  bytearray(b'\x05\x02\x00\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
created marker at 140
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x01\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
data available to read
b'\x01\x01\x01\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x02\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum off
LoomControl: sending  b'\x01\x01\x01'
data available to read
b'\x01\x01\x01\x01'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x01\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd8\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
data available to read
b'\x04\x03\xd6\x00\x00\x00'
checking if received message is a pick request
not a request
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
sending vacuum toggle
sending vacuum on
LoomControl: sending  b'\x01\x01\x04'
LoomControl: sending  bytearray(b'\x05\x02\x03\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
data available to read
b'\x01\x01\x04\x01'
checking if received message is a pick request
received vacuum on confirmation
LoomControl: sending  bytearray(b'\x05\x02\x04\x00\x06\x01\x06\x01^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x04\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x02^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x05\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x03^\x8f^\xe8\x85N\x8d\xef\xd4J\xad\xd4\xe8_\xe8\xd4\xe8%\xd2?<\xb4\xf0\xd2\xb4\x0f/=<\xb4\x06\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x80\x00\x0f\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x00')
sent pick 0
placing marker on row 0
ym = 140
marker y = 0
scene y =  140.0
logging received in terminal
got new entry from loomHandler
appended to terminal
emitted messageFromLoom signal
>>> 
