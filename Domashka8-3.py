import time
import requests
from pprint import pprint


def sample_questions(tag):
    url = 'https://api.stackexchange.com/2.3/questions'
    todate = int(time.time())
    fromdate = todate - 172800

    params = {
        'pagesize': 100,
        'fromdate': fromdate,
        'todate': todate,
        'order': 'desc',
        'sort': 'activity',
        'tagged': tag,
        'site': 'stackoverflow',
        'page': 1
    }
    questions_list = []
    page_number = 1
    while True:
        questions = requests.get(url, params=params).json()
        questions_list.extend(questions['items'])
        if questions['has_more'] == True:
            page_number += 1
            params['page'] = page_number
            print('*', end=' ')
            time.sleep(1)
        else:
            break

    for question in questions_list:
        print(question['question_id'], question['tags'])

    print(len(questions_list))
    print(questions['has_more'])

if __name__ == '__main__':
    sample_questions('python')


# for i in range(1,23):
#   params['page'] = i
#   questions = requests.get(url, params=params).json()
#   print('*', end = ' ')
# pprint(questions_list)


# pprint(questions_list)

