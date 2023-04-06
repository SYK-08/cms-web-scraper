from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape_csv.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'yt-video-link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    # prints the first heading text of the website if not used with 'find_all'
    print("\n", headline)

    summary = article.find('div', class_="entry-content").text
    print(summary)

    try:
        # accessing the source of the embed video link of the website
        vid_src = article.find('iframe', class_="youtube-player")['src']
        vid_id = vid_src.split('?')[0]
        vid_id = vid_id.split('/')[4]  # required video id
        link_temp = "https://www.youtube.com/watch?v="
        yt_link = f"{link_temp}{vid_id}"
    except Exception as e:
        yt_link = None

    print("Link to the video:", yt_link)

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
