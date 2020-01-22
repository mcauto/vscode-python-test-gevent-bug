"""
test example
"""
import grequests

def test_google():
    """ request google.com """
    urls = ['https://gabia.com', 'https://google.com', 'https://naver.com']
    rs = (grequests.get(url=url) for url in urls)
    responses = grequests.map(rs)
