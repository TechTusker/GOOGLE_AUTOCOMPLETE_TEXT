#pip install request [an external python packet]
import json
import requests

completion_query = 'Ubuntu VS'

headers = {
    "Users-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}
response = requests.get(f'http://google.com/complete/search?client=chrome&q={completion_query}',
                        proxies={'http': '116.125.141.115'})

for completion in json.loads(response.text)[1]:
    print(completion)

#https://proxyscrape.com/free-proxy-list only use port 80 i.e. for http port