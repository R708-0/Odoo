{
    "name" : "awesome_owl",
    "description" : "practica para dashboards",
    "author" : "Diego Melgar Parada",
    "depends" : ["web"],
    "data": [
        'views/assets.xml',
    ],
    "assets": {
        'web.assets_backend': [
            '/awesome_owl/static/src/mi_componente.js',
            '/awesome_owl/static/src/mi_componente.xml',
        ],
    }

    "installable" : True,
    "application" : False,
    "auto_install" : False,
}