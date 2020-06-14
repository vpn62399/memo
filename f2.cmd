echo off
echo rem FFmpeg > filelist.cmd
md H264_qsv
for %%a in (*.mp4) do echo ffmpeg -i %%a -r 29.97 -c:v h264_qsv -b:v 12M .\H264_qsv\%%a >> filelist.cmd
for %%a in (*.MTS) do echo ffmpeg -i %%a -r 29.97 -c:v h264_qsv -b:v 12M -vf bwdif .\H264_qsv\%%a.mp4 >> filelist.cmd
for %%a in (*.avi) do echo ffmpeg -i %%a -r 29.97 -c:v h264_qsv -b:v 9M -vf bwdif .\H264_qsv\%%a.mp4 >> filelist.cmd

rem md H264
rem for %%a in (*.mp4) do echo ffmpeg -i %%a -r 29.97 -c:v libx264 -crf 23 .\H264\%%a >> filelist.cmd
rem for %%a in (*.MTS) do echo ffmpeg -i %%a -r 29.97 -c:v libx264 -crf 23 -vf bwdif .\H264\%%a.mp4 >> filelist.cmd

rem md MP3
rem for %%a in (*.mp4) do echo ffmpeg -i %%a .\MP3\%%a.mp3 >> filelist.cmd

rem filelist
rem for %%a in (*.mp4) do echo file %%a >> filelist.txt
rem for %%a in (*.MTS) do echo file %%a >> filelist.txt
rem ffmpeg -f concat -i filelist.txt -c copy output.mp4

echo shutdown /s /t 300 >> filelist.cmd
echo pause >> filelist.cmd
echo shutdown /a >> filelist.cmd
echo pause >> filelist.cmd
rem pause


rem sample
rem for %%a in (*.avi) do echo "ffmpeg -i %%a -vf vidstabdetect -an -f null - && ffmpeg -i %%a -vf vidstabtransform -r 29.97 -c:v h264_qsv -b:v 9M -vf bwdif .\H264_qsv\%%a.mp4" >> filelist.cmd
rem for %%a in (*.avi) do echo ffmpeg -i %%a -r 29.97 -c:v h264_qsv -b:v 9M -vf bwdif -movflags +faststart .\H264_qsv\%%a.mp4 >> filelist.cmd
