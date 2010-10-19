#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from rollyourown.seo.admin import register_seo_admin, get_inline
from django.contrib import admin
from userapp.seo import Coverage, WithSites

register_seo_admin(admin.site, Coverage)
register_seo_admin(admin.site, WithSites)

from userapp.models import Product, Page, Category

class ProductAdmin(admin.ModelAdmin):
    inlines = [get_inline(Coverage), get_inline(WithSites)]

class PageAdmin(admin.ModelAdmin):
    inlines = [get_inline(Coverage), get_inline(WithSites)]

admin.site.register(Product)#, ProductAdmin)
admin.site.register(Page, PageAdmin)