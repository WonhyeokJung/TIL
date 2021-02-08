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



# 배열

## 선언

- Arr = list()
- Arr = []

## 접근

- Arr[idx]

## 정렬

- 오름차순( Ascending. 작 > 큰)
- 내림차순(Descending)

**대표적인 정렬 방식**

1. 버블 정렬 (Bubble Sort)
2. 카운팅 정렬 (Counting Sort)
3. 선택 정렬 (Selection Sort)
4. 퀵 정렬 (Quick Sort)
5. 삽입 정렬 (Insertion Sort)
6. 병합 정렬 (Merge Sort)