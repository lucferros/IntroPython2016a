#!/usr/bin/env python

"""
Python class example.
"""


# The start of it all:
# Fill it all in here.
class Element(object):

    def __init__(self, content=None):
        self.content  = '<!DOCTYPE html>\n'

    def append(self, new_content):
        self.content += new_content

    def render(self, file_out, ind=""):
        file_out.write(self.content)

class Html(Element):

    def __init__(self, content=None):
        self.content = '\t<html>\n'


class Body(Element):

    def __init__(self, content=None):
        self.content = '\t\t<body>\n'
