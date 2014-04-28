# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import logging
#from plone import api


#logger = logging.getLogger("getcontentlist.py")


class NearbySearch(BrowserView):

    template = ViewPageTemplateFile('template/nearbysearch.pt')

    def __call__(self):
        request = self.request
        string = getattr(request, 'string', '')
        if string == '':
            return None
        catalog = self.context.portal_catalog
        self.brain = catalog({'portal_type':'twtour.content.attractions',
                              'cityCode':string,
                              'review_state':'published'},)
        self.string = string
        return self.template()
