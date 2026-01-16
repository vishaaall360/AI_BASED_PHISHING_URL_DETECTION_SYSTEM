import re
from urllib.parse import urlparse

def extract_features(url):
    return [
        len(url),
        url.count('.'),
        url.count('-'),
        url.count('@'),
        url.count('?'),
        url.count('%'),
        url.count('/'),
        int('https' not in url),
        int(bool(re.search(r'\d', url)))
    ]
