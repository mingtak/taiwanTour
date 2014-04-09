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

from plone.indexer import indexer


regionList = SimpleVocabulary(
    [SimpleTerm(value=u'Northern', title=_(u'Northern')),
     SimpleTerm(value=u'Central', title=_(u'Central')),
     SimpleTerm(value=u'Southern', title=_(u'Southern')),
     SimpleTerm(value=u'Eastern', title=_(u'Eastern')),
     SimpleTerm(value=u'OutlyingIslands', title=_(u'OutlyingIslands')),]
    )


class ICity(form.Schema, IImageScaleTraversable):
    """
    Cities Infomation
    """
    region = schema.Choice(
            title=_(u"Region"),
            vocabulary=regionList,
            required=True,
        )


class City(Container):
    grok.implements(ICity)


class SampleView(grok.View):
    """ sample view class """

    grok.context(ICity)
    grok.require('zope2.View')

    # grok.name('view')


@indexer(ICity)
def region_indexer(obj):
     return obj.region
grok.global_adapter(region_indexer, name='region')
