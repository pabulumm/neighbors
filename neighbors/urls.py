"""neighbors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from accounts.views import user_login

urlpatterns = [
	url(r'^$', user_login, name='index'),
	url(r'^neighborhood/', include('neighborhood.urls', namespace="neighborhood")),
	url(r'^account/', include('accounts.urls', namespace="accounts")),
	url(r'^budget/', include('budget.urls', namespace="budget")),
	url(r'^discussions/', include('discussions.urls', namespace="discussions")),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^markers/', include('markers.urls', namespace="markers")),
	url(r'^feed/', include('feed.urls', namespace="feed")),
	url(r'^admin/', include(admin.site.urls)),
]
