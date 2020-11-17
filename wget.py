import requests
def wget(url):
    filename = url[url.rfind('/') + 1::]
    try:
        r = requests.get(url, allow_redirects = True)
    except:
        raise ValueError('Error retrieving ' + url)
    with open(filename, 'wb') as f:
        f.write(r.content)