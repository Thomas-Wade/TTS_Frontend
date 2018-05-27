import sys, getopt

def readCommand(argv):
    model=''
    inputExcel=''
    remaindLine = 'SummarizeIssueWordsInfo.py -m <Excel>\<Wordlist> -i <HURS ExcelPath>'

    if not argv:
        print(remaindLine)
        sys.exit(2)

    try:
        opts, args = getopt.getopt(argv,"hm:i:",["help", "model=","input="])
    except getopt.GetoptError:
        print(remaindLine)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', 'help'):
            print(remaindLine)
            sys.exit()
        elif opt in ('-m', 'model'):
            model = arg
        elif opt in ('-i', 'input'):
            inputExcel = arg.strip('"')
    return model, inputExcel

model, inputExcel = readCommand(sys.argv[1:])
import ProcessHandle
ProcessHandle.StartProcess(model, inputExcel)

        