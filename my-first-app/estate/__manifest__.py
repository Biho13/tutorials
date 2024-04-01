{
    'name': 'Real Estate',  # The name that will appear in the App list
    'version': '1.0',  # Version
    'category': 'Real Estate',  # This line says the module is an App, and not a module
    'installable': True,
    'application': True,
    'Author': 'BIHOLONG Jean Jacques',
    'depends': ['base'],  # dependencies
    
    "data": [
    'security/ir.model.access.csv',
    'views/estate_propert_list_views.xml',
    'views/estate_property_form_views.xml',
    'views/estate_property_search_views.xml',
    'views/list_type_views.xml',
    'views/list_tag_views.xml',
    'views/estate_menus.xml',

    ],
   
   
}
