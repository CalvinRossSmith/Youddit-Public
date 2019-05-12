from moviepy.editor import VideoFileClip
import random
import time

def getDuration(clips):
  total = 0.0 
  for clip in clips:
    try:
      duration = clip["duration"]
      total += duration
    except:
      print("failuer")
  return total

def distabutor(clips, minDur, done=[]):
  n = getDuration(clips) // minDur
  print(clips)
  clips.sort(key=lambda x: x["duration"], reverse=True)
  buckets = []
  for x in range(int(n)):
    buckets.append([])

  curBucket = 0
  while len(clips) > 0:
    clip = clips[0]
    if len(buckets) == 0:
      break
    buckets[curBucket].append(clip)
    if getDuration(buckets[curBucket]) > minDur:
      done.append(buckets[int(curBucket)])
      del buckets[curBucket]
      if(len(buckets) == 0):
        break
    clips = clips[1:]
    curBucket = int((curBucket + 1) % len(buckets))

  unused = []
  for x in buckets:
    for y in x:
      unused.append(y)
  
  unused = unused + clips

  if getDuration(unused) > minDur:
    return distabutor(unused, minDur, done)
  

  return (done)
  

def splitClips(clips, minDuration):
  """
  Splits the clips into sub lists that have at least minDuration seconds of length
  """
  doneBuckets = distabutor(clips, minDuration)

  outputa = list(map(lambda x: list(map(lambda y: y["clip"], x)), doneBuckets))
  
  return (outputa)


if __name__ == "__main__":
  outp = splitClips(["../testfiles/clip1.mp4", "../testfiles/clip2.mp4", "../testfiles/clip3.mp4", "../testfiles/clip4.mp4"], 10)
  for x in outp:
    print(x)