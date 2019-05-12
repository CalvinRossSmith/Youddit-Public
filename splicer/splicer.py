from moviepy.editor import concatenate_videoclips, VideoFileClip, CompositeAudioClip, AudioFileClip, afx
from splicer import processing as pros
from random import shuffle
import gc

def loadVideos(paths):
  clips = []
  for path in paths:
    vid = VideoFileClip(path)
    clips.append(vid)
  return clips

def interlaceClips(clips, clip):
  outputClips = []

  for x in clips:
    outputClips.append(x)
    outputClips.append(clip)

  outputClips = outputClips[:-1]

  return outputClips

def spliceVideos(paths, interlace=None, startClip=None, endClip=None):
  if startClip != None:
    clips = [startClip]
  else:
    clips = []
  
  clips = loadVideos(paths)

  clips = list(pros.processClips(clips))

  if interlace != None:
    clips = interlaceClips(clips, interlace)
  
  if endClip != None:
    clips.append(endClip)
  vid = concatenate_videoclips(clips, method="compose")
  return vid , clips

def overlayMusic (video, musicPath):
  videoLen = video.duration
  if not musicPath == None:
    shuffle(musicPath)
    try:
      music = AudioFileClip(musicPath[0])
    except:
      shuffle(musicPath)
      music = AudioFileClip(musicPath[0])
    musicLooped = afx.audio_loop(music, duration=videoLen)
    if musicLooped.duration > videoLen:
      musicLooped.set_duration(videoLen)
    try:
      vidAud = video.audio.volumex(1)
    except:
      vidAud = video.audio
    finAud = CompositeAudioClip([musicLooped.volumex(0.1),vidAud])
    return finAud, music, musicLooped
  else:
    return video.audio

def fullVideoSplicer(paths, saveTo, interlace=None, startClip=None, endClip=None, pathToMusic=None):
  if not startClip == None:
    startClip = VideoFileClip(startClip)
  if not interlace == None:
    interlace = VideoFileClip(interlace)
  if not endClip == None:
    endClip = VideoFileClip(endClip)
  final, clips = spliceVideos(paths, interlace=interlace, startClip=startClip, endClip=endClip)
  final.audio, music, musicLooped = overlayMusic(final, pathToMusic)
  print (final.duration)
  final.write_videofile(saveTo, codec='libx265', preset='ultrafast')
  for clip in clips:
    clip.close()
  musicLooped.close()
  music.close()
  final.close()
  gc.collect()



if __name__ == "__main__":
  final, clips = spliceVideos(["../testfiles/clip1.mp4", "../testfiles/clip2.mp4", "../testfiles/clip3.mp4", "../testfiles/clip4.mp4"], interlace=VideoFileClip("../testfiles/interlace.mp4"), startClip=VideoFileClip("../testfiles/end.mp4"), endClip=VideoFileClip("../testfiles/end.mp4"))
  #final = spliceVideos(["../testfiles/clip3.mp4"])
  #final = pros.processClip(VideoFileClip("../testfiles/clip4.mp4"))
  #final.preview()
  final.write_videofile("outputfile.mp4", fps=30, codec='libx265', bitrate='8000k', preset='ultrafast', threads=4)