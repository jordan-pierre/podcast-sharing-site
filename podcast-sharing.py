import requests
import re


def podcast_sharing():
    # -- Provide a 'share podcast' URL
    # TODO: Change input_url to either be read from console, clipboard, or Django web app.
    # TED Radio Hour (no hyphen in name)
    input_url = 'https://podcasts.google.com/?feed=aHR0cHM6Ly93d3cubnByLm9yZy90ZW1wbGF0ZXMvcnNzL3BvZGNhc3QucGhwP2lkPTUxMDI5OA&episode=YTM0YWEwMWQtZWM5MS00NzM5LWEyY2UtODQ0YjQzZjg5NGJk'
    # Tim Ferriss show (hyphen in name)
    input_url = 'https://podcasts.google.com/?feed=aHR0cHM6Ly9yc3MuYXJ0MTkuY29tL3RpbS1mZXJyaXNzLXNob3c&episode=Z2lkOi8vYXJ0MTktZXBpc29kZS1sb2NhdG9yL1YwLzJvSHJURnZGcWU1TEJOSVNvY0tKbWdBVXo2ODJaUFp1M29uZjFVcmZxOFE'

    # -- Get the HTML from the URL provided
    input_html = requests.get(input_url).text

    # -- Use the URL to tell which platform it's from
    if "podcasts.google.com" in input_url:
        show, episode = get_google_podcast_info(input_html)
    elif "podcasts.apple.com" in input_url:
        #  show, episode = get_apple_podcast_info(input_html) TODO: Add Apple Podcasts function
    elif "open.spotify.com" in input_url:
        #  TODO: Add Spotify function
    elif "overcast.fm" in input_url:
        #  TODO: Add Overcast function
    elif "castro.fm" in input_url:
        #  TODO: Add Castro function
    elif "pca.st" in input_url:
        #  TODO: Add PocketCasts function
    else:
        #  TODO: Raise unsupported site exception
    #  TODO: Raise invalid URL exception
    print(show, episode)

    # -- Select the output URL platform
    # TODO: Make a select from list feature either in console or browser.
    output_platform = 'Apple'

    # -- Use Podcast show name and episode name to search for the specific episode
    new_url = get_new_url(show, episode, output_platform)

    # -- Print new_url, print to clipboard, or add to a class variable (if using Django web app)
    # TODO: Post new URL somewhere

def get_google_podcast_info(html):
    # -- Scrape Google Podcasts site for the name of Podcast show and episode.
    page_title = re.search('<title>(.+?)</title>', html).group(1)
    show = page_title.split('-')[0]
    episode = page_title.split('-')[1:]  # in case the title has more than one '-'
    episode = ''.join(episode)
    return show, episode

def get_new_url(show, episode, output_platform):
    new_url = 'example.com'
    # FIXME: DOESN'T SEEM POSSIBLE TO SEARCH WITHIN ITUNES STORE, GOOGLE PODCASTS, ETC FROM BROWSER.
    return new_url

if __name__ == '__main__':
    podcast_sharing()
