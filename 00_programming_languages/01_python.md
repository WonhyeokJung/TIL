# Python

파이썬에 관하여 배운 것들을 정리하는 문서.

## 0. 스타일 가이드

사용자들끼리 정해둔 규약을 스타일 가이드라 하고, 이를 정리한다. 기본적으로 수업 내에서는 PEP - 8을 사용한다.

보통 기업들은 각자 자신의 스타일 가이드를 보유하고 있다.

- 실제 규약
  - 식별자(Identifiers) 짓기
    - 파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름(name)이다.
    - 최대한 의미를 포함할 수 있도록 명명한다.
    - 식별자의 이름은 영문 알파벳(대,소문자), 언더바, 숫자로 구성되고, 길이 제한은 없다.
    - 단어별 연결은 _(언더바)를 사용한다.
      - food_1
    - 사용 금지 키워드가 있다.(파이썬 문서 2.3.1참조)
    - 첫 글자에 숫자는 금지!
  - 등호 앞뒤는 스페이스바를 넣어준다.(확인해야함)
  - 코드 줄에 주석 입력시 `space` 2번 후 입력한다.
  - 함수명은 동사형으로(def get_food), ()가 있다./ 메서드명에는 .이 있다.(list.append). 즉, 메서드는 특정 객체에 종속되는 함수이다.
- 클래스 내 규약
  - Python은 ' " 둘다 문자에 사용이 가능하나, 클래스 내에서는 '을 우선적으로 사용하고, 필요한 경우 "를 사용하도록 한다.
    - = f" ~ ' ' " (fstring문 등)

## 1. 기본 주의사항

- 대소문자는 구별된다.
- 스펠링을 자주 체크한다.
- 1줄에 1문장(statement)가 원칙
- 파이썬은 기본적으로 ;를 작성하지 않는다. 한 줄에 여러 코드를 작성할 때는 가능하나, 기본적으로 그렇게 하지 않는다.
- 함수는 함수를 보기만 해도 내용을 알기 쉽게 `get_food_names`
- JAVA처럼 PACKAGE(폴더) 개념도 있음. `from java(패키지).x(패키지).weather_api import get_foods` 특정 폴더 내의 특정 값만 import 하겠다.

## 2. 명령어

명령어는 기본적으로, 내가 잘 안쓰거나 잘 모르는 내용 중 중요한 것만을 정리한다.

| 명령어          | 내용                                                | 예제            |
| --------------- | --------------------------------------------------- | --------------- |
| 문장 줄 구분    | 코드 줄을 여러줄 작성할 때                          | \               |
| hello\ \n world | """ """시, \n해도 이어짐                            |                 |
|                 | [] {} ()는 엔터없이 가능                            |                 |
| =               | 할당연산자(대입연산자)                              | 값대입          |
| type() / id()   | 타입 확인 / id값 확인                               |                 |
| *값 바꾸기      | x, y = y, x 파이썬 전용 !!                          |                 |
| e-n             | n자리까지 소수점으로                                | 314e-2          |
| del             | 내용 지우고, 그 전 저장 내용이 있으면 롤백한다.     | del print       |
| 0b / 0o / 0x    | 각 2, 8, 16 진수                                    | 0b10            |
| e/E-n           | 소수점 n째 자리가 있는 수로 만들기                  | 314E-2          |
| round(x, n)     | x n째 자리까지 반올림. 5는 경우에 따라 결과가 다름. | round(3.585, 2) |
| abs             | 절대값                                              | abs(3.3-3.62)   |
| is / is not     | 각 Object ID값 비교                                 | a is b          |
| ==              | 값 비교(ID값 아닌 그냥 '값' 비교)                   | a == b          |
| dir()           | 해당 함수에서 이용가능한 모든 메서드를 출력한다.    | dir(math)       |

## 3. 문법(Syntax)

### 0) 주석

- 한 줄 주석은 `#` 으로 표현
- 여러 줄의 주석은
  1. 한 줄씩 `#` 을 사용하거나,
  2. `"""` 또는 `'''` 으로 표현이 가능하다.

### 1) 변수와 리스트, 딕셔너리

1. Variable

   변수는 소문자로 정의하며, 우리가 임의로 명칭을 준 모든 값들이다. 값이 변할 가능성이 있는 상수를 변수로 지정한다.

2. List

   리스트는 배열(Array)의 일종이다. 타 언어와 달리 Python에서는 List로 명명한다.

   구조는 alphabets = [a, b, c] 이며, List임을 알기 쉽도록 변수명을 복수로 지정한다.

   배열과 같이, [0] 등을 통해 배열값을 얻어올 수 있다.

   ```python
   lunch = [
       '밥', '면',
       '빵'
   ]   ]  # 닫는 위치는 이 두 가지가 있지만, (1)방식을 사용.
   ```

   

3. Dictionary

   딕셔너리는 alphabet = {'a':'에이', 'b':'b', '씨':'씨' }로 지정되며 리스트와 달리 단수형으로 명명한다. 

   좌항을 Key값, 우항을 Value값이라 명명하며, Key값을 통해 Value값을 얻어올 수 있다.

   alphabet[Variable x]는 사용이 불가능 하며, ['Key값']을 입력해야만 출력이 가능하다.

### 2) Fstring

파이썬은 사용자 편의 구성이 많은데, fstring도 그 중 하나이다.

```python
fahrenheit = '35'
print("해당 도시의 현재 화씨는 :" + str(fahrenheit))
print(f"해당 도시의 현재 화씨는 : {fahrenheit}")
```



2번째 문장 구조로 계속 변수를 추가하여 문장을 출력하다 보면 작성이 귀찮고 보기 난잡해진다. 이럴때 이용하는 것이 fstring이다. 

fstring을 이용하면 f"내용" 구조로, 출력할 변수는 {변수명}로 입력하고 나머지 내용은 일반적인 문장 입력처럼 그대로 입력해주면 된다.

또한 f' f" 둘다 가능하며, f''' 이처럼 '를 3번 입력해줄 시 `enter` 입력도 가능하다.

* f' 처럼 싱글쿼터를 싱글로 사용시,  컴마(,) 뒤에 띄어쓰기를 필수로 해야한다.

### 3) 데이터&제어문

#### (1)기초 문법

- 주석(Comment)
  - 

## 4. 문법

강의 순서에 기초한 문법을 바탕으로, 모든 문법 중 기초적으로 이미 습득한 문법 혹은 이론은 제외하고, **"내가 헷갈리는"** 문법만을 집중적으로 정리한다.

### 0) 정리예시

### 1) 코드 라인

- 1줄에 1문장
- `;` 사용 가능하나 기본적으로 안쓴다. 한 줄 표기 시 이론적으로는 사용 가능.
- 여러 줄 작성시, `\`  / `""" """`  사용 가능하며 후자가  정석이다.
- `[] {} ()`  은 `\` 없어도 가능하다.

### 2) 변수(Variable)

- x, y , z = 1, 2, 3 처럼 나열도 가능. but 양변 항수가 같아야 한다.
- **서로 값을 바꾸고 싶을 경우, x, y = y, x 로 가능.**
- 임시변수 temp = x 저장 후, y, x 순으로 바꾸는 것도 가능하다.

### 3) 식별자(Identifiers)

- 변수명, 함수명등 우리가 지정한 임의의 이름을 식별자라고 한다.

- 첫 글자에 숫자 금지
- **내장 함수에 사용 가능하나, 사용시 그 기능이 사라지므로 주의한다!**
- 대소문자 구별

### 4) 데이터 타입(Data Type)

#### Number

##### Integer

- 정수(integer) / long type은 3.x 부터는 없어짐
- 8진수는 `0o` 2진수는 `0b` 16진수는 `0x` 로도 표현 가능. eg. 0x16 == 16진수인 16

##### float

- 부동소수점.실수(float)
- 소숫점을 포함하거나, e를 포함.
- e/E도 사용가능. eg. pi = 314e-2 -> 3.14
- 부동소수점 처리 `abs(0.38-0.23) <= 1e-10 #정말 작은 수보다 더 작은 지 T/F 판단`
- 혹은  `import math \ math.isclose(a, b) 연산값과 기대값이 가까운가로 확인`
- 0 출력하고 싶을시 `%.4f` 를 이용하도록 한다.

