# from django.contrib import admin
# from django.urls import path
# from testapp import views

# from testapp.views import EmployeeListView, TableDataView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('get_data/', TableDataView.as_view(), name='emp_data'),
#     path('', EmployeeListView.as_view(), name='employee-list'),
#     path('insert/', EmployeeCreateView.as_view(), name='employee-insert'),
#     path('delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),
#     path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
# ]


from django.contrib import admin


from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_view, name='show_view'),
    path('update/<int:pk>/', views.update_employee, name='update_view'), 
    path('delete/<int:pk>/', views.delete_view, name='delete_view'), 
    path('insert/', views.insert_view, name='insert_view'),]
