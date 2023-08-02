import scrapy.crawler
import gradio as gr
import modules.utils as utils # A module for shared functions and variables
import modules.shared as shared
from urllib.request import urlopen
import urllib.error as err

use_google_search=False
search_term=False
search_cache = {}

def ui():

    global use_google_search, search_term # Use global keyword to access global variables

    # Add a new checkbox for Google search option
    use_google_search = gr.Checkbox(label="Use Google Search", value=False)
    return [use_google_search, search_term]

def input_modifier(user_input):

    global use_google_search, internet_connected, search_cache

    if use_google_search:

        if user_input.lower().startswith("sear") or search_term:

            query = user_input.strip("sear").strip()
            # Check if there is internet connection only once by sending a request to Google
            try:
                shared.processing_message = "*Checking for internet connectivity*"
                response = urlopen('https://www.google.com', timeout=20)
                internet_connected = True
            except err:
                internet_connected = False
                shared.processing_message = "*Connection failed...*"
                return "Please check your internet connection and try again"
            if internet:
                shared.processing_message = "*Searching online...*"
                # Create a Scrapy spider class to perform the search
                class GoogleSpider(scrapy.Spider):
                    name = "google_spider"
                    start_urls = [f"https://www.google.com/search?q={query}"]

                    def parse(self, response):
                        results = response.xpath("//div[@class='g']")
                        for result in results:
                            title = result.xpath(".//h3/text()").get()
                            link = result.xpath(".//a/@href").get()
                            yield {"title": title, "link": link}

                # Run the spider and store the results in a list
                search_results = []
                process = scrapy.crawler.CrawlerProcess()
                process.crawl(GoogleSpider)
                process.start()
                for item in process.spider.crawler.stats.get_value('items_scraped'):
                    search_results.append(item)

                # Use a list comprehension to create a list of texts and links from the 
                # search results
                search_texts = [(item["title"], item["link"]) for item in search_results[:3]]

                search_output = "\n".join([f"{text}\nSource: {link}\n" for text, link in search_texts])
                shared.processing_message = "*Received results...*"
                return f"Here are some results from Google search based on your input:\n\n{search_output}"     
    shared.processing_message = "*Typing...*"
    return user_input

def output_modifier(output):
    return output

def bot_prefix_modifier(prefix):
    return prefix
