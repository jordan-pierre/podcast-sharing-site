import requests
import os
import re
from datetime import datetime

def podcast_sharing():
    # Ted radio hour (no hyphen in name)
    input_url = 'https://podcasts.google.com/?feed=aHR0cHM6Ly93d3cubnByLm9yZy90ZW1wbGF0ZXMvcnNzL3BvZGNhc3QucGhwP2lkPTUxMDI5OA&episode=YTM0YWEwMWQtZWM5MS00NzM5LWEyY2UtODQ0YjQzZjg5NGJk'

    # Tim Ferriss show (hyphen in name)
    input_url = 'https://podcasts.google.com/?feed=aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL3RpbS1mZXJyaXNzLXNob3c&episode=Z2lkOi8vYXJ0MTktZXBpc29kZS1sb2NhdG9yL1YwLzJvSHJURnZGcWU1TEJOSVNvY0tKbWdBVXo2ODJaUFp1M29uZjFVcmZxOFE'
    input_html = requests.get(input_url).text
    # -- if 'podcasts.google.com' then do Google podcasts method
    if "podcasts.google.com" in input_url:
        show, episode = get_google_podcast_info(input_html)

    print(show, episode)


def get_google_podcast_info(html):
    page_title = re.search('<title>(.+?)</title>', html).group(1)
    show = page_title.split('-')[0]
    episode = page_title.split('-')[1:]  # in case the title has more than one '-'
    episode = ''.join(episode)
    return show, episode


if __name__ == '__main__':
    podcast_sharing()
