# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# Conector para conectate
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------

import urlparse,urllib2,urllib,re
import os

from core import scrapertools
from core import logger
from core import config

def get_video_url( page_url , premium = False , user="" , password="", video_password="", page_data="" ):
    logger.info("tvalacarta.servers.conectate get_video_url(page_url='%s')" % page_url)

    data = scrapertools.cache_page(page_url)

    url = scrapertools.get_match(data,"'hd.file'\s*:\s*'([^']+)'")
    
    video_urls = []
    video_urls.append( [ "MP4 [conectate]" , url ] )

    for video_url in video_urls:
        logger.info("tvalacarta.servers.conectate %s - %s" % (video_url[0],video_url[1]))

    return video_urls

# Encuentra vídeos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []

    return devuelve
