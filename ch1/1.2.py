test_cases = [
    ("dog", "god", True),
    ("abcd", "bacd", True),
    ("3563476", "7334566", True),
    ("wef34f", "wffe34", True),
    ("dogx", "godz", False),
    ("abcd", "d2cba", False),
    ("2354", "1234", False),
    ("dcw4f", "dcw5f", False),
    ("DOG", "dog", False),
    ("dog ", "dog", False),
    ("aaab", "bbba", False),
]


# 1.2
# runtime: O(N)
# spacetime: O(N)
def solution(s: str, t: str) -> bool:
    s_map = {}
    t_map = {}

    for char in s:
        s_map[char] = s_map.get(char, 0) + 1

    for char in t:
        t_map[char] = t_map.get(char, 0) + 1

    return s_map == t_map

passes = 0
for test in test_cases:
    if solution(test[0], test[1]) == test[2]:
        passes += 1

print(f"{passes}/{len(test_cases)} passed!")
