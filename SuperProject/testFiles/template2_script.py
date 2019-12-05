# script for template 2 (instead of .BMP file)

import numpy as np
import cv2 as cv

_WARP_REP_2 = [[0, 0, 1, 1], [1, 1, 0, 0]]
_WARP_REP_HALF = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
_DOUBLE = [[0, 0, 0, 1], [0, 1, 1, 1], [0, 1, 0, 0], [1, 1, 0, 1]]

class Yarn(object):
    def __init__(self, name="", code="", color='0xFFFFFF'):
        self.name = name # a string
        self.code = code # a 3-char or shorter code
        self.color = color # a string containing a hex code

class Pattern(list):
    def __init__(self):
        self.name = ""
        self.data = []
        self.yarns = [0]
        self.yarnOrder = []

    def __init__(self, patternName="", data=[]):
        self.name = patternName
        self.data = list.copy(data)
        self.yarns = [0]
        self.yarnOrder = []
        #self.setYarnOrder()

    def __len__(self):
        return len(self.data)

    def setYarnOrder(self, order=None):
        if order is None:
            for row in self.data:
                self.yarnOrder += self.yarns
        elif len(order) == len(self.data):
            self.yarnOrder = order
        else:
            print ("invalid yarn order")

class Region(object):
    def __init__(self, startRow=0, endRow=100, shape = None, pattern = None):
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
    patterns = [Pattern("2x2 Rep", _WARP_REP_2), Pattern("Doubleweave", _DOUBLE), Pattern("2x2 Rep Half", _WARP_REP_HALF)]

    regions = [Region(), Region(), Region(), Region(), Region()]
    regions[0].pattern = patterns[0] # rep weave
    regions[0].endRow = 105

    regions[1].pattern = patterns[2] # rep weave with every other row empty
    regions[1].startRow = 106
    regions[1].endRow = 393
    regions[1].startCol = 0
    regions[1].endCol = 395

    regions[2].pattern = patterns[1] # doubleweave
    regions[2].startRow = regions[1].startRow
    regions[2].endRow = regions[1].endRow
    regions[2].startCol = 396
    regions[2].endCol = 923

    regions[3].pattern = patterns[2]
    regions[3].startRow = regions[1].startRow
    regions[3].endRow = regions[1].endRow
    regions[3].startCol = 924
    regions[3].endCol = 1319

    regions[4].pattern = patterns[0]
    regions[4].startRow = 394
    regions[4].endRow = 499
    regions[4].startCol = 0
    regions[4].endCol = 1319

    for r in regions:
        r.updateWidth()
        print ("region", r,"width:", r.width)

    img = np.empty((0, 1320))

    for i in range(0, 500):
        rowToSend = regionsToRow(regionsOnRow(regions, i), i)
        #print ("sending row to loom:", rowToSend)
        imgRow = rowToPixels(rowToSend)
        #print ("image row:", imgRow)
        img = np.append(img, [imgRow], axis=0)
        if (i % 10 == 0):
            print ("row number:",i)
            cv.imshow('image',img)

    cv.imshow('image',img) # can call imshow multiple times to update the display window
    cv.imwrite('2_doubleweaving_SCRIPT.bmp', img)
