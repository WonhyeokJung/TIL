# Algorithm 
- 문제를 해결하기 위한 절차나 방법.
- 컴퓨터가 어떤 일을 수행하기 위한 **단계적** 방법
- 다시 말하면, 어떠한 문제를 해결하기 위한 절차


## 표현방식
- 크게 수도코드(의사코드), 순서도, 자연어, 코드 등이 있다.

**수도코드(의사코드, pseudocode)**

- 코드 형태로 짜되, 자연어를 이용하여 논리를 표현하기 위한 코드

> **슈더코드 예시**

![image-20210208101959913](C:\Users\kuyhnow\AppData\Roaming\Typora\typora-user-images\image-20210208101959913.png)

**순서도(Flow Chart)**

> **순서도 예시**

![image-20210208131252284](03_Algorithm.assets/image-20210208131252284.png)

> 출처 : https://www.youtube.com/watch?app=desktop&v=vOEN65nm4YU

## 좋은 알고리즘의 기준

1. 정확성
2. 작업량 : 적은 연산 ***시간복잡도***
3. 메모리 사용량
4. 단순성
5. 최적성



## 시간복잡도(Time Complexity)

- 실행되는 명령문의 개수를 계산

```python
def ClacSum( n ):
    sum <- 0; # 1번
    # for문 전체를 n번
    for i in range(1, n+1): # 1번
        sum <- sum + i; # 1번
    return sum;

# 1 + n*2 = 2n+1 번
```



**Big-Oh Notation 빅-오 표기법**

- 시간 복잡도 함수 중 가장 **큰 영향력**을 주는 n에 대한 항만을 표시
- 최악의 경우를 고려하여 계산해보는 방법
- 계수(Coefficient)는 생략(3n은 n으로)
- 최고차항만 고려(O(3n^2 + 10n + 100) = O(n^2) )

> 예제

```python
# n개의 데이터를 입력받아 저장한 후 #n 각 데이터에 1씩 증가시킨 후 #n 각 데이터를 화면에 출력하는 #n
# 알고리즘의 시간복잡도는 어떻게 될까?
3n = n ,
Answer : O(n)
```

- n^2부터는 시간이 기하급수적으로 늘어난다.

![image-20210208125005592](03_Algorithm.assets/image-20210208125005592.png)



## 배열(Array)

- 파이썬은 List[ ]를 배열처럼 사용한다.

### 선언

- Arr = list()
- Arr = []

### 접근

- Arr[idx]

### 정렬

- 오름차순( Ascending. 작 > 큰)
- 내림차순(Descending)

**대표적인 정렬 방식**

1. 버블 정렬 (Bubble Sort)

   > 인접한 두개의 원소를 비교하며 자리를 계속 교환하는 방식
   >
   > 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
   >
   > 거품이 올라오는 것 같아 버블 정렬이라 부른다.

    - Time complexity : O(n^2)

   ```python
   # List 내의 값을 오름차순으로 정렬하는 Bubble Sort 예제
   def BubbleSort(a): # List a eg.[1,3,5,2,4]
       for i in range(len(a)-1, 0, -1): # 범위의 끝 위치 for i in range(4,0,-1) 4,3,2,1
           # range는 마지막 숫자 -1이 아닌, 마지막 숫자를 포함하지 않는 것.
           for j in range(0,i):
               if a[j] > a[j+1]:
                   a[j], a[j+1] = a[j+1], a[j]
   ```

   ```python
   arr = [55, 7, 78, 12, 42]  # 정렬 하고자 하는 배열
   
   
   def BubbleSort(arr):  # 정렬할 List
       for i in range(len(arr) - 1, 0, -1):  # 범위의 끝 위치
           for j in range(0, i):
               print("현재상태",arr)
               if arr[j] > arr[j + 1]:
                   arr[j], arr[j + 1] = arr[j + 1], arr[j]
               print("스왑과정",arr)
           print("-----------------------------------")
   
   BubbleSort(arr)
   
   print(arr)
   ```

   

