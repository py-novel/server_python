import requests
import chardet
import urllib3
urllib3.disable_warnings()

from reptile_factory.utils.get_headers import get_headers

def get(target_url):
    response = requests.get(
        target_url, 
        headers=get_headers(),
        verify=False, 
        allow_redirects=True
    )
    response_content = response.content
    html = response_content.decode(encoding=chardet.detect(response_content)['encoding'])
    return html

def post(target_url, data):
    response = requests.post(
        target_url, 
        data=data,
        headers=get_headers(),
        verify=False, 
        allow_redirects=True
    )
    response_content = response.content
    html = response_content.decode(encoding=chardet.detect(response_content)['encoding'])
    return html
