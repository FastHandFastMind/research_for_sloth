import csv
from datetime import datetime
from newsplease import NewsPlease

def crawl(url_list):
    articles = []
    logs = []
   
    # Extract the article
    try:
        for url in url_list:
            article = NewsPlease.from_url(url)
            articles.append(article.title)
            articles.append(article.maintext.strip())
            articles.append(url)
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
