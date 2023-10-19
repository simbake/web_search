import gradio as gr
import modules.shared as shared
from googlesearch import search
from bs4 import BeautifulSoup
import re
import requests

search_access = False


def ui():
    global search_access
    checkbox = gr.Checkbox(value=search_access, label="Enable Google Search")
    checkbox.change(fn=update_search_access, inputs=checkbox)
    return checkbox, search_access


def update_search_access(checkbox_value):
    global search_access
    search_access = checkbox_value  # assign the value of the checkbox to the variable
    return search_access, checkbox_value


def input_modifier(user_input, state):
    # print(state['context'])
    global search_access
    if search_access:
        if user_input.lower().startswith("search"):
            shared.processing_message = "*Searching online...*"
            try:
                
                query = user_input.replace("search", "").strip()
                search_results = search(query, num_results=1)
                search_data = [(get_text(result), result) for result in search_results]
                state[
                    "context"
                ] = "Summarize the online results and answer the question correctly, provide links where necessary"
                user_prompt = f"{user_input}\n online results: {search_data[0]}"
                print(f"{user_prompt}")
                return user_prompt
            except Exception as e:
                # print the type and message of the exception
                print(type(e), e)
                state[
                    "context_instruct"
                ] = "Tell the user they are experiencing connection issues"
                return ""

    shared.processing_message = "*Typing...*"
    return user_input


def output_modifier(output):
    return output


def bot_prefix_modifier(prefix):
    return prefix

def get_text(url):
    response = requests.get(url)
    soup = "\n".join(
        [
            p.text
            for p in BeautifulSoup(response.text, "html.parser").find_all(
                ["section", "p"]
            )
        ]
    )
    soup = soup[:2044]
    text = re.sub(r"\s+", " ", soup.strip())
    output = "\n".join([text, f" -Source: {response.url}"])
    return output
