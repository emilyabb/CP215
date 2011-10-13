import urllib2


def extract_links(html_text):
    pass


def crawl(starting_url):
    urls = [starting_url]

    while len(urls) > 0:
        url = urls.pop()

        url_object = urllib2.urlopen(url)
        html_text = url_object.read()
        
        new_urls = extract_links(html_text)
        urls += new_urls
