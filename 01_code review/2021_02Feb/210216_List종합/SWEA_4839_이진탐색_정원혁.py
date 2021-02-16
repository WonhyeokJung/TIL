def binary_Search(page, searching_page):
    start = 1
    end = page
    # 몇 번 했는 지 추가
    count = 0
    while start <= end:
        middle = (start + end) //2
        if middle == searching_page:
            count += 1
            return count
        elif middle > searching_page:
            end = middle
            count += 1
        else:
            start = middle
            count += 1
    return False


# Test Case
T = int(input())

for tc in range(1, T+1):
    # 전체 페이지 수 P, A가 찾을 페이지 pa, B가 찾을 페이지 pb
    P, pa, pb = map(int, input().split())
    if binary_Search(P, pa) > binary_Search(P, pb):
        print("#{} B".format(tc))
    elif binary_Search(P, pa) < binary_Search(P, pb):
        print("#{} A".format(tc))
    else:
        print("#{} 0".format(tc))