##### complex

- 복소수. 허수부를 j로 표현한다.
- a = 3 - 4j

| 명령어       | 설명                               | 예제          |
| ------------ | ---------------------------------- | ------------- |
| .real        | 실수부 출력                        | a.real        |
| .imag        | 허수부 출력                        | a.imag        |
| .conjugate() | 켤레복소수 출력                    | a.conjugate() |
| abs()        | 절대값 리턴(int, float에서도 가능) | abs(a)        |



#### String

- Single quotes / Double quotes 로 표현
- `'` `"` 혹은 `'''` `"""`  가능. 후자는 특수한 경우 사용(엔터값 필요하거나 등등)
- `PEP-8` 에 따르면 **Pick a rule and Stick to it. 하나의 문장부호를 선택 유지하도록 권장**
- 문자열 내 문장부호는 `\"` `\'` 등으로 사용
- '하이'+'안녕' `하이안녕`  'hi'*3 + 'hong' `hihihi hong` 

##### Escape Sequence

| 예약문자 | 내용(의미) |예약문자 | 내용(의미) |
| -------- | ---------- | -------- | -------- |
| \n       | 줄바꿈 |\t|탭(4pt)|
| \r | 캐리지 리턴 |\0|널(Null)|
| \\\ | \ |\\'|단일인용부호(작은따옴표)|
| \\" | 이중인용부호(큰따옴표) |\\\n|\n 그대로 출력.|

##### String interpolation

- 문자열에 변수값 넣는 방법

| 종류       | 설명                           | 예제                                        |
| ---------- | ------------------------------ | ------------------------------------------- |
| formatting | 문자열 내에 값을 치환하는 방법 | a = apple ('나는 %s을 먹었다.' % a)         |
|            | %s %c %d %f %o %x              | 문자열 / char / 정수 / float / 8진 /16진수  |
|            | %0.4f                          | 소수점 네자리 까지 **0도 출력함.**          |
| f-string   | f'{}' 문장 내 변수만 {}로 묶기 | print(f'Hello, {name}') `f''' '''` 도 가능. |

- 출력 형식 지정뿐만 아니라, 연산도 가능하다.
- eg. `pi = 3.141592 / f'원주율은 {pi:.4}`

#### Boolean

- True = 1/ False = 0
- `0, 0.0, (), {}, [], '', None` 은 전부 **False**. 이외는 전부 True이다.
- `None` 타입 == 값이 없음을 의미. # 앞으로 '없다'로 표현.

### 5) 형변환

#### 암시적 형 변환(Implicit Type Conversion)

- 자동으로 이뤄지는 형 변환
- boolean, int, float, complex 사이에서만 자동적으로 가능하다.

#### 명시적 형 변환(Explicit Type Conversion)

- 직접 해줘야 하는 형 변환

- 숫자형 String -> int, float, list, tuple, dict로가 기본 과정

- **String '3.5' -> int로 불가능함에 유의**

  

### 6) 연산자(Operator)

#### 산술 연산자

| 연산자 | 내용     | 연산자 | 내용   |
| ------ | -------- | ------ | ------ |
| +      | 덧셈     | -      | 뺄셈   |
| *      | 곱셈     | /      | 나눗셈 |
| //     | 몫       | %      | 나머지 |
| **     | 거듭제곱 |        |        |

- 나눗셈( / )은 항상 float를 반환
- 몫과 나머지 동시에 얻으려면 : quotient, remainder = divmod(5, 2) == 5/2

#### 비교 연산자

| 연산자 | 내용           | 연산자 | 내용    | 연산자 | 내용     |
| ------ | -------------- | ------ | ------- | ------ | -------- |
| <      | 미만           | <=     | 이하    | >      | 초과     |
| >=     | 이상           | ==     | 같음    | !=     | 같지않음 |
| is     | 객체아이덴티티 | is not | 부정된~ | is     | id값비교 |

#### 논리 연산자

| 연산자  | 내용                            |
| ------- | ------------------------------- |
| a and b | a와 b 모두 True시에 True 반환   |
| a or b  | a와 b 모두 False시만 False 반환 |
| not a   | True -> False, False -> True    |

`&`, `|` 는 파이썬에선 `비트연산자`

##### **단축평가**

- 첫 번째 값이 확실하고, 반환값이 True임이 확실하면 연산을 멈춘다.

- 속도 향상이 가능하나, 값의 정확도가 떨어질 수 있음.

- eg. `'a' and 'b' and '' and 'd'`   > `''` 반환.

- `('a' or 'b') in vowels` > `True` 'a'에서 연산 끝내고 모음(vowels)에 있는 지 확인하니까.

- ①('a' or 'b') 시행 후 결과값 > 'a' ② in vowels 시행

  ```python
  print(3 or 5)
  print(3 or 0)  # 앞이 트루니 앞만 봄
  print(0 or 3)  # 끝까지 봄. 앞이 false니까
  print(0 or 0)  # 3 3 3 0
  ```

#### 복합연산자

- 파이썬은 a++ / ++a **불가능**

| 연산자  | 내용    | 연산자 | 내용    | 연산자  | 내용    | 연산자 | 내용    |
| ------- | ------- | ------ | ------- | ------- | ------- | ------ | ------- |
| a += b  | a = a+b | a -= b | a = a-b | a *= b  | a = a*b | a /= b | a = a/b |
| a //= b |         | a %= b |         | a **= b |         |        |         |

#### 기타 주요 연산자

##### Concatenation ( 병합)

- 자료형은 `+` 로 합치기 가능 : 'abc' + 'efg' = 'abcefg'
- [1,2,3] + [4,5,6] = [1,2,3,4,5,6]

##### Containment Test

- `in` 연산자 이용, 요소 여부 확인 가능
- eg. `a` in `apple` = True
- 1 in [1,2,3] = True
- 1 in range(1,5) = True

##### Identity

- `is`연산자를 통해 동일 Object(객체)인지 확인 가능 > ID값 비교 연산

  ```python
  a = 'hi'
  b = 'hi'
  print(a is b)
  print(id(a), id(b))
  ```

##### Indexing/Slicing(인덱싱/슬라이싱)

- Indexing : 인덱스로 찾기. ([0],[1], ...)
- Slicing : 범위 잘라내기

#### 연산자 우선순위

