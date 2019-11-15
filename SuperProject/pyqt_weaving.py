# GUI portion: during weaving

# Details/state description: vacuum is on, threads are raised, weaver should have shuttles ready and does not have hands available except for simple button presses

# simple woven patterns for testing, store as a list of lists or AxB matrix
# for example, plainweave represents: 	0  	1 
#										1  	0 
plainweave = [[0, 1], [1, 0]]
twill = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]

# yarns listed as [ SHORTCODE, HEX_COLOR ]
yarn = [] # if yarn list is blank, fill with default yarn ['A', '0xFFFFFF'] (yarn A, white color)
twoYarns = [['A', '0xFFFFFF'], ['B', '0xFF0000']]

patternRow = 0
totalRows = 0
currentRowinTotal = 0

def renderPattern(pattern):
	

# 	BUTTON: Pause

# 	DISPLAY: Row number

# 	DISPLAY: Pattern repeat tracker
# 	Function/Appearance:
# 	- shows drawdown for the woven structure
# 	- marker that shows place in the structure

# 	DISPLAY: Yarn for this row (solid color or short code)

# 	DISPLAY: Weaving Progress/History (similar to entrance menu's)
# 	Function/Appearance:
# 	- the current row being woven (highlighted/boxed?)
# 	- below the current row, the previous rows that had been woven this session (grayed out?)

# 	DISPLAY (or buttons?): pedals (reverse, refresh, advance)
# 	Function/Appearance:
# 	- ALL: highlight/change color when physical pedal pressed
# 	- Reverse: send loom the previously woven row
# 	- Refresh: send loom the current row again
# 	- Advance: send loom the next row in design

def advance():
	patternRow = (patternRow + 1) % len(pattern) # loop back to row 1 of pattern if we are in the last one
	totalRows += 1
	currentRowinTotal += 1

	return generateNextRow()

def refresh():
	return regenerateRow()

def reverse():
	return fetchPrevRow()