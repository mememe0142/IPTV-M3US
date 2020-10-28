# -*- coding: utf-8 -*-

import json
import sys
import xbmc

try:
	from urlparse import parse_qsl
	from urllib import quote_plus
except:
	from urllib.parse import parse_qsl
	from urllib.parse import quote_plus

if __name__ == '__main__':
	item = sys.listitem
	# message = item.getLabel()
	path = item.getPath()
	# xbmc.log('path = %s' % path, 2)
	plugin = 'plugin://plugin.video.venom/'
	args = path.split(plugin, 1)
	params = dict(parse_qsl(args[1].replace('?', '')))

	year = params.get('year', '')
	imdb = params.get('imdb', '')
	tmdb = params.get('tmdb', '')
	tvdb = params.get('tvdb', '')
	tvshowtitle = params.get('tvshowtitle', '')
	systvshowtitle = quote_plus(tvshowtitle)

	xbmc.executebuiltin('ActivateWindow(Videos,plugin://plugin.video.venom/?action=seasons&tvshowtitle=%s&year=%s&imdb=%s&tmdb=%s&tvdb=%s,return)' % (systvshowtitle, year, imdb, tmdb, tvdb))