0.  `()`을 통한 grouping
1. Slicing
2. Indexing
3. 제곱연산자 `**`
4. 단항연산자 `+`, `-` (음수/양수 부호)
5. 산술연산자 `*`, `/`, `%`
6. 산술연산자 `+`, `-`
7. 비교연산자, `in`, `is``
8. ``not`
9. and
10. ``or`

```python
-3 ** 6 # -729. - 연산자가 제일 마지막
```

### 7) 문장과 표현식

#### 표현식(Expression)

- 표현식 > `evaluate` > 값
- 하나의 값으로 환원될 수 있는 문장. `식별자` `값(리터럴)` `연산자`의 구성
- 하나의 값도 표현식이 가능 eg. 'hello'

#### 문장(Statement)

- 파이썬이 실행 가능한 최소한의 코드 단위
- 'hello'는 문장으로도 가능. 
- Statement includes Expression
- `greeting = 'Bye' + '!' * 3` 문장 | `'Bye' + '!' * 3` 표현식



### 8) 컨테이너(Container)

- 여러 개의 값을 저장할 수 있는 것. 
- 모두 명사형으로 정의함.

#### Sequence형 컨테이너

- `List` `Tuple` `Range` `String` `Binary`
- 데이터가 순서대로 나열된 것
- **Sorted(정렬됨)** 의미하지 않음에 주의!!!
- 순서를 가질 수 있음
- Index 접근 가능

##### List

- 선언방식

  1. a = []

  2. a = list()

  3. ```python
     a = [
         '김밥',
         '라면'
     ]
     ```

  4. **For문 이용**

     ```python
     # 자료를 따오고자 할 때
     temp = [0,1,2,3,4,5,6,8,7]
     test = []
     for i in range(len(temp)):
         test += [temp[i]]
     
     print(test)
     # 그대로 카피함.
     ```

- 특정 원소의 수정, 읽기가 가능하다.

###### List의 복사 (mutable의 복사)

- List, Dict, Set

> ```python
> import copy
> a = [1, 2, 3]
> # 같은 주소값
> b = a # 같은 주소값 참조로 값 변경시 같이 변함
> # 다른 주소값(새로생성)
> b = a[:] # Slice 연산자
> c = list(a) # list() 활용. 
> d = copy.copy(a)
> ```

- Mutable은 이처럼 같은 주소값을 참조하여 값이 같이 변한다.

###### Swallow Copy(얕은 복사) vs Deep Copy(깊은 복사)

- 위의 것은 얕은 복사였다. 2차원 배열의 경우 2차원 값은 여전히 같은 주소값을 참조하기 때문이다.

> ```python
> a =[[1, 2, 3], 2, 3]
> b = list(a)
> b = a
> print(a, b)
> b[0][0] = 100
> print(a, b) # 둘 다 [[100, 2, 3], 2, 3]
> b[1] = '원소'
> print(a, b) # 둘 다 [1]값 '원소'로. 2차원배열이 속해 있어 주소값이 둘은 여전히 같다..
> ```

- deepcopy() 메서드를 사용하여 분리할 수 있다.

```python
import copy
a = [[1,2,3],2,3]
b = copy.deepcopy(a) # 이거 사용 해야함
print(a,b)
b[0][0] = 100
print(a, b)
# [[1, 2, 3], 2, 3] [[100, 2, 3], 2, 3]
```



###### 그렇다면, String의 복사는? (Immutable의 복사)

- Number, String, Boolean, Range(), Tuple(), Frozenset()

> ```python
> # 값 변경이 불가능. 서로 다른 값을 출력. 주소값 역시 다름.
> a = '안녕하세요'
> b = a # 주소값이 같았으나,
> b = 10 # 주소값이 다시 달라져버려
> print(a) # '안녕하세요'
> print(b) # 10
> print(id(a))
> print(id(b))
> ```





##### Tuple

- 선언방식

  1. a = (1, 2) / 소괄호는 생략가능 a = 1, 2
  2. 사실 모든 원소는 Tuple 형태로 이루어져 있음.

  ```python
  x, y = 1, 2 // # tuple
  # 둘이 값을 바꾸고 싶을 때
  x, y = y, x
  ```

  3. 빈 튜플의 생성도 가능 / a =()

  4. ```python
     #값이 하나라면 tuple로 출력이 불가능하므로
     tuple = (1,) # 이와 같이 선언해 줍니다.
     ```

- 특정 원소의 수정 불가. 읽기는 가능

##### Range

- 기본적으로 길이 읽기 용임.

##### String

- 문자열

##### Binary

| 이름  | 선언방식                                                     | 상세                |
| ----- | ------------------------------------------------------------ | ------------------- |
| List  | lunches = ['만두전골', '밥'] `x=[]`  / 특정 원소 수정 가능   | literal 생성        |
|       | l1 = list() ``x=list()` / Index는 [0]부터 시작한다.          | 표준생성            |
| Tuple | List와 유사. `()` 로 표현. 특정 원소 수정 불가능. 재선언 필수. | 불변(Immutable)     |
|       | 하나의 항목인 튜플은 값에 쉼표를 붙여 표현한다.              | tuple = ('hello', ) |
|       | Tuple과 List는 Indexing은 가능하다. tuple[0] = 'a' 등 수정은 불가능. | print(tuple[0])     |
| Range | 숫자의 시퀀스 나타내기 위해 사용. `range(n, m, s)` n부터 m-1까지 | s만큼 증가          |
|       | `range(n)` 0부터 n-1까지. `range(n, m)` n부터 m-1까지        |                     |
|       | list로 출력가능. `list(range(3))` 출력시,  `[0,1,2]`         |                     |
|       | `[range(3)]` 시, 'range(3)'이라는 str원소를 넣는것이다. range의 원소X |                     |

##### 시퀀스에서 활용 가능한 연산자/함수

| Operation    | 설명                                                         | 결과 타입    |
| ------------ | ------------------------------------------------------------ | ------------ |
| x `in` s     | containtment test                                            | Boolean      |
| x `not in` s | 인자 포함 여부 테스트                                        | Boolean      |
| s1 `+` s2    | concatenation(병합)   **list, tuple 항끼리 덧셈 아님에 주의!!** | s1s2         |
| s `*` n      | n번만큼 반복하여 합치기 `[0] * 6 : 0이 6개인 list`           | sssssssss(n) |
| s[i]         | Indexing                                                     | s[0]         |
| s[i:j]       | slicing(잘라내기). i번 인덱스부터 j-1번 인덱스까지           | s[0:3]       |
| s[i:j:k]     | k간격으로 slicing. # j 생략시 끝까지 의미                    | s[1:10:3]    |
| min(s)       | 최소값  `a=[1,2,3] min(a) = 1`                               |              |
| max(s)       | 최대값  `a=[1,2,3] max(a) = 3`                               |              |
| s.count(x)   | x의 개수 `a = [1, 1, 1, 2] a.count(1) = 3`                   |              |



#### Non-Sequence형 컨테이너

- `Set` `Dictionary` (중괄호팀)
- 비시퀀스형 컨테이너는 인덱스의 순서를 보장하지 않는다.
- 자료 순서가 멋대로 튀어나올 수 있으므로 항상 유의한다.

##### Set

- 선언방식
  1. set = {}는 불가능! ( dict화됨)
  2. set = {1,2,3}
  3. set = set() 빈 괄호로 만들고 싶을떄

##### Dictionary

- 선언방식
  1. a = {}
  2. a = dict()
- **KEY값**은 변경이 불가능하다(**Immutable**만 올수 있음)
- value값은 List, Dict 다 들어갈 수 있다.

