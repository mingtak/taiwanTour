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


# Interface class; used to define content-type schema.

class ISpecialSlider(form.Schema, IImageScaleTraversable):
    """
    Special Slider for taiwan-tour.tw
    """
    #slide 1
    slideImage1 = NamedBlobImage(
        title=_(u'Slide Image1'),
        required=False,
    )

    slideImage1Slogan = schema.TextLine(
        title=_(u'Slide Image1 Slogan'),
        required=False,
    )

    slideImage1Description = schema.TextLine(
        title=_(u'Slide Image1 Description'),
        required=False,
    )

    #slide 2
    slideImage2 = NamedBlobImage(
        title=_(u'Slide Image2'),
        required=False,
    )

    slideImage2Small = NamedBlobImage(
        title=_(u'Slide Image2, web site logo'),
        required=False,
    )

    slideImage2Slogan = schema.TextLine(
        title=_(u'Slide Image2 Slogan'),
        required=False,
    )

    slideImage2Description = schema.TextLine(
        title=_(u'Slide Image2 Description'),
        required=False,
    )

    #slide 3
    slideImage3 = NamedBlobImage(
        title=_(u'Slide Image3'),
        required=False,
    )

    slideImage3Small = NamedBlobImage(
        title=_(u'Slide Image3, small image'),
        required=False,
    )

    slideImage3Slogan = schema.TextLine(
        title=_(u'Slide Image3 Slogan'),
        required=False,
    )

    slideImage3Description1 = schema.TextLine(
        title=_(u'Slide Image3 Description1'),
        required=False,
    )

    slideImage3Description2 = schema.TextLine(
        title=_(u'Slide Image3 Description2'),
        required=False,
    )

    #slide 4
    slideImage4 = NamedBlobImage(
        title=_(u'Slide Image4'),
        required=False,
    )

    slideImage4Small = NamedBlobImage(
        title=_(u'Slide Image4, small image'),
        required=False,
    )

    slideImage4Slogan = schema.TextLine(
        title=_(u'Slide Image4 Slogan'),
        required=False,
    )

    slideImage4Description1 = schema.TextLine(
        title=_(u'Slide Image4 Description1'),
        required=False,
    )

    slideImage4Description2 = schema.TextLine(
        title=_(u'Slide Image4 Description2'),
        required=False,
    )


class SpecialSlider(Container):
    grok.implements(ISpecialSlider)


class SampleView(grok.View):
    """ sample view class """

    grok.context(ISpecialSlider)
    grok.require('zope2.View')
    grok.name('view')

    # Add view methods here
