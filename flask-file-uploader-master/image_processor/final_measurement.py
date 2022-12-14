import requests

from image_processor import diagonal_results, concatenate, perpendicular_results, thresh
import cv2
import math
from flask import flash
import urllib.request
import numpy as np
import logging

calculate_perpendicular_dimensions = []
calculate_diagonals_dimensions = []
final_measurements = []


def get_circumference(images, months, gender):
    baby_img_url = urllib.request.urlopen(images[0])
    baby_arr = np.asarray(bytearray(baby_img_url.read()), dtype=np.uint8)
    baby_img = cv2.imdecode(baby_arr, -1)

    coin_img_url = urllib.request.urlopen(images[1])
    coin_arr = np.asarray(bytearray(coin_img_url.read()), dtype=np.uint8)
    coin_img = cv2.imdecode(coin_arr, -1)

    flipped_baby = cv2.flip(baby_img, 1)
    baby_inv = cv2.bitwise_not(baby_img)
    flipped_inv_baby = cv2.flip(baby_inv, 1)
    inverted_coin = cv2.bitwise_not(coin_img)

    concatenated_image_with_inverted_coin = concatenate.concat_tile_resize([[inverted_coin, flipped_baby]])
    concatenated_image_with_inverted_baby = concatenate.concat_tile_resize([[coin_img, flipped_inv_baby]])

    calculate_perpendicular_dimensions.append(
        thresh.apply_low_thresh_for_perpendicular(concatenated_image_with_inverted_coin))
    calculate_perpendicular_dimensions.append(
        thresh.apply_high_thresh_for_perpendicular(concatenated_image_with_inverted_baby))
    calculate_diagonals_dimensions.append(thresh.apply_low_for_diagonals(concatenated_image_with_inverted_coin))
    calculate_diagonals_dimensions.append(thresh.apply_high_for_diagonals(concatenated_image_with_inverted_baby))

    perpendicular_measurements = perpendicular_results.calculate_results(calculate_perpendicular_dimensions, months, gender)

    baby_widths = []
    widths = perpendicular_measurements[0]
    for i in range(1, len(widths), 2):
        baby_widths.append(widths[i])

    baby_heights = []
    heights = perpendicular_measurements[1]
    for i in range(1, len(heights), 2):
        baby_heights.append(heights[i])

    logging.debug(baby_widths)
    logging.debug(baby_heights)

    baby_sum_widths = math.fsum(baby_widths) / len(baby_widths)
    baby_sum_heights = math.fsum(baby_heights) / len(baby_heights)

    baby_circ_by_width = (math.fsum(baby_widths) / len(baby_widths)) * 3.14
    baby_circ_by_height = (math.fsum(baby_heights) / len(baby_heights)) * 3.14

    final_circ = (baby_circ_by_width + baby_circ_by_height) / 2
    logging.debug('C according to heights = ', round(baby_circ_by_height))
    logging.debug('C according to widths = ', round(baby_circ_by_width))
    logging.debug('Final C = ', round(final_circ))

    cranial_info = perpendicular_results.calculate_cranial_ratio(baby_sum_widths, baby_sum_heights)

    diagonal_measurements = diagonal_results.calculate_results(calculate_diagonals_dimensions, months, gender)

    baby_diagonal_A = []
    diagonal_A = diagonal_measurements[0]
    for i in range(1, len(diagonal_A), 2):
        baby_diagonal_A.append(diagonal_A[i])

    baby_diagonal_B = []
    diagonal_B = diagonal_measurements[1]
    for i in range(1, len(diagonal_B), 2):
        baby_diagonal_B.append(diagonal_B[i])

    sum_of_baby_diagonal_A = math.fsum(baby_diagonal_A) / len(baby_diagonal_A)
    sum_of_baby_diagonal_B = math.fsum(baby_diagonal_B) / len(baby_diagonal_B)

    asymmetry_index_results = diagonal_results.calculate_asymmetry_index(sum_of_baby_diagonal_A, sum_of_baby_diagonal_B)

    requests.delete("https://app.simplefileupload.com/api/v1/file?url={}".format(images[0]),
                    auth=('p7227b3b4018aa3ece264cc9d6705d297', 's7a93e13256c625f12581fd203020bd9e'))

    message = 'O per??metro cranial da sua crian??a ?? de aproximadamente: {0} cm.'.format(round(final_circ))
    flash(message)
    message2 = 'A largura da cabe??a ?? de aproximadamente: {0} cm.'.format('{:.2f}'.format(baby_sum_widths))
    flash(message2)
    message3 = 'A altura da cabe??a ?? de aproximadamente: {0} cm.'.format('{:.2f}'.format(baby_sum_heights))
    flash(message3)
    if cranial_info[0] > 0:
        message4 = 'O ??ndice de propor????o craniana de seu beb?? ?? de aproximadamente: "{0}". Indicando: "{1}"'.format('{:.2f}'.format(cranial_info[0]), cranial_info[1])
        flash(message4)
    else:
        message4 = 'N??o foi poss??vel calcular o ??ndice de propor????o craniana de seu beb??. Envie outra imagem de seu beb?? seguindo as dicas mencionadas acima.'
        flash(message4)
    if asymmetry_index_results[0] > 0:
        message5 = 'O ??ndice de assimetria da ab??bada craniana de seu beb?? ?? de aproximadamente: "{0}". Indicando: "{1}"'.format('{:.2f}'.format(asymmetry_index_results[0]), asymmetry_index_results[1])
        flash(message5)
    else:
        message5 = 'N??o foi poss??vel calcular o ??ndice de assimetria da ab??bada craniana de seu beb??. Envie outra imagem de seu beb?? seguindo as dicas mencionadas acima.'
        flash(message5)
    message6 = 'Informe estas medidas para o profissional da sa??de respons??vel pela sua crian??a para confirmar o diagn??stico.'
    flash(message6)

    baby_heights.clear()
    baby_widths.clear()
    baby_diagonal_A.clear()
    baby_diagonal_B.clear()
