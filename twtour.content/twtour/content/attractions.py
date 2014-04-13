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

    headImage = NamedBlobImage(
        title=_(u'head Image'),
        required=True,
    )

    image1 = NamedBlobImage(
        title=_(u'Image1'),
        required=False,
    )

    image2 = NamedBlobImage(
        title=_(u'Image2'),
        required=False,
    )

    image3 = NamedBlobImage(
        title=_(u'Image3'),
        required=False,
    )

    image4 = NamedBlobImage(
        title=_(u'Image4'),
        required=False,
    )

    image5 = NamedBlobImage(
        title=_(u'Image5'),
        required=False,
    )

    copyrightMark = schema.Bool(
        title=_(u'copyright mark'),
        description=_(u'If image copyright OK, please checked the box'),
        required=True,
    )

#validator, 同性質的可以綁在一起共用同一個validator
@form.validator(field=IAttractions['headImage'])
@form.validator(field=IAttractions['image1'])
@form.validator(field=IAttractions['image2'])
@form.validator(field=IAttractions['image3'])
@form.validator(field=IAttractions['image4'])
def validateImage(image):
    if not hasattr(image, 'size'):
        return
    if image._width > 500:
        raise Invalid(_(u'Image width over 500px'))
    if image._height > 500:
        raise Invalid(_(u'Image height over 500px'))
    if image.size > 512000:
        raise Invalid(_(u'Image size over 512KB'))


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
def notifyUser(item, event):
    item.exclude_from_nav = True
    item.reindexObject()


@indexer(IAttractions)
def cityCode_indexer(obj):
     return obj.cityName.to_object.cityCode
grok.global_adapter(cityCode_indexer, name='cityCode')
