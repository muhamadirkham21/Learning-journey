import cv2

def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)

    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)


def read_video(path):

    capture = cv2.VideoCapture(path)

    while True:
        isTRue, frame = capture.read()

        frame_resize = rescale_frame(frame)
        cv2.imshow('Video', frame_resize)

        if cv2.waitKey(20) and 0xFF==ord('d'):
            break

    capture.release()
    cv2.destroyAllWindows()


def read_image(path):
    img = cv2.imread(path)
    rescale_img = rescale_frame(img)
    cv2.imshow('image', rescale_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


