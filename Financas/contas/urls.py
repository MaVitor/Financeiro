from django.urls import path
from .views import HomeView, statement_view, statement_detail, last_month_statement

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('statement/new/', statement_view, name='statement_form'),
    path('statement/<int:pk>/', statement_detail, name='statement_detail'),
    path('last-month-statement/', last_month_statement, name='last_month_statement'),
]