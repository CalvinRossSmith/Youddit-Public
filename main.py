
from scraper import redditScraper
from downloader import videoDownloader
from splicer import splicer
from videoDistributer import distributer
from videoDistributer import maxClipDuration
import random
import ntpath
import os
import shutil
import gc

def randomName (__paths):
    return (ntpath.basename(random.choice(__paths)))

def mainYoudit():
    channel = 'CHANNEL NAME'
    subredditList = ['SUBREDDIT1', 'SUBREDDIT2', 'SUBREDDIT3', 'SUBREDDIT4', 'SUBREDDIT5', 'SUBREDDIT6', 'SUBREDDIT7', 'SUBREDDIT8']
    pathToDownload = ('/ABSOLUTEPATH/'+channel+'/')
    format = 'mp4'
    finalSave = ('/ABSOLUTEPATH/'+channel+'/')

    for subreddit in subredditList:
        listOfPosts = redditScraper.redditScraper(subreddit, amountOfPosts=None,topOfWhat='all')
        for post in listOfPosts:
            path = (pathToDownload + post["title"] + "." + format)
            videoDownloader.videoDownload([post["url"]], path, format)
    listOfPaths = ([(pathToDownload+f) for f in os.listdir(pathToDownload) if os.path.isfile(os.path.join(pathToDownload, f))])

    print("")
    print("Sorting by max duration")
    listWithDurMax = maxClipDuration.maxDuration(listOfPaths, 45)
    listOfPaths = None
    print("")
    print("Sorting into buckets")
    bucketListPaths = distributer.splitClips(listWithDurMax, 300)
    print("")
    print("Grabing Music")
    listMusicPath = ([('./copyrightFreeMusic/'+f) for f in os.listdir('./copyrightFreeMusic/') if os.path.isfile(os.path.join('./copyrightFreeMusic/', f))])
    if not os.path.exists(finalSave):
        os.makedirs(finalSave)
    vidNum = 1
    for pathLists in bucketListPaths:
        gc.collect()
        print("")
        print("Making video # "+str(vidNum)+"/"+str(len(bucketListPaths)))
        titleName = randomName(pathLists)
        try:
            splicer.fullVideoSplicer(pathLists, finalSave+titleName, pathToMusic=listMusicPath)
        except:
            print ("failed during making a video")
            print("")
        vidNum += 1
        gc.collect()
    print("")
    print("Removing the cached clips")
    shutil.rmtree(pathToDownload)
        
if __name__ == "__main__":
    mainYoudit()
    