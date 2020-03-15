from contact_info_class import ContactClass
import csv
import os
import json
import sys
import re

def findPhoneNum(contact_info):
	for strs in contact_info:
		match = re.search(r'[0-9]*[.]*[0-9]{3}[.]*[0-9]{4}', strs)
		if match:
			return match.group()
		else:
			match = ""
	return match

def findEmail(contact_info):
	for strs in contact_info:
		match = re.search(r'[\w.-]+@[\w.-]+', strs)
		if match:
			return match.group()
		else:
			match = ""
	return match

text_src= r"C:\Users\Zachary_Roga\Documents\contactProject\contact_file2.csv";
contact_destin = r"C:\Users\Zachary_Roga\Documents\contactProject\contact_sample.vcf";
with open(text_src, "r") as contact_file:
	csv_reader = csv.reader(contact_file, delimiter=',');
	contact_info = []; #file structure to hold FN, LN, TELEPHONE, EMAIL;)
	for row in csv_reader:
		for i in range(1, len(row), 2):
			contact_info.append(row[i]);
print(contact_info);

MyContact = ContactClass(contact_info[0], contact_info[1], findPhoneNum(contact_info), findEmail(contact_info));

allvcf = open(contact_destin, 'w');
allvcf.write( 'BEGIN:VCARD' + "\n");
allvcf.write( 'VERSION:3.0' + "\n");
allvcf.write( 'N:' + MyContact.first + ';' + MyContact.last + "\n");
allvcf.write( 'FN:' + MyContact.last + ' ' + MyContact.first + "\n");
#allvcf.write( 'ORG:' + 'ATI' + "\n");
allvcf.write( 'TEL;CELL:' + MyContact.tele + "\n");
allvcf.write( 'EMAIL:' + MyContact.email + "\n");
allvcf.write( 'END:VCARD' + "\n");
allvcf.write( "\n");

contact_file.close();