2. 카운팅 정렬 (Counting Sort)

   > 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

   - Counting Sort의 원리

   ```python
   
   ```

   

   - **정수 or 정수로 표현할 수 있는 자료**에만 적용가능(각 항목 발생 회수를 Count하기 때문)
   - 충분한 공간을 할당하려면, 집합 내 가장 큰 정수(Integer)를 알아야한다.
   - [0,1,1억]이런 경우처럼 최대 정수가 너무 큰 경우는 사용하지 않는 편이 좋다.
   - Time Complexity : O(n+k) / n =len(list) k = 정수의 최대값 max(integer)

   ```python
   # 원리
   [0,4,1,3,1,2,4,1]
   # 각 숫자가 몇개씩 있는지 Count
   count = [0]*5 # 0~4까지 총 5개므로
   return [1,3,1,1,2]
   
   [1,4,5,6,8] # 첫 항부터 각 누적합
   
   
   ```

   - 뒤에서부터 카운팅 하는 이유는 **안정정렬(Stable Sort)**을 위함. 
   - eg) 같은 1도 list 내 순서가 있었을텐데 그 순서를 유지해주기 위함이다.

   ```python
   def Counting_Sort(A, B, k):
       # A[] --- 입력 배열(1 to k) = Data
       # B[] --- 정렬된 배열 = result
       # C[] --- Counting Array
       
       # B = [0]*len(A) 여기서 B를 정의하면 B를 return해야 한다.
       C =[0]*k
       
       for i in range(0, len(B)): #Counting
           C[A[i]] += 1
       for i in range(1, len(C)): #원소별 누적합
           C[i] += C[i-1]
       for i in range(len(B)-1, -1, -1): # New Array sorted stable
           B[C[A[i]]-1] = A[i]
           C[A[i]] -= 1
   ```

   

   ![image-20210208150102009](03_algorithm.assets/image-20210208150102009.png)

   

3. 선택 정렬 (Selection Sort)

   > 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
   >
   > **Selection Algorithm**을 전체 자료에 적용한 것.

   - 정렬 과정
     1. 주어진 List 중 최소값을 찾는다.
     2. 그 값을 List의 맨 앞에 위치한 값과 교환한다.
     3. 맨 처음 위치를 제외한 나머지 List를 대상으로 위의 과정을 반복한다.

   ```python
   arr = [64, 25, 10, 22, 11] # 0 < arr[i] <= 100
   min = 100
   minIndex = 0 # 이게 아래로 들어가야 맞음. minIndex = i로. 안그러면 
   			 # 기존 minIndex값이 유지될 가능성이 존재함
   for i in range(len(arr)-1):
       for j in range(len(arr)):
       	if arr[j] < min :
           	min = arr[j]
               minIndex = j
   	arr[i], arr[minIndex] = arr[minIndex], arr[i]
   ```

   ```python
   # 구현 예
   def selectionSort(arr):
       for i in range(0, len(arr)-1):
           min = i
           for j in range(i+1, len(arr)):
               if arr[min] > arr[j]:
                   min = j
           arr[i], arr[min] = arr[min], arr[i]
   ```

   

4. 퀵 정렬 (Quick Sort)

5. 삽입 정렬 (Insertion Sort)

6. 병합 정렬 (Merge Sort)



## 완전검색(Exhaustive Search)

> 문제의 해법으로 생각할 수 있는 모든 경우를 나열 및 확인하는 기법

- Brute-force 혹은 Generate-and-Test 기법으로도 부른다.
- 모든 경우 테스트 후, 최종 해법을 도출하므로 경우의 수가 작을 때 유용.

## 순열(Permutation)

> 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것

- 시간복잡도(Time Complexity) : n!

- 서로 다른 n개중 r개를 택하는 순열 : nPr
  - 식 :  nPr = n\*(n-1)\*(n-2)\*...\*(n-r+1)
