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


class ISpecialView(form.Schema, IImageScaleTraversable):
    """
    Special View
    """
    body = RichText(
        title=_(u'content body'),
        required=False,
    )


class SpecialView(Container):
    grok.implements(ISpecialView)


class HomePageView(grok.View):
    """ view class """
    grok.context(ISpecialView)
    grok.require('zope2.View')
    grok.name('homePageView')


class AttractionsView (grok.View):
    """ view class """
    grok.context(ISpecialView)
    grok.require('zope2.View')
    grok.name('attractionsView')


class NewsView(grok.View):
    """ view class """
    grok.context(ISpecialView)
    grok.require('zope2.View')
    grok.name('newsView')


class EventView(grok.View):
    """ view class """
    grok.context(ISpecialView)
    grok.require('zope2.View')
    grok.name('eventView')


class SampleView2(grok.View):
    """ sample view class """
    grok.context(ISpecialView)
    grok.require('zope2.View')
    grok.name('view2')
