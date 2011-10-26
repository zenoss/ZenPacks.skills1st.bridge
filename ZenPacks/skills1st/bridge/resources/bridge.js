(function(){

var ZC = Ext.ns('Zenoss.component');


function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.BridgeInterfacePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'BridgeInterface',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'hasMonitor'},
                {name: 'monitor'},
                {name: 'Port'},
                {name: 'RemoteAddress'},
                {name: 'RemoteInterface'},
                {name: 'RemoteDevice'},
                {name: 'PortStatus'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'Port',
                dataIndex: 'Port',
                header: _t('Port'),
                sortable: true,
            },{
                id: 'RemoteAddress',
                dataIndex: 'RemoteAddress',
                header: _t('Remote Address'),
                sortable: true
            },{
                id: 'RemoteInterface',
                dataIndex: 'RemoteInterface',
                header: _t('Remote Interface'),
                sortable: true,
                width: 200,
            },{
                id: 'RemoteDevice',
                dataIndex: 'RemoteDevice',
                header: _t('Remote Device'),
                sortable: true,
                width: 200,
            },{
                id: 'PortStatusValue',
                dataIndex: 'PortStatus',
                header: _t('Port Status Value'),
                width: 80,
                sortable: true,
            },{
                id: 'PortStatus',
                dataIndex: 'PortStatus',
                header: _t('Port Status'),
                renderer: function(pS) {
			if (pS==3) {
			  return Zenoss.render.pingStatus('up');
			} else {
			  return Zenoss.render.pingStatus('down');
			}
		},
                width: 80,
                sortable: true,
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                width: 120,
                sortable: true
            }]
        });
        ZC.BridgeInterfacePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('BridgeInterfacePanel', ZC.BridgeInterfacePanel);
ZC.registerName('BridgeInterface', _t('Bridge Interface'), _t('Bridge Interfaces'));
})();


