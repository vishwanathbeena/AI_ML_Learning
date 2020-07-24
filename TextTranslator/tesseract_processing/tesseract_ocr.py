import pytesseract
def extract_text_from_image(roilist):
    # in order to apply Tesseract v4 to OCR text we must supply
    # (1) a language, (2) an OEM flag of 4, indicating that the we
    # wish to use the LSTM neural net model for OCR, and finally
    # (3) an OEM value, in this case, 7 which implies that we are
    # treating the ROI as a single line of text
    results = []
    config = ("-l tel --oem 1 --psm 7")
    for roi in roilist:
        text = pytesseract.image_to_string(roi, config=config)
    # add the bounding box coordinates and OCR'd text to the list
    # of results
        results.append(text)
    return text

def core_tesseract_OCR(image):
    config = ("-l tel --oem 1 --psm 7")
    return pytesseract.image_to_string(image, config=config)
