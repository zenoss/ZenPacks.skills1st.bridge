################################################################################
#
# This program is part of the Bridge Zenpack for Zenoss.
# Copyright (C) 2010 Jane Curry
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""info.py

Representation of Bridge components.

$Id: info.py,v 1.2 2010/12/14 20:45:46 jc Exp $"""

__version__ = "$Revision: 1.4 $"[11:-2]

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info
#from Products.ZenUtils.Utils import convToUnits
from ZenPacks.skills1st.bridge import interfaces


class BridgeInterfaceInfo(ComponentInfo):
    implements(interfaces.IBridgeInterfaceInfo)

    Port = ProxyProperty("Port")
    RemoteAddress = ProxyProperty("RemoteAddress")
    RemoteInterface = ProxyProperty("RemoteInterface")
    RemoteDevice = ProxyProperty("RemoteDevice")
    PortStatus = ProxyProperty("PortStatus")
    PortComment = ProxyProperty("PortComment")

    @property
    def RemoteInterface(self):
        return self._object.getRemoteInterfaces()

    @property
    def RemoteDevice(self):
        return self._object.getRemoteDevice()



