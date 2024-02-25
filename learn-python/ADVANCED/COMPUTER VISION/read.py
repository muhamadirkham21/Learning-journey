import cv2

def read_image(path):
    img = cv2.imread(path)
    cv2.imshow('image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def read_video(path):

    capture = cv2.VideoCapture(path)

    while True:
        isTRue, frame = capture.read()
        cv2.imshow('Video', frame)

        if cv2.waitKey(20) and 0xFF==ord('d'):
            break

    capture.release()
    cv2.destroyAllWindows()

def read_stabil_video(path):

    capture = cv2.VideoCapture(path)

    if not capture.isOpened():
        print("Error: Could not open video file.")
        exit()
    
    while True:
        ret, frame = capture.read()

        if not ret:
            print("End of video")
            break

        cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break


    capture.release()
    cv2.destroyAllWindows()


read_image('images/cat_2.jpg')