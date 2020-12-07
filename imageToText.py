from PIL import Image
import PIL.Image
import cv2
import datetime
from os import listdir,makedirs
from os.path import isfile, join

from pytesseract import image_to_string
import pytesseract

#path to ocr
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
TESSDATA_PREFIX = 'C:\\Program Files (x86)\\Tesseract-OCR\\tessdata\\'


pather = input("ENTER The path to your screenshots to be cropped:")

#replace the single slashes with double

pather = pather.replace("\\","\\\\")
pather = pather+"\\\\"

print("path saved")

#output folder
outputPath = "CroppedOutput"

#put all the list of files in a list , using  a list comprehension
allFiles = [f for f in listdir(pather) if isfile(join(pather, f))]
img={}


for theImages in allFiles:
    #rename the images  prefix with c
    filenamer=outputPath+"\\c"+theImages
    theImages = pather+theImages
    print(theImages)
    print("")
    img = cv2.imread(theImages)
    #print(img.shape)
    #optimum crop_img = img[356:1040, 0:1810]
    crop_img = img[356:1040, 0:1810]
    #cv2.imshow("cropped", crop_img)
    #filenamer = "c"+crop_img
    cv2.imwrite(filenamer,crop_img)
    output = pytesseract.image_to_string(PIL.Image.open(filenamer).convert("RGB"), lang='eng')

    #write to file by appended
    with open("extracted"+datetime.datetime.today().strftime('%Y-%m-%d-%H')+".txt","a") as fopener:
        fopener.write("\n")
        fopener.write(filenamer) #the filename
        fopener.write("\n")
        fopener.write(output)
        fopener.close()

    #cv2.waitKey(0)
print("successfully cropped")
