import link_reader
import article_crawler
import chatgpt_request_sender
import mail_sender

url_list = link_reader.read()
article_crawler.crawl(url_list)
chatgpt_request_sender.get_GPT_responses()
# mail_sender.send() 



