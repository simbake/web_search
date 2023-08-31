import gradio as gr
import modules.shared as shared
from bs4 import BeautifulSoup
import re
import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession

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
    global search_access
    if search_access:
        if user_input.lower().startswith("search"):
            shared.processing_message = "*Searching online...*"
            query = user_input.replace("search", "").strip()
            search_data = google_results(query,state)
            state[
                    "context"
                ] = "Retrieve the answer to User question in Google search results and give a relevant answer."
                
            user_prompt = f"User question: {user_input}\n Google search results: {[search_data]}"
            return str(user_prompt)               
    shared.processing_message = "*Typing...*"
    return user_input


def output_modifier(output):
    return output


def bot_prefix_modifier(prefix):
    return prefix


def print_data(data):
    return data

def google_results(query,state):
    query = urllib.parse.quote_plus(query)
    url="https://www.google.com/search?hl=en&q="+query
    try:
        session = HTMLSession()
        response = session.get(url)
        search_results = response.html.find('#rso', first=True).raw_html
        bs = BeautifulSoup(search_results, "html.parser")
        results = bs.find_all("div")
        unwanted_tags = ["script","style","noscript","a","img"]
        filtered_result = [tag.text for tag in results if tag.name not in unwanted_tags]
        soup = "\n".join(
            [
            p
            for p in filtered_result
            ]
        )
        text = soup.strip()    
        return text[:2045]
    except requests.exceptions.RequestException as e:
        print(e)
        state[
                    "context_instruct"
                ] = "Tell the user they are experiencing connection issues"
        return ""