- nPn = n! (Factorial) (중복값도 다 다른 하나로 세기)
  - 식: nPn = n\*(n-1)\*(n-2)\*...\*2\*1( =  n-n+1)

```python
# {1,2,3}을 포함하는 모든 순열을 생성하는 함수
for i1 in range(1, 4): # 순열 len이 3이니까 4로 설정한 것. 하나가 늘면, for문도 하나씩 늘어난다.
    for i2 in range(1, 4):
        if i2 != i1 :
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2 :
                    print(i1, i2, i3)
```



## 탐욕 알고리즘 (Greedy Algorithm)

> 최적해를 구하는 데 사용하는 근시안적인 방법
>
> 여러 경우 중 하나를 결정해야 할 때, 그 순간 최적이라고 생각한 것을 선택해 나가는 방식으로 해답에 도달.

- 순간순간 선택이 최적이었다고 하더라고, 최종 해답이 최적이라는 보장은 불가능하다.
- 그냥 머릿속으로 되는대로 해나가면 Greedy

1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구하고, 이를 부분해 집합(Solution set)에 추가
2. 실행 가능성 검사 : 새로운 부분해 집합이 실행 가능한지 확인. 제약 조건을 위반하지 않는 지도 검사.
3. 해 검사 : 새로운 부분해 집합이 문제의 해가 되는 지를 확인. 아직 전체 문제의 해가 완성되지 않았다면 1)부터 다시 시작.



```python
# 거스름돈 문제
# 거스름돈을 가장 최소한의 수로 주려면?

#1) 단위가 큰 동전으로만 거스름돈을 만들면 동전의 개수가 줄어드므로 일단 이 방법을 선택.
#2) 거스름돈이 액수를 초과하는가 확인. 초과하면 마지막에 추가한 동전을 빼고, 1)로 돌아가
#	현재보다 한 단계 작은 단위의 동전을 추가
#3) 해 검사. 액수가 모자라다면 다시 1)로 돌아가 추가할 동전을 고른다.

#문제 :
1260원을 거슬러주는데, 400원짜리 동전이 존재한다면? 500원부터 진행했기 때문에 최소한으로 지급이 불가.
```



## 2차원 배열

> 1차원 List를 묶어놓은 List

### 선언

- 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- Python에선 데이터 초기화를 통해 변수선언과 초기화가 가능
- **열의 길이**는 각각 달라도 됨

```python
arr = [[0,1,2,3],[4,5,6,7]] # 2행 4열의 2차원 List
0	1	2	3
4	5	6	7

# 2 행렬이용
arr = [[0 for i in range(w)] for j in range(h)]
arr = [[0]*w for j in range(h)]

#3 선언만 n = 행 수
arr = [[] for i in range(n)]

#4 0으로 초기화한 2차원배열 (정사각형 형태)
arr = [[0]*n for i in range(n)]

#5 0으로 초기화했지만 직사각형 형태 2차원배열
arr = [[0 for j in range(2)] for i in range(3)]
arr = [[0]*2 for i in range(3)]
[[0,0],[0,0],[0,0]]

#6 톱니형 리스트
arr = [[0]*i for i in [3,1,3,2,5]]

# CF
arr = [[]]*n
arr = [[0]*n]*n
# 이와 같은 선언은 주소값을 똑같이 참조하여, 다같이 숫자를 입력받게 된다.
```



### 입력(Input)

> 2차원 배열의 input 방법

```python
3 4
1 2 3 4
5 6 7 8
9 1 2 3

# 크게 3가지가 있다.
# N = 행, M = 열

# 1
N, M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split()))
           
for i in arr:
    print(i)
#2
N, M = map(int,input().split())
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int,input().split())
                   
for i in arr:
    print(i)
                  
#3
N, M = map(int, input().split())
                  # 쓰지 않을 변수라 _ 사용
arr = [list(map(int, input().split())) for _ in range(N)]
                  # [[map(int, input().split()))] for _ in range(N)]로 할시
                  # 맵 주소값을 리스트에 담아두는 쓴 맛을 볼 수 있으므로 주의
for i in arr:
    print(i)
```



