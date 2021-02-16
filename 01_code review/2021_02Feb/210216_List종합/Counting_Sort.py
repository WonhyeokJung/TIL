A = [0, 4, 1, 3, 1, 2, 4, 1]  # 정렬 대상 배열
B = [0]*len(A)  # sorted A
C = []  # Counting Array

# 각기 다른 원소의 수
k = 5

# C는 각 원소의 개수만큼 카운팅을 하기 위해 사용한다.
C =[0]*k

# C에 각 Index번호와 일치하는 숫자들의 개수를 C[index]에 추가한다.
for i in range(len(A)):
    C[A[i]] += 1

print(C)  # [1,3,1,1,2]

# 그리고 각 항들을 누적합으로 바꿔준다
for i in range(1, len(C)):
    C[i] += C[i-1]

print(C)  # [1,4,5,6,8]

for i in range(len(A)-1, -1, -1):
    C[A[i]] -= 1
    B[C[A[i]]] = A[i]

print(B)  # 03_Algorithm의 설명을 참고할 것.
