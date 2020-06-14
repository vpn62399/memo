@ECHO OFF
title %1 to MP4
ffmpeg -i %1 -r 29.97 -c:v h264_qsv -b:v 9M -vf bwdif %~n1_temp.mp4
title %1 to STB MP4
ffmpeg -i %~n1_temp.mp4 -vf vidstabdetect -an -f null - && ffmpeg -i %~n1_temp.mp4 -vf vidstabtransform -c:v h264_qsv -b:v 9M  %~n1_STB.mp4

rem ffmpeg -i %1 -vf vidstabdetect -an -f null - && ffmpeg -i %1 -vf vidstabtransform -c:v h264_qsv -c:a copy -b:v 9M  %~n1_STB.mp4
rem ffmpeg -i %1 -vf vidstabdetect -an -f null - && ffmpeg -i %1 -vf vidstabtransform,unsharp=5:5:0.8:3:3:0.4 -c:v h264_qsv -c:a copy -b:v 9M  %~n1_STB.mp4
rem ffmpeg -i %1 -vf vidstabtransform -c:v h264_qsv -b:v 9M  %~n1_STB.mp4

set SDL_AUDIODRIVER=directsound
start ffplay -x 640 -y 480 -volume 100 %~n1_STB.mp4

shutdown /s /t 600 
pause
shutdown /a 
pause 

:EXIT

rem https://ffmpeg.org/ffmpeg-filters.html#vidstabdetect-1
rem https://looooooooop.blog.fc2.com/blog-entry-1108.html
rem https://looooooooop.blog.fc2.com/blog-entry-1021.html

rem ffmpeg -i inp.mpeg -vf vidstabdetect -an -f null
rem ffmpeg -i inp.mpeg -vf vidstabtransform,unsharp=5:5:0.8:3:3:0.4 inp_stabilized.mpeg