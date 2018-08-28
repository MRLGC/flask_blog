import re

def parse_content(content):
    new_content = re.findall('<.*?>(.*?)</.*?>', content)
    return new_content
