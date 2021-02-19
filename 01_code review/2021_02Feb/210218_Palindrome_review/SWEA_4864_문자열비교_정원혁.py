def BruteForce(pattern, text):
    len_text = len(text)
    len_pattern = len(pattern)

    i = 0
    j = 0
    # 둘중 하나라도 범위를 넘으면 그만
    while j < len_pattern and i < len_text:
        if text[i] != pattern[j]:
            # j만큼 온 길이를 빼준다.
            i = i - j
            # i값이 망가지므로 j를 나중에
            j = -1
        # if문을 돌았다면 j는 다시 0부터, i는 j의 길이만큼 빼고 계속 그대로 순환.
        # 돌지 않았다면 그냥 각각 +1씩
        i += 1
        j += 1

    # 성공
    if j == len_pattern:
        return 1 
    
    # 실패
    else:
        return 0  # 실패


T = int(input())
# Test case 수만큼 돌면서
for tc in range(1, T + 1):
    pattern = input()
    text = input()

    print("#{} {}".format(tc, BruteForce(pattern, text)))
