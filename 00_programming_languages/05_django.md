# Django

> 파이썬을 기반으로 하는 Web Framework(Server 관리를 담당한다.)

- 동적 웹 페이지(Dynamic web page)나, Web application, Web service 등의 개발 보조용으로 만들어지는 어플리케이션 프레임워크의 일종
- **웹 페이지 개발 과정 중 겪는 어려움을 줄이는 것**이 주 목적, 기본 웹 페이지 개발 기능을 담고 있다.
- 기본적인 구조나 필요한 코드들을 제공
- Node.js가 개인 카페를 창업하는 거라면, Django는 프랜차이즈 카페 창업이라 볼 수 있다.
- 주요 기업 : Spotify, Instagram, Dropbox, Delivery Hero...

**MTV 패턴**

- Model, Template, View. 각각 데이터베이스 관리, 레이아웃(화면, 사용자인터페이스), 중심컨트롤러(심장)을 담당

- 일반적으로 소프트웨어는 MVC패턴(Model, View, Controller)이나, 장고는 MTV 패턴을 채택했다.
-  장고에선 V가 중심 컨트롤러(심장)역할을 하고, Template이 Layout을 구성한다. 



**시작 전 설정**

![image-20210308105221214](05_django.assets/image-20210308105221214.png)

![image-20210308105229099](05_django.assets/image-20210308105229099.png)

![image-20210308105314550](05_django.assets/image-20210308105314550.png)



**작동 방식**

1. HTTP Request
2. URLS(urls.py)로 요청을 받아 방향을 잡음.
3. View(views.py)로 URL 전달
4. Model(models.py) <> View URL에서 요구받은 데이터를 read/write data
5. Template(<filename>.html) -> View로 전달 및 하나의 완성된 문서 작성.
6. HTTP response(HTML)



## **프로젝트 개시**

**One Project, One Virtual Environment**: 하나의 Project가 하나의 가상 환경을 역할한다.

1PJT == 1Venv(가상환경) == 1Git Repo



**가상환경 파이썬을 생성하고 싶다면**

> why? global에 설치된 pip와 다르게, 각 가상환경에 맞는 pip만 쓰게 하려고(각자 필요한 패키지만 사용위해.)

**GITHUB 사용 시에는, VENV 폴더를 전체를 IGNORE 해야함에 유의**

**아래 작업은 실행시 매번 해야한다. + 폴더위치 변경이나 폴더명 변경시, venv지우고 다시 해야함.**

- **프로젝트 폴더 내**에서 `python -m venv '원하는 가상 파이썬 폴더명'`을 입력한다. #보통 venv로 통일
- 하지만 `which python` 해도 여전히 python은 global Python 경로가 지정된다.
- `source venv/Scripts/activate` 입력
- (폴더명) 출력이 되면 성공. 앞으로 위 프로젝트는 venv 파이썬을 자기 파이썬으로 사용한다.
- pip list 검색시, 모든 pip는 초기화되어, pip, setuptools만이 존재한다.

![image-20210308134858708](05_django.assets/image-20210308134858708.png)

- `pip install django`. 아래가 Django시 설치해야 하는 Pacakge & Version

![image-20210308134956763](05_django.assets/image-20210308134956763.png)

![image-20210308135057114](05_django.assets/image-20210308135057114.png)

**requirements.txt로 쓰는 것이 약속한 Rule**. 즉, `pip freeze requirements.txt`

- `pip freeze > 만든txt명.txt` 시, 현재 설치된 pip목록이 전부 txt에 복사 및 업로드 된다.
- freeze는 버젼을 동결시키는 명령어
- `pip install -r 만든txt명.txt` 로, 전부 설치 가능



####################################################################

- `deactivate` 입력시 비활성화 가능.
- 프로젝트 폴더 내에(venv폴더가 있는 경로와 같은 경로) `.gitignore` 생성
- `.gitignore` 상단에 `/폴더명(위에 그대로 했다면 venv/이 되겠죠?)`입력. venv 하위는 다 무시된다.
- `gitignore.io` 사이트에서 `django, vscode, python, venv` 추가 후 붙여넣기