| 이름      | 선언방식                                                     | 상세          |
| --------- | ------------------------------------------------------------ | ------------- |
| Set       | `set_a = {1}` 수학의 집합과 동일하게 처리. 빈 집합은  {}아닌 `set()`로 선언함 | set ={1,2,3}  |
|           | **비어있는 중괄호{}는 DICT로 정의하기로 약속했기 때문**      |               |
|           | **중복값을 가질 수 없고, 순서도 없다.**  List의 중복값을 제거 후, 다시 List로 가능. | set(list_a)   |
|           | `set(list_a)  list(set(list_a))`                             |               |
| 차집합    | set_a - set_b                                                | minus         |
| 합집합    | set_a \| set_b                                               | or            |
| 교집합    | set_a & set_b                                                | and           |
| Dict      | Dictionary. `dict()` 혹은 `dict = {}`로 선언. Key와 Value의 형태로 구성. | dict{'a':'1'} |
|           |                                                              |               |
| Key값     | Key값은 **변경 불가능(immutable)한 데이터**만(str, int, float, bool, tuple, range) |               |
|           | Key값은 중복이 불가능함. 같은 Key 값 존재시 value를 최신 것이 덮어써 출력. |               |
|           | 접근 역시 index가 아닌 Key값으로 접근. **찾기는 대괄호에 주의** | dict['서울']  |
| value값   | list, dictionary 포함한 모든 것이 가능                       |               |
|           | 비어있는 중괄호 dict = {}는 빈 dict이다.                     |               |
| .keys()   | 키 값들 확인                                                 | dict.keys()   |
| .values() | 밸류 값들 확인`p_values = phone.values() / print(list(p_values))` | dict.values() |
| .items()  | 키와 밸류값 전부 확인.                                       |               |
| .clear()  | 키, 밸류값 전부 지우고 빈 딕셔너리만 남김.                   | dict.clear()  |
| in        | 딕셔너리 안의 값 조회 가능 if '배' in dict: print(~)         | a in dict     |

```python
for (k, v) in phone.items():
    print(k, v)
phone.items()
```

#### 컨테이너형의 형변환

<img src="https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png" alt="typecasting" style="zoom:50%;" />

- Dict는 Key : Value 구조 때문에 어떤 형태에서도 변환이 불가능

- Dict는 Key로 value값에 접근이 가능하여, Dict를 형변환시 Key값을 받아오게 구조되어 있음.

- Range 역시 구조상 다른 형태에서 Range로의 형변환은 불가능

  | 기본형       | String         | List      | Tuple     | Range | set       | dictionary |
  | ------------ | -------------- | --------- | --------- | ----- | --------- | ---------- |
  | 'ab'         | X              | ['a','b'] | ('a','b') | X     | {'a','b'} | X          |
  | [1,2,3]      | '[1,2,3]'      | X         | (1,2,3)   | X     | {1,2,3}   | X          |
  | (1,2,3)      | '(1,2,3)'      | [1,2,3]   | X         | X     | {1,2,3}   | X          |
  | r=range(1,3) | 'r=range(1,3)' | [1,2]     | (1,2)     | X     | {1,2}     | X          |
  | {1,2,3}      |                |           |           | X     | X         | X          |
  | {'a':1}      | "{'a':1}"      | ['a']     | ('a')     | X     | {'a'}     | X          |

### 9) 데이터의 분류

#### immutable(변경 불가능한) 데이터

- immutable 데이터는 데이터 수정이 아닌, **재선언만** 가능하다. 특정 원소의 변경은 **불가능**
- **각자 자기값**을 가짐

```python
num1 = 20
num2 = num1 # 주소값을 참조하지 않음. 그냥 값 자체를 받아옴.
num2 = 10
print(num1, num2)
result : 20, 10
num1값이 바뀌지 않음!
```

- 리터럴(literal)
  - 숫자(Number)
  - 글자(String)
  - 참/거짓(Boolean)
- range()
- tuple()
- frozenset()

#### mutable(변경 가능한) 데이터

- 대괄호, 중괄호 친구들. 특정 원소의 변경이 가능.
- **같은 주소값을 참조하는 게 가능하다. 특정 원소 수정시 같이 변화함.**

```python
num1 = [1,2,3,4]
num2 = num1 # 주소값을 참조함.
#같은 List를 참조해서, 공간 자체가 마치 주소값처럼 움직임.
num2[0] = 100
print(num1, num2)
result: [100, 2, 3, 4] [100, 2, 3, 4]
```

- list []
- dictionary {a:b}
- set {}

<img src="https://user-images.githubusercontent.com/18046097/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png" alt="container"  />

### 10) 조건문(Conditional Statement, IF)

- True/False를 판단할 수 있는 조건과 함께 사용이 필수이다.
- PEP 8에서는 4spaces를 권장하고, 일반적으로 `tab`이 4spaces를 보장한다.

```python
if <expression>:
    <code block>
elif <expression>: # else if. 선택적으로 사용 가능하다.
else: # 역시 선택적으로 사용가능하다.
    <code block>
    
if a>0:
    print('양수입니다.')
else:
    print('음수입니다.')
```

```python
# 참고
if num%2:  # 홀수를 의미함. 0 = False / 1 = True이므로 홀수일시, True값을 반환.
```

```python
# 중첩 조건문
if score >= 90:
    print('A')
    if score >=95:
        print('참잘했어요.')
```

#### 삼항연산자(= 조건표현식)

- IF~ELSE문을 한줄로 구성할 수 있는 방법이다.

```python
# 실행문 if문 else문 구조
# true_value if <expression> else false_value
print('0보다 큼') if a > 0 else print('0보다 크지 않음')
```

#### if not x: x가 false일때, if문을 실행

```python
a = []
if not a:
    # 이 경우 if문은 실행될까?
    # 실행된다. [] 빈 list는 false값을 출력하니까!
```





### 11) 반복문(Loop Statement, FOR & WHILE)

#### While문

- 반드시 종료조건 설정이 필수이다.

- 보통 코드 구성은 이와 같다.

  ```python
  a = 0 # for문과 달리 외부 변수설정이 필요한 경우가 99%다.
  while a < 5:
      print(a)
      a += 1 # 이 코드가 없다면 무한루프에 빠지게 된다.
  ```

  ```python
  message = ''
  while message != '안녕':
      print('안녕이라고 할 때까지 보내주지 않을 거에요.')
      meesage  = input("'안녕'을 입력해주세요 : ")
  print('안녕하세요')
  ```

  ```python
  num = int(input())
  i = 0
  j = 0
  while i < num:
      i += 1
      j += i
  print(j)
  
  # 합을 구할 때도 인자가 두개 필요하다.
  ```

  

#### For문

- for <임시변수> in <순회가능한데이터(iterable)>: 

  ​	<코드블럭>

  ```python
  #
  for num in [1, 2, 3, 4, 5]:
      print(num)
  print('끝')
  ```

  ```python
  # range(10) => 0~9 처음부터 끝까지 다 털어옴
  for i in range(10):
      # i = 하나씩 꺼내서 i에 저장중
      print(i)
  ```

  ```python
  nums = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 11]
  j = 0
  for i in range(1,11):
      j = i + j
  print(j)
  
  k = 1
  for i in range(1, 11):
      k = i*k
  print(k)
  ```

```python
# 이처럼 list의 index도 활용가능
lunch = ['짜장면', '초밥', '피자', '햄버거']
for idx in range(len(lunch)): # idx = index
# print(idx) 전체길이를 0부터 4까지 하나씩. range를 index통으로 만들어서 사용.
    print(idx+1, lunch[idx])
```

##### enumerate() 내장 함수

- enumerate() 내장 함수를 활용시, 추가적인 변수 활용 가능

