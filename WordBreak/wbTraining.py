import os

def sentenceToChar(sentenceTxt):
    outputFile = os.path.splitext(sentenceTxt)[0] + '_out_1.txt'
    with open(outputFile, 'w', encoding = 'utf-8') as writer:
        for line in open(sentenceTxt, 'r', encoding = 'utf-8'):
            dealLine(line, writer)

def dealLine(line, writer):
    line = line.strip('\n').encode('utf-8').decode('utf-8-sig')
    writer.write('<BOS>\tS\n')
    words = line.split('  ')
    for word in words:
        if len(word) == 1:
            writer.write('{0}\tS\n'.format(word))
        elif len(word) > 1:
            writer.write('{0}\tB\n'.format(word[0]))
            for w in word[1:-1]:
                writer.write('{0}\tM\n'.format(w))
            writer.write('{0}\tE\n'.format(word[-1]))
    writer.write('<EOS>\tS\n')

def convertToBMES(bmesFile):
    allLines = open(bmesFile, 'r', encoding = 'utf-8').readlines()
    with open(r"E:\Result\WB_Training\CorpusDongxu\test_1.data", 'w', encoding = 'utf-8') as writer:
        for line in allLines:
            if line == '\n':
                writer.write('<EOS>\tS\n')
                writer.write('<BOS>\tS\n')
            else:
                writer.write(line)

def GetTrainingWordList(trainingFile):
    wordListPath = os.path.dirname(trainingFile) + '\\wordlist.txt'
    wordList = set()
    word = ''
    for line in open(trainingFile, 'r', encoding = 'utf-8' ):
        w, t = line.strip('\n').split('\t')
        if t == 'S':
            wordList.add(w)
        elif t == 'E':
            word += w
            wordList.add(word)
            word = ''
        else:
            word += w
    with open(wordListPath, 'w', encoding = 'utf-8') as writer:
        for w in wordList:
            writer.write(w + '\n')





GetTrainingWordList(r"E:\Result\WB_Training\CorpusDongxu\train.data")



        
