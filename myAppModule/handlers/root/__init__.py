import os

# import the apps configuration
from myAppModule import config



# Register the Secure Header tool
import myAppModule.tools.secureheaders

# import handler after initializing all the tools
from root import Root
from root import handler_name

# add a new template collection to the template_lookup plug-in
from myAppModule.plugins.mako import template_collection
template_collection.add_collection(
    collection=handler_name,
    base_dir=os.path.join(os.getcwd(), os.path.dirname(__file__), 'templates'))

# set config options for /home handler
config.conf.update({
    '/{0}'.format(handler_name): {
        'tools.rendertemplate.templateCollection': handler_name,
    },
})

# create the root handler object
rootHandler = Root()
