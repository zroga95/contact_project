from microsoftContactConverter import *
from createVcfFile import createVCF
from email_contact_file import *
import os

base_path = os.getcwd();
image_file = input('enter a image file name in current directory (blank for sample data)')
if image_file == "":
	image_file = r"\business_cards"+ r"\business_card6.jpg"
file_card = base_path + image_file
use_azure=input("Azure set up? Y/N")
if use_azure == "Y":
	card_text = getText(file_card)
	source_file = writeArrayCSV(card_text, base_path+"\contact_file2.csv")
else:
	source_file= base_path + input('enter a file name in current directory (blank for sample data)')
contact_file = createVCF(source_file)
sendAttachedEmail("zroga95@gmail.com", contact_file)
# fix and incorporate email function