1. 원하는 폴더에서 Git bash 실행
2. `django-admin startproject <원하는 프로젝트명>` 입력 **파이썬 컨벤션에 따라 숫자로 시작 불가**
3. Django의 모든 명령어는 위처럼 3등분됨을 유의한다.
4. 이 과정에서 서버는 이미 구동되어 있다.
5. 해당 폴더에서(`manage.py` 확인) `python manage.py runserver` 입력시, 서버 Open

![image-20210308093130840](05_django.assets/image-20210308093130840.png)

6. 주소를 `Ctrl + Click`으로 눌러보면,

![image-20210308093209473](05_django.assets/image-20210308093209473.png)

7. 위 사이트가 등장한다.

![image-20210308093413236](05_django.assets/image-20210308093413236.png)

8. 실행시 위처럼 Upload가 되며, 종료시엔 `Ctrl + C`로 종료한다.
9. 서버 생성시, 항상 위 과정을 거친 후 사용한다.

![image-20210308100412625](05_django.assets/image-20210308100412625.png)

- init은 폴더를 패키지로 인식하도록 한다.
- asgi, wsgi는 비동기 웹과 연동시 사용
- **Urls**는 위에서 나왔던, 요청을 받아 알맞은 View(Appropriate View)로 전달하는 곳.
- settings는 각종 설정이 가능하다. 여기서 시간이나, 언어 등도 설정이 가능하다.

```python
# Internationalization
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul' # (기존은 UTC)
```



## 앱 생성

1. `python manage.py startapp <원하는앱명>`으로 생성한다.
2. <원하는앱명> 폴더가 생성된다.
   1. __init__.py는 폴더를 하나의 패키지로 접근할 수 있도록, 패키지의 공간을 만들어주는 역할.
   2. **admin.py** 관리자 사이트를 커스텀
   3. apps.py는 손대지 말것
   4. **models.py** **MTV 패턴**의 M을 담당
   5. tests.py는 테스트 코드 작성용
   6. **views.py**는 패턴의 V를 담당(중간관리자)
   7. T는 Django가 자동적으로 만들어주지 않아서, 직접 만들 것임.

![image-20210308100333538](05_django.assets/image-20210308100333538.png)



**주의점**

![image-20210308094612483](05_django.assets/image-20210308094612483.png)

1. 장고는 프로젝트와 앱이 동일 경로에 생성이 된다.

![image-20210308094647805](05_django.assets/image-20210308094647805.png)

2. 그래서 장고에 앱 등록을 직접 해줘야 하는데,
3. Project 폴더 내의 `Settings.py`에서, INSTALLED_APPS 항목에 '앱이름'을 작성해준다.

![image-20210308094839867](05_django.assets/image-20210308094839867.png)

4. 순서가 정해져있어서, 내가 작성한 apps는 항상 맨위에 작성해주는 것이 충돌 가능성을 낮춘다.



## 사이트 주소 설정

> 작성순서 : [1] Url에 Path 작성
>
> [2] Views.py에 request 함수 작성[return render() 필수 유의]
>
> [3] apps명>templates>html 작성

1. `Urls.py` 에서 작성
2. 가보면, path('admin/')이 기본적으로 존재하는데, 내 Url에서 `/admin` 입력시, Django가 기본 제공하는 admin 화면이 확인 가능하다.

![image-20210308101102210](05_django.assets/image-20210308101102210.png)

3. urlpatterns에 주소를 작성하며, 장고는 항상 Path에 엔드슬래시가 필수이다.

![image-20210308101442371](05_django.assets/image-20210308101442371.png)

```python
urlpatterns = [
    path('admin/', admin.site.urls), # 엔드슬래시 필수
    path('index/', )
    path('메인페이지로 들어오고자 하는 Url주소', '호출할 적절한 View 함수')
]
```

4. __View함수는 Project에 있지 않고, 각 App에 존재함에 유의한다.__

![image-20210308101507537](05_django.assets/image-20210308101507537.png)

5. Views에 함수를 작성시, 반드시 첫번째 인자는 "**request"**임에 유의한다.

![image-20210308101526105](05_django.assets/image-20210308101526105.png)

6. 첫 Return값도 위처럼, return render(request, '템플릿 경로')로 작성한다.

![image-20210308101631729](05_django.assets/image-20210308101631729.png)

7. **Template을 작성**한다.(원하는 App내에 Template 폴더 생성후, 함수명.html 파일을 작성한다.)

![image-20210308102219553](05_django.assets/image-20210308102219553.png)

