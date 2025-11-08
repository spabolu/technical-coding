# 1.5
# runtime: O(N)
# spacetime: O(1)
def solution(s1: str, s2: str) -> bool:
    if abs(len(s1) - len(s2)) > 1:
        return False

    # s1 is shorter (or equal) to s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    i = j = 0
    found_diff = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if found_diff:
                return False
            else:
                found_diff = True

            # if the length is the same but the letters don't match
            # then this is a replacement
            if len(s1) == len(s2):
                i += 1
            # if not the same lenght, we move up the longer string's char
            # to continue matching
            j += 1
        else:
            i += 1
            j += 1

    return True


print(solution("pale", "ple"))  # true
print(solution("pales", "pale"))  # true
print(solution("", "d"))  # true
print(solution("a", "b"))  # true
print(solution("pale", "bake"))  # false
print(solution("pas", "pale"))  # false
