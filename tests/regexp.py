import re

page = ''
with open('data/full_web_page.data', 'r', encoding='utf-8') as data:
    page = ''.join(data.readlines())

print(type(page))
print(len(page))
pattern = re.compile(
                     r'<tr data-id=".*?"(?: class="((?:high|low)-rating)")?>\s*<td class="rating-cell">\s*.*</span>\n\s*</td>\n\s*<td class.*\n\s*<span.*>.*</span>\n\s*<span class="sub-lang">(.*)?</span>\n\s*</td>\n\s*<td>\n\s*<a href="(.*)?">'
                     ,re.UNICODE)

# print(page)
print(pattern.findall(page))
