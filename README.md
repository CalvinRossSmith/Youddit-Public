# Youddit-Release

![Youddit](youdditProfilePic.png)

## Demo

[Demo YouTube Channel](https://www.youtube.com/channel/UCTGH8r_5szNZ6riHOWlU0wg "Demo")

## Summary

Youddit is made up of customizable python scripts. These scripts include a reddit web scraper that looks for urls of a selected subreddit. A downloading script is then called that will search each url to look and see if a video is attached to the url, if so the video will be downloaded. Once a whole grouping of videos are downloaded they are randomly compiled into 5 minute compilations. Once the video is created it is uploaded to YouTube.

## Quick Start

1. Install the required pip packages (moviepy, praw, youtube_dl)
2. Input your own client id for reddit (https://github.com/reddit-archive/reddit/wiki/oauth2) inside of scraper/redditScraper.py
3. Go to ./main.py
4. Decide which subreddits you would like to download videos from and add/remove them from the list “subredditList”
5. Change what you would like your channel name to be, this will be the name of the directory where the clips are temporarily stored
6. Add the absolute path for downloading to “pathToDownload”
7. Add the absolute path for your final save location “finalSave”
8. Create a directory at root called “copyrightFreeMusic”
9. Move your copyright free music into the directory from above
10. Type python3 ./main.py into termal to start

## ToDo
- [x] Video Downloader
- [x] Scrape reddit for videos to download
- [x] Resizing tool for videos
- [x] Create a distrubutor to organize videos into 5 minute montages
- [x] Discard clips over a certian length
- [x] Compile the videos together
- [x] Overlay music to videos
- [x] Stress test it to make sure it can handle 5000+ clips compiling down to 150+ videos
- [ ] Finish a youtube uploader
- [ ] Create a config file tool so that a user can quickly switch between subreddits and youtube channels

