from bs4 import BeautifulSoup as bs
import os

# return baseurl
# e.g., '/' if local, '~yixuezhao' if on my server
def get_baseurl_from_config():
    config_file = 'config/_default/config.toml'
    with open(config_file) as file:
        for line in file:
            if 'baseurl' in line and not '#' in line:
                baseurl = line.split('\"')[1]
                return baseurl.replace('/', '')

# filepath: public/mentoring/index.html
# baseurl: ~yixuezhao
# path_to_update: 'js/load-photoswipe.js'
def add_baseurl_to_html(filepath, baseurl):
    # Open the HTML in which you want to make changes
    html = open(filepath)
    # Parse HTML file in Beautiful Soup
    soup = bs(html, 'html.parser')

    # update '/js/load-photoswipe.js'
    old_text = soup.find('script', {'src': '/js/load-photoswipe.js'})
    if old_text is None:
        raise ValueError('/js/load-photoswipe.js', 'not found, please check file:', filepath)
    new_text = '/' + os.path.join(baseurl, 'js/load-photoswipe.js')
    # replace old text with new text
    old_text['src'] = new_text

    # update '/css/hugo-easy-gallery.css'
    old_text = soup.find('link', {'href': '/css/hugo-easy-gallery.css'})
    if old_text is None:
        raise ValueError('/css/hugo-easy-gallery.css', 'not found, please check file:', filepath)
    new_text = '/' + os.path.join(baseurl, 'css/hugo-easy-gallery.css')
    # replace old text with new text
    old_text['href'] = new_text

    # Alter HTML file to see the changes done
    with open(filepath, 'wb') as f_output:
        f_output.write(soup.prettify("utf-8"))
    
    print('Done! :) replaced file', filepath)
    



if __name__ == '__main__':
    baseurl = get_baseurl_from_config()
    print('baseurl is:', baseurl)
    add_baseurl_to_html('public/mentoring/index.html', baseurl)
    add_baseurl_to_html('public/misc/index.html', baseurl)

    