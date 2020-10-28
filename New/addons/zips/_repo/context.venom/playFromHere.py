# -*- coding: utf-8 -*-

import json
import sys
import xbmc

try:
	from urlparse import parse_qsl
	from urllib import quote_plus
except:
	from urllib.parse import parse_qsl, quote_plus


if __name__ == '__main__':
	item = sys.listitem
	# message = item.getLabel()
	path = item.getPath()
	# xbmc.log('path = %s' % path, 2)
	plugin = 'plugin://plugin.video.venom/'
	args = path.split(plugin, 1)
	params = dict(parse_qsl(args[1].replace('?', '')))

	year = params.get('year', '')

	if 'meta' in params:
		meta = json.loads(params['meta'])
		imdb = meta.get('imdb', '')
		tmdb = meta.get('tmdb', '')
		tvdb = meta.get('tvdb', '')
		season = meta.get('season', '')
		episode = meta.get('episode', '')
		tvshowtitle = meta.get('tvshowtitle', '').encode('utf-8', 'ignore')

	else:
		imdb = params.get('imdb', '')
		tmdb = params.get('tmdb', '')
		tvdb = params.get('tvdb', '')
		season = params.get('season', '')
		episode = params.get('episode', '')
		tvshowtitle = params.get('tvshowtitle', '')

	systvshowtitle = quote_plus(tvshowtitle)

	xbmc.executebuiltin('RunPlugin(plugin://plugin.video.venom/?action=playEpisodesList&tvshowtitle=%s&year=%s&imdb=%s&tmdb=%s&tvdb=%s&season=%s&episode=%s,return)' % (systvshowtitle, year, imdb, tmdb, tvdb, season, episode))