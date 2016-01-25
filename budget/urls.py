
from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^new_budget/', views.create_budget, name='create'),
	url(r'^manage_budget/', views.manage_budget, name='manage'),
	url(r'^new_expense/', views.new_expense, name='new_expense'),
	url(r'^expense/', views.expense_detail, name='expense_detail'),
]