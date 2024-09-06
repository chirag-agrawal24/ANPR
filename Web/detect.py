from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np
from datetime import datetime
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch
# import torch_directml
import os

model=YOLO("../model/number_plate_detect/best.pt")

def get_plate(image,fname):
    
    result=model.predict(image,show_boxes=True,save=False,conf=0.25)[0]
    rs=[]
    files=[]
    
    for box in result.boxes:
        left, top, right, bottom = np.array(box.xyxy.cpu(), dtype=np.int32).squeeze()
        region=result.orig_img[top: bottom,left:right]
        now=datetime.now()
        filename="static/predict/"+fname
        # filename="predict/"+fname+str(now.strftime("%Y%m%d%H%M%S"))+"_"+str(len(rs))+".png"
        # print(filename)
        cv2.imwrite(filename,region)

        files.append(filename)
        rs.append(region)

    return rs,files

ocr_model =  VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-small-printed")

processor = TrOCRProcessor.from_pretrained("microsoft/trocr-small-printed")


def extract_text(img):

    
    image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    
    pixel_values = processor(image, return_tensors="pt").pixel_values

    if torch.cuda.is_available():#NVIDIA GPU
        device = torch.device("cuda:0")
    # elif torch_directml.device():#FOR AMD GPU
    #     device=torch_directml.device()
    else:#FOR CPU
        device=torch.device("cpu")
    
        
    pixel_values = pixel_values.to(device)
    ocr_model.to(device)
    
    generated_ids = ocr_model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
    number_plate=""
    for ch in generated_text:
        if ch.isalnum():
            number_plate+=ch
    # print(number_plate)
    return number_plate

def save_text(filename, text):
    name, ext = os.path.splitext(filename)
    with open('{}.txt'.format(name), mode='w') as f:
        f.write(text)
    f.close()

def OCR(filepath,filename):
    results,files=get_plate(filepath,filename)
    text=""
    for result, file in zip(results,files):
        text=extract_text(result)
        save_text(file,text)
    if text=="":
        return (None,text)
    return file,text