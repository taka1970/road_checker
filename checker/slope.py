def check_slope(start_elev, end_elev, length):
    slope = (end_elev - start_elev) / length * 100
    return slope, slope <= 3.0
