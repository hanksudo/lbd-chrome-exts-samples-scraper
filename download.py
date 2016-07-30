import os
import urllib2
from bs4 import BeautifulSoup

ZIP_PATH = "zips"
BASE_URL = "https://developer.chrome.com/extensions/"
SAMLES_URL = BASE_URL + "samples"


def download_zip(path):
    try:
        filename = path.split("/")[-1]
        with open("{}/{}".format(ZIP_PATH, filename), "w") as f:
            f.write(urllib2.urlopen(BASE_URL + path).read())
    except Exception as e:
        print e


def main():
    if not os.path.exists(ZIP_PATH):
        os.mkdir(ZIP_PATH)

    # download page
    with open("samples.html", "w") as f:
        f.write(urllib2.urlopen(SAMLES_URL).read())

    with open("samples.html") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    for sample in soup.select(".sample"):
        a_link = sample.h2.a
        print "Downloading: {} ...".format(a_link.renderContents())
        download_zip(a_link.get("href"))


if __name__ == "__main__":
    main()
