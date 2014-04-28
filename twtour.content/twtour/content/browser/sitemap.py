# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import logging
#from plone import api


#logger = logging.getLogger("getcontentlist.py")


class SiteMap(BrowserView):

    template = ViewPageTemplateFile('template/sitemap.pt')

    def __call__(self):
        request = self.request
        catalog = self.context.portal_catalog
        self.brain = catalog({'portal_type':['twtour.content.attractions',
                                             'twtour.content.tournews',
                                             'twtour.content.tourevent',
                                             'twtour.content.specialview',],
                              'review_state':'published',
                              'Language':['en-us', 'zh-tw', 'zh-cn']},)
        return self.template()
