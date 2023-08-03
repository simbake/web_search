import gradio as gr
import modules.shared as shared
from googlesearch import search
import requests

search_access=False

def ui():
    global search_access
    checkbox = gr.Checkbox(value=search_access, label="Enable Google Search")
    checkbox.change(fn=update_search_access, inputs=checkbox)
    return checkbox,search_access
    
def update_search_access(checkbox_value):
    global search_access
    search_access = checkbox_value    # assign the value of the checkbox to the variable
    return search_access,checkbox_value
    
def input_modifier(user_input):
    
    global search_access
    if search_access:
        
        if user_input.lower().startswith("search"):
            
            query = user_input.strip("search").strip()
            # Check if there is internet connection by sending a request to Google
            try:
                shared.processing_message = "*Checking for internet connectivity*"
                requests.get("https://www.google.com")
                internet = True
            except requests.exceptions.ConnectionError:
                internet = False
                return user_input
            if internet == True:
                shared.processing_message = "*Searching online...*"
                search_results = search(query, num_results=3)
                # Use list comprehension to create a list of texts and links from the 
                # search results
                search_data = "\n".join(search_results)
                user_input__results = f"{user_input}\n\n{search_data}"
                return user_input__results                    
    shared.processing_message = "*Typing...*"
    return user_input
    
def output_modifier(output):
    return output

def bot_prefix_modifier(prefix):
    return prefix
