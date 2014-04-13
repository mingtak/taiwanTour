# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import logging
#from plone import api


#logger = logging.getLogger("getcontentlist.py")


class AttractionsSearch(BrowserView):

    template = ViewPageTemplateFile('template/attractionssearch.pt')

    def __call__(self):
        request = self.request
        string = getattr(request, 'string', '')
        if string == '':
            return None
        catalog = self.context.portal_catalog
        self.brain = catalog({'portal_type':'twtour.content.attractions',
                              'SearchableText':string,
                              'review_state':'published'},
                             sort_on='cityCode')
        self.string = string
        return self.template()
