# Download Video Stream

This script downloads streaming video data to your local. Works in very specific cases.
`download_video_parts()` downloads parts of the video to a temp folder.
`stitch_videos()` puts it all together

## Note
stitch_videos() is currently super memory ineffient as it adds all the parts to memoery before trying to stitch it together. Using FFMPEG directly will probably be better, but I didn't want to install it when I wrote this up, it's just a quick and dirty solution.
I may improve it in the future. I currently don't need it so I'll leave it as it is.