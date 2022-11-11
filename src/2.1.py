import pandas as pd
import numpy as np
import sys
import math

def getValuesAmount(dataFrame, column, toPrint=False):
    columnDict = {}
    columnList = dataFrame[column].tolist()

    for e in columnList:
        if type(e) == float:
            if not 'Unknown' in columnDict:
                columnDict['Unknown'] = 0
            columnDict['Unknown'] = columnDict['Unknown'] + 1
        else:
            if not e in columnDict:
                columnDict[e] = 0
            columnDict[e] = columnDict[e] + 1
    
    if toPrint:
        print(f'### {column} ###')
        for k, v in columnDict.items():
            print(f'    {k}: {v}')
        print("")

    return columnDict

def getStatValues(dataFrame, column, toPrint=False):
    columnDict = {}
    columnListTmp = dataFrame[column].tolist()
    columnList = [item for item in columnListTmp if not math.isnan(item) == True]

    columnDict['unknown'] = len(columnListTmp) - len(columnList)
    columnDict['amean'] = np.mean(columnList)

    if min(columnList) < 0:
        columnDict['gmean'] = 'Undefined'
    else:
        columnDict['gmean'] = np.exp(np.log(columnList).mean())

    columnDict['hmean'] = len(columnList) / np.sum( [(1/item) for item in columnList] )
    columnDict['median'] = np.median(columnList)
    columnDict['span'] = max(columnList) - min(columnList)
    columnDict['std'] = np.std(columnList)

    if toPrint:
        print(f'### {column} ###')
        print(f'    Unknown: {columnDict["unknown"]}')
        print(f'    Aritmetic mean: {columnDict["amean"]}')
        print(f'    Geometric mean: {columnDict["gmean"]}')
        print(f'    Harmonic mean: {columnDict["hmean"]}' )
        print(f'    Median: {columnDict["median"]}' )
        print(f'    Span: {columnDict["span"]}' )
        print(f'    Standart deviation: {columnDict["std"]}' )
        print("")
    
    return columnDict

if __name__ == '__main__':
    dtype = {'Species': str, 'Region': str, 'Island': str, 'Stage': str, 'Individual ID': str, 'Clutch Completion': str, 'Date Egg': str, 'Culmen Length (mm)': float, 'Culmen Depth (mm)': float, 'Flipper Length (mm)': float, 'Body Mass (g)': float, 'Sex': str, 'Delta 15 N (o/oo)': float, 'Delta 13 C (o/oo)': float}
    penguins = pd.read_csv(sys.argv[1])
    getValuesAmount(penguins, 'Species', True)
    getValuesAmount(penguins, 'Region', True)
    getValuesAmount(penguins, 'Island', True)
    getValuesAmount(penguins, 'Stage', True)
    getValuesAmount(penguins, 'Clutch Completion', True)
    getStatValues(penguins, 'Culmen Length (mm)', True)
    getStatValues(penguins, 'Culmen Depth (mm)', True)
    getStatValues(penguins, 'Flipper Length (mm)', True)
    getStatValues(penguins, 'Body Mass (g)', True)
    getValuesAmount(penguins, 'Sex', True)
    getStatValues(penguins, 'Delta 15 N (o/oo)', True)
    getStatValues(penguins, 'Delta 13 C (o/oo)', True)
