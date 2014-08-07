#!/usr/bin/env python

import cgi
import cgitb
cgitb.enable()

def formprocessor(
    environ,
    start_response):
    response_body = 'The request method was %s' % environ['REQUEST_METHOD']
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

# form=cgi.FieldStorage()
# text=form["Comment"].value
# print cgi.escape(text) >> test.rst
