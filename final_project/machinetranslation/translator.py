"""
This module provides functions to translate text from English to French and French to English.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-11-29',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Function to translate string from English to French.
    """
    if english_text is not None:
        translation_object = language_translator.translate(
            text=english_text,
            source = 'en',
            target = 'fr').get_result()
        french_text = translation_object['translations'][0]['translation']
    else:
        french_text = None
    return french_text

def french_to_english(french_text):
    """
    Function to translate string from French to English.
    """
    if french_text is not None:
        translation_object = language_translator.translate(
            text=french_text,
            source = 'fr',
            target = 'en').get_result()
        english_text = translation_object['translations'][0]['translation']
    else:
        english_text = None
    return english_text
