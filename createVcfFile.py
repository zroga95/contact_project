from contact_info_class import ContactClass
import csv
import os
import json
import sys
import re
#names lists retreived from https://github.com/smashew/NameDatabases
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


def findFirstLast(contact_info):
	first_name_database=curr_dir + r"\first_names.txt"
	last_name_database=curr_dir + r"\last_names.txt"
	possible_options = []
	first, last  = "", ""
	for strs in contact_info:
		match = re.search(r'[a-zA-Z]{3}[a-zA-Z]*', strs)
		if match:
			possible_options.append(match.group())
	for line in open(first_name_database, "r"):	
		if line.strip() in possible_options:
			first=line
	for line in open(last_name_database, "r"):	
		if line.strip() in possible_options:
			last=line
	return first, last


def createVCF(text_src):
	global curr_dir
	curr_dir = os.getcwd()
	if text_src == curr_dir:
		text_src= curr_dir+r"\contact_file2.csv"

	contact_destin = curr_dir+ r"\contact_sample.vcf"
	with open(text_src, "r") as contact_file:
		csv_reader = csv.reader(contact_file, delimiter=',')
		contact_info = []; #file structure to hold FN, LN, TELEPHONE, EMAIL;)
		for row in csv_reader:
			for i in range(1, len(row), 2):
				contact_info.append(row[i])
	first_name, last_name = findFirstLast(contact_info)
	MyContact = ContactClass(first_name, last_name, findPhoneNum(contact_info), findEmail(contact_info)) #first, last, phone, email

	allvcf = open(contact_destin, 'w')
	allvcf.write( 'BEGIN:VCARD' + "\n")
	allvcf.write( 'VERSION:3.0' + "\n")
	allvcf.write( 'N:' + MyContact.first + ';' + MyContact.last + "\n")
	allvcf.write( 'FN:' + MyContact.last + '  ' + MyContact.first + "\n")
	#allvcf.write( 'ORG:' + 'ATI' + "\n")
	allvcf.write( 'TEL;CELL:' + MyContact.tele + "\n")
	allvcf.write( 'EMAIL:' + MyContact.email + "\n")
	allvcf.write( 'END:VCARD' + "\n")
	allvcf.write( "\n")

	contact_file.close()
