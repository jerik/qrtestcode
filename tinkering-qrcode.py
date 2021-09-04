#!/usr/bin/env python3
# see: https://stackoverflow.com/a/16069857/1933185
import logging, sys, pdb
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
import cv2
import fitz


def hey(ho):
    logging.debug(ho)  # logging disabled


def show(pattern):
    print(f'Now I show you my: {pattern}')


def readqr(filename='test-qrcode.png'):
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, vertices_array, ninary_qrcode = detector.detectAndDecode(image)
    if vertices_array is not None:
        hey('QRCode data: %s' % data)
    else:
        hey('There is an error somewhere')


# https://stackoverflow.com/a/47877930/1933185
def extract_images(arr_images, filename='Dokument1.pdf'):
    #hey('here i am extracting %s' % filename)
    doc = fitz.open(filename)
    for i in range(len(doc)):
        for img in doc.getPageImageList(i):
            xref = img[0]
            #hey("i: %s, xref %s" % (i, xref))
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:  # thi sis GRAY orRGB
                pix.writePNG("p%s-%s.png" % (i, xref))
            else:
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG("p%s-%s.png" % (i, xref))
                pix1 = None
            arr_images.append("p%s-%s.png" % (i, xref))
            pix = None


if __name__ == '__main__':
    hey('*'*20)
    # readqr()
    pngs = []
    extract_images(pngs, 'Dokument1.pdf')
    readqr(pngs[0])
    hey("It's working :)")
