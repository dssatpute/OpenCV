import cv2
import pytesseract
import io
import json
import requests
#Read the Image
img=cv2.imread('txt.png')

#h,w,_=img.shape                #defining the hieght and wieght of image
#roi = img[0: h, 400: w]        #croping the image to desired region of interest

url_api = "https://api.ocr.space/parse/image" #URL for appending API
_,compressed=cv2.imencode('.jpg',img,[1,90]) #encoding image to .jpg to reduce size
file_bytes = io.BytesIO(compressed)          #convert into bytes to send on server

result = requests.post(url_api,
              files = {"txt.jpg": file_bytes},
              data = {"apikey":'YOURAPIKEY',
                      "language": "eng"})

result = result.content.decode()
result = json.loads(result)
parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)
