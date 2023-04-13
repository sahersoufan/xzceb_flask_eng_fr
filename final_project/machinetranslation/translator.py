import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2019-04-30',
    authenticator=authenticator
)

language_translator.set_service_url(url)



def english_to_french(english_text):
    try:
        if english_text is None:
            return None
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        print(json.dumps(french_text, indent=2, ensure_ascii=False))
    except ApiException as ex:
        print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
    return french_text.get('translations')[0].get('translation')


def french_to_english(french_text):
    try:
        if french_text is None:
            return None
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        print(json.dumps(english_text, indent=2, ensure_ascii=False))
    except ApiException as ex:
        print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
    return english_text.get('translations')[0].get('translation')

# try:
#     # Invoke a method
# except ApiException as ex:
#     print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
