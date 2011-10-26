################################################################################
#
# This program is part of the Bridge Zenpack for Zenoss.
# Copyright (C) 2010 Jane Curry
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""interfaces

describes the form field to the user interface.

$Id: interfaces.py,v 1.2 2010/12/14 20:46:34 jc Exp $"""

__version__ = "$Revision: 1.4 $"[11:-2]

from Products.Zuul.interfaces import IComponentInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IBridgeInterfaceInfo(IComponentInfo):
    """
Info adapter for Bridge Interface component
"""
    Port = schema.Text(title=u"Port", readonly=True, group='Details')
    RemoteAddress = schema.Text(title=u"Remote MAC", readonly=True, group='Details')
    RemoteInterface = schema.Text(title=u"Remote Interface", readonly=True,group='Details')
    RemoteDevice = schema.Text(title=u"Remote Device", readonly=True, group='Details')
    PortStatus = schema.Text(title=u"Port Status", readonly=True, group='Details')
    PortComment = schema.Text(title=u"Port Comment", group='Details')

