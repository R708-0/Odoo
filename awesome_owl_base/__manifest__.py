{
    "name": "Awesome Owl Base",
    "description": "modulo de prueba owl",
    "author":"Diego Melgar Parada",

    "depends": ['base','web'],
    "installable": True,
    "application": True,

    "data": [
        "views/templates.xml",
    ],

    "assets": {
        'awesome_owl_base.assets_playground': [
            ('include', 'web._assets_helpers'),
            ('include', 'web._assets_backend_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            # 'web/static/lib/bootstrap/scss/_maps.scss',
            ('include', 'web._assets_bootstrap'),
            ('include', 'web._assets_core'),
            'web/static/src/libs/fontawesome/css/font-awesome.css',
            'awesome_owl_base/static/src/**/*',
        ],
        'web.assets_backend': [
            'awesome_owl_base/static/src/style.css'
        ],
    },
}