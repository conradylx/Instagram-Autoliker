# Instagram Autoliker

An automated bot for liking posts on Instagram using Selenium WebDriver.

## Description

This script automatically logs into Instagram, scrolls through the feed, and likes posts. It uses Selenium for browser automation and supports both English and Polish language versions of Instagram.

## Features

- Automatic Instagram login
- Cookie acceptance handling
- Feed scrolling and new post loading
- Automatic post liking (default 15 iterations)
- Multi-language interface support (EN/PL)
- Intelligent detection of unliked posts

## Requirements

- Python 3.7+
- Google Chrome (latest version)
- Instagram account

## Installation

```bash
git clone https://github.com/conradylx/Instagram-Autoliker.git
cd Instagram-Autoliker
python -m venv venv
#Activate venv - Windows
venv\Scripts\activate
#Activate venv - Linux
source venv/bin/activate
pip install -r requirements.txt
mv example.env .env
```
Then edit the .env file and fill in your credentials:
```text
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```
Run the script:
```bash
python main.py
```

The script will automatically:
- Open Chrome browser
- Log into your account
- Start liking posts in the feed
- Execute 15 cycles of scrolling and liking
- Close the browser when finished

License
MIT
