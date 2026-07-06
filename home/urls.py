from django.urls import path
from . import views 

urlpatterns = [
    path('',views.List_View.as_view(),name='list'),
    path('detail/<int:pk>/',views.Detail_View.as_view(),name='detail'),
    path('create',views.Create_View.as_view(),name='create'),
    path('update/<int:pk>',views.Update_View.as_view(),name='update'),
    path('delete/<int:pk>',views.Detele_View.as_view(),name='delete'),
    
    path('api',views.Api_List_View.as_view()),
    # path('list/', views.ListPageView.as_view(), name='list-page'),
    # path('detail/', views.DetailPageView.as_view(), name='detail-page'),
    # path('api/<int:pk>/', views.HomeDetailAPIView.as_view(), name='home-detail-api'),
    # path('api/<int:pk>/', views.Api_Detail_View.as_view(), name='api-detail'),
]
