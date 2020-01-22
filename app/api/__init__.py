"""
API package
"""
import grequests

def example():
    urls = ['https://gabia.com', 'https://google.com', 'https://naver.com']
    rs = grequests.get(url=url) for url in urls)
    responses = grequests.map(rs)
    return responses
