import Globals
import os.path

#from AccessControl import Permissions as permissions
#from Products.ZenModel.Device import Device

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

#BridgeIntTab = { 'id'              : 'BridgeInt'
#               , 'name'            : 'Bridge Interfaces standalone tab'
#               , 'action'          : 'BridgeDeviceDetail'
#               , 'permissions'     : (permissions.view, ) 
#               }
#
#Device.factory_type_information[0]['actions'] += (BridgeIntTab,)
