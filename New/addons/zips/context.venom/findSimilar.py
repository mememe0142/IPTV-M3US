# -*- coding: utf-8 -*-

import json
import sys
import xbmc

try:
	from urlparse import parse_qsl
except:
	from urllib.parse import parse_qsl


if __name__ == '__main__':
	item = sys.listitem
	# message = item.getLabel()
	path = item.getPath()
	# xbmc.log('path = %s' % path, 2)
	plugin = 'plugin://plugin.video.venom/'
	args = path.split(plugin, 1)
	params = dict(parse_qsl(args[1].replace('?', '')))

	imdb = params.get('imdb', '')
	action = 'tvshows' if 'tvshowtitle' in params else 'movies'

	xbmc.executebuiltin('ActivateWindow(Videos,plugin://plugin.video.venom/?action=%s&url=https://api.trakt.tv/%s/%s/related,return)' % (action, 'shows' if 'tvshows' in action else 'movies', imdb))