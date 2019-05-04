from django.urls import path
from . import views
urlpatterns = [
<<<<<<< HEAD
    path('categories/<int:id>', views.category),
=======
    path('categories/<int:id>', views.category, name="list_cats"),
>>>>>>> c1e30cfb0050b6ff6eb3be8c26ba002274d586c9
    path('categories', views.list_cates),
    path('<int:id>', views.showOne, name='show_project'),
    path('<int:id>/donatation', views.addDonate, name='add_donation'),
    path('<int:id>/reportPro', views.report_pro, name='report_pro'),
    path('<int:id>/reportCom', views.report_com, name='report_com'),
    path('<int:id>/cancel', views.cancel_pro, name='cancel_pro'),
    path('new',views.new),
    path('search', views.search , name='search'),
<<<<<<< HEAD
=======
    path('<int:id>/rate',views.add_rate, name='add_rate')
>>>>>>> c1e30cfb0050b6ff6eb3be8c26ba002274d586c9

]

