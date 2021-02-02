# 이것은 별다른 코드는 아니고,
# 단순한 실수체크용.

import json


def check(data):
    temp = []
    for i in data:
        temp += i
    
    #37.5도 이상이 연속된 횟수를 측정할 count 변수
    count = 0
    # 온도들을 for문을 돌리며
    for j in temp:
        #37.5도보다 높았었다면
        if j >= 37.5:
            #count를 추가하고
            count += 1
            #count가 3이상이 된 순간
            if count >= 3:
                #true를 반환합니다.
                return 'True'


        # 연속으로 3회이상 열이 났을 경우 True를 반환하는 코드인데,
        # 여기를 이렇게 세팅하는 실수를 저질렀다.
        # elif j < 37.5 and count > 0:
           # count -= 1

        # 수정안.
        elif j < 37.5 :
            count = 0
    return 'False'

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem03_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(check(temperature_list))
    # => True

# 실수는 줄일 수 있도록 항상 조심!