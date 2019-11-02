import face_recognition 
import os
import math 

facesDirectory = "../media/images"
queryImageFile = "../media/queries/query.png" 

maxDistance = 10000
amountOfImages = 13000

# Euclidian Distance Function
def euclidianDistance(x, y):
    if len(y) == 0:
        return maxDistance
    accumulate = 0
    for i in range(len(y)):
        accumulate += (x[i] - y[i])**2
    return math.sqrt(accumulate)

def sortTuple(tup):
    tup.sort(key = lambda x: x[1])
    return tup

def knnSearch(query, data, amountOfNeighbors):
    results = []
    for index, row in enumerate(data):
        distance = euclidianDistance(query, row)
        results.append((index, distance))
    results = sortTuple(results)
    results = [i[0] for i in results]
    return results[:amountOfNeighbors]

def loadImages(): 
    imageFiles = os.listdir(facesDirectory)
    imagesVector = []
    for imageFile in imageFiles:
        if imageFile[0] != ".":
            image = face_recognition.load_image_file(facesDirectory + "/" + imageFile) 
            encoding  = face_recognition.face_encodings(image)
            if len(encoding):
                imagesVector.append(encoding[0])
            else:
                imagesVector.append([])
        if len(imagesVector) == amountOfImages:
            break
    return imagesVector

queryImage = face_recognition.load_image_file(queryImageFile)
queryEncoding = face_recognition.face_encodings(queryImage)[0]
# print(queryEncoding)

imageList = os.listdir(facesDirectory) 
cleanList = []
for image in imageList:
    if image[0] != ".": 
        cleanList.append(image)

dataImages = loadImages() 

topList = knnSearch(queryEncoding, dataImages, 5) 

for element in topList: 
    print(cleanList[element])
