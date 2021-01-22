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
- e/E도 사용가능. eg. pi = 314e-2 -> 3.14
- 부동소수점 처리 `abs(0.38-0.23) <= 1e-10 #정말 작은 수보다 더 작은 지 T/F 판단`
- 혹은  `import math \ math.isclose(a, b) 연산값과 기대값이 가까운가로 확인`
- 0 출력하고 싶을시 `%.4f` 를 이용하도록 한다.

##### complex

- 복소수. 허수부를 j로 표현한다.
- a = 3 - 4j

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
- **KEY값**은 변경이 불가능하다
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
num값이 바뀌지 않음!
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

#### 함수의 선언

```python
def func(x, y):
    <code block>
    return value  # 결과값 전달. return값이 없다면, None 반환.
```





#### 함수의 호출

