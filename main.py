import os
import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

cap = cv2.VideoCapture(0)
Classifier = Classifier('Resources/Model/keras_model.h5','Resources/Model/labels.txt')

# Import all Bin images
imgBinsList = []
pathFolderBins = "Resources/Bins"
pathList = os.listdir(pathFolderBins)
print(pathList)

for path in pathList:
    bin_image = cv2.imread(os.path.join(pathFolderBins, path), cv2.IMREAD_UNCHANGED)
    bin_image_rgb = cv2.cvtColor(bin_image, cv2.COLOR_RGBA2RGB)
    imgBinsList.append(bin_image_rgb)

while True:
    _, img = cap.read()
    imgResize=cv2.resize(img,(326,205))

    imgBackground = cv2.imread('Resources/BackGround_img2.png')

    prediction = Classifier.getPrediction(img)
    classID = prediction[1]
    print(classID)
    
    bin_image = imgBinsList[classID]
    bin_image_resized = cv2.resize(bin_image, (170, 270))  # Resize bin image to match overlay region
    imgBackground[138:138 + 270,480:480 + 170] = bin_image_resized  # Overlay bin image

    imgBackground[138:138+205,65:65+326]= imgResize

    # Displays
    # cv2.imshow("Image", img)
    cv2.imshow("Output", imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

'''import os
import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

cap = cv2.VideoCapture(1)
Classifier = Classifier('Resources\Model\keras_model.h5','Resources\Model\labels.txt')

# Import all Bin images
imgBinsList = []
pathFolderBins = 'Resources\Bins'
pathList = os.listdir(pathFolderBins)

for path in pathList:
    imgBinsList.append(cv2.imread(os.path.join(pathFolderBins, path), cv2.IMREAD_UNCHANGED))

while True:
    _, img = cap.read()
    imgResize=cv2.resize(img,(325,205))

    imgBackground = cv2.imread('Resources/BackGround_img2.png')

    prediction = Classifier.getPrediction(img)
    classID = prediction[1]
    print(classID)
    bin_image = imgBinsList[classID]
    bin_image_resized = cv2.resize(bin_image, (180,300))  # Resize bin image to match overlay region
     
    #imgBackground = cvzone.overlayPNG(imgBackground,bin_image_resized, (300,400))
    cv2.imshow("OP", bin_image_resized)
    cv2.waitKey(1)
    imgBackground[138:138+205,65:65+325]= imgResize

    # Displays
    # cv2.imshow("Image", img)
    cv2.imshow("Output", imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   '''
'''
while True:
        _, img = cap.read()
        imgResize=cv2.resize(img,(325,205))

        imgBackground=cv2.imread('Resources\BackGround_img2.png')

        predection = Classifier.getPrediction(img)

        classID=predection[1]
        print(classID)
        if classID!=0:
          imgBackground = cvzone.overlayPNG(imgBackground, imgBinsList[classID], (185,288))   

        imgBackground[138:138+205,65:65+325]= imgResize


        # Displays
        cv2.imshow("Image", img)
        cv2.imshow("Output",imgBackground)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
          break
'''