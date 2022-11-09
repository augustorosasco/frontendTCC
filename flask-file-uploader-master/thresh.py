import cv2


def apply_low(image):
    th, low = cv2.threshold(image, 38, 255, cv2.THRESH_BINARY)
    return low


def apply_high(image):
    th, high = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY)
    return high
