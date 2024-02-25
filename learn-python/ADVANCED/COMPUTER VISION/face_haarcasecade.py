import cv2 as cv

img = cv.imread('/home/irkham/Learning-journey/learn-python/ADVANCED/COMPUTER VISION/images/JokoW.jpg')
rescale = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)

cv.imshow('image', rescale)

gray = cv.cvtColor(rescale, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_casecade = cv.CascadeClassifier('/home/irkham/Learning-journey/learn-python/ADVANCED/COMPUTER VISION/haarcascade_face.xml')

faces_rect = haar_casecade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

print(f'number of faces : {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(rescale, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('result', rescale)

cv.waitKey(0)
cv.destroyAllWindows()