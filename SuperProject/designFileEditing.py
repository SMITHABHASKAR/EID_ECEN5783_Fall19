# pattern generation/editing classes and functions

import numpy as np
import PIL as cv

_MODULES = 6
_TPM = 220
_ROWWIDTH = _MODULES * _TPM

class Yarn(object):
    def __init__(self, index=0, name="Default", code="A", color='0xFFFFFF'):
        self.id = index
        self.name = name # a string
        self.code = code # a 3-char or shorter code
        self.color = color # a string containing a hex code

class Pattern(list):
    def __init__(self, patternName="", data=[]):
        self.name = patternName
        self.data = list.copy(data)
        self.yarns = [Yarn()] # one default yarn
        self.yarnOrder = self.yarns * len(self.data) # list with length = pattern height; default: use the yarn on every row

    def __len__(self):
        return len(self.data)

    # input: order - a list of Yarn objects
    def setYarnOrder(self, order=None):
        if order is None:
            for row in range(0, len(self.data)):
                yarnIndex = row % len(self.yarns)
                self.yarnOrder[row] = self.yarns[yarnIndex]
        elif len(order) == len(self.data):
            self.yarnOrder = order
        else:
            print ("invalid yarn order")

    # input: Pattern object
    # returns a copy of the pattern with each row spaced out with an empty (all 0's) row
    def halfPattern(self):
        newPattern = Pattern(self.name + " halved")
        for row in list.copy(self.data):
            #print("halving row", row)
            newPattern.data.append(list.copy(row))
            newPattern.data.append([0] * len(row))
        print ("halved pattern:", newPattern.data)
        return newPattern

    # input: Pattern object
    # returns a copy of the pattern with each row copied, doubling the height of the pattern
    def doublePattern(self):
        newPattern = Pattern(self.name + " doubled")
        for row in list.copy(self.data):
            #print ("doubling row", row)
            newPattern.data.append(list.copy(row))
            newPattern.data.append(list.copy(row))
        print ("doubled pattern:", newPattern.data)
        return newPattern

class Region(object):
    def __init__(self, index=0, startRow=0, endRow=100, shape = None, pattern = None):
        self.id = index
        self.startRow = startRow
        self.endRow = endRow
        self.shape = shape # None for a rectangular region
        self.startCol = 0
        self.endCol = 1319  # startCol, endCol, width only make sense for a rectangular region
        self.width = abs(self.endCol - self.startCol + 1)
        self.pattern = None # Pattern object

        self.yarns = []
        self.yarnOrder = []

    def updateWidth(self):
        if self.shape is None:
            #print ("updating width of region")
            self.width = abs(self.endCol - self.startCol + 1)

    def setFullWidth(self):
        self.startCol = 0
        self.endCol = 1319 # flexibility for num of modules?
        self.width()

    def isFullWidth(self):
        if self.width() == 1320:
            return True
        else: return False

    def isOnRow(self, rowNum):
        #print ("Region starts on", self.startRow, "and ends on", self.endRow)
        #print ("Is region on row", rowNum, "?")
        if (rowNum >= self.startRow and rowNum <= self.endRow):
            #print ("Region is on row", rowNum)
            return True
        else:
            #print ("Region is NOT on row", rowNum)
            return False
            
    def patternRow(self, rowNum):
        if rowNum >= self.startRow:
            return (rowNum - self.startRow) % len(self.pattern)

    def patternToRegion(self, patternRowNum):
        # return a row of weaving, based on patternToRow
        fill = self.pattern.data[patternRowNum]
        print ("pattern row:", fill)
        regionRow = np.array([], dtype=int)
        if self.shape is None: # for a rectangular region
            while (regionRow.size < self.width):
                rem = self.width - regionRow.size
                if (rem < len(fill)): # ideally, we wouldn't want a partial repeat of a pattern, but right now there's no user warning for that
                    regionRow = np.append(regionRow, fill[0:rem])
                else:
                    regionRow = np.append(regionRow, fill)
        # elif [TODO: non-rectangular region]
        #print ("region row -", len(regionRow), "ends:", regionRow)
        return regionRow

class WeaveDesign(object):
    def __init__(self, name="New Design"):
        self.patterns = [] # list of patterns used in design
        self.regions = [] # list of regions defined in the design
        self.yarns = [] # list of yarns used in design

        self.img = np.empty((0, _ROWWIDTH)) # array to store image data
        self.name = name # string for file name

    def addPattern(self, pattern):
        self.patterns.append(pattern)

    def addRegion(self, region):
        self.regions.append(region)

    def regionsOnRow(regions, rowNum):
        #print ("filtering regions:", regions)
        regs = []
        for r in regions:
            if r.isOnRow(rowNum):
                regs += [r]
        return regs

    # input: list of Region objects
    def regionsToRow(regions, rowNum):
        #regionsOnRow = regionsOnRow(regions, rowNum)
        #print ("regions:",regions)
        rowToSend = np.array([], dtype=int)
        if regions == []:
            #print ("error: no regions defined on this row")
            return None
        for r in regions:
            #print ("appending region", r)
            rowToSend = np.append(rowToSend, r.patternToRegion(r.patternRow(rowNum)))
        #print ("returning rowToSend from regions -", len(rowToSend), "ends:", rowToSend)
        return rowToSend

    def rowToPixels(row):
        # rows sent to loom are 0's and 1's,
        # but a B&W bitmap needs 0 -> 255 for white pixels
        # and 1 -> 0 for black pixels
        pixelRow = np.empty(len(row), dtype=int)
        #print (len(pixelRow))
        for i in range(0, len(pixelRow)):
            if (row[i] == False):
                #print ("false")
                pixelRow[i] = 255
            elif (row[i] == True):
                #print ("true")
                pixelRow[i] = 0
            # print (pixelRow[i], row[i])
        return pixelRow

if __name__ == "__main__":
    w = WeaveDesign("designFileEditing.py test")

    # load patterns from patterns.json as Pattern objects
    with open('patterns.json', 'r') as patternFile:
        data = patternFile.read() 
        patternList = json.loads(data) # a list of dicts

        for p in patternList:
            patternObj = Pattern(p['name'], p['pattern'])
            w.addPattern(patternObj)
            print (patternObj.name)

    print ("patterns loaded:", len(w.patterns))
