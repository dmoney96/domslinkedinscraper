# domslinkedinscraper
OSINT scraper for LinkedIN, utilizing layered scraping and rotating proxies

# domslinkedinosint

INSTRUCTIONS

Dom's LinkedIN [OSINT] scraper:

This is a simple Python script that uses Selenium and BeautifulSoup to scrape information from LinkedIn profiles.

Setup
Prerequisites:
To use this script, you'll need to have the following installed on your machine:

Python 3
Chrome browser

Installation:
Clone this repository to your local machine.
Navigate to the repository directory.
Install the required Python packages by running the following command:

Copy code
[pip install -r requirements.txt]
  
Usage

Download chromedriver from the official ChromeDriver downloads page: 
https://chromedriver.chromium.org/downloads

Extract the chromedriver executable file from the downloaded archive and move it to a directory that's included in your PATH (zsh=~/.zshrc file ; bash= ~/.bashrc file). You can find a list of directories in your PATH by running the following command in your terminal:
bash
  
Copy code
[echo $PATH]

Alternatively, you can specify the location of chromedriver directly in your Python code by passing the path to the executable_path parameter when creating a new webdriver.Chrome instance. For example:
python:
  
Copy code
[driver = webdriver.Chrome(executable_path='/path/to/chromedriver')]
  
  *I put mine in my ~/.zshrc file, which is in my path, because zsh is the default terminal on the machine I use most


Update the urls list variable in the main function with the URLs of the LinkedIn profiles you want to scrape, and add in your favorite dns or other proxies by editing the main.py file, once you've cloned this repository to your machine.

In your terminal, navigate to the directory where Main.py is located and run the following command:

[python Main.py]

  
The script will log in to LinkedIn,once you've entered your username and password into your main.py file in your text editor, coding app, or with nano or vim, then it will scrape the profiles you've specified (again, in your main.py file, which you should do each time you want to scrape a different target or login with a different username and/or password), and save the data to a profiles.json file in the same directory.

 Please note that I cannot guarantee that the target you are researching won't see you looking at their page. Best to use a sock puppet account for your login and password file, so your personal LinkedIN page isn't implicated in the searches you are performing on your target.
 
 <> or [] indicates that the code to copy is within. Please do not copy the <> $ or [] into your code, as those characters are used simply as a placeholder, to indicate where the code to be copied begins and ends.
 
 **If you're looking for some safe, reliable, free DNS proxies, I'd like to recommend the DNSecure and DNSCloak tools (both have web applications or websites, as well as safe, free to use, downloadable apps for smartphones, tablets, desktops, and laptops). 
 
Contributing

  If you'd like to contribute to this project, feel free to submit a pull request or open an issue.

License:

This project is licensed under the MIT License. See the LICENSE file for details.



