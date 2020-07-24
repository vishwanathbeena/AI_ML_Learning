import cv2
def load_image(path):
    image = cv2.imread(path)
    orig = image.copy()
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return orig , image

def resize_image(image,width=320,height=320):
    (origH, origW) = image.shape[:2]
    (newW,newH) = (width,height)
    rW = origW/float(newW)
    rH = origH / float(newH)
    resized_image =  cv2.resize(image,(newW,newH))
    return resized_image,rW,rH


