import doctest
import unittest

from pkg_resources import resource_listdir

import zope.app.wsgi.testlayer
import zope.testbrowser.wsgi
from zope.app.wsgi.testlayer import http

import grokcore.security


class Layer(
        zope.testbrowser.wsgi.TestBrowserLayer,
        zope.app.wsgi.testlayer.BrowserLayer):
    pass


layer = Layer(grokcore.security, allowTearDown=True)


def suiteFromPackage(name):
    layer_dir = 'functional'
    files = resource_listdir(__name__, f'{layer_dir}/{name}')
    suite = unittest.TestSuite()
    for filename in files:
        if not filename.endswith('.py'):
            continue
        if filename == '__init__.py':
            continue
        dottedname = 'grokcore.security.tests.{}.{}.{}'.format(
            layer_dir, name, filename[:-3])
        test = doctest.DocTestSuite(
            dottedname,
            extraglobs=dict(
                getRootFolder=layer.getRootFolder,
                http=http,
            ),
            optionflags=(
                doctest.ELLIPSIS +
                doctest.NORMALIZE_WHITESPACE +
                doctest.REPORT_NDIFF +
                doctest.IGNORE_EXCEPTION_DETAIL))
        test.layer = layer
        suite.addTest(test)
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in [
            'role']:
        suite.addTest(suiteFromPackage(name))
    return suite
