from moviepy.editor import CompositeVideoClip, ColorClip

out_width = 1920
out_height = 1080
out_ratio = out_width / out_height

def processClip(clip):
    """
    Preprocesses a single clip to be concatanted and outputted
    """
    clip_width = clip.w
    clip_height = clip.h

    front_clip = clip.copy()
    if clip_width / clip_height > out_ratio:
        front_clip = front_clip.resize(width=out_width)
        back_clip = ColorClip((out_width, out_height), (0, 0, 0), duration=clip.duration)
        return overlayClips(front_clip, back_clip)
    elif clip_width / clip_height < out_ratio:
        front_clip = front_clip.resize(height=out_height)
        back_clip = ColorClip((out_width, out_height), (0, 0, 0), duration=clip.duration)
        return overlayClips(front_clip, back_clip)
    else:
        return clip.resize((out_width, out_height))  # clip is already the right size, just send it back with no changes


def processClips(clips):
    """
    Processes a list of clips to be concatanted and outputted
    """
    for clip in clips:
        yield processClip(clip)


def overlayClips(clipTop, clipBottom):
    """
    Overlays a one clip on top of another
    Used for doing the gauss blur style bars on the video
    """
    return CompositeVideoClip([clipBottom.set_pos("center"), clipTop.set_pos("center")], size=(out_width, out_height))
