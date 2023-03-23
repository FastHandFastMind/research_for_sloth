import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime


def crawl(url_list):
    articles = []
    logs = []

    for url in url_list:
        content= ''
        # Make a request to the website and get the HTML content
        response = requests.get(url.strip())
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the title and article content
        try:
            title = soup.find('h1').get_text()
            if title == '':
                title = soup.find('h2').get_text()
        except:
            title = "Unknown title"
            
        try:
            nb_p = soup.find_all('p')
            print(len(nb_p))
            threshold = len(nb_p)/2

            div_main_content_class = ""
            for div in soup.find_all('div', {'class': True}):
                list_of_p = div.findAll('p')
                if len(list_of_p) > threshold:
                    for p in list_of_p:
                        content = content+p.get_text().strip()
                    articles.append(title)
                    articles.append(content)
                    articles.append(url)
                    break
        except:
            logs.append(url)
            
    # Save the articles into a csvfile
    with open('data/articles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(0, len(articles), 3):
            writer.writerow([articles[i],articles[i+1],articles[i+2]])
    csvfile.close()

    # Save the link that cannot be accessed to a logfile
    with open('data/log.txt', 'w') as logfile:
        if len(logs) > 0 :
            now = datetime.now()
            logfile.write(now.strftime("%m/%d/%Y, %H:%M:%S")+"\n")
            for log in logs:
                logfile.write(log+"\n")
            logfile.write("*****************")
    logfile.close()
