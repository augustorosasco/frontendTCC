import cv2


<<<<<<< Updated upstream
def low(image_path):
    low_thresh = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    th, low = cv2.threshold(low_thresh, 60, 255, cv2.THRESH_BINARY)  # valores testados: 85, 55 e 140
    if 'inverted' in image_path:
        path_to_low_thresh = 'resources/images_processed/threshold_low_inverted.jpg'
        cv2.imwrite(path_to_low_thresh, low)
        return path_to_low_thresh
    path_to_low_thresh = 'resources/images_processed/threshold_low.jpg'
    cv2.imwrite(path_to_low_thresh, low)
    return path_to_low_thresh
=======
def apply_low(image):
    th, low = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)  # valores testados: 85, 55 e 140
    return low
>>>>>>> Stashed changes


'''def mid(image_path):
    mid_thresh = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    th, mid = cv2.threshold(mid_thresh, 85, 255, cv2.THRESH_BINARY)
    if 'inverted' in image_path:
        path_to_mid_thresh = 'resources/images_processed/threshold_mid_inverted.jpg'
        cv2.imwrite(path_to_mid_thresh, mid)
        return path_to_mid_thresh
    path_to_mid_thresh = 'resources/images_processed/threshold_mid.jpg'
    cv2.imwrite(path_to_mid_thresh, mid)
    return path_to_mid_thresh'''


def high(image_path):
    high_thresh = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    th, high = cv2.threshold(high_thresh, 185, 255, cv2.THRESH_BINARY)
    if 'inverted' in image_path:
        path_to_high_thresh = 'resources/images_processed/threshold_high_inverted.jpg'
        cv2.imwrite(path_to_high_thresh, high)
        return path_to_high_thresh
    path_to_high_thresh = 'resources/images_processed/threshold_high.jpg'
    cv2.imwrite(path_to_high_thresh, high)
    return path_to_high_thresh
