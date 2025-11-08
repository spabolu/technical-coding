test_cases = [
    ("abcd", True),
    ("s4fad", True),
    ("", True),
    ("23ds2", False),
    ("hb 627jh=j ()", False),
    ("".join([chr(val) for val in range(128)]), True),
    ("".join([chr(val // 2) for val in range(129)]), False),
]

# 1.1
def solution(s: str) -> bool:
    sett = set(s)
    return len(sett) == len(s)

passes = 0
for test in test_cases:
    if solution(test[0]) == test[1]:
        passes += 1

print(f'{passes}/{len(test_cases)} passed!')