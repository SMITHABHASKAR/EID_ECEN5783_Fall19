from template2_script import *
# import (weaving) Pattern, Region methods
# functions: regionsOnRow, regionsToRow, rowToPixels (which came from pyqt_weaving)

_BROKENTWILL_4 = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 0, 0]]
_BRKTWILL_HALF = []
_WAFFLE = [[0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0]]

# input: Pattern object
# returns a copy of the pattern with each row spaced out with an empty (all 0's) row
def halfPattern(pattern):
    newPattern = Pattern()
    for row in list.copy(pattern.data):
        #print("halving row", row)
        newPattern.data.append(list.copy(row))
        newPattern.data.append([0] * len(row))
    print ("halved pattern:", newPattern.data)
    return newPattern

# input: Pattern object
# returns a copy of the pattern with each row copied, doubling the height of the pattern
def doublePattern(pattern):
    newPattern = Pattern()
    for row in list.copy(pattern.data):
        #print ("doubling row", row)
        newPattern.data.append(list.copy(row))
        newPattern.data.append(list.copy(row))
    print ("doubled pattern:", newPattern.data)
    return newPattern

if __name__ == "__main__":
    brokenTwill = Pattern("4x4 Broken Twill", _BROKENTWILL_4)
    waffle = Pattern("Waffle", _WAFFLE)
    patterns = [brokenTwill, waffle]

    halvedBrokenTwill = halfPattern(patterns[0])
    doubledWaffle = doublePattern(patterns[1])
    patterns.append([halvedBrokenTwill, doubledWaffle])
    
    regions = [Region(), Region(), Region(), Region(), Region()]
    startBorder = regions[0]
    startBorder.pattern = brokenTwill
    startBorder.endRow = 105

    rBorder = regions[1]
    rBorder.pattern = halvedBrokenTwill
    rBorder.startRow = startBorder.endRow + 1
    rBorder.endRow = 393
    rBorder.endCol = 395

    pressureSensor = regions[2]
    pressureSensor.pattern = doubledWaffle
    pressureSensor.startRow = rBorder.startRow
    pressureSensor.endRow = rBorder.endRow
    pressureSensor.startCol = rBorder.endCol + 1
    pressureSensor.endCol = 923

    lBorder = regions[3]
    lBorder.pattern = rBorder.pattern
    lBorder.startRow = rBorder.startRow
    lBorder.endRow = rBorder.endRow
    lBorder.startCol = pressureSensor.endCol + 1
    lBorder.endCol = 1319

    endBorder = regions[4]
    endBorder.pattern = startBorder.pattern
    endBorder.startRow = rBorder.endRow + 1
    endBorder.endRow = 499

    for r in regions:
        r.updateWidth()
        #print ("region", r,"width:", r.width)

    img = np.empty((0, 1320))

    for i in range(0, endBorder.endRow + 1):
        rowToSend = regionsToRow(regionsOnRow(regions, i), i)
        #print ("sending row to loom:", rowToSend)
        imgRow = rowToPixels(rowToSend)
        #print ("image row:", imgRow)
        img = np.append(img, [imgRow], axis=0)
        if (i % 10 == 0):
            print ("row number:",i)
            cv.imshow('image',img)

    cv.imshow('image',img) # can call imshow multiple times to update the display window
    cv.imwrite('3_pressureSensor_SCRIPT.bmp', img)
