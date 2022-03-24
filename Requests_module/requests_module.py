import requests

r = requests.get('https://www.hackerearth.com/practice/python/iterators-and-generators/iterators-and-generators-1/tutorial/')

print(r)        #<Response [200]>
print(dir(r))
# print(help(r))

# print(r.text)   #use HTML parser to further
""" <html>
    <body>... """

print(r.status_code)        
#200 success,300 request has more than one possible responses, 400 client error()(not have permission), 500 server error( site crashesh)
print(r.ok)     #True if <400
print(r.headers)
#{'Content-Type': 'text/html; charset=utf-8', 'X-XSS-Protection': '1; mode=block', 'X-Content-Type-Options': 'nosniff', 'Content-Security-Policy': "default-src 'self' * 'unsafe-eval' 'unsafe-inline' data: filesystem: about: blob: ws: wss:", 'Content-Encoding': 'gzip', 'Strict-Transport-Security': 'max-age=31536000; includeSubDomains', 'Vary': 'Accept-Encoding, Cookie', 'X-Frame-Options': 'SAMEORIGIN', 'X-Akamai-Transformed': '9 22416 0 pmb=mRUM,2', 'Expires': 'Thu, 24 Mar 2022 07:00:10 GMT', 'Cache-Control': 'max-age=0, no-cache, no-store', 'Pragma': 'no-cache', 'Date': 'Thu, 24 Mar 2022 07:00:10 GMT', 'Content-Length': '24398', 'Connection': 'keep-alive', 'Set-Cookie': 'HE_UTS_ID_CL=d2eb3a2a9e3441358f86a18a5e2fb53144a18c83810b4d929d312951df94427a; Domain=.hackerearth.com; expires=Wed, 19-Mar-2042 07:00:09 GMT; httponly; Max-Age=630720000; Path=/, HE_UTS_ID_LP="/practice/python/iterators-and-generators/iterators-and-generators-1/tutorial/"; Domain=.hackerearth.com; expires=Fri, 25-Mar-2022 07:00:09 GMT; httponly; Max-Age=86400; Path=/, HE_UTS_ID=dbea3db012124d95994ffe6c8e0860a6d4e35f4607064979bde114ee1234bc2f; Domain=.hackerearth.com; expires=Thu, 24-Mar-2022 07:30:09 GMT; httponly; Max-Age=1800; Path=/, csrftoken=sO6W4RsVDwww8re4M7fFH2m9YShZWyrEqR7ZVroC1x2XufgaqerXt62MAhNEhlNu; expires=Thu, 23-Mar-2023 07:00:09 GMT; Max-Age=31449600; Path=/; SameSite=None; secure', 'Server-Timing': 'edge; dur=74, origin; dur=443, cdn-cache; desc=MISS'}



""" rpic =requests.get('https://images.unsplash.com/photo-1647971886522-82b13c7d663b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60')
print(rpic.content) """

# \x06\xf3\xb7\x81\xdd\x1d\xb6\'Hb\xf6\x94#R\xcf"g\x86%\x8e\x19\xa7\x18\xd2d\xdeE\xbf\x93\xc1%V.7\xe
# 9>\x92\xd5\xfb\xfe0j\xe9\xe9S\xe1yT(R%\xc9\x1eF\x88\xbeEVP\xb9\x15\xa6\xcc\x8e%a\x9cDL\xd4\xa7$\xac\xac\x8da\xfe\x0f\xf
# 6\xfe\xce\xd3I\xff\x00\xd3D\xf9\x16\xcf\x8d\xe6\x84!\x96i\xcb\xbaYm\xb4Vy51!rK\x91\x0b\x92\x87\x86w$\xd3\xa4\xc4(\x92\x82\x1e\x9bCE.......

""" with open('Requests_module/gen_pic.png','wb') as f:
    f.write(rpic.content) """
    


""" content
 |      Content of the response, in bytes.
 text
 |      Content of the response, in unicode.
 |      
 |      If Response.encoding is None, encoding will be guessed using
 |      ``chardet``.
 |      
 |      The encoding of the response content is determined based solely on HTTP
 |      headers, following RFC 2616 to the letter. If you can take advantage of
 |      non-HTTP knowledge to make a better guess at the encoding, you should
 |      set ``r.encoding`` appropriately before accessing this property. """


# HTTP bin is a simple HTTP request and response service. Assume that you won’t have any errors dealing with it.


payload = {'page':1, 'count': 20}

r2 = requests.get('https://httpbin.org/', params=payload)
print(r2.status_code)
print(r2.url)           #https://httpbin.org/?page=2&count=25
print(r2.text)        

payload = {'username':"siddharth", 'password': "testing"}
r3 = requests.post('https://httpbin.org/post', data=payload)
print(r3.text)
""" </html>
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "password": "testing", 
    "username": "siddharth"
  }, 
  "headers": { """

print(r3.json())
# {'args': {}, 'data': '', 'files': {}, 'form': {'password': 'testing', 'username': 'siddharth'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '31', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0', 'X-Amzn-Trace-Id': 'Root=1-623c2573-0e5cea270aaef89b4586c5a0'}, 'json': None, 'origin': '14.99.102.226', 'url': 'https://httpbin.org/post'}
r_dict = r3.json()
print(r_dict['form'])           #{'password': 'testing', 'username': 'siddharth'}


ar = requests.get('https://httpbin.org/basic-auth/sidd/1234', auth=('sidd',1234))
print(ar.text)
""" {
  "authenticated": true, 
  "user": "sidd"
} """

print(ar)
# <Response [200]>

ar = requests.get('https://httpbin.org/basic-auth/sidd/1234', auth=('siddhar',1234), timeout=3)
print(ar.text)      #blank
print(ar)           # <Response [401]>




print("\n \n----------------------------------ERROR HANDALING --------------------------------------")
import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')



>>> requests.post('https://httpbin.org/post', data={'key':'value'})
>>> requests.put('https://httpbin.org/put', data={'key':'value'})
>>> requests.delete('https://httpbin.org/delete')
>>> requests.head('https://httpbin.org/get')
>>> requests.patch('https://httpbin.org/patch', data={'key':'value'})
>>> requests.options('https://httpbin.org/get')

response = requests.head('https://httpbin.org/get')

>>> response.headers['Content-Type']            #'application/json'
>>> response = requests.delete('https://httpbin.org/delete')
>>> json_response = response.json()
>>> json_response['args']