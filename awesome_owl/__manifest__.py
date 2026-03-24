{
    "name": "Awesome Owl",
    "description": "modulo de prueba owl",
    "author":"Diego Melgar Parada",

    "depends": ['base','web'],
    "installable": True,
    "application": True,

    "data": [
        "views/templates.xml",
    ],

    "assets": {
        'awesome_owl.assets_playground': [
            ('include', 'web._assets_helpers'),
            ('include', 'web._assets_backend_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            # 'web/static/lib/bootstrap/scss/_maps.scss',
            ('include', 'web._assets_bootstrap'),
            ('include', 'web._assets_core'),
            'web/static/src/libs/fontawesome/css/font-awesome.css',
            'awesome_owl/static/src/**/*',
        ],
        'web.assets_backend': [
            'awesome_owl/static/src/style.css'
        ],
    },
}