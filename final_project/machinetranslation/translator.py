'''
    Program that interacts with Watson Translator. Two functions
    will convert either English to French or French to English.

'''
import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create an instance of the IBM Watson translator here
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator=authenticator
)

# Set the URL
language_translator.set_service_url(url)


def english_to_french(english_text):
    '''
        Method: englishToFrench()

        Purpose: Translates a string of English text to French.

        Parameters: String englishText - String to be translated.

        Returns: String that has been translated to French.
    '''
    if(english_text):
        french_translation = language_translator.translate(english_text, model_id='en-fr').get_result()
        return french_translation.get("translations")[0].get("translation")
    return ""

def french_to_english(french_text):
    '''
        Method:  frenchToEnglish()

        Purpose:  Translates a string of French text to English.

        Parameters: String frenchText - String to be translated

        Returns: String that has been translated to English
    '''
    if(french_text):
        english_translation = language_translator.translate(french_text,  model_id='fr-en').get_result()
        return english_translation.get("translations")[0].get("translation")
    return ""