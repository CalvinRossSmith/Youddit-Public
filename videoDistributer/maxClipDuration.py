from moviepy.editor import VideoFileClip

def maxDuration(clips, maxDura):
  #maxDura is in seconds
  ret = []
  for clip in clips:
    try:
      vid = VideoFileClip(clip)
      if vid.duration <= maxDura:
        ret.append({"clip": clip, "duration": vid.duration})
      vid.reader.close()
      vid.close()
    except:
      print ("fail in max")
  return ret