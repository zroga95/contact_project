import requests
import csv
import os
import json
from io import BytesIO
import tkFileDialog
from Tkinter import *

ocr_url = "https://microsoft-azure-microsoft-computer-vision-v1.p.rapidapi.com/ocr"

path = os.getcwd() + "/business_cards";
with open(os.getcwd()+'/azure_key.json') as f:
        headers = json.load(f)

params = {'language': 'unk', 'detectOrientation': 'true'}

def getText(filePathed):
    payload= open(filePathed, mode="rb").read()
    response = requests.post(ocr_url, headers=headers, params=params, data=payload)
    #response.raise_for_status()
    analysis = response.json()
    # Extract the word bounding boxes and text.
    line_infos = [region["lines"] for region in analysis["regions"]]
    word_infos = []
    word_infos.append(filePathed)
    for line in line_infos:
        for word_metadata in line:
            for word_info in word_metadata["words"]:
                word_infos.append(word_info['text'].encode('utf-8'))
                word_infos.append(word_info['boundingBox'])
    print word_infos
    return word_infos

with open("C:\Users\Zachary_Roga\Documents\contactProject\contact_file2.csv", "w") as contact_file:
    writer = csv.writer(contact_file, delimiter=',')
    #commented code for capturing folder
    #for files in os.listdir(path):
    #print(str(path)+'/'+str(files))
    #print(os.path.basename(files))
    #fileCard=str(path)+'/'+str(files)
    fileCard = ""
    while (len(fileCard) < 1):
        fileCard= tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")));
    
    #try:
    cardText = getText(fileCard)
    #except:
    #    print("error")# on "+ str(files))
    #else:
    writer.writerow(cardText)
    #contact_writer = csv.writer(contact_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
contact_file.close()