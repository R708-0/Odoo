{
    "name": "FarmaClara",
    "author": "Diego Melgar Parada",
    "description": "Sistema de farmacias",
    "version": "1.0.1",
    "depends":['base','product','stock','point_of_sale','web'],
    "data":[
        'views/farmaclara_ventas.xml',
        'views/farmaclara_inventario.xml',
    ],
    "assets":{
        'web.assets_backend':[
            'FarmaClara/static/src/css/farmaclara_style.css',
            'FarmaClara/static/src/css/inventario_form.css',
        ],
        'web.assets_frontend':[
            'FarmaClara/static/src/css/farmaclara_style.css',
            'FarmaClara/static/src/css/inventario_form.css',
        ],
    },

    "installable": True,
    "application": True,
}