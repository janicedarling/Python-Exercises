def isPerm(s1, s2):
    if len(s1) != len(s2):
        return False

    sd1 = {} 
    sd2 = {}

    for c in s1:
        if c not in sd1:
            sd1[c] = 1
        else:
            sd1[c] += 1
    for c in s2:
        if c not in sd1:
            return False
        if c not in sd2:
            sd2[c] = 1
        else:
            sd2[c] += 1

    return sd1 == sd2
