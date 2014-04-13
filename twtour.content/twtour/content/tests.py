import doctest
import unittest

from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

import twtour.content

OPTION_FLAGS = doctest.NORMALIZE_WHITESPACE | \
               doctest.ELLIPSIS

ptc.setupPloneSite(products=['twtour.content'])


class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            zcml.load_config('configure.zcml',
              twtour.content)

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='twtour.content',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='twtour.content.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'INTEGRATION.txt',
            package='twtour.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),

        # -*- extra stuff goes here -*-

        # Integration tests for TourNews
        ztc.ZopeDocFileSuite(
            'TourNews.txt',
            package='twtour.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for TourEvent
        ztc.ZopeDocFileSuite(
            'TourEvent.txt',
            package='twtour.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for SpecialSlider
        ztc.ZopeDocFileSuite(
            'SpecialSlider.txt',
            package='twtour.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for City
        ztc.ZopeDocFileSuite(
            'City.txt',
            package='twtour.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for SpecialView
        ztc.ZopeDocFileSuite(
            'SpecialView.txt',
            package='twtour.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        # Integration tests for Attractions
        ztc.ZopeDocFileSuite(
            'Attractions.txt',
            package='twtour.content',
            optionflags = OPTION_FLAGS,
            test_class=TestCase),


        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
