from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^blinkm/', include('blinkm.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    
    #(r'^$', 'direct_to_template', {'template': 'chooser/index.html'}),
    (r'^$', direct_to_template, {'template': 'chooser/index.html'}),
    (r'^current_script$', 'chooser.views.current_script'),
    (r'^submit/$', 'chooser.views.method_submit'),
    (r'^reset/$', 'chooser.views.reset'),
)