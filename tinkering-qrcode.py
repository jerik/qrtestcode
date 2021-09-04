#!/usr/bin/env python3
# see: https://stackoverflow.com/a/16069857/1933185
import logging, sys, pdb
logfile = sys.argv[0].replace('.py', '.log')
logging.basicConfig(filename=logfile, level=logging.DEBUG)
import cv2


def hey(ho):
    logging.debug(ho)  # logging disabled


def show(pattern):
    print(f'Now I show you my: {pattern}')


if __name__ == '__main__':
    hey('*'*20)
    filename = 'test-qrcode.png'
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, vertices_array, ninary_qrcode = detector.detectAndDecode(image)
    if vertices_array is not None:
        print('QRCode data:', data)
    else:
        print('There is an error somewhere')
