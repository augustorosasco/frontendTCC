import requests

import dimensions
import concatenate
import thresh
import math
import cv2
from flask import flash
import urllib.request
import numpy as np


def get_circumference(images, months, gender):
    baby_img_url = urllib.request.urlopen(images[0])
    baby_arr = np.asarray(bytearray(baby_img_url.read()), dtype=np.uint8)
    baby_img = cv2.imdecode(baby_arr, -1)

    coin_img_url = urllib.request.urlopen(images[1])
    coin_arr = np.asarray(bytearray(coin_img_url.read()), dtype=np.uint8)
    coin_img = cv2.imdecode(coin_arr, -1)

    flipped_baby = cv2.flip(baby_img, 1)
    rotated_baby = cv2.rotate(flipped_baby, cv2.ROTATE_90_CLOCKWISE)
    baby_inv = cv2.bitwise_not(baby_img)
    flipped_inv_baby = cv2.flip(baby_inv, 1)
    rotated_inv_baby = cv2.rotate(flipped_inv_baby, cv2.ROTATE_90_CLOCKWISE)
    inverted_coin = cv2.bitwise_not(coin_img)
    to_calculate_dimensions = []

    #concatenated_image_normal = concatenate.concat_tile_resize([[coin_img, rotated_baby]])
    concatenated_image_with_inverted_coin = concatenate.concat_tile_resize([[inverted_coin, flipped_baby]])
    concatenated_image_with_inverted_baby = concatenate.concat_tile_resize([[coin_img, flipped_inv_baby]])

    #to_calculate_dimensions.append(concatenated_image_normal)
    to_calculate_dimensions.append(thresh.apply_low(concatenated_image_with_inverted_coin))
    to_calculate_dimensions.append(thresh.apply_high(concatenated_image_with_inverted_baby))

    final_measurements = dimensions.calculate_dimensions(to_calculate_dimensions, months, gender)
    requests.delete("https://app.simplefileupload.com/api/v1/file?url={}".format(images[0]), auth=('p7227b3b4018aa3ece264cc9d6705d297', 's7a93e13256c625f12581fd203020bd9e'))
    print('widths: ', final_measurements[0])
    print('heights: ', final_measurements[1])

    baby_widths = []
    widths = final_measurements[0]
    for i in range(1, len(widths), 2):
        baby_widths.append(widths[i])

    baby_heights = []
    heights = final_measurements[1]
    for i in range(1, len(heights), 2):
        baby_heights.append(heights[i])

    print(baby_widths)
    print(baby_heights)
    baby_sum_widths = math.fsum(baby_widths) / len(baby_widths)
    baby_circ_by_width = (math.fsum(baby_widths) / len(baby_widths)) * 3.14
    print('C according to width = ', round(baby_circ_by_width))
    baby_sum_heights = math.fsum(baby_heights) / len(baby_heights)
    baby_circ_by_height = (math.fsum(baby_heights) / len(baby_heights)) * 3.14
    print('C according to heights = ', round(baby_circ_by_height))
    final_circ = (baby_circ_by_width + baby_circ_by_height) / 2
    message = 'O perímetro cranial da sua criança é de aproximadamente: {0} cm.'.format(round(final_circ))
    flash(message)
    message2 = 'A largura da cabeça é de aproximadamente: {0} cm.'.format('{:.2f}'.format(baby_sum_widths))
    flash(message2)
    message3 = 'A altura da cabeça é de aproximadamente: {0} cm.'.format('{:.2f}'.format(baby_sum_heights))
    flash(message3)
    message4 = 'Informe estas medidas para o profissional da saúde responsável pela sua criança para confirmar o ' \
               'diagnóstico. '
    flash(message4)
    baby_heights.clear()
    baby_widths.clear()
