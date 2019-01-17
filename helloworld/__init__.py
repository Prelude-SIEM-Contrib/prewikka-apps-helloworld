from __future__ import absolute_import, division, print_function, unicode_literals

from prewikka import template, view

"""A HelloWorld plugin"""

class HelloWorld(view.View):
    plugin_name = "Hello World"
    plugin_author = "Antoine Luong"
    plugin_license = "GPL"
    plugin_version = "5.0.0"
    plugin_copyright = "CSSI"
    plugin_description = N_("A plugin that says hello world!")

    @view.route("/helloworld", menu=("HelloWorld", "HelloWorld"))
    def render(self):
        return template.PrewikkaTemplate(__name__, "templates/helloworld.mak").render()
