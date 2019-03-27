from os import getenv
from telegram.ext import Updater
import requests
from time import sleep
from bs4 import BeautifulSoup
import re


def get_proxy_urls():
    url = 'http://spys.one/socks/'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    ips_and_descriptions = soup.find_all('font', class_='spy14')
    pattern_for_regex = '([0-9]{1,3}[\.]){3}[0-9]{1,3}'
    proxy_ips = []
    for ip_and_description in ips_and_descriptions:
        match = re.search(pattern_for_regex, ip_and_description.contents[0])
        if match is None:
            continue
        proxy_ips.append('{}:1080'.format(match[0]))
    return proxy_ips


def create_post_on_telegtam(path_to_picture, message_for_posting):
    token = getenv('TOKEN_FOR_TELEGRAM')
    chat_id = getenv('TELEGRAM_CHAT_ID')
    proxy_urls = get_proxy_urls()
    for proxy_url in proxy_urls:
        REQUEST_KWARGS= {'proxy_url': 'socks5://{}/'.format(proxy_url)}
        try:
            updater = Updater(token, request_kwargs=REQUEST_KWARGS)
            updater.bot.send_message(
                chat_id=chat_id,
                text=message_for_posting)
            updater.bot.send_photo(
                chat_id=chat_id,
                photo=open(path_to_picture, 'rb'))
            break
        except:
            continue
