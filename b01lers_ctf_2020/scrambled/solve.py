from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib


cj = cookielib.CookieJar()


opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())

# create a request object to be used to get the page.
req = Request("http://web.ctf.b01lers.com:1002")
f = opener.open(req)

# see the first few lines of the page
html = f.read()
# print(html[:50])

# Check out the cookies
print ("the cookies are: ")
for cookie in cj:
    print cookie.name, cookie.value

cookie_map = {}

while len(cookie_map) != 67:
    print len(cookie_map)
    # create a request object to be used to get the page.
    req = Request("http://web.ctf.b01lers.com:1002")
    f = opener.open(req)

    # see the first few lines of the page
    html = f.read()
    # print(html[:50])

    # Check out the cookies
    for cookie in cj:
        if cookie.name == "transmissions":
            if not cookie.value in cookie_map:
                cookie_map[cookie.value] = True

for cookie in cookie_map:
    print cookie
    # for i in range(1, 3):
    #     cookies = dict(frequency=str(i), transmission="kxkxkxkxsht_47kxkxkxkxsh")

    #     r = requests.get("http://web.ctf.b01lers.com:1002", cookies=cookies)
    #     for c in r.cookies:
    #         print(c)
    #         # print(c.name, c.value)
