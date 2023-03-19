import const_file.PROMPT as PROMPT

def create (summary, length, method, row0, row1):
    prompt = summary + row0 + length + method + PROMPT.NO_CHEATING + row1
    return prompt
