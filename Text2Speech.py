#!/usr/bin python -tt
#Program to convert text to speech using Google Text to Speech

from gtts import gTTS
import os
import pdf2text_convert
def convertText2Speech(fl_name):
	rd_file=open(fl_name,'r')
	data=rd_file.read()
	tts=gTTS(text=data, lang='en')
	tts.save(fl_name + ".mp3")
	os.system("mpg321 "+fl_name+ ".mp3")
def main():
	#Getting file name from user
	file_name=raw_input("Enter the file name: ")
	split_flname=file_name.split(".")[1]
	#check if it is text file or pdf file
	if split_flname == "txt":
		convertText2Speech(file_name)
	elif split_flname == "pdf":
		pdf_flname = pdf2text_convert.getPDFContent(file_name)
		convertText2Speech(pdf_flname)
	else:
		print("Please enter valid file")
if __name__ == '__main__':
	main()
