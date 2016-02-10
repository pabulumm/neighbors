
from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^new_budget/', views.create_budget, name='create'),
	url(r'^manage_budget/', views.manage_budget, name='manage'),
	url(r'^new_expense/', views.new_expense, name='new_expense'),
	url(r'^expense/(?P<expense_id>[0-9]+)/', views.expense_detail, name='expense_detail'),
	url(r'^expense/(?P<expense_id>[0-9]+)/', views.approve_expense, name='approve_expense'),
]