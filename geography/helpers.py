# -*- coding: utf-8 -*-
from importlib.machinery import SourceFileLoader
from string import whitespace

import pycountry
import wolframalpha  # https://pypi.org/project/wolframalpha/
from babel import Locale, UnknownLocaleError

try:
    from core import verified, VerifiedData
except ModuleNotFoundError:
    core = SourceFileLoader(
        'core', 'jupyter_demo/core.py').load_module()
    from core import verified, VerifiedData
try:
    from settings import WOLFRAM_KEY
except ModuleNotFoundError:
    settings = SourceFileLoader('settings', 'jupyter_demo/settings.py').load_module()
    from settings import WOLFRAM_KEY

MINIMAL_AREA = 20  # An area less than this wouldn't be enough to sustain crops to accompany pork


@verified
def agricultural_neighbor_filter(neighbors, client=None) -> VerifiedData:
    """
    Filter out any neighbors who do not have enough land for growing crops that would be tasty with
    pork.
    :param neighbors: The countries to be considered.
    :type neighbors: Collection
    :param client: A WolframAlpha Client to use.
    :type client: wolframalpha.Client
    :return: A revised collection, contained within a VerifiedData instance
    """
    if client is None:
        client = wolframalpha.Client(app_id=WOLFRAM_KEY)
    vegetable_neighbors = []
    for neighbor in neighbors:
        result = client.query(F"annual crop area of {neighbor} in km^2")
        area = -1
        for pod in result.pods:
            if pod.title == 'Result':
                for subpod in pod.subpods:
                    explanation = subpod.plaintext
                    measurement_position = explanation.find('km^2')
                    if measurement_position < 0:
                        raise RuntimeError('Unable to interpret the crop area for {neighbor}! '
                                           '{context}'.format(neighbor=neighbor, context=explanation))
                    area = int(explanation[:measurement_position].strip(whitespace))
                    break
                if area > 0:
                    break
        if area < 0:
            raise RuntimeError(F'Unable to find a crop area for {neighbor}!')
        if area >= MINIMAL_AREA:
            vegetable_neighbors.append(neighbor)
    return vegetable_neighbors, "Annual crop area was obtained through WolframAlpha."


@verified
def language_compatibility_filter(countries, languages=('English',)) -> VerifiedData:
    """
    Check whether these country speak any of our languages.
    :param countries: A collection of countries being considered
    :type countries: A list of country names or pycountry objects
    :param languages: The human-readable names of languages spoken by our ambassadors
    :type languages: collection
    :return: The languages that are compatible, contained within a VerifiedData instance.
    """
    real_languages = list(
        filter(lambda l: l is not None,
               [pycountry.languages.get(name=language) for language in languages]))
    # Casting as a list prevents it from being consumed on the first iteration
    verified_countries = []
    for c in countries:
        if isinstance(c, str):
            found = pycountry.countries.search_fuzzy(str(c))
            if len(found) == 0:
                raise ValueError("{0} isn't a good match for any particular country.".format(c))
            verified_countries.append(found[0])
        else:
            verified_countries.append(c)
    result = []
    for country in verified_countries:
        for language in real_languages:
            try:
                locale = Locale(language.alpha_2, country.alpha_2)
            except UnknownLocaleError:
                continue  # This shouldn't be a surprise
            result.append(country)
            break
    explanation = "These countries have locales including at least one of {languages}: " \
                  "{countries}".format(languages="; ".join(list([l.name for l in real_languages])),
                                       countries="; ".join(list(c.name for c in result)))
    return result, explanation