## 순회

> n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법

### 행 우선 순회

```python
# i 행의 좌표
# j 열의 좌표
for i in range(len(Array)): # N, M 알고 있다면 N 
    for j in range(len(Array[i])): # M
        Array[i][j] # 필요한 연산 수행
```

```python
arr = [[1,2,3,4],
       [5,6,7,8],
       [10,11,12,13]
       ]
N = 3  # 행의 길이 len(arr)
M = 4  # 열의 길이 len(arr[i])

for i in range(N):
    for j in range(M):
        print(arr[i][j])
        
# 행 우선 순회를 역순으로(각 행을 우에서 좌 순으로 출력)
for i in range(N):
    for j in range(M-1, -1, -1):
        print(arr[i][j])
```



### 열 우선 순회

> 보통은 열의 길이가 일정한 경우에만 사용
>
> 다른 경우 매번 List의 길이를 구해서 한다.

```python
# i 행의 좌표
# j 열의 좌표
for j in range(len(Array[0])):
    for i in range(len(Array)):
        Array[i][j]  # 필요한 연산 수행
```

```python
N, M
for j in range(M):
    for i in range(N):
        print(arr[i][j])

# 열 거꾸로 출력(각 열을 아래에서 위 순으로 출력)
for j in range(M):
    for i in range(N-1, -1, -1):
        Array[i][j]
```



### 지그재그 순회

> 첫 행은 좌에서 우로, 다음 행은 우에서 좌로, 지그재그로 순회하는 방식

```python
# i 행의 좌표
# j 열의 좌표
for i in range(len(Array)):
    for j in range(len(Array[0])):
        Array[i][j + (m-1-2*j)*(i%2)]
        # 필요한 연산 수행
```

```python
# 대각선으로 순회하는 방법

```

```python
# 가운데에서 바깥으로, 달팽이 모양으로 하는 방법

```



## 델타를 이용한 2차원 배열 탐색

> 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

```python
# 상하좌우의 탐색
            
arr = [[1,2,3], [4,5,6], [7,8,9]]
# 현재 서있는 위치 좌표
r = 1
c = 1
# 행의 길이
N = 3

#상하좌우 dc, dr(column, row)로도 표현함
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# dxy = [[0,-1],[0,1][-1,0],[1,0]]

for i in range(4):
    ny = r + dy[i]
    nx = c + dx[i]
    
    # Python은 리스트 인덱스 -1이면 값을 가져오므로, 이런 위험을 없애기 위해 if문으로 제약조건.
    # 범위를 벗어나면 작업을 건너뛰기.
    if ny < 0 or ny >= N or nx < 0 or nx>= N: continue
    print(arr[ny][nx])
    # 범위 안에 들어오면 작업을 하게 하기.
    # if 0 <=ny<N and 0<=nx<N:
        # print(arr[ny][nx])
```



> 대각선으로 4방향의 인접 배열 요소를 탐색하는 방법

```python

```



### 전치행렬

> 행과 열의 값들을 열과 행의 값으로 전치

```python
1 2 3	  1 4 7
4 5 6 = > 2 5 8
7 8 9	  3 6 9
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1,2,3], [4,5,6], [7,8,9]] # 3*3 행렬

for i in range(3):
    for j in range(3):
        # 이 조건문이 없으면 두번씩 수행해서, 원래값으로 돌아오므로
        if i < j :
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```



## 부분집합의 생성

```python
# 공집합을 포함한 부분집합의 개수

N = 3 # 원소의 개수 eg.{1,2,3}
2**N # 공집합을 포함한 부분집합의 수
# 각 원소를 포함하거나, 포함하지 않거나

# 각각 0, 1의 값을 가지는 16개의 부분집합 생성
bit = [0, 0, 0, 0]
for i in range(2) : 
    bit[0] = i  # 0번째 원소
    for j in range(2):
        bit[1] = j  # 1번째 원소
        for k in range(2):
            bit[2] = k  # 2번째 원소
            for l in range(2):
                bit[3] = l  # 3번째 원소
                print(bit)
0 0 0 0 # 0
0 0 0 1 # 1
0 0 1 0 # 2
0 0 1 1 # 3
....
1 1 1 1 # 15

# 이진수와 수의 순서대로 나온다? for문을 한번에...
for i in range(2**n):
    # bit 연산자를 이용할 것. 아래를 참조..
```



