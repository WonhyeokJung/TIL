# 0204_Programmers_Python_완주하지못한선수

## 실패_1

```python
def solution(participant, completion):
    answer = ''
       
    for marathoner in participant:
        if not marathoner in completion:
            answer = marathoner
            break;
        if marathoner in completion:
            completion.remove(marathoner)
    return answer
```

### 의문점

- 정확성은 통과했으나, 효율성 면에서 엄청나게 떨어지는지 효율성을 아예 통과하지 못했다.
- 단순 for, if문의 중첩 문제는 아니라고 생각하는데, 아래는 결과적으로 통과했기 때문이다.
- sorted가 준 영향이 큰 듯 한데, sorting의 중요성이 따로 있는 지 의문이다.



## 내 해답

```python
def solution(participant, completion):
    answer = ''
    completion.append('z'*5)
    a = sorted(participant)
    b = sorted(completion)
    for i in range(len(a)):
        if a[i] != b[i]:
            answer = a[i]
            break
    
    return answer
```

### 풀이

- 답의 핵심 개념이 HASH에 있다는 의견을 들었다. for문 내에서 같은 이름을 2번 조회해 찾아야 한다면 효율성을 통과하지 못한다는 의견이었다.
- if문에서 성공시 브레이크문은 필수이다. 하지 않으면 아래 문장들을 계속 수행하는 모습을 발견할 수 있었다.

