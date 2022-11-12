import dimensions


def calculate_results(images_to_be_processed, months, gender):
    results = dimensions.calculate_dimensions(images_to_be_processed, months, gender)
    return results


def calculate_cranial_ratio(widths, heights):
    cranial_ratio = (widths / heights) * 100
    if cranial_ratio < 75:
        return 'Nenhum índice de Braquicefalia', cranial_ratio
    elif 75.0 <= cranial_ratio <= 84.9:
        return 'Normalidade', cranial_ratio
    elif 85.0 <= cranial_ratio <= 94.9:
        return 'Braquicefalia Suave', cranial_ratio
    elif 95.0 <= cranial_ratio <= 104.9:
        return 'Braquicefalia Moderada', cranial_ratio
    elif cranial_ratio >= 105.0:
        return 'Braquicefalia Severa', cranial_ratio