8. App내 views파일에 경로 지정후,

![image-20210308102320106](05_django.assets/image-20210308102320106.png)

9. Urls 에 **패키지** 추가[from 패키지명 import py명] 후, 경로를 입력해준다. **트레일링 콤마**도 필수로

![image-20210308102410803](05_django.assets/image-20210308102410803.png)

10. 이 모든 것은 저장시 실시간으로 업로드된다.

![image-20210308102433203](05_django.assets/image-20210308102433203.png)

11. Index 함수를 아래와 같이 작성 후에, 사이트로 이동해보면, ( ! + Tab시 기본 doctype  자동 완성)

![image-20210308105956778](05_django.assets/image-20210308105956778.png)

12. 이와같은 페이지를 볼 수 있다.

![image-20210308110033489](05_django.assets/image-20210308110033489.png)

**참고사항**

새 URL 작성후엔 로켓 화면은 404Error로 출력되게 된다.

![image-20210308105909268](05_django.assets/image-20210308105909268.png)

## Django Template

> 가공된 데이터를 받아 잘 표현하는 것이 목표. HTML을 더 강렬하게 표현해주기 위해 사용

- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
- 사용자 인터페이스를 구성하게 될 Layout을 작성한다.

### Variable, Filters, Tags, Comments

### Variable(변수)

- {{ variable }}
- render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것



![image-20210308104226354](05_django.assets/image-20210308104226354.png)

![image-20210308104428594](05_django.assets/image-20210308104428594.png)



2.

![image-20210308104241915](05_django.assets/image-20210308104241915.png)

키, 밸류값은 되도록 이름을 통일할것

![image-20210308104331770](05_django.assets/image-20210308104331770.png)

![image-20210308104452683](05_django.assets/image-20210308104452683.png)



### Template Inheritance

- 템플릿 상속은 코드의 재사용성에 초점
- 상속시, **사이트의 모든 공통 요소 포함** + **하위 템플릿이 재정의(Override)하는



**Tags**

`{% extends %}` & `{% block %}`

**extends**

- 자식(하위)템플릿이 부모 템플릿 확장함을 알림
- 반드시 **템플릿 최상단**에 작성

**block**

- 하위 템플릿에서 재지정(Override)할 수 있는 블록을 정의
- 부모 py에 위치할 공간에 block 작성 후, 그 이후에 자식에 태그를 작성한다.
- 하위 템플릿이 채울 수 있는 공간을 제공



Project 폴더내에 templates 폴더 생성

Settings.py - Templates - APP_DIRS = TRUE는 앱에 있는 템플릿경로는 기본적으로 활성화 되어 있음. but 프로젝트 파일내 경로는 직접 활성화 해야함. DIRS : []에 직접 작성할 수 있다. [BASE_DIR / '프로젝트명' / 'templates'] python pathlib 검색후 참조. 이 과정이 없으면 에러 남

![image-20210308141723544](05_django.assets/image-20210308141723544.png)



#### 기본적인 작성순서 예시

```python
# 1. Project 폴더 내 urls.py에 path 작성
# 2. App 폴더 내 views.py에 def 함수 작성
# 검색창 페이지 예시
def throw(request):
    return render(request, 'throw.html')
def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)  # 요청받으면, catch.html 실행, context전달
```



![image-20210308145933243](05_django.assets/image-20210308145933243.png)

### WHY?

**Django의 설계 철학**

- "표현과 로직(View)을 분리"
  - Template System은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐.
  - 이 기본을 넘어서면 안된다.
- "중복을 배제"
  - 대다수 동적 웹사이트는 공통 header, footer, navbar 같은 공통 디자인을 가짐
  - 이러한 요소를 분리하여 중복 코드를 없앰



## 기본 컨벤션(Style Guide)

- App 이름은 **복수형**
- App **반드시** 생성(startapp) 후 등록
- {{ 내용 }} 내용 좌우로 한칸씩 띄어쓰기



## HTML FORM

- 

### HTML input element

- 사용자로부터 데이터를 입력 받기 위해 사용

- 핵심 속성

  - name

  - 중복 가능, 양식 제출시 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음

  - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(Name은 key, Value는 vale)로 

    **?key=value&key=value** 형태로 전달



###  HTTP

> HyperText Transfer Protocol

