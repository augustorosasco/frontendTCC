import cv2


def apply_low(image):
    th, low = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)  # valores testados: 85, 55 e 140
    return low


def apply_high(image):
    th, high = cv2.threshold(image, 185, 255, cv2.THRESH_BINARY)
    return high
