# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460154029.549683
_enable_loop = True
_template_filename = 'C:/Users/Robin/Desktop/6nations/web/views/templates/base.html'
_template_uri = 'base.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html lang="fr">\n<head>\n    <meta charset="UTF-8">\n    <title>Tournoi des 6 nations</title>\n    <link href="/static/css/bootstrap.min.css" rel="stylesheet">\n</head>\n<body>\n<nav class="navbar navbar-inverse navbar-fixed-top">\n    <div class="container">\n        <div class="navbar-header">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar"\n                    aria-expanded="false" aria-controls="navbar">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="#">Gestion Kendo</a>\n        </div>\n        <div id="navbar" class="collapse navbar-collapse">\n            <ul class="nav navbar-nav">\n                <li class="active"><a href="#">Adherents</a></li>\n                <li><a href="#about">Professeurs</a></li>\n            </ul>\n        </div><!--/.nav-collapse -->\n    </div>\n</nav>\n<div class="container">\n\n</div>\n<script src="/static/js/jquery.min.js"></script>\n<script src="/static/js/bootstrap.min.js"></script>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/web/views/templates/base.html", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "base.html"}
__M_END_METADATA
"""
