# 1.9
# runtime: O()
# spacetime: O()
def solution(s1: str, s2: str) -> bool:
    if len(s1) == len(s2) != 0:
        print(s2 in s1 * 2) # "foo" * 2 = "foofoo"
    return False

print(solution("erbottlewat", "waterbottle")) # true
print(solution("foofoo", "foo")) # true
print(solution("foo", "bar")) # false
