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

cityCodeList = SimpleVocabulary(
    [SimpleTerm(value=u'NewTaipei', title=_(u'New Taipei City')),
     SimpleTerm(value=u'Keelung', title=_(u'Keelung City')),
     SimpleTerm(value=u'Taipei', title=_(u'Taipei City')),
     SimpleTerm(value=u'Taoyuan', title=_(u'Taoyuan City')),
     SimpleTerm(value=u'HsinchuCounty', title=_(u'Hsinchu County')),
     SimpleTerm(value=u'HsinchuCity', title=_(u'Hsinchu City')),
     SimpleTerm(value=u'Miaoli', title=_(u'Miaoli County')),
     SimpleTerm(value=u'Taichung', title=_(u'Taichung City')),
     SimpleTerm(value=u'Changhua', title=_(u'Changhua County')),
     SimpleTerm(value=u'Nantou', title=_(u'Nantou County')),
     SimpleTerm(value=u'Yunlin', title=_(u'Yunlin County')),
     SimpleTerm(value=u'ChiayiCity', title=_(u'Chiayi City')),
     SimpleTerm(value=u'ChiayiCounty', title=_(u'Chiayi County')),
     SimpleTerm(value=u'Tainan', title=_(u'Tainan City')),
     SimpleTerm(value=u'Kaohsiung', title=_(u'Kaohsiung City')),
     SimpleTerm(value=u'Pingtung', title=_(u'Pingtung County')),
     SimpleTerm(value=u'Yilan', title=_(u'Yilan County')),
     SimpleTerm(value=u'Hualien', title=_(u'Hualien County')),
     SimpleTerm(value=u'Taitung', title=_(u'Taitung County')),
     SimpleTerm(value=u'Penghu', title=_(u'Penghu County')),
     SimpleTerm(value=u'Kinmen', title=_(u'Kinmen County')),
     SimpleTerm(value=u'Lienchiang', title=_(u'Lienchiang County')),]
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

    cityCode = schema.Choice(
            title=_(u"City Code"),
            vocabulary=cityCodeList,
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
def cityCode_indexer(obj):
     return obj.cityCode
grok.global_adapter(cityCode_indexer, name='cityCode')


@indexer(ICity)
def region_indexer(obj):
     return obj.region
grok.global_adapter(region_indexer, name='region')
