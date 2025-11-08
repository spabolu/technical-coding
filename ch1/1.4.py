from collections import Counter

# 1.4
# runtime: O(N)
# spacetime: O(N)
def solution(s: str) -> bool:
    s_clean = ""

    for char in s:
        if char.isalpha():
            s_clean += char.lower()

    counter = Counter(s_clean)

    return sum(val % 2 for val in counter.values()) <= 1


print(solution("Tact Coa"))  # true
print(solution("a-Bba"))  # true
print(solution("So patient a nurse to nurse a patient so"))  # false
print(solution("a-bba!"))  # true
print(solution("jhsabckuj ahjsbckj"))  # true
print(solution("Random Words"))  # false
print(solution("waDhdha"))  # true
