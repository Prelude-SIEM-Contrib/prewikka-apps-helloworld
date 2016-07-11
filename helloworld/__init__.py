"""A HelloWorld plugin"""
from prewikka import view


class HelloWorld(view.View):
    """The view that displays Hello World"""
    plugin_name = "Hello World"
    plugin_author = "Antoine Luong"
    plugin_license = "GPL"
    plugin_version = "1.0.0"
    plugin_copyright = "CSSI"
    plugin_description = "A plugin that says hello world!"
    view_name = "Hello"
    view_section = "Hello"

    def render(self):
        return "<div>Hello World!</div>"
