# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460891155.5432985
_enable_loop = True
_template_filename = '/home/antony/Documents/python/gestionKendo/web/views/templates/adherents.mako.html'
_template_uri = 'adherents.mako.html'
_source_encoding = 'ascii'
_exports = ['container']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.mako.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def container():
            return render_container(context._locals(__M_locals))
        adherents = context.get('adherents', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'container'):
            context['self'].container(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def container():
            return render_container(context)
        adherents = context.get('adherents', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div class="col-lg-12">\n        <div class="col-lg-2"></div>\n        <div class="col-lg-8">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    Les adherents\n                </div>\n                <div class="panel-body">\n                    <table class="col-lg-12">\n                        <thead>\n                        <th>Nom</th>\n                        <th>Prenom</th>\n                        <th>Date de naissance</th>\n                        <th>Action</th>\n                        </thead>\n                        <tbody>\n')
        for adherent in adherents:
            __M_writer('                        <tr>\n                            <form action="details">\n                                <td>')
            __M_writer(str(adherent.nom))
            __M_writer('</td>\n                                <td>')
            __M_writer(str(adherent.prenom))
            __M_writer('</td>\n                                <td>')
            __M_writer(str(adherent.dateNaissance))
            __M_writer('</td>\n                                <td>\n                                    <input type="hidden" name="licence" value="')
            __M_writer(str(adherent.licence))
            __M_writer('">\n                                    <input type="submit" value="Afficher detail">\n                                </td>\n                            </form>\n                        </tr>\n')
        __M_writer('                        </tbody>\n\n                    </table>\n                </div>\n            </div>\n        </div>\n        <div class="col-lg-2"></div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/antony/Documents/python/gestionKendo/web/views/templates/adherents.mako.html", "source_encoding": "ascii", "line_map": {"35": 1, "69": 63, "45": 2, "27": 0, "52": 2, "53": 20, "54": 21, "55": 23, "56": 23, "57": 24, "58": 24, "59": 25, "60": 25, "61": 27, "62": 27, "63": 33}, "uri": "adherents.mako.html"}
__M_END_METADATA
"""
