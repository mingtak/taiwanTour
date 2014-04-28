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
from plone.formwidget.autocomplete import AutocompleteMultiFieldWidget, AutocompleteFieldWidget
from zope.lifecycleevent.interfaces import IObjectAddedEvent

from twtour.content import MessageFactory as _
from twtour.content.attractions import IAttractions

from random import choice


# Interface class; used to define content-type schema.

class ITourEvent(form.Schema, IImageScaleTraversable):
    """
    Taiwan Tour Event
    """

    leadImageLink = schema.TextLine(
        title=_(u'Lead Image Url'),
        required=True,
    )

    location = schema.TextLine(
        title=_(u'Location'),
        required=False,
    )

    startDate = schema.Datetime(
        title=_(u'Event start date'),
        required=True,
    )

    endDate = schema.Datetime(
        title=_(u'Event end date'),
        required=True,
    )

    detail = RichText(
        title=_(u'Event detail information'),
        required=False,
    )

    eventWebSite = schema.URI(
        title=_(u'Event web site URL'),
        required=False,
    )

    form.widget(relatedAttractions=AutocompleteMultiFieldWidget)
    relatedAttractions = RelationList(
        title=_(u"Related attractions"),
        value_type=RelationChoice(
            source=ObjPathSourceBinder(
                object_provides=IAttractions.__identifier__,
            ),
        ),
        required=True,
    )

    eventDM = schema.TextLine(
        title=_(u'Event DM'),
        required=False,
    )


class TourEvent(Container):
    grok.implements(ITourEvent)


class SampleView(grok.View):
    """ sample view class """

    grok.context(ITourEvent)
    grok.require('zope2.View')

    grok.name('view')


@grok.subscribe(ITourEvent, IObjectAddedEvent)
def initialItem(item, event):
    item.exclude_from_nav = True
    subject = list(item.Subject())
    subject.append(item.Title())
    if item.location is None:
        subject.append(choice(['Taiwan Travel', 'Taiwan Tour', 'Formosa', 'Backpacker']))
    else:
        subject.append(item.location)
    for relatedItem in item.relatedAttractions:
        subject.append(relatedItem.to_object.Title())
    item.setSubject(subject)
    item.reindexObject()