```python
# enumerate()를 활용해서 출력해봅시다.
lunch = ['짜장면', '초밥', '피자', '햄버거']
enumerate(lunch) # 주소값으로 어딘가 저장
list(enumerate(lunch)) # 인덱스와 값을 튜플로 정렬해줌. 인덱스 , 값 둘이 같이 필요할때만! 씀

#출력값
# [(0, '짜장면'), (1, '초밥'), (2, '피자'), (3, '햄버거')]
# Tuple로 반환
```

```python
for idx, menu in enumerate(lunch): # 값이 항상 2개임에 유의
    print(idx, menu)
    
# 출력값
#0 짜장면
#1 초밥
#2 피자
#3 햄버거
```

#### 반복제어

##### break

- `for`나 `while`문에서 탈출한다. java와같이 하나 위를 탈출함.

  ```python
  numbers = range(1, 100001)
  user_input = int(input('십만 이하의 숫자를 입력하세요 : '))
  
  # 사용자 입력정수가 numbers에 있다면, True 출력/아니면 False 출력
  while True:
      if user_input in numbers:
          print('True')
          break # if문 바깥의 while문을 탈출함
      else:
          print('False')
          break
  else: # 여기 위치한다면 break가 필요가 없음.
      print('False')
  
  for number in numbers:
      if user_input == number:
          print('True')
          break  # 끝까지 더 찾으면서 Resource 찾을 필요가 없으니까
      else:
          print('False')
          break
          
  numbers = [1, 27, 2, 3, 5, 19]
  target = 10000
  idx = 0
  flag = False
  while idx < len(numbers):
      if target == numbers[idx]:
          flag =True
          break
      idx += 1
  ```

##### Continue

- 한 번의 수행을 건너뜀

  ```python
  for i in range(6):
      if i % 2 == 0:
          continue # 이번 회차는 생략(한단계 위의 것을 생략. 여기선 for문). 다음 회차로 JUMP함 
      print(i)
  ```

  

##### else

- 반복문을 끝까지 시행하고 실행됨 (반복문 바깥에 있을 시. 바깥에 있으니까 당연히)

- but 반복문이 `break`문으로 종료될때는 **실행되지 않는다.**

  ```python
  numbers = range(1, 100001)
  user_input = int(input('십만 이하의 숫자를 입력하세요 : '))
  
  # 사용자 입력정수가 numbers에 있다면, True 출력/아니면 False 출력
  while True:
      if user_input in numbers:
          print('True')
          break
  
  else:
      print('False')
  ```

  

##### Pass

- 아무 것도 하지 않음.
- function을 만들어두고, 기능을 나중에 추가하고자 할때 보통 활용.

### 12) 함수(Function)

- 함수란 특정한 기능을 하는 코드의 묶음으로, 코드의 기능별 분화로 유지보수에 좋다.
- 함수의 지역변수(Local valuable) 값은 JAVA와 같이, 함수 내에서만(지역 내에서만) 사용 가능하다.
- 함수도 하나의 '값'이란 사실을 잊지 않는다. 다만 **우리가 길게 정의한 값**일 뿐이다.

#### 함수의 선언

```python
def func(x, y):
    <code block>
    return value  # 결과값 전달. return값이 없다면, None 반환.
```

#### 함수의 호출

- `func()` / `func(val1, val2)`와 같이 한다.

#### 함수 예시

```python
# 주어진 수의 세제곱
def cube(n):
    result = n**3
    return result # return값이 없으면 none반환. return 잊지 말 것!
```

```python
# 사각형의 넓이
def rectangle(i, j):
    result = i*j
    return result
```

#### 내장함수

- built-in function

  - 30가지가 있으며, python 문서에서 찾아볼 수 있다.
  - https://docs.python.org/ko/3/library/functions.html

- ```python
  dir(print) # 처럼 검색을 통해 내장함수에서 사용 가능한 메서드도 검색이 가능하다.
  ```



#### 함수의 Output

##### return

- 오직 **한 개**의 객체만 반환.

  ```python
  return (a+b) # 가능(연산자로 결합이 가능하다면 하나로 반환 가능)
  return a, b, c # 가능. 하나의 'Tuple'로 immutable한 객체를 반환
  ```

##### sort(정렬)

- sort에는 2가지 종류가 있음. **변수명.sort() / sorted(변수명)**
- **sorted**는 tuple도 가능. 완전히 새로운 변수를 만들어서 Return 즉, **함수**
- a.sort()는 tuple은 불가능. 값을 변경하여 정렬하는 메서드이기 때문.
- **메서드**에는 값변경, 값창출 두 가지 종류가 있고, 각각마다 다르므로 확인이 필수이다.



#### 함수의 Input

##### 매개변수(Parameter) & 인자(argument)

###### 매개변수(Parameter)

- ```python
  def func(x):
      return x + 2
  ```

- x가 parameter(매개변수)이다.

- 입력을 받아 함수 내부에서 활용할 `변수`라고 생각하면 된다.

###### 전달인자(argument)

```python
func(2)
```

- 여기서 2는 전달인자이다.
- 함수 호출자가 입력한 `입력값`이라 보면 된다.
- 함수 호출시 주로 볼 수 있다.



##### 함수의 인자

###### 위치인자(positional Argument)

- 함수는 기본적으로 인자를 위치로 판단한다.

- 따라서 인자 순서에 맞게 입력하는 것이 중요하다.

  ```python
  def (width, height)
  # 넓이, 높이 순으로 입력 안하면 잘못된 결과가 출력된다.
  ```

###### 기본 인자 값(Default Argument Values) / 함수 선언시 이용

- 기본 인자 값(디폴트 인자 값)도 입력이 가능하다

  ```python
  def greeting(name = '익명'):
      print(f'{name}, 안녕?')
      
  # 호출시 인자 입력없이 greeting() 으로 호출하면 익명이 출력된다.
  # 인자값을 입력시, 평소 함수랑 똑같이 출력되고, 안하면 디폴트 값으로 출력된다.
  ```

- Default 인자 다음에, 위치인자가 자리할 수는 없다.

  ```python
  def greeting(name = '익명', age): # ERROR. age에 디폴트 설정하지 않으면 불가능
  ```



###### 키워드 인자(Keyword Arguments)  / 함수 호출시 이용

- 키워드 인자는 직접 변수의 이름으로 특정 인자의 전달이 가능

  ```python
  def greeting(age, name='익명'):
      print(f'안녕, 난 {name} {age}살이야')
  ```

- 하지만, 디폴트 인자처럼 **키워드인자** 뒤에 **위치 인자** 활용은 불가능하다.(기본인자값과 원리 비슷!!)

- 위치인자의 의미가 없어지기 때문이다.

```python
greeting(name='곰', age='30') # 가능. 전부 명확히 기재해 줘서. (뒤에 위치 인자가 없으니까)

# 불가능. 위치 바꿔서
greeting(name = '곰', 30): 
# 키워드 인자 활용시, 위치 인자를 이어 사용은 불가능하다. but 반대로는 가능!
# 가능. 순서를 명확히 지켜서
greeting(30, '곰')
```

| 인자명( = 사용자가 매개변수에 입력한 값) | 형태                 | 활용                           |
| ---------------------------------------- | -------------------- | ------------------------------ |
| 위치인자                                 | (30, '홍길동' ..)    |                                |
| 디폴트 인자 / def abc(a = '가'):         | ()입력X / ('홍길동') | 함수 선언시 뒤에 위치인자 못옴 |
| 키워드 인자                              | (abc = '나다')       | 함수 호출시 뒤에 위치인자 못옴 |

