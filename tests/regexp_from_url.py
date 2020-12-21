from urllib.request import urlopen, Request
import re
from contextlib import closing

req = Request('https://yts-subs.com/movie-imdb/tt1483013')
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')

# page = ''
# with closing(urlopen(req)) as webpage:
webpage = urlopen(req)
encoding = webpage.headers.get_content_charset('charset')
# page = str(webpage.read(), encoding)
page = webpage.read().decode('utf-8')

print(type(page))
print(len(page))
pattern = re.compile(
                     r'<tr data-id=".*?"(?: class="((?:high|low)-rating)")?>\s*<td class="rating-cell">\s*.*</span>\n\s*</td>\n\s*<td class.*\n\s*<span.*>.*</span>\n\s*<span class="sub-lang">(.*)?</span>\n\s*</td>\n\s*<td>\n\s*<a href="(.*)?">'
                     ,re.UNICODE)

# print(page)
print(pattern.findall(page))