# 1.6
# runtime: O(N)
# spacetime: O(N)
def solution(s: str) -> str:
    if not s:
        return s

    count = 1
    pieces = []
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            pieces.append(s[i - 1] + str(count))
            count = 1

    pieces.append(s[-1] + str(count))

    compressed = "".join(pieces)
    return compressed if len(compressed) < len(s) else s


print(solution("aabcccccaaa"))  # "a2b1c5a3"
print(solution("abcdef"))  # "abcdef"
print(solution("aabb"))  # "aabb"
print(solution("aaa"))  # "a3"
print(solution("a"))  # "a"
print(solution(""))  # ""
