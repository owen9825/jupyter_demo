# -*- coding: utf-8 -*-

from unittest import TestCase

import pycountry
from babel import UnknownLocaleError
import logging

from geography.helpers import language_compatibility_filter

logger = logging.getLogger(__name__)


class GeographyTester(TestCase):
    """
    Note that in order for the tests to be worthwhile, they must be more stable than the tested
    code, which is open to the idea of countries and languages changing over time.
    
    todo: Change the world and ensure that our WolframAlpha client is updating its observations.
    """
    
    def test_language_compatibility_filtering_sanity(self):
        compatible_countries = language_compatibility_filter(
            countries=pycountry.countries, languages=['English'])
        self.assertGreater(len(compatible_countries.data), 0,
                           msg="It was thought that there would be at least one country that "
                               "speaks English! What is our ambassador to do? Maybe there's a hint "
                               f"in the explanation: {compatible_countries.calculation_log}")
        logger.info(compatible_countries.calculation_log)

    def test_language_compatibility_filtering_stability(self):
        compatible_countries = language_compatibility_filter(countries=[], languages=["English"])
        self.assertEqual(len(compatible_countries.data), 0,
                         msg="No countries were provided, so how were {results} generated as "
                             "results? {explanation}".format(
                             results="; ".join(compatible_countries.data),
                             explanation=compatible_countries.calculation_log))
        mystery_languages = language_compatibility_filter(countries=['New Zealand'],
                                                          languages=["Jeg forstår ikke"])
        self.assertEqual(len(mystery_languages.data), 0,
                         msg="We weren't expecting any language to be compatible, since we gave a "
                             F"nonsense language. {mystery_languages.calculation_log}")
        languages_nowhere = language_compatibility_filter(countries=[],
                                                          languages=["Jeg forstår ikke"])
        self.assertEqual(len(languages_nowhere.data), 0,
                         msg="We weren't expecting any languages, since we didn't provide any "
                             F"countries. {languages_nowhere.calculation_log}")
