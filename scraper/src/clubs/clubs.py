import requests
import re
from bs4 import BeautifulSoup

URL = "http://www.thedsu.ca/club-collective/"
r = requests.get(URL)
club_type = []
clubs = []
club = {
    "name": "",
    "email": "",
    "president": "",
    "url": "",
    "description": "",
    "location": "",
    "club_type": ""
}


def runClubTypes(url):
    i = 1
    print(url + 'page/' + str(i))
    while requests.get(url + 'page/' + str(i)).ok:
        req = requests.get(url + 'page/' + str(i))
        beauty = BeautifulSoup(req.content, 'html.parser')
        i += 1
        for club_item in beauty.findAll('a', attrs={'class': 'grid-item'}):
            print(club_item.get('href'))
            request = requests.get(club_item.get("href"))
            if request.ok:
                beautify = BeautifulSoup(request.content, "html.parser")
                club["name"] = club_item.get("href")[45:-1]
                club["email"] = beautify.find("div", attrs={"class": "campaign-contact-wrapper"}).a["href"][7:].strip()
                elementDiv = beautify.find("div", attrs={"class": "campaign-contact-wrapper"})
                element = elementDiv.p.getText()
                president = re.sub("\r\n|\n|\r|\t", "", element[16:])
                club["president"] = president[0:(president.find("Email"))]
                club["url"] = club_item.get("href")
                club["description"] = re.sub("\xa0", " ", cleanhtml(
                    str(beautify.find("div", attrs={"class": "plain-content-wrapper"}))).strip())
                locationDiv = beautify.find("span", text=re.compile("Location"), attrs={"class": "sub-heading"})
                locationP = locationDiv.findParent().getText() if locationDiv else ""
                location = re.sub("\r\n|\n|\r|\t|Location", "", locationP)
                club["location"] = location
                club["club_type"] = url[47:-1]
                print(club)
                clubs.append(club)


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    regex = re.compile(r'[\n\r\t]')
    cleantext = regex.sub(" ", raw_html)
    cleantext = re.sub(cleanr, '', cleantext)
    return cleantext


if r.ok:
    soup = BeautifulSoup(r.content, 'html.parser')
    grid = soup.find('ul', attrs={'class': 'block-grid-3'})

    for link in grid.findAll('a', attrs={'class': 'grid-item'}):
        club_type.append(link.get('href'))

    for page in club_type:
        runClubTypes(page)
        print("Clubs are now collected")
else:
    print(r.status_code)

print(len(clubs))