#############################################################################
#
# Copyright (c) 2006-2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Grokkers for security-related components."""

import martian
import grokcore.component
import grokcore.component.util
import grokcore.security

from zope.security.interfaces import IPermission
from martian.error import GrokError


def default_fallback_to_name(factory, module, name, **data):
    return name

class PermissionGrokker(martian.ClassGrokker):
    martian.component(grokcore.security.Permission)
    martian.priority(1500)
    martian.directive(grokcore.component.name)
    martian.directive(grokcore.component.title,
                      get_default=default_fallback_to_name)
    martian.directive(grokcore.component.description)

    def execute(self, factory, config, name, title, description, **kw):
        if not name:
            raise GrokError(
                "A permission needs to have a dotted name for its id. Use "
                "grok.name to specify one.", factory)
        # We can safely convert to unicode, since the directives make sure
        # it is either unicode already or ASCII.
        permission = factory(unicode(name), unicode(title),
                             unicode(description))

        config.action(
            discriminator=('utility', IPermission, name),
            callable=grokcore.component.util.provideUtility,
            args=(permission, IPermission, name),
            order=-1 # need to do this early in the process
            )
        return True


from zope.i18nmessageid import Message
from zope.securitypolicy.rolepermission import rolePermissionManager
from zope.securitypolicy.interfaces import IRole

from grokcore.security.directive import permissions
from grokcore.security.components import Role


class RoleGrokker(martian.ClassGrokker):
    """Grokker for components subclassed from `grok.Role`.

    Each role is registered as a global utility providing the service
    `IRole` under its own particular name, and then granted every
    permission named in its `grok.permission()` directive.

    """
    martian.component(Role)
    martian.priority(martian.priority.bind().get(PermissionGrokker()) - 1)
    martian.directive(grokcore.component.name)
    martian.directive(
        grokcore.component.title, get_default=default_fallback_to_name)
    martian.directive(grokcore.component.description)
    martian.directive(permissions)

    def execute(self, factory, config, name, title, description,
                permissions, **kw):
        if not name:
            raise GrokError(
                "A role needs to have a dotted name for its id. Use "
                "grok.name to specify one.", factory)
        # We can safely convert to unicode, since the directives makes sure
        # it is either unicode already or ASCII.
        if not isinstance(title, Message):
            title = unicode(title)
        if not isinstance(description, Message):
            description = unicode(description)
        role = factory(unicode(name), title, description)

        config.action(
            discriminator=('utility', IRole, name),
            callable=grokcore.component.util.provideUtility,
            args=(role, IRole, name),
            )

        for permission in permissions:
            config.action(
                discriminator=('grantPermissionToRole', permission, name),
                callable=rolePermissionManager.grantPermissionToRole,
                args=(permission, name),
                )
        return True