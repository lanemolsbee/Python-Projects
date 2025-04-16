def primary_stress_position(phoneme_list):
    for i in range(len(phoneme_list)):
        if len(phoneme_list[i]) == 3 and phoneme_list[i][2] == "1":
            return i
    return None