## 비트 연산자

- & : bit 단위로 AND 연산을 한다.
  - eg. `print(6 & 11) = 2`

```python
0110
1011
& : 0010 따라서, 2
    
# 이를 통해, 원하는 위치에 비트가 있는지 확인 가능하다
0110 # 수
0100 # 원하는 연산자 위치만 1을 가지는 수
```



- | : bit 단위로 OR 연산을 한다.
- Left Shift 연산자 **<<** : 피연산자의 bit 열을 왼쪽으로 이동시킨다.
- Right Shift 연산자 **>\>** : 피연산자의 bit 열을 오른쪽으로 이동시킨다.



**<< 연산자**

```python
2 << 3
# 2의 bit를 왼쪽으로 3번 이동
value : 0000 0010
result: 0001 0000
```



- **1<< n **: 2**n 즉, 원소가 n개일 경우의 모든 부분 집합의 수를 의미한다.

**& 연산자**

- i & (1<<j) : i의 j번째 bit가 1인지 아닌지를 리턴한다.

### Bit Operation 이용한 부분집합의 생성

```python
# bit 연산자를 이용한 부분집합 생성
for i in range(1<<n):# 1<<ㅜ은 연산해보면 2**n과 같다.
    for j in range(n):
        # 각 bit 자리 수의 true 여부 확인. 
        if i&(1<<j):
            
```

```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr) # n : 원소의 개수

for i in range(1<<n): # 1<<n : = 2**n.arr의 부분 집합의 개수
    for j in range(n): # 원소의 수만큼 비트를 비교
        if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end = ", ")
    print()
print()
```



## 검색

> 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업



- 목적하는 탐색 키를 가진 항목을 찾는 것
  - 탐색 키(Search Key) : 자료를 구별하여 인식할 수 있는 키

### 종류

- 순차 검색(Sequential Search)
- 이진 검색(Binary Search)
- 인덱싱(Indexing)



### 순차검색(Sequential Search)

**일렬로 되어 있는 자료를 순서대로 검색하는 방법**

- 가장 간단하고 직관적
- 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용
- 구현이 쉬우나, 검색 범위가 넓은 경우 수행시간 증가로 비효율적
- **정렬이 되어있는 경우**, **정렬이 되어있지 않은 경우** 2가지가 있다.



**정렬되어 있지 않은 경우**

> 시간복잡도 : O(n)

1. 첫 번째 원소부터 순서대로, 검색 대상과 키값(우리가 찾고싶은 값)이 같은 원소가 있는 지 비교하며 검색

2. 키 값이 동일한 원소를 찾으면, 그 원소의 Index 반환

3. 마지막까지 찾지 못하면 검색을 실패한다.

```python
arr = [4, 9, 11, 23, 2, 19, 70]
#2를 찾는 경우
key = 2
for i in range(len(arr)):
    if arr[i] == key :
        return i
    	break
else:
    print("못찾음.")
```

4. 찾고자 하는 원소의 순서에 따라 비교 횟수가 결정됨
   1. 정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수 = (1/n) * (1+2+3+...+n) = (n+1)/2
   2. 첫 번째 원소를 찾을 때는 1번, 두 번째 원소 찾을 때는 2번 비교

```python
# 구현 예
def sequentialSearch(arr, n ,key): #arr, n = len(arr), key = 찾는값
    i = 0
    while i<n and arr[i]!=key:
        i += 1
    if i<n : return i
    else : return -1
```



**정렬되어 있는 경우**

> 시간복잡도 : O(n)

