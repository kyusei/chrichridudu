# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1461150665.291091
_enable_loop = True
_template_filename = '/home/antony/Documents/python/gestionKendo/web/views/templates/details.equipe.mako.html'
_template_uri = 'details.equipe.mako.html'
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
        grades = context.get('grades', UNDEFINED)
        adherent = context.get('adherent', UNDEFINED)
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
        grades = context.get('grades', UNDEFINED)
        adherent = context.get('adherent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div class="col-lg-12">\n        <div class="col-lg-2"></div>\n        <div class="col-lg-8">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    Adherent\n                </div>\n                <div class="panel-body">\n                    <p>Nom : ')
        __M_writer(str(adherent.nom))
        __M_writer('</p>\n                    <p>Prenom : ')
        __M_writer(str(adherent.prenom))
        __M_writer('</p>\n                    <p>Date de naissance : ')
        __M_writer(str(adherent.dateNaissance))
        __M_writer('</p>\n                    <div class="row">\n                        <div class="col-lg-12">\n                            <div class="panel panel-default">\n                                <div class="panel-heading">\n                                    Grades\n                                </div>\n                                <div class="panel-body">\n')
        for grade in grades:
            __M_writer('                                    <p>')
            __M_writer(str(grade.libelle))
            __M_writer('</p>\n')
        __M_writer('                                </div>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n            <div class="col-lg-2"></div>\n        </div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 23, "65": 25, "27": 0, "36": 1, "71": 65, "46": 2, "54": 2, "55": 12, "56": 12, "57": 13, "58": 13, "59": 14, "60": 14, "61": 22, "62": 23, "63": 23}, "filename": "/home/antony/Documents/python/gestionKendo/web/views/templates/details.equipe.mako.html", "uri": "details.equipe.mako.html"}
__M_END_METADATA
"""
