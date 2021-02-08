# Input

> 사용자로부터 무언가 입력 받을 때 사용.

```python
#변수명 선언도 가능
x = input("원하는 숫자를 입력하세요 : ")
```

- 공백을 기준으로 input받은 값 자르기

![image-20210208170336330](file://C:\Users\kuyhnow\ssafy_personal\TIL\00_programming_languages\01_python.assets\image-20210208170336330.png?lastModify=1612789740)

> map(type, input().split())
>
> input 받은 값을 공백을 구분자로 하여 split하고, int로 형변환한다. 각 값을 a, b, c처럼 각 변수에 할당 가능.



-  공백없이 이어져 온 것을 처리하는 방법

```python
#가나다라 -- 그냥 list에 넣기
a = list(input())
#하지만 숫자를 정수형으로 list에 넣고 싶다면? 157584
a = list(map(int, input())) #[1,5,7,5,8,4]
```

- , 단위로 split하고 싶다면?

```python
#가, 나, 다 , 단위로 나누고 싶다면?
a = list(input().split(","))
```

- 코드 내에서 input값을 한번에 받기도 가능하다.

```python
"""
입력 이거 통으로 해도 한줄씩 알아서 읽음.
3
9
7 4 2 0 0 6 0 7 0
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
"""

# 표준 답안

# T = int(input())

# 번거롭게 T없이, 바로 변수에 대입도 가능하다.
for tc in range(1, int(input())+1):
    N = int(input())
    box = list(map(int,input().split()))
    ans = 1

    print("#{} {}".format(tc, ans))
```





# sys

- Python Interpreter가 제공하는, 변수와 함수를 직접 제어할 수 있게 해주는 모듈

- 여기선 Text문을 불러오는데 사용되었다.

```python
#같은 폴더내의 input.txt파일을 "read"만 해온다.
sys.stdin = open("input.txt", "r")
```

