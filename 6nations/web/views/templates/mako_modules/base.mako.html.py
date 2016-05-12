# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1462997962.1806073
_enable_loop = True
_template_filename = 'C:/Users/Robin/Desktop/6nations/web/views/templates/base.mako.html'
_template_uri = 'base.mako.html'
_source_encoding = 'ascii'
_exports = ['container']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def container():
            return render_container(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html lang="fr">\n<head>\n    <meta charset="UTF-8">\n    <title>Tournoi des 6 nations</title>\n    <link href="/static/css/bootstrap.min.css" rel="stylesheet">\n    <link href="/static/css/style.css" rel="stylesheet">\n</head>\n<body>\n<nav class="navbar navbar-inverse navbar-fixed-top">\n    <div class="container">\n        <div class="navbar-header">\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar"\n                    aria-expanded="false" aria-controls="navbar">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="#">Gestion 6 Nations</a>\n        </div>\n        <div id="navbar" class="collapse navbar-collapse">\n            <ul class="nav navbar-nav">\n                <li class="active"><a href="#">Equipes</a></li>\n                <li><a href="#about">Matchs</a></li>\n            </ul>\n        </div><!--/.nav-collapse -->\n    </div>\n</nav>\n<div id="body">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'container'):
            context['self'].container(**pageargs)
        

        __M_writer('\n</div>\n<script src="/static/js/jquery-1.12.3.min.js"></script>\n<script src="/static/js/bootstrap.min.js"></script>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "34": 31, "23": 1, "40": 31, "28": 32, "46": 40}, "filename": "C:/Users/Robin/Desktop/6nations/web/views/templates/base.mako.html", "source_encoding": "ascii", "uri": "base.mako.html"}
__M_END_METADATA
"""
