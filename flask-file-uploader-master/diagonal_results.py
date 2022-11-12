import dimensions


def calculate_results(images_to_be_processed, months, gender):
    results = dimensions.calculate_dimensions(images_to_be_processed, months, gender)
    return results


def calculate_asymmetry_index(diagonal_A, diagonal_B):
    final_diagonal = diagonal_A - diagonal_B
    asymmetry_index = (final_diagonal / diagonal_A) * 100
    if asymmetry_index <= 3.49:
        return asymmetry_index, 'Normalidade'
    elif 3.5 <= asymmetry_index <= 6.24:
        return asymmetry_index, 'Plagiocefalia Suave'
    elif 6.25 <= asymmetry_index <= 8.74:
        return asymmetry_index, 'Plagiocefalia I Moderada'
    elif 8.75 <= asymmetry_index <= 10.99:
        return asymmetry_index, 'Plagiocefalia II Moderada'
    elif asymmetry_index >= 11:
        return asymmetry_index, 'Plagiocefalia Severa'
