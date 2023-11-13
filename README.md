No longer maintained. I no longer have hardware to run language models, someone else should fork and continue development.
# web_search
 Web search extension for [text-generation-webui](https://github.com/oobabooga/text-generation-webui)

 Thanks to [TheCyberViking](https://github.com/TheCyberViking) for the initial simple web search code. You can see it [here](https://github.com/oobabooga/text-generation-webui/discussions/932)

 | ![Screenshot from 2023-09-02 16-50-05](https://github.com/simbake/web_search/assets/6049383/513d9b46-5354-4970-a09c-4fbfd4bc61e4) | ![Screenshot from 2023-09-02 16-48-47](https://github.com/simbake/web_search/assets/6049383/f26caad6-d89e-43c8-b7e6-a6b35806c491) |
 |:---:|:---:|
| ![Screenshot from 2023-09-02 16-45-22](https://github.com/simbake/web_search/assets/6049383/36c52e5a-4146-444e-b254-ed7c48a0e946) |![Screenshot from 2023-09-02 16-43-01](https://github.com/simbake/web_search/assets/6049383/d09fa1f0-a1b1-4f45-adb3-9c9b1c517246) |

 
 This extension enables' a language model to receive google search data according to the users' input.[Currently supports google search only]


 How to use
 
 One needs to type search then what you want to search for, example:
 
 Type ```search the weather in Nairobi, Kenya today.```

 Requirements

 - Google chrome browser

 How to install

*** Make sure to run these commands in the cmd script that came with text-generation-webui. eg ```cmd_linux.sh```(Linux) ***

1. First clone the repo to ```text-generation-webui/extensions``` folder

2. Then ```cd web_search``` and run ```pip install -r requirements.txt```

3. Add ```web_search``` to launch commands of text-generation-webui
   like so ```--extension web_search```

4. Run text-gen-webui. There will be a checkbox with label ```Use Google Search``` in chat tab, this enables or disables the extension.

5. Done

!!!Have fun!!!