- 웹에서 이뤄지는 모든 데이터 교환의 기초
- 주어진 리소스가 수행할 원하는 작업을 나타내는 Request Methods를 정의
- HTTP request method 종류
  - GET, POST, PUT, DELETE...
  - GET : 정보 요구(검색 등). 정보를 수정하지는 않는다.
  - PUT : 수정
  - DELETE : 삭제

**GET**

- 서버로부터 정보 조회하는 데 사용
- 데이터를 가져올 때만 사용
- body가 아닌, Query String Parameters를 통해 전송
  - body에 들어가면, URL에 검색어가 들어가지 않음. 즉, 입력어가 URL에 출력됨
- 



## URL

> Fowarding. 들어온 요청을 단순히 Views로 보내는 역할

- Dispatcher(발송자, 운항 관리자)로서의 URL
- 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작됨

**App URL mapping**

- App의 View 함수가 많아지면서, 사용하는 path() 또한 많아지고, app 또한 더 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 코드 유지보수에 좋지 않음
- 각 app에 urls.py를 작성
- 중간관리자를 배치한다고 생각하면 된다.(URL부서 - 각 APP별 URL팀을 배치한다고 생각하면 편함)

**Variable Routing**

- URL 자체를 동적으로 사용하여, 주소를 동적으로 변경시킨다.

![image-20210308155921013](05_django.assets/image-20210308155921013.png)

- <str>의 경우는 생략가능하나, <int>는 생략불가능

**Naming URL patterns**

- 링크에 URL을 직접 작성하는 것이 아닌, path()함수의 name인자를 정의해 사용
- Django Template Tag 중 하나인 URL태그를 사용해서 path() 함수에 작성한 Name을 사용할 수 있음

- 위 이미지의 path 중 `name = 'index'` 등이 내가 임의로 정해준 이름이다.

```python
# urls.py 내 작성 내용
# urlpatterns는 url이 없어도 urls.py 내에 반드시 작성되어 있어야 한다.
from django.urls import path
from . import views  # 앱 내 urls.py 생성했다면 필수
urlpatterns =[
    path('index/', views.index, name='index')  # 내가 줄 URL명, views에서 index함수 호출, 주소명할당
]

################### 이하 index.html ###################
# <a>태그에 따로 주소를 길게 쓰지 않아도, 편하게 url태그로 연결이 가능
{% extends 'base.html' %}  {# Block 템플릿의 경로 작성#}

{% block content %}
  <h1>안녕하세요!! 여기가 메인 페이지입니다.</h1>
  <a href="{% url 'greeting' %}">greeting</a>  {# url 'path에정해진이름' 알아서 주소값을 찾아준다#}
  <a href="/dinner/">dinner</a>
  <a href="{% url 'throw' %}">throw<throw/a>
{% endblock %}
```



**Project 폴더의 urls.py**

> include라는 것을 따로 import 해줬다. URL 책임을 하위 URL에 할당해주기 위해서

![image-20210308163511950](05_django.assets/image-20210308163511950.png)

- 그렇다면, articels.urls는 어떻게 되어있을까?

> 자기와 연관된 path를 전부 담고 있으며, URL Name을 정의해주었다.

![image-20210308163555783](05_django.assets/image-20210308163555783.png)

- 그렇다면, 마지막 pages는 어떨까?

![image-20210308164258479](05_django.assets/image-20210308164258479.png)



## Views

**URL**이 보내온 Request를 받아 response(응답)을 반환함.(return HTML)



vscode & git bash

컨트롤 알트 화살표 여러줄 동시 입력

프로젝트 지우기 rm -rf 프로젝트 폴더명

프로젝트 폴더 프로젝트 폴더 - 프로젝트 폴더가 아닌 이자리에 직접하고 싶을떄

`django-admin startproject intro .`

앱도 rm -rm 앱폴더명도 이렇게 지우기



프로젝트 폴더는 settings.py를 들고 있음

settings에

\# Installed_apps에 앱 적는 것이 가장 먼저 해야할 것

59LIne의 DIRS(TEMPLATES에 DIR관리)



트레일링 컴마 필수 



요청들어온다(-> url)

요청 포워딩(url -> view)

요청 해결한다(view + html)

return 한다(html)



url은 요청을 받아주고

template 외형 및 보여질 내용을 짜주며

view는 이 모든 구조를 해결해준다.