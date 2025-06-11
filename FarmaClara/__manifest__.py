{
    "name": "FarmaClara",
    "author": "Diego Melgar Parada",
    "description": "Sistema de farmacias",
    "version": "1.0.1",
    "depends":['point_of_sale','web'],
    "data":[
        'views/farmaclara_ventas.xml',
        'views/farmaclara_inventario.xml',
    ],
    "assets":{
        'web.assets_backend':[
            'FarmaClara/static/src/css/farmaclara_style.css',
            'FarmaClara/static/src/css/farmaclara_inv_form_style.css',
        ],
    },

    "installable": True,
    "application": True,
}