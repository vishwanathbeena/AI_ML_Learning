import cv2
import numpy as np
import pytesseract
from constants import constants
from imutils.object_detection import non_max_suppression
from ocr_processing import decode_prediciton as dp
def east_text_detector(image,**kwargs):
    # define the two output layer names for the EAST detector model that
    # we are interested in -- the first is the output probabilities and the
    # second can be used to derive the bounding box coordinates of text
    (H,W) = image.shape[:2]
    layerNames = [
        "feature_fusion/Conv_7/Sigmoid",
        "feature_fusion/concat_3"]
    # load the pre-trained EAST text detector
    print("[INFO] loading EAST text detector...")
    net = cv2.dnn.readNet(constants.east_path)
    # construct a blob from the image and then perform a forward pass of
    # the model to obtain the two output layer sets
    blob = cv2.dnn.blobFromImage(image, 1.0, (W, H),(123.68, 116.78, 103.94), swapRB=True, crop=False)
    net.setInput(blob)
    (scores, geometry) = net.forward(layerNames)
    (rects, confidences) = dp.decode_predictions(scores, geometry,**kwargs)
    #converting confidences to float as NMSBoxes does not accept numpy.float32
    # confidences_list = [float(v) for v in confidences]
    # print(type(confidences_list[0]))
    boxes = non_max_suppression(np.array(rects), probs=confidences)
    # boxes = cv2.dnn.NMSBoxes(rects, confidences_list, kwargs['min_confidence'], 0.4)
    # print('type of boxes')
    # print(type(boxes))
    # print('boxes are')
    # print(boxes)
    return boxes

def get_text_bounding_boxes_on_image(orig,boxes,rW,rH,**kwargs):
    # initialize the list of result
    # loop over the bounding boxes
    (origH, origW) = orig.shape[:2]
    output = orig.copy()
    print('Original image size is' ,(origH, origW))
    results = []
    for (startX, startY, endX, endY) in boxes:
        # scale the bounding box coordinates based on the respective
        # ratios
        startX = int(startX * rW)
        startY = int(startY * rH)
        endX = int(endX * rW)
        endY = int(endY * rH)
        # in order to obtain a better OCR of the text we can potentially
        # apply a bit of padding surrounding the bounding box -- here we
        # are computing the deltas in both the x and y directions
        dX = int((endX - startX) * kwargs['padding'])
        dY = int((endY - startY) * kwargs['padding'])
        # apply padding to each side of the bounding box, respectively
        startX = max(0, startX - dX)
        startY = max(0, startY - dY)
        endX = min(origW, endX + (dX * 2))
        endY = min(origH, endY + (dY * 2))
        # extract the actual padded ROI
        roi = orig[startY:endY, startX:endX]

        # in order to apply Tesseract v4 to OCR text we must supply
        # (1) a language, (2) an OEM flag of 4, indicating that the we
        # wish to use the LSTM neural net model for OCR, and finally
        # (3) an OEM value, in this case, 7 which implies that we are
        # treating the ROI as a single line of text
        config = ("-l tel --oem 1 --psm 3")
        text = pytesseract.image_to_string(roi, config=config)
        # add the bounding box coordinates and OCR'd text to the list
        # of results
        results.append(((startX, startY, endX, endY), text))
        #results.append(roi)
        # sort the results bounding box coordinates from top to bottom
        results = sorted(results, key=lambda r: r[0][1])
        # loop over the results
        for ((startX, startY, endX, endY), text) in results:
            # display the text OCR'd by Tesseract
            print("OCR TEXT")
            print("========")
            print('type of string {}'.format(type(text)))
            print("{}\n".format(text))
            # strip out non-ASCII text so we can draw the text on the image
            # using OpenCV, then draw the text and a bounding box surrounding
            # the text region of the input image
            text = "".join([c if ord(c) < 128 else "" for c in text]).strip()

            cv2.rectangle(output, (startX, startY), (endX, endY),
                          (0, 0, 255), 1)
            cv2.putText(output, text, (startX, startY - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
            # show the output image
    cv2.imshow("Text Detection", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #return results
