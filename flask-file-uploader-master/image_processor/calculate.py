def width(dist, months, gender):
    pixels_per_metric = 0
    if months == 1:
        if gender.str.lower().str.lower() == 'f':
            pixels_per_metric = dist / 11.62
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 11.87
    elif months == 2:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.2
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.42
    elif months == 3:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 4:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.9
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 13.12
    elif months == 5:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 13.2
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 13.53
    elif months == 6:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 13.47
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 13.82
    elif months == 7:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 8:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 9:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 10:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 11:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 12:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 13:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 14:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 15:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 16:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 17:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 18:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 19:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 20:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 21:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 22:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 23:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    elif months == 24:
        if gender.str.lower() == 'f':
            pixels_per_metric = dist / 12.58
        elif gender.str.lower() == 'm':
            pixels_per_metric = dist / 12.9
    return pixels_per_metric
