'''

'''

import requests
import pandas as pd


def score(cve_id):
    headers = {
        'Authorization' : 'Bearer AAAAAAAAAAAAAAAAAAAAAMtqbgEAAAAAKa1EB%2Br6mDVj2GrRsjx0u5wpywg%3DeeAJYlaNB9O3Vqk2197w7wROtogh1wHUI2sYlv8cuxahyRhiTP'
    }

    response = requests.get('https://api.twitter.com/2/tweets/search/recent?query={}&tweet.fields=created_at&max_results=100'.format(cve_id), headers=headers).json()
    print(response)
    meta = response['meta']
    pagination_token = meta['next_token']
    count = 0
    while(True):

        response_loop = requests.get('https://api.twitter.com/2/tweets/search/recent?query={}&tweet.fields=created_at&max_results=100&pagination_token={}'.format(cve_id,pagination_token), headers=headers).json()
        meta_loop = response_loop['meta']


        result = meta_loop['result_count']
        count += result

        try:
            pagination_token = meta_loop['next_token']
        except:
            break

    print('Total tweets = ' + str(count))

    if(count >= 400):
        return 'Critical'

    elif(count <= 400 and count >= 300):
        return 'High'

    elif(count <= 300 and count >= 200):
        return 'Medium'
    else:
        return 'Low'


score('test')