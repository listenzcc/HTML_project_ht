# coding: utf-8

import os

article_dir = 'articles'
html_dir = 'htmls'

article_name_list = list(os.path.join(article_dir, e)
                         for e in os.listdir(article_dir))


def parse_article(fname):
    # Parse article into article dict
    article = {}
    with open(fname, 'r') as fid:
        # Parse components, assuming article is well formed
        article['Title'] = fid.readline().split(':', maxsplit=1)[1].strip()
        article['Author'] = fid.readline().split(':', maxsplit=1)[1].strip()
        article['Data'] = fid.readline().split(':', maxsplit=1)[1].strip()
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


def write_as(fid, string, label, style=''):
    # Write string in fid as label
    fid.write('<%s style=\"%s\">%s</%s>\n' %
              (label, style, string, label))


def article_to_html(article, article_name):
    # Write html from article dict
    with open(article_name+'_title.html', 'w') as fid:
        write_as(fid, article['Title'], 'h1')
        write_as(fid, article['Author'], 'span')
        write_as(fid, article['Data'], 'span',
                 'float:right; padding-right:20px')
        write_as(fid, article['Abstract'], 'p', 'text-align:justify')
        write_as(fid, 'Keywords:', 'span',
                 'font-size:larger')
        for e in article['Keywords']:
            write_as(fid, e, 'span', 'font-style:oblique')
    with open(article_name+'_context.html', 'w') as fid:
        for e in article['Context']:
            write_as(fid, e, 'p')
        write_as(fid, 'Article ends', 'p', 'color:gray; font-style:oblique')


article = parse_article(article_name_list[0])

article_to_html(article, os.path.join(
    html_dir, article['Title']))

for e in article.items():
    print(e)
