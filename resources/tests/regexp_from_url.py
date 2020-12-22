from urllib.request import urlopen, Request
import re
from contextlib import closing

req = Request("https://yts-subs.com/movie-imdb/tt1483013")
req.add_header(
    "User-Agent",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
)

# with closing(urlopen(req)) as webpage:
webpage = urlopen(req)
encoding = webpage.headers.get_content_charset("charset")
# page = str(webpage.read(), encoding)
page = webpage.read().decode(encoding)
page1 = page
print(
    "Before writing : type {0} len {1}".format(
        type(page),
        len(page),
    )
)

# with open('temp.data', 'w') as data:
#     data.write(page)
# page = ''
# with open('temp.data','r') as data:
#     page=''.join(data.readlines())
# page2 = page

# page=page.split('\n')
# page=''.join(page)
# page=page.replace('\t','')
# page=page.replace('\r','')

print(
    "After writing : type {0} len {1}".format(
        type(page),
        len(page),
    )
)
# print("page1.split")


# pattern = re.compile(r'.*<tr data-id=".*?"(?: class="((?:high|low)-rating)")?>\s*<td class="rating-cell">\s*.*</span>\n\s*</td>\n\s*<td class.*\n\s*<span.*>.*</span>\n\s*<span class="sub-lang">(.*)?</span>\n\s*</td>\n\s*<td>\n\s*<a href="(.*)?">')
pattern = re.compile(
    r'<tr data-id=".*?"(?: class="((?:high|low)-rating)")?>\s*<td class="rating-cell">\s*.*</span>\s*</td>\s*<td class.*\s*<span.*>.*</span>\s*<span class="sub-lang">(.*)?</span>\s*</td>\s*<td>\s*<a href="([^">]*)?'
)
print(pattern.findall(page))
