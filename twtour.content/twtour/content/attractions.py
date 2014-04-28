# -*- coding: utf-8 -*-
from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from zope.lifecycleevent.interfaces import IObjectAddedEvent

from twtour.content import MessageFactory as _
from plone.formwidget.autocomplete import AutocompleteMultiFieldWidget, AutocompleteFieldWidget
from twtour.content.city import ICity

# import for back_references
from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog

from collective import dexteritytextindexer
from plone.indexer import indexer
from random import choice
import logging

logger = logging.getLogger("attractions.py")


def back_references(source_object, attribute_name):
    """ Return back references from source object on specified attribute_name """
    catalog = getUtility(ICatalog)
    intids = getUtility(IIntIds)
    result = []
    for rel in catalog.findRelations(
                            dict(to_id=intids.getId(aq_inner(source_object)),
                                 from_attribute=attribute_name)
                            ):
        obj = intids.queryObject(rel.from_id)
        if obj is not None and checkPermission('zope2.View', obj):
            result.append(obj)
    return result


class IAttractions(form.Schema, IImageScaleTraversable):
    """
    Attractions for taiwan tour
    """

    form.widget(cityName=AutocompleteFieldWidget)
    cityName = RelationChoice(
        title=_(u"City Name"),
        source=ObjPathSourceBinder(
                object_provides=ICity.__identifier__,),
        required=True,
    )

    contact = RichText(
        title=_(u'contact information'),
        required=True,
    )

    webSiteUrl = schema.URI(
        title=_(u'website url'),
        required=False,
    )

    dexteritytextindexer.searchable('introduction')
    introduction = RichText(
        title=_(u'Introduction'),
        required=True,
    )

    dexteritytextindexer.searchable('location')
    location = schema.TextLine(
        title=_(u'Location'),
        required=False,
    )

    dexteritytextindexer.searchable('address')
    address = schema.TextLine(
        title=_(u'Address'),
        required=False,
    )

    transportation = RichText(
        title=_(u'Transportation'),
        required=False,
    )

    leadImageLink = schema.TextLine(
        title=_(u'Lead Image Link'),
        description=_(u'using in homepage and content, width:height=3:2'),
        required=True,
    )

    imageLinkList = schema.Text(
        title=_(u'Image Link List'),
        description=_(u'using in gallery'),
        required=True,
    )

    sourcesOfArticles = schema.TextLine(
        title=_(u'Sources of articles'),
        description=_(u'Sources of articles'),
        required=True,
    )


class Attractions(Container):
    grok.implements(IAttractions)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IAttractions)
    grok.require('zope2.View')

    grok.name('view')

    # Add view methods here

    def findBackReferences(self, portal_type):
        backReferences = back_references(self.context, 'relatedAttractions')
        resultList = []
        for item in backReferences:
            if item.portal_type == portal_type:
                resultList.append(item)
        return resultList


@grok.subscribe(IAttractions, IObjectAddedEvent)
def initialItem(item, event):
    item.exclude_from_nav = True
    subject = list(item.Subject())
    subject.append(item.Title())
    if item.location is None:
        subject.append(choice(['Taiwan Travel', 'Taiwan Tour', 'Formosa', 'Backpacker']))
    else:
        subject.append(item.location)
    subject.append(item.cityName.to_object.cityCode)
    subject.append(item.cityName.to_object.Title())
    item.setSubject(subject)
    item.reindexObject()


@indexer(IAttractions)
def cityCode_indexer(obj):
     return obj.cityName.to_object.cityCode
grok.global_adapter(cityCode_indexer, name='cityCode')


