'''
#https://github.com/andreztz/pyradios
from pyradios import RadioBrowser
rb = RadioBrowser()
data = rb.search(name="FM ASPEN 102.3", name_exact=True)
radioEnVivo = data[0]["url"]
print(radioEnVivo)
'''
import os
script = "curl --max-time 60 --output output.wav https://us-b4-p-e-qg12-audio.cdn.mdstrm.com/live-audio-aw-bkp/60a2745ff943100826374a70?aid=60106eadf34de307dd720e7b&pid=Ql6BVyib6PaKQY9MrnZ05OCvef5XAFsJ&sid=1CpzakzH9Jo6ihLF88BNMiciY1W0PHDC&uid=bTtY9n2TgNU36rgYafLPghxubV87iVPr&es=us-b4-p-e-qg12-audio.cdn.mdstrm.com&ote=1655238999772&ot=PqOmqK17pEuIIb8a_sA86Q&proto=https&pz=us&cP=128000&awCollectionId=60106eadf34de307dd720e7b&liveId=60a2745ff943100826374a70&propertyName=mediastream-player-aspen-pie"

def grabar():
    os.system(script)
