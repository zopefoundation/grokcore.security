import doctest
import re
import unittest

from pkg_resources import resource_listdir

from zope.testing import cleanup
from zope.testing import renormalizing


def cleanUpZope(test):
    cleanup.cleanUp()


checker = renormalizing.RENormalizing([
    (re.compile(r"martian.error.GrokError:"), r'GrokError:')])


def suiteFromPackage(name):
    layer_dir = 'base'
    files = resource_listdir(__name__, f'{layer_dir}/{name}')
    suite = unittest.TestSuite()
    for filename in files:
        if not filename.endswith('.py'):
            continue
        if filename.endswith('_fixture.py'):
            continue
        if filename == '__init__.py':
            continue
        dottedname = 'grokcore.security.tests.{}.{}.{}'.format(
            layer_dir, name, filename[:-3])
        test = doctest.DocTestSuite(
            dottedname,
            tearDown=cleanUpZope,
            checker=checker,
            optionflags=(
                doctest.ELLIPSIS +
                doctest.NORMALIZE_WHITESPACE +
                renormalizing.IGNORE_EXCEPTION_MODULE_IN_PYTHON2))
        suite.addTest(test)
    return suite


def test_suite():
    suite = unittest.TestSuite()
    for name in [
            'permissions',
            'role',
            'security']:
        suite.addTest(suiteFromPackage(name))
    return suite
