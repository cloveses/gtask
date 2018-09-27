#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import settings
from tornado import web, httpserver, ioloop
from tweb.url_map import load_handlers
import tornado.wsgi

handlers,domain_handlers = load_handlers(settings.HDL_DIR)

application = tornado.wsgi.WSGIApplication(handlers, **settings.web_server)
for (host_pattern, handlers) in domain_handlers:
    application.add_handlers(host_pattern, handlers)
