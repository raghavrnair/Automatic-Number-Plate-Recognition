import easyocr
import os
import pandas as pd
import openpyxl

## reader = easyocr.Reader(['ch_sim','en']) # Load Simplified Chinese + English model into memory
## reader = easyocr.Reader(['ch_tra','en']) # Load Traditional Chinese + English model into memory
reader = easyocr.Reader(['en']) # Load English model into memory

def run_easyocr(df, folder_path):
    num = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            ocr_result = reader.recognize(image_path) #EasyOCR recognition function
            df.loc[num]=[image_path, ocr_result] 
            num += 1
    print(df)

easychsim_df = pd.DataFrame(columns=['image_path', 'ocr_result'])
folder_path = 'C:/Users/htxqteam/Documents/lprnet_pytorch/test/SG_LP'
run_easyocr(easychsim_df, folder_path)

excel_path = 'C:/Users/htxqteam/Desktop/ANPR_Raghav_Results_EN.xlsx'
with pd.ExcelWriter(excel_path) as writer:
    writer.book = openpyxl.load_workbook(excel_path)
    easychsim_df.to_excel(writer, sheet_name='EasyOCR_SG')