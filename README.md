# web_search [WIP]
 Web search extension for [text-generation-webui](https://github.com/oobabooga/text-generation-webui)

 Thanks to [CyberViking](https://github.com/TheCyberViking) for the initial simple web search code. You can see it [here](https://github.com/oobabooga/text-generation-webui/discussions/932)
 
 
 This extension enables' a language model to receive google search data according to the users' input.[Currently supports google search only]


 How to use
 
 One needs to type search then what you want to search for, example:
 
 Type ```search the weather in Nairobi, Kenya today.```

 Requirements

 ```googlesearch-python``` pip package module

 How to install

1. First clone the repo to ```text-generation-webui/extensions``` folder

2. Then ```cd web_search``` and run ```pip install -r requirements.txt```

3. Add ```web_search``` to launch commands of text-generation-webui
   like so ```--extension web_search```

4. Run text-gen-webui. There will be a checkbox with label ```Use Google Search``` in chat tab, this enables or disables the extension.

5. Done

!!!Have fun!!!
   
!!!Demo photos coming soon!!!
