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


from twtour.content import MessageFactory as _
from plone.formwidget.autocomplete import AutocompleteMultiFieldWidget, AutocompleteFieldWidget
from twtour.content.city import ICity


# Interface class; used to define content-type schema.

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

    introduction = RichText(
        title=_(u'Introduction'),
        required=True,
    )

    location = schema.TextLine(
        title=_(u'Location'),
        required=False,
    )

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
