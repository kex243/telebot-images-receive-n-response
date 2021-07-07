# telebot-images-recive-n-response
I use this code for my pix2pixHD implementation working in 'test' mode in Telegram. It recives images from user, puts it into work with imagemagick7 and pix2pixHD and provides output back. It has some protection for extreme cases where images are to be processed. It has some strings to be rewieved and optimised but concept is clear.
req:
telebot (python-telegram-bot from conda)
pytelegrambotapi
additional packages for image processing for my purposes:
os, time, subprocess, glob for file processing and timing for processing (atualy not needed but whatever)
