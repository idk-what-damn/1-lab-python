def are_anagrams(str1, str2):
    str1_clean = str1.lower().replace(" ", "")
    str2_clean = str2.lower().replace(" ", "")

    return sorted(str1_clean) == sorted(str2_clean)