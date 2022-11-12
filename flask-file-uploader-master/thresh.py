import cv2


def apply_low_thresh_for_perpendicular(image):
    th, low = cv2.threshold(image, 38, 255, cv2.THRESH_BINARY)
    return low


def apply_high_thresh_for_perpendicular(image):
    th, high = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY)
    return high


def apply_low_for_diagonals(image):
    th, low = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)
    return low


def apply_high_for_diagonals(image):
    th, high = cv2.threshold(image, 185, 255, cv2.THRESH_BINARY)
    return high
