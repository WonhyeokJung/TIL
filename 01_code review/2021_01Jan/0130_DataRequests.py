import requests
from pprint import pprint


# API 요청하기

class URLMaker:    
    url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    def get_url(self, category='movie', feature='popular', **kwargs):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}'

        for k, v in kwargs.items():
            url += f'&{k}={v}'

        return url
        

    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)
        movie = res.json()

        if len(movie.get('results')):
            return movie.get('results')[0].get('id')
        else:
            return None

# API 이용하기
import requests
from tmdb import URLMaker
from pprint import pprint

def ranking():
    # URLMaker 클래스를 이용, 내 API KEY값을 추가하고
    maker = URLMaker('c9ed7f727f31ffadd0890762e0f98e96')
    # 위를 토대로 URLMaker Class의 get_url() 메서드를 이용, url을 생성합니다.
    url = maker.get_url()
    # 위 주소로 import request 이용한 응답을 요청합니다.
    res = requests.get(url)
    # 받아온 응답을, json형식으로 저장합니다.
    movie_dict = res.json()

    # 각 영화 dictionary의 집합인 movie_list 변수를 만들어 줍니다.
    movie_list = movie_dict.get('results')
    # 각 영화의 평점을 담을 scores 리스트와
    scores = []
    # 영화를 높은 점수대로 정렬할 리스트
    result = []
    # 각 영화의 dictionary를 하나씩 호출하면서
    for movie in movie_list:
        # 각 영화의 딕셔너리 내 평균 점수를
        scores += [movie.get('vote_average')]
    # 순서대로 정렬합니다.
    scores.sort()
    # 역순으로 정렬해서 점수가 높은 순으로 다시 바꿔줍니다.
    scores.reverse()
    
    # 점수들을 정렬했으니, for문으로 하나씩 돌면서
    for i in scores:
        # 영화 목록 리스트를 돌면서
        for j in range(len(movie_list)):
            # 각 영화의 평점이 정렬된 점수 scores와 같으면 result 리스트에 담는다.
            if movie_list[j]['vote_average'] == i:
                # + result 리스트에 이미 영화가 존재하지 않는 경우에만!
                if not movie_list[j] in result:
                    # 무비 리스트에 추가해 줍니다.
                    result.append(movie_list[j])

    # 그 중 평점이 가장 높은 5개의 영화를 저장하여
    highest_5 = result[0:5:1]
    # 반환합니다.
    return highest_5

if __name__ == '__main__':
    # popular 영화 평점순 5개 출력
    pprint(ranking())