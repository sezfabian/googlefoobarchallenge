#!/usr/bin/python3
def solution(x):
    cipherKey = "zyxwvutsrqponmlkjihgfedcba"
    decodedX = ""

    for i in range(len(x)):
        if ord(x[i]) >= ord('a') and ord(x[i]) <= ord('z'):
            decodedX += cipherKey[ord(x[i]) - ord('a')]
            
        else:
            decodedX += x[i]

    return decodedX



print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
