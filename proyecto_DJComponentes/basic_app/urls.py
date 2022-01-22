from django.conf.urls import url
from basic_app import views

#TEMPLATE TAGGING
app_name = "basic_app"

urlpatterns = [
    url(r'^$',views.home,name='home'),
    # REGISTRO
    url(r'^register/$',views.register,name='register'),
    # LOGIN
    url(r'^user_login/$',views.user_login,name='user_login'),
    # FAQ
    url(r'^support/$',views.support,name="support"),
    # CARRITO
    url(r'^carrito/$',views.carrito,name="carrito"),
    # CONSOLAS
    url(r'^consolas/$',views.consolas,name="consolas"),
    url(r'^consolas_xbox/$',views.consolas_xbox,name="consolas_xbox"),
    url(r'^consolas_playstation/$',views.consolas_playstation,name="consolas_playstation"),
    url(r'^consolas_nintendo/$',views.consolas_nintendo,name="consolas_nintendo"),
    # ORDENADORES
    url(r'^ordenadores/$',views.ordenadores,name="ordenadores"),
    url(r'^ordenadores_sobremesa/$',views.ordenadores_sobremesa,name="ordenadores_sobremesa"),
    url(r'^ordenadores_portatiles/$',views.ordenadores_portatiles,name="ordenadores_portatiles"),
    # PERIFÉRICOS
    url(r'^perifericos/$',views.perifericos,name="perifericos"),
    url(r'^perifericos_teclados/$',views.perifericos_teclados,name="perifericos_teclados"),
    url(r'^perifericos_ratones/$',views.perifericos_ratones,name="perifericos_ratones"),
    url(r'^perifericos_cascos/$',views.perifericos_cascos,name="perifericos_cascos"),
    # IMPRESORAS
    url(r'^impresoras/$',views.impresoras,name="impresoras"),
    url(r'^impresoras_tinta/$',views.impresoras_tinta,name="impresoras_tinta"),
    url(r'^impresoras_laser/$',views.impresoras_laser,name="impresoras_laser"),
    url(r'^impresoras_matriciales/$',views.impresoras_matriciales,name="impresoras_matriciales"),
    #VIDEOJUEGOS
    url(r'^videojuegos/$',views.videojuegos,name="videojuegos"),
    url(r'^videojuegos_xbox/$',views.videojuegos_xbox,name="videojuegos_xbox"),
    url(r'^videojuegos_playstation/$',views.videojuegos_playstation,name="videojuegos_playstation"),
    url(r'^videojuegos_ordenador/$',views.videojuegos_ordenador,name="videojuegos_ordenador"),
    url(r'^videojuegos_nintendo/$',views.videojuegos_nintendo,name="videojuegos_nintendo"),

]
