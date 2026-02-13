from bs4 import BeautifulSoup

with open("website.html", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")
print(soup.title)
print(soup.title.string)
print(soup.title.name)
print(soup.body.prettify())
print(soup.a)
print(soup.find_all("p"))