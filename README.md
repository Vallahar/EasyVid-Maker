# Easy Tool for Video Creation

## Links

https://ffmpeg.org/ffmpeg-filters.html#concat

https://kkroening.github.io/ffmpeg-python/

## Issues
Currently, to make it work, I'd have to figure out the python translation of this command:

ffmpeg -loop 1 -f image2 -r 2 -i sources/image1.png -i sources/music.mp3 -c:v libx264 -c:a copy -shortest output.mp4DDDDDD

It loops one image as long as one of the channels finishes
