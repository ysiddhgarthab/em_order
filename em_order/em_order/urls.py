from django.conf.urls import url
from . import food,menu,authority,order
 
urlpatterns = [
    url(r'^$', menu.show_menu),
    url(r'^add_food$', food.add_food),
    url(r'^add_food_check$', food.add_food_check),
    url(r'^food_admin$', food.food_admin),
    url(r'^edit_food$', food.edit_food),
    url(r'^del_food$', food.del_food),
    url(r'^food_detail$', food.food_detail),
    url(r'^add_menu$', menu.add_menu),
    url(r'^add_menu_check$', menu.add_menu_check),
    url(r'^edit_menu$', menu.edit_menu),
    url(r'^edit_menu_check$', menu.edit_menu_check),    
    url(r'^login$',authority.login),
    url(r'^logout$',authority.logout),
    url(r'^del_user$',authority.del_user),
    url(r'^edit_user$',authority.edit_user),
    url(r'^register$',authority.register),
    url(r'^change_password$',authority.change_password),
    url(r'^order$',order.order),
    url(r'^order_check$',order.order_check),
    url(r'^userAdmin$',authority.userAdmin),
]