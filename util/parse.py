import re

def parse_content(content):
    new_content = re.sub('<.*?>', '', content)
    return new_content
