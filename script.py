import gradio as gr
import modules.shared as shared
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib

search_access = False
service = Service()
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--remote-debugging-port=9222')

def google_results(query):
    
    driver = webdriver.Chrome(service=service,options=options)
    query = urllib.parse.quote_plus(query)
    url="https://www.google.com/search?hl=en&q="+query
    driver.get(url)
    html = driver.find_element(By.CLASS_NAME, 'ULSxyf').text
    driver.quit()
    return html


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
            state[
                    "context"
                ] = "The answer to User question is provided to you in Google search results. Give a truthful and correct answer. Answer the question"
            search_data = google_results(query) 
            user_prompt = f"User question: {user_input}\n Google search results: {search_data}"
            return str(user_prompt)               
    shared.processing_message = "*Typing...*"
    return user_input


def output_modifier(output):
    return output


def bot_prefix_modifier(prefix):
    return prefix