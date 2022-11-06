import cv2


def apply_low(image, isInverted):
    th, low = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)  # valores testados: 85, 55 e 140
    return low


def mid(image_path):
    mid_thresh = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    th, mid = cv2.threshold(mid_thresh, 85, 255, cv2.THRESH_BINARY)
    if 'inverted' in image_path:
        path_to_mid_thresh = 'resources/images_processed/threshold_mid_inverted.jpg'
        cv2.imwrite(path_to_mid_thresh, mid)
        return path_to_mid_thresh
    path_to_mid_thresh = 'resources/images_processed/threshold_mid.jpg'
    cv2.imwrite(path_to_mid_thresh, mid)
    return path_to_mid_thresh


def apply_high(image):
    th, high = cv2.threshold(image, 185, 255, cv2.THRESH_BINARY)
    return high
