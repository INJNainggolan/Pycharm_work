import requests

'''
r = requests.head('http://httpbin.org/get')
print(r.headers)
'''

'''
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
'''

'''
r = requests.post('http://httpbin.org/post', data='ABC')
print(r.text)
'''

'''
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.put('http://httpbin.org/put', data=payload)
print(r.text)
'''

'''
kv = {'key1': 'value1', 'key2': 'value2'}
r = requests.request('GET', 'http://python123.io/ws', params=kv)
print(r.url)
'''

'''
kv = {'key1': 'value1', 'key2': 'value2'}
r = requests.request('POST', 'http://python123.io/ws', data=kv)
'''

'''
body = 'AAA'
r = requests.request('POST', 'http://python123.io/ws', data=body)
'''

kv = {'key1':'value1'}
r = requests.request('POST', 'http://python123.io/ws', json=kv)