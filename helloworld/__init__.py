from __future__ import absolute_import, division, print_function, unicode_literals

from prewikka import version, view, template

"""A HelloWorld plugin"""

class HelloWorld(view.View):
    plugin_name = "Hello World"
    plugin_author = "Antoine Luong"
    plugin_license = version.__license__
    plugin_version = version.__version__
    plugin_copyright = version.__copyright__
    plugin_description = N_("A plugin that says hello world!")

    @view.route("/helloworld", menu=(N_('HelloWorld'), N_('HelloWorld')))
    def render(self):
        return template.PrewikkaTemplate(__name__, "templates/helloworld.mak").render()
