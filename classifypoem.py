def classify_by_syl(syl_count):
    # TODO: Contine adding poem classifications
    from numpy import mean
    length = len(syl_count)
    if length == 5 and syl_count[0] == 2 and syl_count[1] == 4 and syl_count[2] == 6 and syl_count[3] == 8 and \
            syl_count[4] == 2:
        form = "Cinquain"
    elif length == 9 and syl_count[0] == 9 and syl_count[1] == 8 and syl_count[2] == 7 and syl_count[3] == 6 and \
            syl_count[4] == 5 and syl_count[5] == 4 and syl_count[6] == 3 and syl_count[7] == 2 and syl_count[8] == 1:
        form = "Nonet"
    elif length == 3 and syl_count[0] == 5 and syl_count[1] == 7 and syl_count[2] == 5:
        form = "Haiku"
    elif length == 6:
        form = "Sextain"
    elif (length == 13 or length == 14) and mean(syl_count) == 8:
        form = "Formal French Rondel"
    else:
        form = "Open Form"
    return form
