# integer to String

def itoa(integer):
    value = []
    while integer > 0:
        value.append(integer % 10)
        integer = integer//10

    result = ""
    for i in range(len(value)-1, -1, -1):
        result += chr(value[i] + 48)
    print(type(result))
    return result

print(itoa(int(input("정수를 입력해주세요 : "))))

