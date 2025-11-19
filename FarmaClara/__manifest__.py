{
    "name": "FarmaClara",
    "author": "Diego Melgar Parada",
    "description": "Sistema de farmacias",
    "version": "1.0.1",
    "depends":['base','product','stock','purchase','point_of_sale','web','spreadsheet_dashboard','spreadsheet_dashboard_account'],
    "data":[
        # 'views/assets.xml',
        'views/farmaclara_ventas.xml',
        'views/farmaclara_inventario.xml',
        'views/farmaclara_compras.xml',
        'views/farmaclara_tablero.xml',
        'data/farmaclara_dashboards.xml',
    ],
    "assets":{
        'web.assets_backend':[
            'FarmaClara/static/src/css/farmaclara_style.css',
            'FarmaClara/static/src/css/inventario_form.css',
            # 'FarmaClara/static/src/scss/dashboard.scss',
            # 'FarmaClara/src/assets/farmaclara_dashboard.js',
        ],
        'web.assets_frontend':[
            'FarmaClara/static/src/css/farmaclara_style.css',
            'FarmaClara/static/src/css/inventario_form.css',
            'FarmaClara/static/src/scss/login.scss',
            # 'FarmaClara/src/assets/farmaclara_dashboard.js',
        ],
    },

    "installable": True,
    "application": True,
}