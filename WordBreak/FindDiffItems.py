import os,re
from openpyxl import Workbook



def fillTheCompareTable(senA, senB):
    table = []
    clumnLen=len(senA)+1
    currentLine = list(range(clumnLen))
    table.append(currentLine)
    
    for itemB in senB:
        preLine=currentLine
        currentLine=[0]*clumnLen
        currentLine[0]=(preLine[0]+1)
        for tableIndex in range(1, len(senA)+1):
            itemA=senA[tableIndex-1]
            if itemA == itemB:
                currentLine[tableIndex]=preLine[tableIndex-1]
            else:
                currentLine[tableIndex]=min(preLine[tableIndex-1], preLine[tableIndex], currentLine[tableIndex-1])+1
        table.append(currentLine)

    return table

def returnMatchingStrs(table, senA, senB):
    resA=resB=str()
    rawIndex=columnIndex=-1
    fillSymbol='_'
    
    while rawIndex >= -len(senA) and columnIndex >= -len(senB):
        minNumAroundCur=min(table[columnIndex-1][rawIndex-1], table[columnIndex-1][rawIndex], table[columnIndex][rawIndex-1])
        if senA[rawIndex]==senB[columnIndex]:
            resA+=senA[rawIndex]
            resB+=senB[columnIndex]
            rawIndex-=1
            columnIndex-=1
        elif table[columnIndex-1][rawIndex-1]==minNumAroundCur:
            resA+=senA[rawIndex]
            resB+=senB[columnIndex]
            rawIndex-=1
            columnIndex-=1
        elif table[columnIndex-1][rawIndex]==minNumAroundCur:
            resA+=fillSymbol
            resB+=senB[columnIndex]
            columnIndex-=1
        elif table[columnIndex][rawIndex-1]==minNumAroundCur:
            resA+=senA[rawIndex]
            resB+=fillSymbol
            rawIndex-=1

    if len(resA)<len(senA):
        time=len(senA)-len(resA)-1
        for x in senA[time::-1]:
            resA += x
            resB+=fillSymbol
    elif len(resB)<len(senB):
        time=len(senB)-len(resB)-1
        for x in senB[time::-1]:
            resB += x
            resA+=fillSymbol

    return resA[::-1],resB[::-1]
            
def findDiffBreakPart(senA, senB):
    expression=r'[^ ]+_[^ ]+'
    matches = re.finditer(expression,senA)
    l = [(m.group(0).replace('_',''),senB[m.span()[0]:m.span()[1]]) for m in matches]
    matches = re.finditer(expression,senB)
    l += [(senA[m.span()[0]:m.span()[1]], m.group(0).replace('_','')) for m in matches]
    return l

def genFileAndPathDict(folderName):
    fileNameList=os.listdir(folderName)
    return {x:os.path.join(folderName, x) for x in fileNameList}


def getDiffList(senA, senB):
    tableResult=fillTheCompareTable(senA,senB)
    (rA,rB)=returnMatchingStrs(tableResult,senA, senB)
    return findDiffBreakPart(rA,rB)


def mainFunc(o14ResultFolder, o16ResultFolder, oriSentence, compareResult):
    o14Dic=genFileAndPathDict(o14ResultFolder)
    o16Dic=genFileAndPathDict(o16ResultFolder)
    oriDic=genFileAndPathDict(oriSentence)

    wb=Workbook()
    ws=wb.active
    ws.title='Wrod break compare'
    txtObj=open(compareResult, 'w', encoding='utf-16')
    for o16File in o16Dic:
        o14Path=o14Dic[o16File]
        o16Path=o16Dic[o16File]
        oriPath=oriDic[o16File]
        writeToExcel(o14Path, o16Path, oriPath, ws)
        #writeToTxt(o14Path, o16Path, oriPath, txtObj)
    wb.save(compareResult)
    txtObj.close()

def writeToTxt(o14Path, o16Path, oriPath, txtObj):
    for o14WB,o16WB,ori in zip(open(o14Path, encoding='utf-16'), open(o16Path, encoding='utf-16'), open(oriPath, encoding='utf-16')):
                if o14WB != o16WB:
                    txtObj.write(ori)



                    
def writeToExcel(o14Path, o16Path, oriPath, worksheet):

    for o14WB,o16WB,ori in zip(open(o14Path, encoding='utf-16'), open(o16Path, encoding='utf-16'), open(oriPath, encoding='utf-16')):
                if o14WB != o16WB:
                    for o14, o16 in getDiffList(o14WB, o16WB):
                        try:
                            worksheet.append(['original sentence', '\'' + ori])
                            worksheet.append(['o16 sentence', '\'' + o14WB, o14])
                            worksheet.append(['o16+ sentence', '\'' + o16WB, o16])
                        except :
                            print(ori)
                         
