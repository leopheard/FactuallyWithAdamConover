from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "https://rss.art19.com/factually-with-adam-conover"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://content.production.cdn.art19.com/images/65/f6/0d/14/65f60d14-3e56-4504-ba10-abe17c25856b/aee12f75e9cb30d31b7e0c41c2a5bc7b9bc19ab95a8e3b29b395b4d806de5a00932bd36960f7201d0142e049c55fb9933192e3b5cd8847485716e9db04814ee6.jpeg"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('latest_episodes'),
            'thumbnail': "https://content.production.cdn.art19.com/images/65/f6/0d/14/65f60d14-3e56-4504-ba10-abe17c25856b/aee12f75e9cb30d31b7e0c41c2a5bc7b9bc19ab95a8e3b29b395b4d806de5a00932bd36960f7201d0142e049c55fb9933192e3b5cd8847485716e9db04814ee6.jpeg"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/latest_episodes/')
def latest_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

if __name__ == '__main__':
    plugin.run()
