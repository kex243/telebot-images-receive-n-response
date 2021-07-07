import telebot 
import os
import time
import subprocess
import glob
from PIL import Image


bot = telebot.TeleBot('1159217083:AAGlcHlLvO-GMa_9aRJ7z9GnqdD401mn7mw')
#@bot.message_handler(commands=['do'])
@bot.message_handler(content_types=["photo"])
def handle_docs_document(message):
	chatID = message.chat.id
	time.sleep(0)
	file_info = bot.get_file(message.photo[-1].file_id)
	time.sleep(0)
	downloaded_file = bot.download_file(file_info.file_path)
	time.sleep(0)
	src = './datasets/cityscapes//test_A//'  + message.photo[-1].file_id + '.jpg'
	src2 = './datasets/cityscapes//test_A//'  + message.photo[-1].file_id + '2'+'.jpg'
	src3 = './datasets/cityscapes//test_A//'  + message.photo[-1].file_id + '3'+'.jpg'
	src4 = './datasets/cityscapes//test_A//'  + message.photo[-1].file_id + '4'+'.jpg'
	src5 = './datasets/cityscapes//test_A//'  + message.photo[-1].file_id + '5'+'.jpg'
	
	time.sleep(0)
	with open(src, 'wb') as new_file:
		new_file.write(downloaded_file)
	im = Image.open(r'./datasets/cityscapes//test_A//'  + message.photo[-1].file_id + '.jpg')
	width, height = im.size
	im.crop((int(round(width-width*0.95)), max(0, int(round(height/2-512))), int(round(width*0.95)), min(height, int(round(height/2+512)) ) )).save(src2)
	im.crop((int(round(width-width*0.90)), max(0, int(round(height/2-512))), int(round(width*0.90)), min(height, int(round(height/2+512)) ) )).save(src3)
	im.crop((int(round(width-width*0.85)), max(0, int(round(height/2-512))), int(round(width*0.85)), min(height, int(round(height/2+512)) ) )).save(src4)
	im.crop((int(round(width-width*0.80)), max(0, int(round(height/2-512))), int(round(width*0.80)), min(height, int(round(height/2+512)) ) )).save(src5)

	try:
		bot.reply_to(message, "Model is almost finished. Image processing on the way.")
	except telebot.apihelper.ApiException:
		print (403)
	time.sleep(0)

	os.system('python test.py')

	time.sleep(0)
	try:
		imgout = './results/assmore/test_latest/images/' + message.photo[-1].file_id + 'synthesized_image.png'
		img = open('./results/assmore/test_latest/images/' + message.photo[-1].file_id + 'synthesized_image.png', 'rb')
		img2 = open('./results/assmore/test_latest/images/' + message.photo[-1].file_id +'2'+ 'synthesized_image.png', 'rb')
		img3 = open('./results/assmore/test_latest/images/' + message.photo[-1].file_id +'3'+ 'synthesized_image.png', 'rb')
		img4 = open('./results/assmore/test_latest/images/' + message.photo[-1].file_id +'4'+ 'synthesized_image.png', 'rb')
		img5 = open('./results/assmore/test_latest/images/' + message.photo[-1].file_id +'5'+ 'synthesized_image.png', 'rb')
		time.sleep(0)
		imgin ='./results/assmore/test_latest/images/' + message.photo[-1].file_id + 'input_label.jpg'
		time.sleep(0)
	except OSError as e:
		print ("oversize")
		bot.send_message(chatID, "Some images are too high to process. Decrease aspect ratio of your image.")
	eval = ["magick", imgout, "label:telegram: anime2hentaibot","-append", imgout]
	subprocess.call(eval, shell=True)
	try:
		bot.send_photo(chatID, img)
		bot.send_photo(chatID, img2)
		bot.send_photo(chatID, img3)
		bot.send_photo(chatID, img4)
		bot.send_photo(chatID, img5)
	except UnboundLocalError:
		print ('4032 error')
	print(chatID)
	time.sleep(1)
	try:
		os.remove(src)
		os.remove(src2)
		os.remove(src3)
		os.remove(src4)
		os.remove(src5)
	except OSError as e:
		print ("no images to remove")
	files = glob.glob('/datasets/cityscapes/test_A/*')
	for f in files:
		os.remove(f)
@bot.message_handler(commands=['start', 'help'])
def handle_docs_document2(message):
	chatID = message.chat.id
	instruction1 = open('./help/1(1).png', 'rb')
	instruction2 = open('./help/1(2).png', 'rb')
	instruction3 = open('./help/1(3).png', 'rb')
	instruction4 = open('./help/1(4).png', 'rb')
	instruction5 = open('./help/1(5).png', 'rb')
	instruction6 = open('./help/1(6).png', 'rb')
	instruction7 = open('./help/1(7).png', 'rb')
	instruction8 = open('./help/1(8).png', 'rb')
	try:
		bot.send_photo(chatID, instruction1)
		bot.send_photo(chatID, instruction2)
		bot.send_photo(chatID, instruction3)
		bot.send_photo(chatID, instruction4)
		bot.send_photo(chatID, instruction5)
		bot.send_photo(chatID, instruction6)
		bot.send_photo(chatID, instruction7)
		bot.send_photo(chatID, instruction8)
		
		bot.send_message(chatID, "Send image according to this instruction. Best result achived with white background, use remove.bg to prepare image. Transparent background will be transformed to white by Telegram. 'Compress image' must be checked.")
		bot.send_message(chatID, "Images need to be prepared with mapping of сlavicle (HTML code 800000), nippels and halos (0000ff and 00ffff), navel (ff00ff), pussy (00ff00).")
		bot.send_message(chatID, "It is not necessary to map visible organs.")

		bot.send_message(chatID, "Optimal body width is 1/2-3/4 of image size centered, so crop your image accordingly. Height is limited by memory capacity with 1400 px. Height below will not be processed. It can include legs or exlude head.")
		bot.send_message(chatID, "Images will be resized to 512 px width, so work area for body is 256-384 px. (Thats where 1/2-3/4 of image comes from.) Image is resized automatically.")
		bot.send_message(chatID, "Output is a serie of images scaled from original to smaller size with 10% width step. Figure out what size of image will be better youself. Best aspect ratio is 1/2 for body with head included.")
		bot.send_message(chatID, "Not all examples will work properly. The more dress is on the image the worse result will be.")
		bot.send_message(chatID, "Network has some issues with dark skin color.")
		
	except telebot.apihelper.ApiException:
		print (4033)
bot.polling(interval=0)
bot.infinity_polling(none_stop=True)
		#os.remove(imgout)
		#os.remove(imgin)