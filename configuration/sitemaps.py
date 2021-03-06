from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone

from zine.models import Article, Issue


class IssueSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 1.0

    def items(self):
        return Issue.published_issues.all()

    @staticmethod
    def lastmod(issue):
        return issue.updated_time


class ArticleSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 1.0

    def items(self):
        return Article.published_articles.all()

    @staticmethod
    def lastmod(article):
        return article.updated_time


class MiscellaneousPageSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    @staticmethod
    def lastmod(page):
        return timezone.now()

    def location(self, obj):
        return reverse(obj)
