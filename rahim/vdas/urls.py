from django.urls import path
from vdas import views




urlpatterns=[
path('home/',views.HomePageView.as_view(),name='home'),
path('employee/<int:pk>/',views.DetailPageView.as_view(),name='detail'),
path('create/',views.CreatePageView.as_view(),name='create'),
path('employee/<int:pk>/edit/',views.UpdatePageView.as_view(),name='edit'),
path('employee/<int:pk>/delete/',views.DeletePageView.as_view(),name='delete'),




path('home1/',views.home,name='home'),
path('employee1/<int:id>/',views.custdetails,name='detail'),
path('create1/',views.custpost,name='create'),
path('employee1/<int:id>/edit1/',views.custupdate,name='edit'),
path('employee1/<int:id>/delete1/',views.custdelete,name='delete'),
path('poll/',views.homeres),
path('poll/<int:id>/',views.poll_details),

path('poll1/',views.PollView.as_view()),
path('poll1/<int:id>/',views.PollDetailView.as_view()),




]
