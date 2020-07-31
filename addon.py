from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://rss.art19.com/nosleep"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://content.production.cdn.art19.com/images/db/11/0f/ef/db110fef-6de8-46ec-b654-5b9579bdebad/94c86043b285dd04bfad3dbceba9956df37fa8baaa168ef6de45dfc05967f9195c3c2027bc558e361af1fb8f61d9ce76004b17355ed507f1870554ee0eebe084.jpeg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://content.production.cdn.art19.com/images/db/11/0f/ef/db110fef-6de8-46ec-b654-5b9579bdebad/94c86043b285dd04bfad3dbceba9956df37fa8baaa168ef6de45dfc05967f9195c3c2027bc558e361af1fb8f61d9ce76004b17355ed507f1870554ee0eebe084.jpeg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
