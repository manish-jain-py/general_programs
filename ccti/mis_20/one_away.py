def is_one_away(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len1 - len2 > abs(1):
        return False

    if len1 == len2:
        mismatch_count = 0
        for ind in range(len1):
            if str1[ind] == str2[ind]:
                continue
            else:
                mismatch_count += 1
                if mismatch_count > 1:
                    return False
    else:
        mismatch_count = 0
        big_string,  short_string = (str1, str2) if len1 > len2 else (str2, str1)

        for ind in range(len(big_string)):
            if ind == len(big_string) - 1:
                if mismatch_count == 0:
                    return True
                else:
                    if big_string[ind] == short_string[ind]:
                        return True
                    else:
                        return False

            if big_string[ind] == short_string[ind]:
                continue
            else:
                mismatch_count += 1

                if mismatch_count > 1:
                    return False
                short_string = short_string[:ind] + big_string[ind] + short_string[ind:]

    return True