##### 가변(임의) 인자 리스트(Arbitary Argument Lists)

###### *args

- 임의의 개수의 인자를 받을 것임을 뜻하며,

- 반환은 **TUPLE**로 반환된다.

- *은 반드시 입력해야하고, args 부분은 원하는 매개변수명을 줄 수 있다.

- 보통 매개변수 목록`func(a, b, *c)`의 마지막에 온다.

  ```python
  # 전달받은 모든 학생을 출력하고 싶다..
  def students(*args):
      for student in args:
          print(student)
  ##### 입력
  students('희은', '대영', '태성')
  print('---')
  students('희은', '대영', '상진', '국현')
  ##### 결과
  희은
  대영
  태성
  ---
  희은
  대영
  상진
  국현
  ```

  ```python
  def students(*args, prof):
      for student in args:
          print(student)
      print(f'존경하는 교수님 {prof}')
  #####
  #가변 인수 이후의 변수는 직접 키워드 인자로 활용. 위치 보장이 안되므로
  students('희은', '태영', prof = '탁희')
  ```

- 가변인수 이후의 변수 입력은 직접 **키워드 인자** 활용이 필수이다. 위치 보장이 안되기 때문

- 하지만 반대라면, 위치가 보장되니 키워드 인자는 불필요하다.

##### 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

###### **kwargs

- 임의의 개수의 키워드 인자(a = 'b')를 받을 것을 의미하며,

- 반환은 **dict**로 반환된다.

- **은 입력 필수, kwargs는 원하는 매개변수명

  ```python
  # 딕셔너리 생성 함수 예시(가변 키워드 인자)
  # dict()가 사실은 함수였음을 알 수 있다.
  dict(name='홍길동', age='1000')
  #####출력문
  {'name': '홍길동', 'age': '1000'}
  ```

- 식별자는 숫자만으로 쓰일 수 없다.

  ```python
  # 주의사항
  # 식별자는 숫자만으로는 이루어질 수가 없다.(키워드인자로 넘기면 함수 안에서 식별자로 쓰이기 때문)
  dict(1='1', 2='2')
  
  # 위의 경우 다음과 같이 사용해야 한다.
  dict(((1, 1), (2, 1)))
  ```

###### URL 생성 예시

```python
# 입력받은 가변 키워드 인자를 활용하여 'https://api.go.kr?'를 BASE_URL로한 URL을 생성하시오.
def my_url(**kwargs): # keywordarguments
    url = 'https://api.go.kr?'
    print(kwargs.items(), type(kwargs.items()))
    for name, value in kwargs.items(): # kwargs 딕셔너리 안에 name, value 값이 있다면
        url += f'{name}={value}&'
    return url
#######입력값
my_url(sidoname='서울', key='asdf')
###### 출력값
dict_items([('sidoname', '서울'), ('key', 'asdf')]) <class 'dict_items'>
'https://api.go.kr?sidoname=서울&key=asdf&'
```



#### 함수와 스코프(Function and Scope)

##### 스코프(Scope)

- 스코프는 범위의 정의이고, 지역 스코프
- 파이썬은 JAVA와 달리, for / while문 등 반복문에선 스코프가 적용되지 않고,
- **오직 함수에서만 Scope가 적용된다**

- **전역 스코프(`global scope`)**: 코드 어디에서든 참조할 수 있는 공간
- **지역 스코프(`local scope`)**: 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간

- **전역 변수(`global variable`)**: 전역 스코프에 정의된 변수
- **지역 변수(`local variable`)**: 로컬 스코프에 정의된 변수

- 함수 내부의 변수는 함수 내부에서만 값이 작동하며, 함수 외부에는 영향을 주지 못한다.



##### 이름 검색 규칙(Resolution, LEGB Rule)

- `L`ocal scope: 정의된 함수

- `E`nclosing scope: 상위 함수 (어떤 함수를 감싼 함수)

- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈

- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

- 이름 검색 규칙은 스코프 원리와 같다.

- 본인 위치에서부터 이름 찾기를 수행하고(하나씩 아래로), 이름을 찾아내면 그 이후로는 찾지 않고 탈출함.

- 예시

  ```python
  print = ssafy
  print('abc') # 더이상 작동안됨
  # `Built-in` 함수를 내 멋대로 `Global`에서 정의했기 때문
  del(print)
  #시 다시 한단계 아래의 Built-in이 활성화 되어 정상 사용 가능
  ```

  1. `print()` 코드가 실행되면
  2. 함수에서 실행된 코드가 아니기 때문에 `L`, `E` 를 건너 뛰고,
  3. `print`라는 식별자를 Global scope에서 찾아서 `print = ssafy`를 가져오고,

  4. 이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 내뱉게 됩니다.

  5. 우리가 원하는 `print()`은 Built-in scope에 있기 때문입니다.

##### 변수의 수명주기

- **빌트인 스코프`(built-in scope)`**: 파이썬이 실행된 이후부터 영원히 유지

- **전역 스코프`(global scope)`**: 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 인터프리터가 끝날때 까지 유지

- **지역(함수) 스코프`(local scope)`**: 함수가 호출될 때 생성되고, 함수가 가 종료될 때까지 유지 (함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됨)



#### 재귀함수

- 자기 자신을 호출하는 함수

- 비효율적이나(반복문보다 시간이 훨씬 많이 걸림) , 코드의 간결화를 꾀할 수 있다.

- `base case` 의 존재가 필수이다. 안그러면 탈출하기 어렵기 때문.

  ```python
  # base case는 보통 if n ==1: return 1 등으로 정의된다.
  ```

  

```python
def sum_n(n):
    # 1~n까지 더하는 코드를 작성하세요
    #base code
    if n == 1:
        return 1 # n이 1이면 계속 sum_n(n-1) 주던걸 마무리하고 1을 내보내 함수를 종료한다.
    else:
        return n + sum_n(n-1) # 자기 자신을 호출하는 함수
print(sum_n(20))
```

```python
print('각 자리의 숫자 하나하나를 더한 값을 구해주는 함수입니다.')
a = input("숫자를 입력해주세요 :")
def sum_str_recur(string):
    n = len(string)
    if n == 1:
        return int(string[0]);
    else:
        return int(string[n-1]) + sum_str_recur(string[0:n-1])
    	#return int(string)//10) + sum_str_recur(string[0:n-1])
print(sum_str_recur(a))
```



##### 최대재귀깊이

