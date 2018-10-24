# coding: utf-8

import os
import random
import time
from make_main_html import write_html_main_layout

article_dir = 'articles'
html_dir = 'htmls'
pic_dir = os.path.join('resources', 'pics')

article_name_list = list(os.path.join(article_dir, e)
                         for e in os.listdir(article_dir))


def parse_article(fname):
    # Parse article into article dict
    article = {}
    with open(fname, 'r') as fid:
        # Parse components, assuming article is well formed
        article['Title'] = fid.readline().split(':', maxsplit=1)[1].strip()
        article['Author'] = fid.readline().split(':', maxsplit=1)[1].strip()
        article['Date'] = fid.readline().split(':', maxsplit=1)[1].strip()
        article['Abstract'] = fid.readline().split(':', maxsplit=1)[1].strip()
        article['Keywords'] = fid.readline().split(': ')[1].split(',')
        # Parse context into context list
        context = []
        while True:
            tmp = fid.readline()
            if tmp == '':
                # When end of file
                break
            context.append(tmp)
    article['Context'] = context
    return article


def pick_pic(pic_dir=pic_dir):
    return os.path.join('..', pic_dir,
                        random.choice(os.listdir(pic_dir)))


def write_as(fid, string, label, style=''):
    # Write string in fid as label
    fid.write('<%s style=\"%s\">%s</%s>\n' %
              (label, style, string, label))


def article_to_html(article, article_name):
    # Write html from article dict
    with open(article_name+'_title.html', 'w') as fid:
        # Title
        write_as(fid, article['Title'], 'h1', 'text-align:center')

        # Picture
        fid.write('<div style=\"text-align: center\">')
        fid.write('<img src=\"%s\" width=\"80%s\"\>\n' % (pick_pic(), '%'))
        fid.write('</div>')

        # Author and Date
        write_as(fid, article['Author'], 'span',
                 'float:left; padding-left:50px')
        write_as(fid, article['Date'], 'span',
                 'float:right; padding-right:50px')

        # Abstract
        write_as(fid, article['Abstract'], 'p',
                 'float:left; text-align:justify')
        # Keyword
        write_as(fid, 'Keywords:', 'span',
                 'font-size:larger')
        for e in article['Keywords']:
            write_as(fid, e, 'span', 'font-style:oblique')

    with open(article_name+'_context.html', 'w') as fid:
        for e in article['Context']:
            write_as(fid, e, 'p')
        write_as(fid, 'Article ends', 'p', 'color:gray; font-style:oblique')


article_num = len(article_name_list)
# Building article list
article_list = []
for j in range(article_num):
    article = parse_article(article_name_list[j])
    # Calculate time stamp as tDate
    article['tDate'] = time.mktime(time.strptime(article['Date']))
    article_list.append(article)

# Sort article list using time stamp
article_list = sorted(article_list, key=lambda e: e['tDate'], reverse=True)

# Make sure article list sorted well
for e in article_list:
    print(e['Date'])
    print(e['tDate'])

# Writing html in simple name
for j in range(article_num):
    article_to_html(article_list[j], os.path.join(
        html_dir, 'article_%05d' % j))

write_html_main_layout(article_list)
