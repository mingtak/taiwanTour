# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import logging
#from plone import api


#logger = logging.getLogger("getcontentlist.py")


class GetContentList(BrowserView):

    template = ViewPageTemplateFile('template/getcontentlist.pt')

    def __call__(self):
        request = self.request
        if not (hasattr(request, 'portal_type') and hasattr(request, 'cityCode')):
            return None
        catalog = self.context.portal_catalog
        self.brain = catalog({'portal_type':request['portal_type'],
                              'cityCode':request['cityCode'],
                              'review_state':'published'},
                             sort_on='sortable_title')
        return self.template()
