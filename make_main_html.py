# coding: utf-8


def parse_date(string):
    s = string.split()
    return('%s %s %s' % (s[4], s[1], s[2]))


def write_html_main_layout(article_list,
                           fname='noname.html',
                           template_fname='template.html'):
    template = []
    with open(template_fname, 'r') as fid:
        # Read template
        while True:
            tmp = fid.readline()
            if tmp == '':
                # When end of file
                break
            template.append(tmp)

    # Writing html file as main layout
    with open(fname, 'w') as fid:
        # Writing template into main layout html
        for e in template:
            if e.find('!--left_panel_nav_tobefilled--') != -1:
                # Add nav things
                for j in range(len(article_list)):
                    fid.writelines('<a href="#ifh_article_%05d">\n' % j)
                    fid.writelines('%s<br>\n' %
                                   parse_date(article_list[j]['Date']))
                    fid.writelines('</a>\n')
                continue
            if e.find('!--main_panel_context_tobefilled--') != -1:
                # Add context things
                for j in range(len(article_list)):
                    fid.writelines(
                        '<div class="iframe_header" id="ifh_article_%05d" onclick="article_wrapper(this)" style="background-color: lightsteelblue; background: linear-gradient(to right, lightsteelblue, white)"> Read more of this </div>\n' % j)
                    fid.writelines(
                        '<iframe src="htmls/article_%05d_title.html", width="100%%" id="article_%05d" name="iframe" frameborder="0" scrolling="yes" onreadystatechange="resize()" onload="resize()"></iframe>\n' % (j, j))
                    fid.writelines('<a href="#ifh_article_%05d">\n' % j)
                    fid.writelines('<div>')
                    fid.writelines(
                        '<hr style="height:1px;border:none;border-top:1px solid #555555;" />\n')
                    fid.writelines(
                        '<p style="position:relative;left:70%;top:-40px; color:gray;">Click here back to title</p>\n')
                    fid.writelines('</div>')
                    fid.writelines('</a>\n')
                continue

            fid.writelines(e)
