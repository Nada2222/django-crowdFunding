from django.urls import path
from . import views
urlpatterns = [
    path('categories/<int:id>', views.category),
    path('categories', views.list_cates),
    path('<int:id>', views.showOne, name='show_project'),
    path('<int:id>/donatation', views.addDonate, name='add_donation'),
    path('<int:id>/reportPro', views.report_pro, name='report_pro'),
    path('<int:id>/reportCom', views.report_com, name='report_com'),
    path('<int:id>/cancel', views.cancel_pro, name='cancel_pro'),
    path('new',views.new),

]