1. 오름차순으로 정렬되어 있다고 가정
2. 자료를 순차적으로 검색하면서 키 값을 비교, 원소의 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료.(오름차순이므로, **원소값이 키값보다 크다면** 존재하지 않음)

```python
data = [2,4,7,9,11,19,23]
key = 11
for i in range(len(data)):
    if arr[i] > key:
        return -1 # 존재하지 않음.
    elif arr[i] == key:
        return i
```

3. 찾고자 하는 원소의 순서에 따라 비교 횟수가 결정됨
   1. 정렬되어 있으므로, 검색 실패를 반환하는 경우 평균 비교 횟수가 반으로 줄어듬

```python
# 구현 예
def sequentialSearch2(arr, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] = key : return i
    else : return -1
```



### 이진검색(Binary Search)

> 시간복잡도(Time Complexity) : O(log n)

**자료 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법**

- 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가며 보다 효율적으로 검색을 수행
- 따라서, **자료가 정렬된 상태여야 한다.**



#### 검색과정

1. 자료의 중앙에 있는 원소를 고름
2. 중앙 원소의 값과 찾고자 하는 목표값 비교
3. 목표값 < 중앙 원소의 값시, 자료의 왼쪽 반에 대해서 새로 검색.
4. 반대라면 자료의 오른쪽 반에 대해 새로 검색 수행
5. 1~4반복 수행

```python
arr = [2,4,7,9,11,19,23]
n = len(arr)
key = 7 # 찾는 값
if arr[n//2] > key:
    n = n//2
```

```python
# 구현 예
# 검색 범위의 시작점과 종료점을 이용하여 검색 반복 수행
# 자료의 삽입이나 삭제가 발생한 경우, 배열의 상태를 항상 정렬 상태로 유지해야 하는 추가 작업이 필요

def binarySearch(arr, key):
    start = 0
    end = len(a)-1
    while start <= end :
        middle = (start + end)//2
        if arr[middle] == key : # 검색 성공
            return true
       	elif arr[middle] > key :
            end = middle -1
        else: start = middle + 1
    return false # 검색 실패
```

```python
# 재귀 함수를 이용한 구현
def binarySearch2(arr, low, high, key):
    if low > high : # 검색실패
        return False
    else :
        middle = (low + high) // 2
        if key == arr[middle]: # 검색 성공
            return True
        elif key < arr[middle]:
            return binarySearch2(arr, low, middle-1, key)
        elif arr[middle] < key:
            return binarySearch2(arr, middle+1, high, key)
```



### 인덱싱(Indexing)

**DB에서 유래한 용어로, 테이블에 대한 동작 속도를 높여주는 자료 구조**

> MySQL배울 때 배웠었던, Original Index 외에 특정 자료에 부여했던 ID Index 부분 참조할 것.

- DB 이외의 분야에선 Look up Table 등의 용어를 사용하기도 한다.
- 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블 저장에 필요한 공간보다 작다.
- how?  인덱스는 Key-Field만 갖고 있고, 테이블의 다른 세부 항목은 없기 때문.
- 대량 데이터의 성능 저하 문제 때문에, **배열 인덱스**를 사용하여 정렬한다.



### 셀렉션 알고리즘(Selection Algorithm)

> 시간복잡도 : O(kn)

**저장되어 있는 자료로부터 K번째로 큰 혹은 작은 원소를 찾는 방법**

- 최소값, 최대값 혹은 중간값을 찾는 알고리즘

**선택 과정**

1. 정렬 알고리즘 이용하여 자료 정렬
2. 원하는 순서에 있는 원소 가져오기

```python
# K번째로 작은 원소를 찾는 알고리즘
# 1번부터 k번째까지 작은 원소들을 작아 배열의 앞쪽으로 이동시키고, 배열의 k번째를 반환
# k가 비교적 작을 때 유용 O(kn)의 수행시간을 필요로 함

def select(list, k):
    for i in range(0, k) :
        minIndex = i
        for j in range(i+1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list[k-1]
```

