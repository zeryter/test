#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url, patterns

urlpatterns = patterns("",
        url(r"", 'web_git.webpage.homepage'),
        )


