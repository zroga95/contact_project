from microsoftContactConverter import *
from createVcfFile import createVCF
from email_contact_file import *
import os

base_path = os.getcwd();

file_card = base_path + r"\business_cards"+ r"\business_card6.jpg"
use_azure=input("Azure set up? Y/N")
if use_azure == "Y":
	card_text = getText(file_card)
	writeArrayCSV(card_text, base_path+"\contact_file2.csv")
	source_file = "\contact_file2.csv"
else:
	source_file= input('enter a file name in current directory (blank for sample data)')
contact_file = createVCF(base_path + source_file)
sendAttachedEmail("zroga95@gmail.com", contact_file)
# fix and incorporate email function