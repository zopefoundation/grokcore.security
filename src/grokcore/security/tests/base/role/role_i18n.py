"""
A Role component have a title and description, that can be internationalized.

Let's grok this package and check we still have a Message object for the
internationalized title and description of the defined roles.

  >>> import grokcore.security.testing
  >>> grokcore.security.testing.grok(__name__)
  >>> from zope.securitypolicy.interfaces import IRole
  >>> from zope.component import getUtility
  >>> from zope.i18nmessageid import Message

A grok.Role without any internationalization. The id, title and description
should be unicode::

  >>> role = getUtility(IRole, name="RoleWithoutI18n")
  >>> print(role.id)
  RoleWithoutI18n

  >>> print(role.title)
  RoleWithoutI18n

  >>> print(role.description)
  My role without i18n

  >>> isinstance(role.id, Message)
  False
  >>> isinstance(role.title, Message)
  False
  >>> isinstance(role.description, Message)
  False

A grok.Role registered with the name and description directives only, both
internationalized. The id is taken from the name directive and should not be a
Message object. The title is taken from the name directive because the title
directive is not used.::

  >>> role = getUtility(IRole, name="RoleWithI18n")
  >>> isinstance(role.id, Message)
  False
  >>> isinstance(role.title, Message)
  True
  >>> isinstance(role.description, Message)
  True

A grok.Role registered with name, title and description directives::

  >>> role = getUtility(IRole, name="RoleWithI18nTitle")
  >>> isinstance(role.id, Message)
  False
  >>> isinstance(role.title, Message)
  True
  >>> isinstance(role.description, Message)
  True
"""

import grokcore.component as grok
from zope.i18nmessageid import MessageFactory

from grokcore.security import Role


_ = MessageFactory("testi18n")


class RoleWithoutI18n(Role):
    grok.name('RoleWithoutI18n')
    grok.description('My role without i18n')


class RoleWithI18n(Role):
    grok.name(_('RoleWithI18n'))
    grok.description(_('My role with i18n'))


class RoleWithI18nTitle(Role):
    grok.name('RoleWithI18nTitle')
    grok.title(_('RoleWithI18n'))
    grok.description(_('My role with i18n'))
