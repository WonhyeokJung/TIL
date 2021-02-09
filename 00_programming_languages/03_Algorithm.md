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
  - 식: nPr = n\*(n-1)\*(n-2)\*...\*2\*1

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

