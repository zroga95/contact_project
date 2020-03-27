from microsoftContactConverter import *
from createVcfFile import createVCF
import os

base_path = os.getcwd();
file_card = base_path + r"\business_cards"+ r"\business_card6.jpg"
use_azure=input("Azure set up? Y/N")
if use_azure == "Y":
	card_text = getText(file_card)
	writeArrayCSV(card_text, r"C:\Users\Zachary_Roga\Documents\contactProject\contact_file2.csv")
source_file= input('enter a file name in current directory')
createVCF(base_path + source_file)
# fix and incorporate email function