s = 'Reverse this strings'

# 자기 문자열 뒤집기
print(s[::-1])

# 자기 문자열 뒤집기
print(''.join(reversed(s)))

# 빈 문자열 만들기
empty_str = ""
for i in range(len(s)-1,-1,-1):
    empty_str += s[i]

print(''.join(empty_str))

# Swap 방식 1
s_list = list(s)

for i in range(len(s)//2):
    s_list[i] , s_list[len(s)-1-i] = s_list[len(s)-1-i], s_list[i]

s = ""
for i in s_list:
    s += i
print(s)