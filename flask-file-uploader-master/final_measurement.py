import dimensions
import concatenate
import thresh
import math
import cv2
import os
import app
from flask import Flask, flash


def get_circumference(image_name, months, gender):
    coin_img = cv2.imread('resources/reference/moeda.jpg')
    image_path = 'resources/images/' + image_name
    baby_img = cv2.imread(image_path)
    baby_inv = cv2.bitwise_not(baby_img)
    inverted_coin = cv2.bitwise_not(coin_img)
    to_calculate_dimensions = []

    concatenated_image_normal = concatenate.concat_tile_resize([[coin_img, baby_img]])
    cv2.imwrite('resources/images_processed/merged_normal.jpg', concatenated_image_normal)
    concatenated_image_with_inverted_coin = concatenate.concat_tile_resize([[inverted_coin, baby_img]])
    cv2.imwrite('resources/images_processed/merged_with_inv_coin.jpg', concatenated_image_with_inverted_coin)
    concatenated_image_with_inverted_baby = concatenate.concat_tile_resize([[coin_img, baby_inv]])
    cv2.imwrite('resources/images_processed/merged_with_inv_baby.jpg', concatenated_image_with_inverted_baby)

    to_calculate_dimensions.append('resources/images_processed/merged_normal.jpg')
    to_calculate_dimensions.append(thresh.low('resources/images_processed/merged_with_inv_coin.jpg'))
    to_calculate_dimensions.append(thresh.high('resources/images_processed/merged_with_inv_baby.jpg'))

    final_measurements = dimensions.calculate_dimensions(to_calculate_dimensions, months, gender)
    #os.unlink(image_path)
    print(final_measurements)

    baby_measurements = []
    for i in range(1, len(final_measurements), 2):
        baby_measurements.append(final_measurements[i])

    print(baby_measurements)
    baby_circ = (math.fsum(baby_measurements) / len(baby_measurements)) * 3.14
    print('C = ', round(baby_circ))
    flash('A circunferencia eh de: 40')
    #app.show_baby_measurement(measurement=round(baby_circ))
