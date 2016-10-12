from os import listdir
from os.path import isfile, join
from pydub import AudioSegment

onlyfiles = [join("C:\\Users\\Sam\\Desktop\\New folder\\Conversion Test\\",f) for f in listdir("C:\\Users\\Sam\\Desktop\\New folder\\Conversion Test") if isfile(join("C:\\Users\\Sam\\Desktop\\New folder\\Conversion Test\\",f)) ]
for f in onlyfiles:

  if f.endswith(".mp3"):
    print(f)
    onlyfiles = AudioSegment.from_mp3(f)
    name = f.split(".")[0].split("\\")[-1]
    print("C:\\Users\\Sam\\Desktop\\New folder\\Conversion Test\\{}.wav".format(name))
    onlyfiles.export ("C:\\Users\\Sam\\Desktop\\New folder\\Conversion Test\\{}.wav".format(name), format="wav")