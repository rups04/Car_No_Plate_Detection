import boto3
client = boto3.client('textract')
img_path = "./images/6.jpeg"

with open(img_path, 'rb') as raw_image:
    _temp_image = raw_image.read()
    bytes_image = bytearray(_temp_image)
    
#call texttract client
response = client.detect_document_text(Document={'Bytes': bytes_image})

blocks = response["Blocks"]

from collections import Counter
block_counts = Counter(x["BlockType"] for x in blocks)

all_lines = [l for l in blocks if l["BlockType"] == "LINE"]
def Plate_no():
    for l in all_lines:
        return(l["Text"])

PlateNo = Plate_no()

import requests
import json
import xmltodict
import os

username = "Himadri"
RegistrationNumber = PlateNo

url = "http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber=" + RegistrationNumber + "&username="+username 

url=url.replace(" ","%20")
r = requests.get(url)
n = xmltodict.parse(r.content)
k = json.dumps(n)
df = json.loads(k)
l=df["Vehicle"]["vehicleJson"]
p=json.loads(l)


s="Your car's details are:\n"+"Description: "+ str(p['Description'])+"\n"+"Car Company: "+str(p['CarMake']['CurrentTextValue'])+"\n"+"Car Model: "+str(p['CarModel']['CurrentTextValue'])+"\n"+"Fuel Type: "+str(p['FuelType']['CurrentTextValue'])+"\n"+"Registration Year: "+str(p['RegistrationYear'])+"\n"+"EngineSize: "+str(p['EngineSize']['CurrentTextValue'])+"\n"+"Vehicle ID: "+str(p['VechileIdentificationNumber'])+"\n"+"NumberOfSeats: "+str(p['NumberOfSeats']['CurrentTextValue'])+"\n"+"Engine No.: "+str(p['EngineNumber'])+"\n"+"Location RTO: "+str(p['Location'])
print(s)

lst = s.split('\n')

file = open('output.txt','w')
file.write('\n'.join(lst))
file.close()

