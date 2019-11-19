import cv2


def run_openCV(image):
    button_name = "Save"
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.namedWindow('image')

    def nothing(x):
        pass

    # create trackbars for change
    cv2.createTrackbar('threshold1', 'image', 0, 255, nothing)
    cv2.createTrackbar('threshold2', 'image', 0, 255, nothing)
    # cv2.createButton(button_name, )
    while True:
        threshold1 = cv2.getTrackbarPos('threshold1', 'image')
        threshold2 = cv2.getTrackbarPos('threshold2', 'image')

        edges = cv2.Canny(img, threshold1, threshold2)

        cv2.imshow('image', edges)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        else:
            pass

    cv2.destroyAllWindows()