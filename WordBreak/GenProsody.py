import os, glob

lang = 'zh-CN'
inputFokder = r'E:\Result\Prosody\sd'

ScriptProcessor = 'ScriptProcessor.exe -mode converttoxml -lang {0} -inscriptdir "{1}" -outscriptdir "{2}" -inscriptwithoutpron'
ScriptTaggerPron = 'ScriptTagger.exe -mode pronunciation -lang {0} -sd "{1}" -td "{2}" -inscriptwithoutpron -report report.txt'
SliceGenerator = 'SliceGenerator.exe -l {0} -phonebased -sd "{1}" -td "{2}"'
ScriptTaggerProsody = 'ScriptTagger.exe -mode prosody -lang {0} -sd "{1}" -td "{2}" -report report.txt'

parentFolder=os.path.dirname(inputFokder)
xml = os.path.join(parentFolder, 'xml')
os.system(ScriptProcessor.format(lang, inputFokder, xml))
pron = os.path.join(parentFolder, 'pron')
os.system(ScriptTaggerPron.format(lang, xml, pron))
slince = os.path.join(parentFolder, 'slince')
os.system(SliceGenerator.format(lang, pron, slince))
prosody = os.path.join(parentFolder, 'prosody')
os.system(SliceGenerator.format(lang, slince, prosody))


