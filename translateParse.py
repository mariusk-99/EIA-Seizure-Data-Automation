import openai
import os
import json
from pathlib import Path

openai.api_key = os.environ.get("OPENAI_API_KEY")

input_dir = 'scraped_sites_test'
output_dir = 'extracted_data'

Path(output_dir).mkdir(parents=True, exist_ok=True)


# Instruction for API request to OpenAI LLM

instructions = """
You are an expert in translating articles and text from most languages
and extracting relevant information from them. Your task is to translate
the following text to english and extract relevant data from it. 

The response should have all the extracted fields in a json format. 
The extracted data must fill the following fields:

Country:[Where the incident happened]
Town/Village:[Where the incident happened]
Date of incident: [When the incident happened]
Title:[Town/Village], [Animal or animal parts that were seized and quantity], 
[Number of people arrested], [Date of incident]
Summary:[Summary of article/report]
Vehicle type: [Choose from: Car/Van, Bicycle, Bus, Motorbike, Tractor, Truck/Lorry, Other (specify which one)]
Transit method: [Choose from: Air-cargo, Air-passenger, Courier, Foot, Post, Road, Sea, Other (specify which one)]

Your response should strictly only have the requested response - the json fields. 
Don't include any explanations or conclusions in the beginning or end of your response.

Below is the text:

"""

def get_chat_completion(instructions, text_content, model="gpt-4"):

    prompt = f"{instructions}\n\n {text_content}"
    # Creating a message as required by the API
    messages = [{"role":"user", "content": prompt}]

    # Calling the ChatCompletion API
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0.3,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response

    

def process_file(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()

    response = get_chat_completion(instructions=instructions, text_content=text_content)

    extracted_response = response.choices[0].message["content"]

    output_file_path = os.path.join(output_dir, os.path.basename(file_path).replace('.txt', '.json'))

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(extracted_response, output_file, ensure_ascii=False, indent=4)

    print(f"Processed {file_path} -> {output_file_path}")

# Iterate over each text file in the input directory

for file_name in os.listdir(input_dir):
    if file_name.endswith('.txt'):
        file_path = os.path.join(input_dir, file_name)
        process_file(file_path)

    