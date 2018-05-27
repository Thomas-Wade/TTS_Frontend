import os, glob

ffmpegPath=r"E:\Sound_Effect\cloudAudio\ffmpeg.exe"
waveSourceFolder=r'E:\Sound_Effect\warning'
outputFolder=['pcm','32','64','128']

def convertToPcm(oriWaveFolder, outputFolder, cmdParrten, suffix):
    oriWaves=glob.glob(oriWaveFolder+r'\*.wav')
    outPath=oriWaveFolder+ '\\'+outputFolder
    os.makedirs(outPath)
    for oriWave in oriWaves:
        fileName=os.path.splitext(os.path.basename(oriWave))[0]
        outWave=outPath+ '\\'+fileName+suffix
        cmd=cmdParrten%(ffmpegPath, oriWave, outWave)
        os.system(cmd)

def run():
    for name in outputFolder:
        if(name=='pcm'):
            convertToPcm(waveSourceFolder,name,'%s -i %s -ac 1 -ar 16000 -sample_fmt s16 %s', '.wav')
        else:
            convertToPcm(waveSourceFolder+'\\'+'pcm',name,'%s -i %s -ab '+name+'000 %s', '.mp3')

run()

