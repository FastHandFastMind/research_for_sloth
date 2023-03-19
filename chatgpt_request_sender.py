import openai
import os
import csv
import prompt_creator
import const_file.PROMPT as PROMPT
import const_file.OPENAI_API_KEY as OPENAI_API_KEY

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY.KEY
openai.api_key = os.environ["OPENAI_API_KEY"]

def making_request_toGPT(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=2000,
      n=1,
      stop=None,
      temperature=0.5,
    )
    return response.choices[0].text.strip()

def get_GPT_responses():
    lines = []
    with open('data/articles.csv','r',newline='') as csvfile:
        reader = csv.reader(csvfile)
        with open('data/chatgpt_response.csv','w') as response_file:
            writer = csv.writer(response_file)
            for row in reader:
                    try:
                        prompt = prompt_creator.create(PROMPT.SUMMARIZE_WITH_TITLE, PROMPT.LENGTH_LIMIT, "", row[0], row[1])
                        response = making_request_toGPT(prompt)
                        writer.writerow([response])
                    except:
                        response_file.write("Token is overnumbered!")
        response_file.close()
    csvfile.close()









