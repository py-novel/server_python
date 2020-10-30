from urllib.parse import urlparse

def get_url_prefix(target_url):
    parsed_result = urlparse(target_url)
    protocol = parsed_result.scheme
    domain = parsed_result.hostname
    url_prefix = f'{protocol}://{domain}'
    return url_prefix