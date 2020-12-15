from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import sys
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def extractAllImgWeb(url):

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('img')

    for tag in tags:

        yield tag.get('src', None)


sys.modules[__name__] = extractAllImgWeb
