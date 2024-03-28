from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
#print(soup.title)

articles = soup.find_all(name="span", class_="titleline")
#print(story.get_text())

title_list = []
link_list = []
rank_list = []

for article_tag in articles:
    story = article_tag.getText()
    title_list.append(story)
    story_link = story.get("href")
    link_list.append(story_link)
    #print(story_link)

story_votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#print(story_votes)
largest_votes = max(story_votes)
index = story_votes.index(largest_votes)
print(title_list)
print(title_list[index])
print(link_list[index])





with open("./web scraping/website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")
#print(soup.title.string)
#print(soup.prettify)
#print(soup.a.string)

all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

for tag in all_anchor_tags:
    quit
    #print(tag.getText())
    #print(tag.get("href"))

heading1 = soup.find(name="h1", id="name")
#print(heading)

section_heading = soup.find(name="h3", class_="heading")
#print(section_heading.name)

company_url = soup.select_one(selector="p a")
#print(company_url)

company_url2 = soup.select_one(selector="#name")
#print(company_url2)

headings = soup.select(".heading")
#print(headings)