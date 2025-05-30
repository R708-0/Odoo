{
    "name": "FarmaClara",
    "author": "Diego Melgar Parada",
    "description": "Sistema de farmacias",
    "version": "1.0.1",
    "depends":['point_of_sale','stock','web'],
    "data":[
        'views/farmaclara_ventas.xml',
        'views/farmaclara_inventario.xml',
    ],
    "assets": {
        'web.assets_backend': [
            'FarmaClara/static/src/css/farmaclara_style.css',
        ],
    },
    "installable": True,
    "application": True,
}