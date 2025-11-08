# 1.2
# runtime: O(N)
# spacetime: O(length)
def solution(url: str, length: int) -> str:
    result = [""] * length

    i = 0
    while i < length:
        if url[i] == " ":
            result[i] = "%20"
        else:
            result[i] = url[i]
        i += 1

    return "".join(result)

print(solution("much ado about nothing      ", 22)) # "much%20ado%20about%20nothing"
print(solution("Mr John Smith       ", 13)) # "Mr%20John%20Smith"
print(solution(" a b    ", 4)) # "%20a%20b"
