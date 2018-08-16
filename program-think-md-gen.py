#!/bin/bash/env python3
# -*- coding: utf-8 -*-


import os
import re
import shutil
import requests
import datetime
from markdownify import markdownify as md


def get_html(url):
    return (requests.get(url).content).decode('utf-8')


def get_article_title(html):
    return ((html.split('<title>')[1]).split('</title>')[0]).split('@')[0]


def get_core_content(html):
    return (html.split("<div class='post-body entry-content'>")[1]).split("<div class='post-copyright'>")[0]


def convert_html_to_md(html):
    html = html.replace('</td></td>', '</td>')    # Fixed incorrect html syntax

    table_list = re.findall(r'<center><table.*?>.*?</table></center>', html, re.S | re.M)

    table_id = 0

    while table_id < len(table_list):
        extra = ' table%03d ' % table_id
        html = html.replace(table_list[table_id], extra + table_list[table_id] + extra)
        table_id += 1

    md_text = md(html)

    table_id = 0

    while table_id < len(table_list):
        extra = 'table%03d' % table_id
        replace_table_text_list = re.findall(r'%s.*?%s' % (extra, extra), md_text, re.S | re.M)
        if replace_table_text_list is not None and len(replace_table_text_list) > 0:
            md_text = md_text.replace(replace_table_text_list[0], table_list[table_id])
        table_id += 1

    return md_text


def fix_markdown_syntax_error(md_text):
    md_text = md_text.replace('★', '## ★')
    md_text = md_text.replace('** ', '**')
    return md_text


def write_markdown_file(file_name, md_text):
    with open(file_name, 'w') as f:
        f.write(md_text)


def find_all_link(md_text):
    name_regex = "[^]]+"
    url_regex = "http[s]?://[^)]+"
    markup_regex = '\\[({0})]\\(\\s*({1})\\s*\\)'.format(name_regex, url_regex)

    return re.findall(markup_regex, md_text)


def make_directory(directory, force_empty=False):
    if force_empty and os.path.exists(directory) and os.path.isdir(directory):
        shutil.rmtree(directory)
    if not os.path.exists(directory):
        os.system('mkdir -p ' + directory)


def extract_image_name_from_link(link):
    return (link.split('//')[1]).split('/')[1]


def download_single_image(link, image_save_path):
    r = requests.get(link, stream=True)

    if r.status_code == 200:
        with open(image_save_path + extract_image_name_from_link(link), 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


def download_all_image(image_save_path, matched_links_list):
    make_directory(image_save_path)

    for link in matched_links_list:
        if link[0] == '不见图 请翻墙':
            # print('Downloading image: %s' % link[1])
            download_single_image(link[1], image_save_path)


def replace_image_link_in_markdown_text(md_text, image_save_path, matched_links_list):
    for link in matched_links_list:
        if link[0] == '不见图 请翻墙':
            # print('Replacing image link: %s' % link[1])
            md_text = md_text.replace(link[1], image_save_path + extract_image_name_from_link(link[1]))
    return md_text


def get_md_name_from_url(url):
    split_list = url.split('/')
    return ((split_list[len(split_list) - 1]).split('.html')[0]) + '.md'


def url_to_markdown(url):
    print('Processing url: %s' % url)
    image_save_path = "images/"
    html = get_html(url)
    md_text = fix_markdown_syntax_error(convert_html_to_md(get_core_content(html)))
    matched_links_list = find_all_link(md_text)
    download_all_image(image_save_path, matched_links_list)
    md_text = replace_image_link_in_markdown_text(md_text, image_save_path, matched_links_list)
    title_name = md(get_article_title(html)).replace('/', '-')
    md_text = '# ' + title_name + '\n\n-----\n\n' + md_text
    write_markdown_file(title_name.strip(' ') + '.md', md_text)


def test_url_to_markdown():
    # url = 'https://program-think.blogspot.com/2018/08/USA-Containment-Strategies-in-Cold-War.html'
    url = 'https://program-think.blogspot.com/2009/05/how-to-break-through-gfw.html'
    url_to_markdown(url)


def find_article_links_in_url(url):
    html = get_html(url)
    pattern = re.compile(r"<h1 class='post-title entry-title'>\n<a href='(.*)'>")
    match_list = pattern.findall(html)
    return match_list


def get_current_year_and_month():
    now = datetime.datetime.now()
    return now.year, now.month


def construct_search_link(year, month):
    return 'https://program-think.blogspot.com/%04d/%02d/' % (year, month)


def download_all_articles_in_url_list(url_list):
    for url in url_list:
        url_to_markdown(url)


def search_and_download_all_articles():
    year = 2009
    month = 1
    current_year, current_month = get_current_year_and_month()

    while year <= current_year:
        year_dir = '%04d' % year
        make_directory(year_dir, True)
        os.chdir(year_dir)
        while ((year != current_year and month <= 12) or (year == current_year and month <= current_month)):
            print("Getting articles in %04d-%02d ......" % (year, month))
            search_url = construct_search_link(year, month)
            month_dir = '%02d' % month
            make_directory(month_dir, True)
            os.chdir(month_dir)
            download_all_articles_in_url_list(find_article_links_in_url(search_url))
            os.chdir('../')
            month += 1
        os.chdir('../')
        month = 1
        year += 1
    print('Done !')


if __name__ == '__main__':
    # test_url_to_markdown()
    # find_article_links_in_url('https://program-think.blogspot.com/2018/07/')
    search_and_download_all_articles()
