from __future__ import unicode_literals
import youtube_dl

#used to log errors
class myLogger(object): #myLogger is a class that hold functions and depending on what the log is
                        #we decide if we want to keep it rn we only print to console an error message if and error occurs
                        #this just makes it so that console doesn't get bogged down
    def debug(self, msg):
        pass #personly don't want to clog console

    def warning(self, msg):
        pass #personly don't want to clog console

    def error(self, msg):
        pass
        #print(msg) #We should atleast see the errors

#used to log copletion of a video being downloaded
def myHook(_done):
    #myHook is the close to the same as the logger except it gets passed an array that has different 
    #stats about the current run
    #Right now we are only checking the status stat to see if it is equal to finish and if it is we print to console to 
    #keep things clean
    if _done['status'] == 'finished':
        pass
        #print('Done downloading, now converting ...') 


#the function tha uses the youtube downloader options to start downloading
def videoDownload(_url, pathToDownload, _format): #the url should be a list of string urls
    
    #the options that we want when downloading a video
    ydlOpts = {
        'format': ('bestvideo[ext='+_format+']+bestaudio[ext=m4a]/'+_format), #the format that it can be
        'logger': myLogger(), #this is used to log errors and such
        'progress_hooks': [myHook], #says when it's done dont know how useful
        'noplaylist': 'true', #makes it so that if the link is in a youtube playlist it wont download the whole playlist
        'outtmpl': (pathToDownload), #output location and name
        'ignoreerrors': 'true', #if error move one
        'restrictfilenames': 'true' #gets rid of spaces in output name
    }
    with youtube_dl.YoutubeDL(ydlOpts) as ydl:
        ydl.download(_url)