from image_processor import dimensions


def calculate_results(images_to_be_processed, months, gender):
    results = dimensions.calculate_dimensions(images_to_be_processed, months, gender)
    return results


def calculate_cranial_ratio(widths, heights):
    cranial_ratio = (widths / heights) * 100
    if 75.0 <= cranial_ratio <= 84.9:
        return cranial_ratio, 'Normalidade'
    elif 85.0 <= cranial_ratio <= 94.9:
        return cranial_ratio, 'Braquicefalia Suave'
    elif 95.0 <= cranial_ratio <= 104.9:
        return cranial_ratio, 'Braquicefalia Moderada'
    elif cranial_ratio >= 105.0:
        return cranial_ratio, 'Braquicefalia Severa'
    else:
        return cranial_ratio, 'Nenhum indício de Braquicefalia'
