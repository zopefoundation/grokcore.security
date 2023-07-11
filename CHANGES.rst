Changes
=======

4.0 (2023-07-11)
----------------

- Add support for Python 3.7, 3.8, 3.9, 3.10, 3.11.

- Drop support for Python 2.7, 3.4, 3.5, 3.6.


3.0.1 (2018-01-12)
------------------

- Rearrange tests such that Travis CI can pick up all functional tests too.

3.0.0 (2018-01-05)
------------------

- Fix several test error that came to light.

1.7 (2018-01-03)
----------------

- Python 3 compatibility.

1.6.3 (2016-01-29)
------------------

- Update tests.

1.6.2 (2012-05-07)
------------------

- Properly declare zope.dottedname as a dependency.

1.6.1 (2012-05-02)
------------------

- Fix the package to properly work if the extra ``role`` is not
  specified.

1.6 (2012-05-01)
----------------

- The Permission and Role components moved from the grok package to the
  grokcore.security package where it belongs.

- The permissions() directive moved from the grok package to
  grokcore.security where it belongs.

1.5 (2010-11-01)
----------------

- Upped the requirements for martian and grokcore.component.

- Made package comply to zope.org repository policy.

1.4 (2009-12-13)
----------------

* **note** Backed out the version requirements for
  grokcore.component-2.0 and martian-0.12. These requirements
  stood in the way of further development especially towards
  grok-1.1 based on the ZTK. The 1.3 version should probably
  have been called 2.0 like with grokcore.component.

* Ported setup.py dependency fixes from trunk.

* Use zope.security instead of zope.app.security.

1.3 (2009-09-16)
----------------

* Use the grok.zope.org/releaseinfo information instead of our own
  copy of ``versions.cfg``, for easier maintenance.

* Depend on grokcore.component 2.0 and the 0.12 Martian - this changes
  inheritance issues but doesn't appear to affect grokcore.security
  itself.

1.2 (2009-09-14)
----------------

* Changed the default permissions from grok.View to zope.View. There seems no
  particular reason not to use the standard zope.View permission defined
  in zope.app.security.

  NOTE: YOU MUST STILL ASSIGN THIS PERMISSION TO USERS IN YOUR
  site.zcml FILE. OTHERWISE YOU DO NOT HAVE ACCESS TO ANY VIEWS.

* Made sure to include zope.app.security configuration as well, as that
  package defines the zope.View permission. Note that in the future this will
  change to zope.security.

* Bring versions.cfg in line with grok 1.0 release candidate
  versions.cfg.


1.1 (2009-07-03)
----------------

* Changed the default permissions from zope.Public to grok.View.

  NOTE: YOU MUST ASSIGN THIS PERMISSION TO USERS IN YOUR
  site.zcml FILE. OTHERWISE YOU DO NOT HAVE ACCESS TO ANY VIEWS.

1.0 (2008-08-03)
----------------

* Created ``grokcore.security`` in July 2008 by factoring
  security-related components, grokkers and directives out of Grok.
