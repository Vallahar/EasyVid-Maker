import ffmpeg

input_still = ffmpeg.input("sources/image1.png")
input_audio = ffmpeg.input("sources/music.mp3")

(
    ffmpeg
    .concat(input_still, input_audio, v=1, a=1)
    .output("output/video.mp4")
    .run(overwrite_output=True)
)
