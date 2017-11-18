from PIL import Image
import pytesseract
import argparse
import os
import cv2

def main():
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                    help="type of preprocessing to be done")
    args = vars(ap.parse_args())

    # load the example image and convert it to grayscale
    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the
    # image
    if args["preprocess"]=="thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # make a check to see if median blurring should be done to remove
    # noise
    elif args["preprocess"]=="blur":
        gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text = pytesseract.image_to_string(Image.open(filename), lang="jpn")
    os.remove(filename)
    print(text)

    # show the output images
    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

if __name__== "__main__":
    main()

#https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
#https://qiita.com/bohemian916/items/67f22ee7aeac103dd205