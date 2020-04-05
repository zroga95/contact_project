import requests
import csv
import os
import json
from io import BytesIO
#import tkFileDialog

def getText(filePathed):
    ocr_url = "https://microsoft-azure-microsoft-computer-vision-v1.p.rapidapi.com/ocr"
    with open(os.getcwd()+'/azure_key.json') as f:
        headers = json.load(f)
    params = {'language': 'unk', 'detectOrientation': 'true'}
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
    #print(word_infos);
    return word_infos;

def writeArrayCSV(arrayed, csv_pathed):
    with open(csv_pathed, "w") as contact_file:
        writer = csv.writer(contact_file, delimiter=',')
        #commented code for capturing folder
        #for files in os.listdir(path):
        #print(str(path)+'/'+str(files))
        #print(os.path.basename(files))
        #fileCard=str(path)+'/'+str(files)

        #except:
        #    print("error")# on "+ str(files))
        #else:
        writer.writerow(arrayed)
        #contact_writer = csv.writer(contact_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    contact_file.close()
    return csv_pathed
