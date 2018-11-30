from django.conf.urls import url
from . import food,menu,authority,order
 
urlpatterns = [
    url(r'^$', menu.show_menu),
    url(r'^add_food$', food.add_food),
    url(r'^add_food_check$', food.add_food_check),
    url(r'^add_menu$', menu.add_menu),
    url(r'^add_menu_check$', menu.add_menu_check),
    url(r'^edit_menu$', menu.edit_menu),
    url(r'^edit_menu_check$', menu.edit_menu_check),    
    url(r'^login$',authority.login),
    url(r'^logout$',authority.logout),
    url(r'^register$',authority.register),
    url(r'^order$',order.order),
    url(r'^order_check$',order.order_check),
]