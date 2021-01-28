# 오답 문제 정리
# 2진수 문제였는데, 출력에 문제를 겪었다.

def dec_to_bin(n):
    # 여기에 코드를 작성합니다.
    # 
    a = n//2
    b = ''
    # 더이상 나눌 수가 없을떄,
    if a == 1:
        # 먼저 출력되어야 할 1을 추가하고 (어차피 b는 항상 위에서 초기화 되므로
        # 여기서 b는 또다시 새로운 값의 b이다.)
        b += '1'      
        # 뒤이어 나머지 반환
        b += str(n%2)
        # b를 돌려줌
        return b
    else:
        # 나머지가 1이면 1 반환
        if n % 2 == 1:
            b += '1'
        # 0으로 떨어지면 0반환
        elif n % 2 == 0:
            b += '0'
        # 재귀함수를 먼저 return 시켜줌. 2진수의 출력순을 따르기 위해서(역순)
        return dec_to_bin(n//2) + b
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # => '1010'
    print(dec_to_bin(5))
    # => '101'
    print(dec_to_bin(50))
    # => '110010'
    print(dec_to_bin(124))


# 출력에 문제를 겪은 코드라인은, line 26으로
# return b + dec_to_bin(n//2)로 계속 출력을 시도하니
# 수가 역순으로 출력되었다.
# 단순히 순서만 바꿔주면 되는건데, list.insert나 reversed, [::-1] 등 온갖 뻘짓을 다했다.
# 당연하다 생각했던 부분을 다르게 생각해보는 감각도 키우는 것이 중요하다..