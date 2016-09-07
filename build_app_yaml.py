#!/usr/bin/env python2
"""Build an app.yaml file given various snippets."""

import collections

import yaml


def dict_representer(dumper, data):
    """Representer to dump OrderedDict in the correct order."""
    return dumper.represent_dict(data.iteritems())
yaml.add_representer(collections.OrderedDict, dict_representer)


EXTRA_HEADERS = [
    ('X-Narwhal', 'A small arctic whale. The male has a long tusk.'),
]

EXTENSION_MIME = [
    # html
    ('html', 'text/html'),
    ('css', 'text/css'),
    ('js', 'application/javascript'),
    # source code
    ('c', 'text/x-c'),
    ('h', 'text/x-c'),
    ('py', 'text/x-python'),
    # text / markup
    ('txt', 'text/plain'),
    ('md', 'text/x-markdown'),
    ('rst', 'text/x-rst'),
    ('xml', 'application/xml'),
    ('xsl', 'application/xml'),
    # documents
    ('pdf', 'application/pdf'),
    # fonts
    ('eot', 'application/vnd.ms-fontobject'),
    ('otf', 'application/font-otf'),
    ('ttf', 'application/font-ttf'),
    ('woff', 'application/font-woff'),
    ('woff2', 'application/font-woff2'),
    # images
    ('ico', 'image/x-icon'),
    ('jpg', 'image/jpeg'),
    ('svg', 'image/svg+xml'),
    # videos
    ('mp4', 'video/mp4'),
]

EXTENSION_TO_EXPIRATION = {
    'mp4': '27d',
    'eot': '27d',
    'otf': '27d',
    'ttf': '27d',
    'woff': '27d',
    'woff2': '27d',
}

BASE = [
    ('application', 'www-gwax'),
    ('version', 'master'),
    ('runtime', 'python27'),
    ('api_version', 1),
    ('threadsafe', True),
    ('default_expiration', '10m'),
]


LE_WELL_KNOWN = collections.OrderedDict([
    ('url', r'/\.well-known/(.+)'),
    ('static_files', r'well-known/\1'),
    ('upload', r'well-known/(.+)'),
    ('mime_type', 'text/plain')
])


def asset_handler(extension, mime):
    handler = collections.OrderedDict()
    url = r'/(.+\.{ext}$)'.format(ext=extension)
    handler['url'] = url
    handler['static_files'] = r'static/\1'
    handler['upload'] = 'static' + url
    handler['mime_type'] = mime
    handler['secure'] = 'always'
    if extension in EXTENSION_TO_EXPIRATION:
        handler['expiration'] = EXTENSION_TO_EXPIRATION[extension]
    handler['http_headers'] = collections.OrderedDict(EXTRA_HEADERS)
    return handler


def file_catch_all_handler():
    handler = collections.OrderedDict()
    url = r'/(.+\.[A-Za-z0-9]+$)'
    handler['url'] = url
    handler['static_files'] = r'static/\1'
    handler['upload'] = 'static' + url
    handler['secure'] = 'always'
    handler['http_headers'] = collections.OrderedDict(EXTRA_HEADERS)
    return handler


def index_handlers():
    handlers = []
    for url in [r'/(.+)/', r'/(.+)']:
        handler = collections.OrderedDict()
        handler['url'] = url
        handler['static_files'] = r'static/\1/index.html'
        handler['upload'] = (
            'static' + url + '/index.html').replace('//', '/')
        handlers.append(handler)
    handlers.append(collections.OrderedDict([
        ('url', '/'),
        ('static_files', 'static/index.html'),
        ('upload', 'static/index.html')
    ]))

    for handler in handlers:
        handler['mime_type'] = 'text/html'
        handler['secure'] = 'always'
        handler['http_headers'] = collections.OrderedDict(EXTRA_HEADERS)

    return handlers


def main():
    app_dict = collections.OrderedDict(BASE)
    handlers_list = []
    app_dict['handlers'] = handlers_list

    handlers_list.append(LE_WELL_KNOWN)
    for extension, mime in EXTENSION_MIME:
        handlers_list.append(asset_handler(extension, mime))
    handlers_list.append(file_catch_all_handler())
    handlers_list.extend(index_handlers())

    with open('app.yaml', 'w') as outfile:
        yaml.dump(app_dict, outfile, default_flow_style=False)

if __name__ == '__main__':
    main()
