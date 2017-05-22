def one_away(s1, s2):
    mismatch_count = 0
    if len(s1) == len(s2):
        for i, char in enumerate(s1):
            if s1[i] == s2[i]:
                continue
            else:
                mismatch_count += 1
                if mismatch_count > 1:
                    return False
    else:
        if len(s1) > len(s2):
            bigger_str = [c1 for c1 in s1]
            smaller_str = [c2 for c2 in s2]
        else:
            bigger_str = [c2 for c2 in s2]
            smaller_str = [c1 for c1 in s1]
        for i, char in enumerate(bigger_str):
            if i < len(smaller_str):
                if bigger_str[i] == smaller_str[i]:
                    continue
            else:
                mismatch_count += 1
                if mismatch_count > 1:
                    return False
                smaller_str = smaller_str[:i] + [bigger_str[i]] + smaller_str[i:]
    return True


print one_away("pale", "bake")
