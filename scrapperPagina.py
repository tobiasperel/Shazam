from lxml import html, etree
import requests
from datetime import datetime
from datetime import timedelta
# Get the original webpage html content
webpageLink = 'http://www.howtowebscrape.com/examples/simplescrape1.html'
page = requests.get(webpageLink)
# convert the data received into searchable HTML
extractedHtml = html.fromstring(page.content)
# use an XPath query to find the image link (the 'src' attribute of the 'img' tag).
imageSrc = extractedHtml.xpath("//img/@src") # in our example, result = ‘/images/GrokkingAlgorithms.jpg’
# strip off the actual *page* being called as we only want to base url
imageDomain = webpageLink.rsplit('/', 1) # in our example, result = http://www.howtowebscrape.com/examples/

# test if this is an absolute link or relative
if imageSrc[0].startswith("http"):
    # start with http, therefore take this as the full link
    imageLink = imageSrc[0]
else:
    # does not start with http, therefore construct the full url from the base url plus the absolute image link
    imageLink = str(imageDomain[0]) + str(imageSrc[0])

# extract file name from link
filename = imageLink.split("/")[-1] 
# download image using GET
rawImage = requests.get(imageLink, stream=True)
# save the image received into the file
with open(filename, 'wb') as fd:
    for chunk in rawImage.iter_content(chunk_size=1024):
        fd.write(chunk)

def downloadFile(AFileName):
    # extract file name from AFileName
    print(AFileName)
    filename = AFileName.split("/")[-1] 
    print(1)
    # download image using GET
    rawImage = requests.get(AFileName, stream=True)
    print(2)
    print(filename)
    # save the image recieved into the file
    with open(filename, 'wb') as fd:
        for chunk in rawImage.iter_content(chunk_size=1024):
            fd.write(chunk)
            
    return

#downloadFile("http://www.howtowebscrape.com/examples/media/images/BigRabbit.mp4")
#downloadFile("http://www.howtowebscrape.com/examples/media/images/Clapping.mp3")
downloadFile("https://mdstrm.com/audio/60a2745ff943100826374a70/icecast.audio")
#downloadFile("https://us-b4-p-e-pb13-audio.cdn.mdstrm.com/live-audio-aw-bkp/60a2745ff943100826374a70?aid=60106eadf34de307dd720e7b&pid=7ZsYsiwOYpASEqiisY976dd6q7C6bLAt&sid=7X2Ppm65hHIB7y2nuqJZGoaQx1xpDEQu&uid=bTtY9n2TgNU36rgYafLPghxubV87iVPr&es=us-b4-p-e-pb13-audio.cdn.mdstrm.com&ote=1655169010119&ot=eYiItrp8KKxfyb2XIrH5TA&proto=https&pz=us&cP=128000&awCollectionId=60106eadf34de307dd720e7b&liveId=60a2745ff943100826374a70&propertyName=mediastream-player-aspen-pie")
#downloadFile("http://www.howtowebscrape.com/examples/media/images/SampleSlides.pptx")
#downloadFile("http://www.howtowebscrape.com/examples/media/images/SampleZip.zip")