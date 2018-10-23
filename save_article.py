# encoding: utf-8

import os
from make_fake_article import mk_article

article, title = mk_article()

article_dir = os.path.join(os.path.curdir, 'articles')

with open(os.path.join(article_dir, title+'.txt'), 'w') as fid:
    fid.write(article)
