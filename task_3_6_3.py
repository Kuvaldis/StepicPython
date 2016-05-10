import requests

numbers = """992
928
994
995
929
997
999
909
974
942
914
983
985
989
990"""

for number in numbers.split('\n'):
    url = 'http://numbersapi.com/' + number + '/math'
    params = {
        'json': True
    }

    res = requests.get(url, params=params)
    json = res.json()
    print('Interesting' if json['found'] else 'Boring')
