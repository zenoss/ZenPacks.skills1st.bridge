######################################################################
#
# BridgeDevice object class
#
######################################################################

from Globals import InitializeClass
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from copy import deepcopy


class BridgeDevice(Device):
    "A Bridge Device"

    _relations = Device._relations + (
        ('BridgeInt', ToManyCont(ToOne,
            'ZenPacks.skills1st.bridge.BridgeInterface', 'BridgeDev')),
        )

    factory_type_information = deepcopy(Device.factory_type_information)
#    factory_type_information[0]['actions'] += (
#            { 'id'              : 'BridgeInt'
#            , 'name'            : 'Bridge Interfaces'
#            , 'action'          : 'BridgeDeviceDetail'
#            , 'permissions'     : (ZEN_VIEW, ) },
#            )


    def __init__(self, *args, **kw):
        Device.__init__(self, *args, **kw)
        self.buildRelations()


InitializeClass(BridgeDevice)
