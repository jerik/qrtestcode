#!/usr/bin/env python3
# see: https://stackoverflow.com/a/16069857/1933185
import logging, sys, pdb
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
import cv2
import sys


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


def extract_images(filename='Dokument1.pdf'):
    hey('here i am extracting')
    with open(filename, 'rb') as file
    file.seek(0)
    pdf = file.read()


if __name__ == '__main__':
    hey('*'*20)
    # readqr()
    extract_images('foo')
