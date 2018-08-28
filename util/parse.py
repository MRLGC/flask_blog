import re

def parse_content(topic):
    topic.content = re.findall('<.*?>(.*?)</.*?>', topic.content)
    return topic
