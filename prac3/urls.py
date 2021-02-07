from django.urls import path
from prac3 import views

app_name = 'prac3'

urlpatterns =[
    path('',views.index,name='index'),
    path('<int:question_id>/detail',views.detail, name='detail'),
    path('<int:question_id>/vote',views.vote,name='vote')
]