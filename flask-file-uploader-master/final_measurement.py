import dimensions
import concatenate
import thresh
import math
import cv2
import os
import app
from flask import flash


def get_circumference(image_name, months, gender):
    coin_img = cv2.imread('resources/reference/moeda.jpg')
    image_path = 'resources/images/' + image_name
    baby_img = cv2.imread(image_path)
    final_baby_img = cv2.flip(baby_img, 1)
    baby_inv = cv2.bitwise_not(baby_img)
    final_baby_inv_img = cv2.flip(baby_inv, 1)
    inverted_coin = cv2.bitwise_not(coin_img)
    to_calculate_dimensions = []

    concatenated_image_normal = concatenate.concat_tile_resize([[coin_img, final_baby_img]])
    cv2.imwrite('resources/images_processed/merged_normal.jpg', concatenated_image_normal)
    concatenated_image_with_inverted_coin = concatenate.concat_tile_resize([[inverted_coin, final_baby_img]])
    cv2.imwrite('resources/images_processed/merged_with_inv_coin.jpg', concatenated_image_with_inverted_coin)
    concatenated_image_with_inverted_baby = concatenate.concat_tile_resize([[coin_img, final_baby_inv_img]])
    cv2.imwrite('resources/images_processed/merged_with_inv_baby.jpg', concatenated_image_with_inverted_baby)

    to_calculate_dimensions.append('resources/images_processed/merged_normal.jpg')
    to_calculate_dimensions.append(thresh.low('resources/images_processed/merged_with_inv_coin.jpg'))
    to_calculate_dimensions.append(thresh.high('resources/images_processed/merged_with_inv_baby.jpg'))

    final_measurements = dimensions.calculate_dimensions(to_calculate_dimensions, months, gender)
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
    message = 'O perímetro cranial de seu bebê é de aproximadamente: {0} cm.'.format(round(final_circ))
    flash(message)
    message2 = 'A largura da cabeça é de aproximadamente: {0} cm.'.format('{:.2f}'.format(baby_sum_widths))
    flash(message2)
    message3 = 'A altura da cabeça é de aproximadamente: {0} cm.'.format('{:.2f}'.format(baby_sum_heights))
    flash(message3)
    message4 = 'Informe estas medidas para o profissional da saúde responsável pelo seu bebê para confirmar o ' \
               'diagnóstico. '
    flash(message4)
    baby_heights.clear()
    baby_widths.clear()
