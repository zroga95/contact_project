from contact_info_class import ContactClass
import csv
import os
import json
import sys

text_src= "C:\Users\Zachary_Roga\Documents\contactProject\contact_file2.csv";
contact_destin = "C:\Users\Zachary_Roga\Documents\contactProject\contact_sample.vcf";
with open(text_src, "r") as contact_file:
	csv_reader = csv.reader(contact_file, delimiter=',');
	contact_info = []; #file structure to hold FN, LN, TELEPHONE, EMAIL;)
	for row in csv_reader:
		for i in range(1, len(row), 2):
			if len(contact_info) < 4:
				contact_info.append(row[i]);
print(contact_info);
MyContact = ContactClass(contact_info[0], contact_info[1], contact_info[2], contact_info[3]);
print(MyContact.last)
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