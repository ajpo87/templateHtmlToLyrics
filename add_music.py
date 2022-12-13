# import moviepy.editor as mpe
#
# clip = mpe.VideoFileClip("data-set-race-01/video_EX9.avi")
# audio_bg = mpe.AudioFileClip("dua_lipa.mp3")
# final_audio = mpe.CompositeAudioClip([audio_bg, clip.audio])
# final_clip = clip.set_audio(final_audio)
# final_clip.write_videofile("data-set-race-01/output.mp4")

from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import argparse

# make a command-line argument parser & add various parameters
parser = argparse.ArgumentParser(description="Python script to add audio to video clip")
parser.add_argument("-v", "--video-file", help="Target video file")
parser.add_argument("-a", "--audio-file", help="Target audio file to embed with the video")
parser.add_argument("-s", "--start", help="Start duration of the audio file, default is 0", default=0, type=int)
parser.add_argument("-e", "--end", help="The end duration of the audio file, default is the length of the video file", type=int)
parser.add_argument("-c", "--composite", help="Whether to add to the existing audio in the video", action="store_true", default=False)
parser.add_argument("-f", "--volume-factor", type=float, default=1.0, help="The volume factor to multiply by the volume of the audio file, 1 means no change, below 1 will decrease volume, above will increase.")
# parse the arguments
args = parser.parse_args()
video_file = args.video_file
audio_file = args.audio_file
start = args.start
end = args.end
composite = args.composite
volume_factor = args.volume_factor
# print the passed parameters, just for logging
print(vars(args))

# load the video
video_clip = VideoFileClip("data-set-race-01/video_dualipa.avi")
# load the audio
audio_clip = AudioFileClip("dua_lipa.mp3")

# use the volume factor to increase/decrease volume
audio_clip = audio_clip.volumex(volume_factor)

# if end is not set, use video clip's end
if not end:
    end = video_clip.end
# make sure audio clip is less than video clip in duration
# setting the start & end of the audio clip to `start` and `end` paramters
audio_clip = audio_clip.subclip(0, end)

# composite with the existing audio in the video if composite parameter is set
if composite:
    final_audio = CompositeAudioClip([video_clip.audio, audio_clip])
else:
    final_audio = audio_clip
# add the final audio to the video
final_clip = video_clip.set_audio(final_audio)

# save the final clip
final_clip.write_videofile("data-set-race-01/final.mp4")