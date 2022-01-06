# Installation/setup
### 1. Clone repo and change to directory
```
git clone https://github.com/ddroder/covid_test_finder.git
cd covid_test_finder
```
### 2. Installing Selenium driver.
This was written with the chrome webdriver, so install the chrome driver and take note of what directory it gets stored to. We will pass the information in later.

steps on linux:
```
wget https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip 
unzip chromedriver_linux64.zip 
sudo mv chromedriver /usr/bin/chromedriver 
sudo chown root:root /usr/bin/chromedriver 
sudo chmod +x /usr/bin/chromedriver 
```



# Usage
This works from the CLI using the main.py script. It expects two parameters:

--store (currently only walmart and cvs)
<br>--zip   (any zip code)<br>
<br>
The following are examples of how to run for different stores.

```
python3 main.py --store walmart --zip 44131
```

```
python3 main.py --store cvs --zip 44321
```


# TODO
Return prettified data 
<br>
Add email updating
<br>
Better documentation

