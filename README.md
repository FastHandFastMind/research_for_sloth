# research_for_sloth
when a sloth was assigned a research task :3

How to use this tool ?

0. Import required libs (Beautifulsoup, OpenAi, etc...)
1. Paste your link you need to do research to link.txt (inside data folder)
2. Set up your OPEN API KEY in OPENAI_API_KEY.py (inside const_file folder)
3. Run main.py and enjoy the show. 

*note: 
- an example of popular articles that this tool can handle well (articles, news with construction like this)
  https://techcrunch.com/2023/03/14/openai-releases-gpt-4-ai-that-it-claims-is-state-of-the-art/
- the content that was crawled from website will be saved in articles.csv so that you can check how well the content was crawled frow the website
- the summary of the content above will be saved in chatgpt_response.csv. You can set up your desired prompt based on some default construction that i made for you in PROMPT.py
- you can use this tool to send the summary file (chatgpt_response.csv) to a specific email. It will be a little tricky then i will introduce that later. :v
- i would be grateful if you could give some pieces of advice or recommendations to make this tool better and better
