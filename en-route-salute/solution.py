def solution(s):
    rightMovers = 0
    salutes = 0

    for i in range(len(s)):
        if s[i] == '>':
            rightMovers += 1
        elif s[i] == '<':
            salutes += rightMovers * 2

    return salutes

print(solution("<<><>><<"))