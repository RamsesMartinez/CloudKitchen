from django.conf.urls import url

from . import views

app_name = 'supplies'

urlpatterns = [
    # auth
    url(r'^$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    # profile
    # url(r'^profiles/$', views.ProfileVIew, name='profiles'),

    # sales
    url(r'^sales/$', views.sales, name='sales'),
    url(r'^sales/new/$', views.new_sale, name='new_sale'),

    # Supplies
    url(r'^supplies/$', views.supplies, name='supplies'),
    url(r'^supplies/new/$', views.new_supply, name='new_supply'),
    url(r'^supplies/(?P<pk>[0-9]+)/$', views.supply_detail, name='supply_detail'),

    # Categories
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^categories/new/$', views.new_category, name='new_category'),
    url(r'^categories/([A-Za-z]+)/$', views.categories_supplies, name='categories_supplies'),

    # Cartridges
    url(r'^cartridges/$', views.cartridges, name='cartridges'),
    url(r'^cartridges/new/$', views.new_cartridge, name='new_cartridge'),

    # Providers
    url(r'^providers/$', views.providers, name='providers'),
]