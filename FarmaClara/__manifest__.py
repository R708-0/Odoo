{
    "name": "FarmaClara",
    "author": "Diego Melgar Parada",
    "description": "Sistema de farmacias",
    "version": "1.0.1",
    "depends":['base','product','stock','purchase','point_of_sale','web'],
    "data":[
        'views/farmaclara_ventas.xml',
        'views/farmaclara_inventario.xml',
        'views/farmaclara_compras.xml',
        'views/farmaclara_tablero.xml',
        #'views/assets.xml',
    ],
    "assets":{
        'web.assets_backend':[
            'FarmaClara/static/src/css/farmaclara_style.css',
            'FarmaClara/static/src/css/inventario_form.css',
            'FarmaClara/static/src/scss/login.scss',
        ],
        'web.assets_frontend':[
            'FarmaClara/static/src/css/farmaclara_style.css',
            'FarmaClara/static/src/css/inventario_form.css',
            'FarmaClara/static/src/scss/login.scss',
        ],
    },

    "installable": True,
    "application": True,
}