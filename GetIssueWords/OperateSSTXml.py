import xml.dom.minidom, os

def writeToScriptTxt(scriptList):
    with open('script.txt', 'w', encoding = 'utf-16') as writer:
        for line in scriptList:
            writer.write(line)
            writer.write('\n')
    return 'script.txt'

def GenSstXml(textPath, language):
    name, suffix = os.path.splitext(textPath)
    xmlPath = name + '.xml'
    cmdPattern = 'StatisticSamplingTest_v3.exe -mode converttext -inscriptfile  {0} -lang {1} -outscriptfile {2} -savepronsource True'
    cmd = cmdPattern.format(textPath, language, xmlPath)
    os.system(cmd)
    return xmlPath

def GetPronAndPronSourceList(sstXmlPath, wordlist):
    xmlTree = xml.dom.minidom.parse(sstXmlPath)
    root = xmlTree.documentElement
    siNodes=root.getElementsByTagName('si')
    res=[]
    for siNode, word in zip(siNodes, wordlist):
        res.append(GetAttrPronAndSource(siNode, word))
    return res


def GetAttrPronAndSource(siNode, word):
    for sentNode in siNode.getElementsByTagName('sent'):
        for wordNode in sentNode.getElementsByTagName('words'):
            for wNode in wordNode.getElementsByTagName('w'):
                if wNode.getAttribute('v') == word:
                    return  wNode.getAttribute('p'), wNode.getAttribute('pronSource')

def GetInfoFromEngine(scriptList, language, wordlist):
    textPath = writeToScriptTxt(scriptList)
    sstPath = GenSstXml(textPath, language)
    pronAndPronSource = GetPronAndPronSourceList(sstPath, wordlist)
    return pronAndPronSource
        
