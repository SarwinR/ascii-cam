import cv2

#density = ['Ñ','@','#','W','$','9','8','7','6','5','4','3','2','1','0','?','!','a','b','c',';',':','+','=','-',',','.','_']
density = ['Ñ','@','#','0','?','!','c',';',':','+','=','-',',','.','_']
imagePath = "code\images\image_1.jpg"
scaleFactor = 20

inputImage = cv2.imread(imagePath)

h = inputImage.shape[0]
w = inputImage.shape[1]
newImageSize = (int(w/scaleFactor), int(h/scaleFactor))
resizedImage = cv2.resize(inputImage, newImageSize, interpolation = cv2.INTER_AREA)

greyImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)

outputString = "\n"
for y in range(0, newImageSize[1]):
    for x in range(0, newImageSize[0]):
        brightness = greyImage[y, x]
        index = int((brightness/255) * len(density)) - 1

        outputString += density[index] + ' '

    outputString += "\n"

cv2.imshow('Black white image', greyImage)
print(outputString)

cv2.waitKey(0)
cv2.destroyAllWindows()