- 자기 자신을 호출하는 재귀함수는 알고리즘 구현시 많이 사용된다.
- 코드가 더 직관적이고 이해하기 쉬운 경우가 있다.
- 팩토리얼 재귀함수를 [Python Tutor](https://goo.gl/k1hQYz)에서 확인해보면, 함수가 호출될 때마다 메모리 공간에 쌓이는 것을 볼 수 있다.
- 이 경우, 메모리 스택이 넘치거나(Stack overflow) 프로그램 실행 속도가 늘어지는 단점이 생긴다.
- 파이썬에서는 이를 방지하기 위해 3,000번이 넘어가게 되면 더이상 함수를 호출하지 않고, 종료된다. (최대 재귀 깊이)



### 13) 에러(Error)

#### 문법 에러(Syntax Error)

- 문법 에러가 있으면 실행되지 않는다.
- EOL(끝맺음 실수), EOF, invalid syntax 등이 있다.

#### 예외(Exception)

- 예기치 못한 상황 발생을 의미
- 문법적으론 옳지만, 실행시 발생

| 에러                         | 의미                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| ZeroDivisioError             | 0을 분모로 하는 나눗셈을 시행                                |
| NameError                    | 정의되지 않은 변수 호출                                      |
| TypeError                    | unsupported oerand type(s) 잘못된 타입 호출                  |
| missing required positional~ | 인자(변수값)이 하나 덜 들어오거나 더 들어옴(함수에서)        |
| index out of range           | 인덱스 범위 초과                                             |
| KeyError                     | 딕셔너리에 없는 키 사용                                      |
| ModuleNotFoundError          | 없는 모듈. 보통 import 잘못했을 때 발생                      |
| ImportError                  | 모듈은 있으나, 가져오는 과정에서 실수(보통 클래스/함수 호출 오류) |
| KeyboardInterrupt            | 사용자가 의도적으로 작동을 멈췄을 때                         |

#### 예외 처리(Exception Handling)

- Try & Except 이용

```python
try:
    <코드 블럭 1>
except [Error명]: # Error명 입력 안하면 모든 Error에 대응 가능하다.
    <코드 블럭 2>
else: # 에러 미발생시 실행할 구문
finally: # 어떤 경우든 실행을 할 구문
    
    
# 여러개 처리
try:
    <코드 블럭 1>
except (예외1, 예외2):
    <코드 블럭 2>


try:
    <코드 블럭 1>
except 예외1:
    <코드 블럭 2>
except 예외2:
    <코드 블럭 3>
```

- Try문에서 예외 발생할 시, Except문을 실행한다. 발생X시, Except문은 실행되지 않는다.

- 예외 발생시, Try문 나머지는 건너뛴다.

- as를 이용한 에러내용 보여주기도 가능하다.

  ```python
  try:
      empty_list = []
      print(empty_list[-1])
  except IndexError as err:
      print(f'{err}, 오류가 발생했습니다.')
      
  # 결과
  # list index out of range, 오류가 발생했습니다.
  ```

- `Else`

  에러가 발생하지 않는 경우 수행되는 문장은 Else로 처리

- `finally`

  반드시 수행해야 하는 문장. 모든 상황에서 실행되어야 하는 경우.

- `raise`

  에러 강제 발생 시키는 구문. 코드를 raise에서 멈추게 한다.

  ```python
  print('시작')
  raise ZeroDivisionError('감히!')
  print('끝') # 출력안됨. Raise는 코드를 멈추게 함.
  ```

- `assert`

  예외 발생 시킴. **상태 검증에 이용**. 무조건 `AssertionError`가 일어난다.

  ```python
  assert Boolean expression, error message
  
  assert len([1, 2]) == 1, '길이가 1이 아닙니다.'
  $ python code.py
  Traceback (most recent call last):
    File "code.py", line 1, in <module>
      assert len([1, 2]) == 1, '길이가 1이 아닙니다.'
  AssertionError: 길이가 1이 아닙니다.
  
  $ python -O code.py
  ```



### 14) 데이터 구조와 메서드(Data Structure & Method)

#### Method의 Return 값 유무에 따른 차이

- Return 값이 있다는 것은, 별도의 변수에 저장할 수 있다는 뜻임.

  ```python
  a = [1,2,3]
  b = a.pop(0)
  print(b)
  # 결과
  1
  # 이처럼 Return이 있다면 별도의 변수명을 선언해서, 값을 저장해줄 수 있다.
  ```

  

| 주제                               | Return O                 | Return X                    |
| ---------------------------------- | ------------------------ | --------------------------- |
| 원본 변경 여부                     | X. 새 값 생성            | O                           |
| 새 주소값 생성                     | O                        | X(값은 값 참조)             |
| 새 Parameter(변수명) 생성필요      | X                        | O                           |
| 원본 재사용 가능 여부              | O. 원본은 그대로 존재함. | X. 원본변경. 기존값못돌아감 |
| 새 변수명으로 새 값 새 주소에 저장 | O                        | X                           |
| Return값                           | 새 값.                   | None                        |

```python
a = [1,2].append(3)
# ([1,2].append(3))는 a란 함수의 변형이 아닌, [1,2]란 값에 append한 것인데,
# 이러면 append는 Return이 없으므로, a를 변형한 것이 아닌 [1,2] 변형하고 없는 return값을
# a에 돌려준 것이다. 그러므로 a자체를 변형할 수 있게, a.append로 해야 한다.
print(a)
# None
# 결과값이 존재할 수 없다. Return값이 없기 때문이다.
a.append(3) # 변수명.append 형태로 해 줘야함.
```



#### 문자열(String) Immutable, Ordered, Iterable 변경불가능, 순서있으며, 순회가능

- https://docs.python.org/ko/3/library/stdtypes.html#string-methods

| 주제      | 메서드                      | 설명                                                        | 예시              |
| --------- | --------------------------- | ----------------------------------------------------------- | ----------------- |
| 조회/탐색 | .find(x)                    | x의 첫번째 위치 반환. 없으면 `-1`반환                       | a.find('p',-2)    |
|           | .index(x)                   | x의 첫번째 위치 반환. 없으면 `Error`                        | a.index('p')      |
| 값 변경   | .replace(old, new[, count]) | 현재 글자, 바꿀 글자, [지정 개수]<br />지정개수 없으면 전부 | z.replace('a','') |
|           | .strip([chars])             | 특정한 문자 양쪽 제거. 지정X시 공백제거                     |                   |
|           | .lstrip, .rstrip            | 왼쪽, 오른쪽 제거                                           |                   |
|           |                             | \r \t \n은 전부 공백으로 인식합니다.                        |                   |
|           | .split()                    | 문자열 특정한 단위로 나누어 리스트 반환                     | a.split(',')      |
|           | 'separator'.join(iterable)  | 특정한 문자열로 만들어 반환                                 | a.join('!')       |
|           |                             | '배!고!파'                                                  |                   |
| 문자 변형 | .capitalize()               | 앞글자만 대문자로                                           |                   |
|           | .title()                    | 어퍼스트로피나 공백 이후 대문자로 반환                      |                   |
|           | .upper()                    | 모두 대문자로 반환                                          |                   |
|           | .lower()                    | 모두 소문자로 반환                                          |                   |
|           | .swapcase()                 | 대<->소문자로 변경. 서로 변경 반환                          |                   |
|           |                             |                                                             |                   |

- 기타

  ```python
  .isalpha() # 알파벳인가
  .isdecimal()
  .isdigit()
  .isnumeric() # 숫자관련 3형체
  .isspace()
  .issuper()
  .istitle()
  .islower()
  ```



#### 리스트(List) Mutable, Ordered, Iterable

- https://docs.python.org/ko/3/tutorial/datastructures.html#more-on-lists

##### 값 추가 및 삭제

| Methods           | 설명                                      | 예시                  | Return값 유무  |
| ----------------- | ----------------------------------------- | --------------------- | -------------- |
| .append(x)        | 값 추가(맨 뒤에)                          | a.append('hi')        | X. 원본 수정   |
| .extend(iterable) | 값 추가. 여러개 가능                      | a.extend([]'이디야']) |                |
| .insert(i, x)     | 정해진 위치 `i`에 값 추가                 | a.insert(0, 'hi')     |                |
| .remove(x)        | 값이 x인 것을 하나만 삭제. 없으면 `error` | a.remove(1)           |                |
| .pop(i)           | `i`위치의 값 삭제 후, 그 항목 Return      | a.pop(0)              | O. 제거된값    |
| .clear()          | List의 모든 항목 삭제. []만 남음.         | a.clear()             | X. 원본을 비움 |

