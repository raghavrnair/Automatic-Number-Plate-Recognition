# Automatic-Number-Plate-Recognition

This is an Automatic Number Plate Recognition Project

Project 1: lprnet_pytorch - Chinese City Parking Dataset

    1. Run MTCNN.py 
        Above script will draw images from a source folder, perform license plate detection, construct a bounding box, crop out the bounding box, and store the resulting cropped images in a destination folder

    2. Run LPRNet_Test.py
        Above script will draw cropped license plate images from source folder, perform OCR on them, print out license plate numbers + processing time in text, and store these values in a Microsoft Excel document

    - Remember to update all the folder or file paths
    - Use chatgpt to understand how individual functions work

Project 2: EasyOCR, PaddleOCR_V3, PaddleOCR_RFL, Pytesseract - Any dataset

    1. Run detect.py in yolov7 folder
        Above script will conduct object detection from a source folder or file, video or image, draw bounding boxes and store output files in a destination folder.

        Use the correct command line arguments by following YOLOV7 repository. You can modify the "detect()" function to suit your use case.

        Use "carplate.pt" as your weights file for license plate detection

        Yolov7 has a different set of dependencies compared to the rest of the project so I ran it using Docker to containerize it. Follow the guidance given on YOLOV7 repository

    2. Run OCR model
        Call the API from respective online respositories. Most of them can be found in this repository or the vehicle tracker folder.

Important Resources: 
- Yolov7: https://github.com/WongKinYiu/yolov7
- lprnet_pytorch: https://github.com/sirius-ai/LPRNet_Pytorch
- PaddleOCR: https://github.com/PaddlePaddle/PaddleOCR
- EasyOCR: https://github.com/JaidedAI/EasyOCR