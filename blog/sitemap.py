# import os
# from blog.models import Post, staffUnit
# from django.shortcuts import reverse
# from django.contrib import sitemaps
#
# class PostSitemap(sitemaps.Sitemap):
#    def items(self):
#        return Post.objects.all()
#
# class staffUnitSitemap(sitemaps.Sitemap):
#    def items(self):
#        return staffUnit.objects.all()
#
# class StaticViewSitemap(sitemaps.Sitemap):
#    def items(self):
#        return ['contact',
#                'agreement',
#                'legal',
#                'reception_director',
#                ]
#
#    def location(self, item):
#        return reverse(item)