##### 탐색 및 정렬

| Methods   | 설명                                           | 예시         | Return값 유무 |
| --------- | ---------------------------------------------- | ------------ | ------------- |
| .index(x) | x 값 찾아 해당 `index` 값 반환. 없으면 `error` | a.index('a') | O.            |
| .count(x) | 원하는 값의 개수를 확인 가능((1)시, 1의 개수)  | a.count('a') |               |
| .sort(x)  | 정렬.                                          | a.sort()     | X. 원본 수정  |

- .count(x)의 응용

```python
a =[1,2,5,2,1,5]
# 1 다 지우기
for i in range(a.count(1)):
#a.count(1) =3 이고 0,1,2 순으로 계속 1 제거하는 것. 즉 숫자 몇갠지 계산 안해도 되는것.
    a.remove(1)
a

# 결과 [2,5,2,5]
```

- sorted()와 sort의 차이

  | 주제         | sorted()                    | sort()                          |
  | ------------ | --------------------------- | ------------------------------- |
  | 정의         | 내장함수(Built-in Function) | 메서드(Method)                  |
  | 원본 값 여부 | 새 값 할당( a = sorted(x))  | 원본 변형(x.sort() \n print(x)) |
  | Return값     | 새 값                       | None                            |


##### .reverse() **_정렬아님!!_**

```python
# 반대로 뒤집습니다.
classroom = ['Tom', 'Stiffany', 'Karen']
classroom.reverse()
print(classroom) # Return값이 없다는 것.
```

##### List Comprehension

- 표현식과 제어문을 통해 리스트를 생성하는 방식
- 여러 줄의 코드를 한줄로 줄일 수 있음.
- Set도 가능함.(Mutable이어서일까?)

```python
# 선언 방식
[expression(출력될 것) for '변수' in iterable]
# 예제
[
    0 for i in range(10)
]
# [0,0,0,0,0,0,0,0,0,0]

# 예제2. 직접 출력해 보세요
[
    [0 for i in range(5)] for i in range(5)
]

# 예제3.
['홀' if i%2 else '짝' for i in range(10)]
#['짝', '홀','짝', '홀','짝', '홀','짝', '홀','짝', '홀']

# 세제곱 만들기
numbers = range(1, 11)
[
    i**3 for i in numbers
]
```

###### List Comprehension + 조건문

- 조건문을 포함하여 리스트를 생성

> ```python
> # 선언 방식
> [expression for '변수' in iterable if 조건식]
> [expression if 조건식 else 식 for '변수' in iterable]
> 
> #예제. 짝수리스트
> ```

계속 작성해주새오.



### 객체 지향 프로그래밍(Object Oriented Programming)

#### Python의 메모리 관리 원칙

- 컴퓨터는 자료를 보조기억장치(HDD, SDD 등)에서 주기억 장치(RAM)로 읽어, 중앙처리장치(CPU)에서 처리한다.
- RAM은 Byte마다 번지가 정해져있어, 자료를 각 번지에 할당, 이 상황을 제어하기 위해 우리는 변수를 선언하고 값을 할당하게 된다.
- 한 번 할당된 메모리 공간은 절대 다른 목적을 위해 **재할당** 되지 않음.(값 할당 해제 or 그 값의 변형만)

#### 변수, 상수, 리터럴, 객체, 인스턴스, 매개변수, 전달인자의 비교

##### 변수(Variable)

- 특정 값을 기억하기 위해 임의로 주는 명칭.

- 각 변수는 주소값에 저장되는데, 이 주소값에 **별명**을 붙여주는 행위이다.

- 즉, 변수는 마치 집주소를 주는 것과 같다.

- 변수와 String의 차이점은 변수는 Single Quote('')없이 선언한다는 것이다.

- 항상 맨 마지막 값만 기억한다.

- **Return이 있는 값들** 등은 변수명 설정을 안해주면 값 되찾기가 불가능하여 **변수명 설정이 필수이다.**

- 변수의 선언과 할당

  ```python
  # 변수의 선언
  # python
  a = 0
  # java
  int a = 0
  
  #변수에 값 할당
  a = 1 # python에선 사실상 할당과 선언이 같이 이뤄지나,
  		# 값은 지속적으로 새로 할당해 변경할 수 있는 점을 잊지 않는다.
  ```




##### 상수(Constant)

- 항상 같은 값을 저장하는 곳
- `PI = 3.14` 등이 있음.
- 변경이 가능하면 상수가 아님에 유의



##### 리터럴

- 숫자(Integer, Float, Complex)
- 문자열(String)
- 논리값(Boolean, True는 1, False는 0)
- 특수(None)
- 컬렉션(Collection) `List`,`Tuple`,`Dictionary`,`set`

##### 함수(Function)

###### 매개변수(Parameter) & 인자(Arguments)

- 혼용되어 사용되므로 구분에 주의
- Parameter는 함수에 입력으로 전달된 값을 받는 **변수**
- 함수를 호출할 때 전달하는 입력값

```python
def add(a, b): # 매개변수 a,b
    return a + b
print(add(3,4)) # 인수 3, 4
```



##### 클래스(Class), 메서드(Method), 객체(Object) & 인스턴스(Instance)

- Class는 제품을 생산할 설계도

- Method는 설계도를 실제화한 도구들

- Object, Instance는 도구를 통해 생산된 구제적 제품

  ```python
  # 객체와 인스턴스의 차이
  a = Cookie()에서 a는 Cookie Class의 구체적 값을 저장하고 있다.
  a는 따라서 '객체'이다.
  하지만 a는 Cookie Class 입장에선 수많은 객체들 중 하나이다.
  따라서, a는 Cookie의 인스턴스이다.
  ```

- 객체를 클래스 기준에서 보면 인스턴스(수많은 객체들 중 하나), 객체 자체를 기준으로 보면 객체





- 위 개념들은 파이썬 언어를 공부하면서 끊임없이 머릿 속에서 충돌하게 되는 언어들인데, 그 때를 위해 참고할 수 있도록 간략하게 정리해둔다.

  |                     | 정의 | 설명                                          | 예시 |
  | ------------------- | ---- | --------------------------------------------- | ---- |
  | 변수(Variable)      |      |                                               |      |
  | 상수(Constant)      |      |                                               |      |
  | 객체(Object)        |      | 모든 객체는 1회성. 이름을 주지 않으면 사라짐. |      |
  | 인스턴스(Instance)  |      |                                               |      |
  | 속성(Attribute)     |      |                                               |      |
  | 매개변수(Parameter) |      |                                               |      |
  | 전달인자(Argument)  |      |                                               |      |

  

### 메서드 임시 저장

- enumerate #sequence형의 인덱스와 값을 튜플로 묶어서 꺼내줌.

- 앞으로 이거 쓰면 인덱스 찾아오는 귀찮은 짓 줄일수 있음. 아래 두개 코드 비교해볼것.

  ```python
  def low_and_up(string):
      i = 0
      result = ''
      while i < len(string):
          if i%2:
              result += string[i].upper()
          else:
              result += string[i]
          i += 1
      return result
  
  def low_and_up(word):
      result = ''
      for idx, char in enumerate(word): # enumerate
          if idx % 2:
              result += char.upper()
          else:
              result += char.lower()
      return result
  ```

  ```python
  print(low_and_up('apple'))
  print(low_and_up('banana'))
  ```

  

