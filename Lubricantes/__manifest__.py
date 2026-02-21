{
    'name':'lubricantes',
    'description':'Sistema de tienda de lubricantes',
    'author': 'Diego Melgar Parada',
    'depends':['base','product','stock','purchase','point_of_sale',],
    'data':[
        'views/lubricantes_inventario.xml',
    ],

    'assets':{
        'web.assets_backend':[
            'Lubricantes/static/src/css/lubricantes_style.css',
            'Lubricantes/static/src/js/lubricantes_ui.js',
        ],

        'web.assets_frontend':[
            'Lubricantes/static/src/css/lubricantes_style.css',
        ],

        'web.assets_qweb':[
            'Lubricantes/static/src/xml/lubricantes_templates.xml',
        ],
    },

    'installable':True,
    'application':True,
}