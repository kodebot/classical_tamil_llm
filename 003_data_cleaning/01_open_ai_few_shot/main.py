import datetime
from openai import OpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import json

load_dotenv()

# Initialize OpenAI API client
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

class Poem(BaseModel):
    poem_number: int
    poem_title: str
    poem_content: list[str]
    poem_meaning: list[str]
    poem_context: list[str]

example_data = [
    {
        "input": {
            "link": "https://vaiyan.blogspot.com/2014/09/001.html", "title": "புறநானூறு 1 Purananuru 1", "content": ["\n", "\n", "\n", "அருந்தவத்தோன்", "\n", "தலையில் கொன்றைப் பூ சூடியவன்.", "\n", "மார்பில் கொன்றை-மாலை அணிந்தவன்.", "\n", "அவனுக்கு ஊர்தி வெண்ணிறக் காளைமாடு.", "\n", "கொடியும் காளைமாடு என்று கூறுகின்றனர்.", "\n", "தொண்டையில் நஞ்சு தேங்கிய கறை.", "\n", "அந்தக் கறை அந்தணர் மறையில் போற்றப்படுகிறது.", "\n", "ஒருபாதி (இடப்புறம்) பெண்-உருவம்.", "\n", "அதனை அவன் தனக்குள் மறைத்துக்கொள்வதும் உண்டு.", "\n", "நெற்றியில் பிறை.", "\n", "அந்தப் பிறை 18 வகையான தேவ கணங்களாலும் போற்றி வணங்கப்படும்.", "\n", "அவன் எல்லா உயிரிங்களுக்கும் பாதுகாவலாக விளங்குபவன்.", "\n", "நீர் வற்றாத கரகத்தைக் கையில் வைத்திருப்பவன்.", "\n", "தாழ்ந்த சடைமுடியிலும் நீர் வற்றுவதில்லை.", "\n", "இந்தக் கோலத்தில் அவன் தவம் செய்துகொண்டிருக்கிறான்.", "\n", "\n", "பாடல்", "\n", "\n", "கண்ணி கார் நறுங் கொன்றை; காமர்", "\n", "வண்ண மார்பின் தாரும் கொன்றை:", "\n", "ஊர்தி வால் வெள் ஏறே; சிறந்த", "\n", "சீர் கெழு கொடியும் அவ் ஏறு என்ப:", "\n", "கறை மிடறு அணியலும் அணிந்தன்று; அக் கறை", "\n", "மறை நவில் அந்தணர் நுவலவும் படுமே:", "\n", "பெண் உரு ஒரு திறன் ஆகின்று; அவ் உருத்", "\n", "தன்னுள் அடக்கிக் கரக்கினும் கரக்கும்:", "\n", "பிறை நுதல் வண்ணம் ஆகின்று; அப் பிறை", "\n", "பதினெண் கணனும் ஏத்தவும் படுமே", "\n", "எல்லா உயிர்க்கும் ஏமம் ஆகிய,", "\n", "நீர் அறவு அறியாக் கரகத்து,", "\n", "தாழ் சடைப் பொலிந்த, அருந் தவத்தோற்கே.", "\n", "\n", "கடவுள் வாழ்த்து.", "\n", "பாரதம் பாடிய பெருந்தேவனார் பாடியது.", "\n", "\n", "காலம்", "      : ", "கி", ".", "பி", ".\n3 ", "ஆம் நூற்றாண்டு", "\n", "ஆங்கிலத்தில்இதன் செய்தி", "\n", "\n", "\n", "\n", "அருந்தவத்தோன்", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "நீர் அறவு அறியாக் கரகம்", "\n", "\n", "\n", "\n", "\n", "கொன்றை", "\n", "\n", "\n", "\n", "\n"]
        },
        "output": {
            "poem_number": 1,
            "poem_title": "அருந்தவத்தோன்",
            "poem_content": [
                "கண்ணி கார் நறுங் கொன்றை; காமர்",
                "வண்ண மார்பின் தாரும் கொன்றை:",
                "ஊர்தி வால் வெள் ஏறே; சிறந்த",
                "சீர் கெழு கொடியும் அவ் ஏறு என்ப:",
                "கறை மிடறு அணியலும் அணிந்தன்று; அக் கறை",
                "மறை நவில் அந்தணர் நுவலவும் படுமே:",
                "பெண் உரு ஒரு திறன் ஆகின்று; அவ் உருத்",
                "தன்னுள் அடக்கிக் கரக்கினும் கரக்கும்:",
                "பிறை நுதல் வண்ணம் ஆகின்று; அப் பிறை",
                "பதினெண் கணனும் ஏத்தவும் படுமே",
                "எல்லா உயிர்க்கும் ஏமம் ஆகிய,",
                "நீர் அறவு அறியாக் கரகத்து,",
                "தாழ் சடைப் பொலிந்த, அருந் தவத்தோற்கே."
            ],
            "poem_meaning": [
                "தலையில் கொன்றைப் பூ சூடியவன்.",
                "மார்பில் கொன்றை-மாலை அணிந்தவன்.",
                "அவனுக்கு ஊர்தி வெண்ணிறக் காளைமாடு.",
                "கொடியும் காளைமாடு என்று கூறுகின்றனர்.",
                "தொண்டையில் நஞ்சு தேங்கிய கறை.",
                "அந்தக் கறை அந்தணர் மறையில் போற்றப்படுகிறது.",
                "ஒருபாதி (இடப்புறம்) பெண்-உருவம்.",
                "அதனை அவன் தனக்குள் மறைத்துக்கொள்வதும் உண்டு.",
                "நெற்றியில் பிறை.",
                "அந்தப் பிறை 18 வகையான தேவ கணங்களாலும் போற்றி வணங்கப்படும்.",
                "அவன் எல்லா உயிரிங்களுக்கும் பாதுகாவலாக விளங்குபவன்.",
                "நீர் வற்றாத கரகத்தைக் கையில் வைத்திருப்பவன்.",
                "தாழ்ந்த சடைமுடியிலும் நீர் வற்றுவதில்லை.",
                "இந்தக் கோலத்தில் அவன் தவம் செய்துகொண்டிருக்கிறான்."
            ],
            "poem_context": [
                "கடவுள் வாழ்த்து.",
                "பாரதம் பாடிய பெருந்தேவனார் பாடியது.",
                "காலம் கி.பி 3 ஆம் நூற்றாண்டு"
            ]
        }
    },
    {
        "input": {
            "link": "https://vaiyan.blogspot.com/2014/09/008.html", "title": "புறநானூறு 8 Purananuru 8", "content": ["\n", "சேரமான் கடுங்கோ வாழியாதன்", "\n", "சேரலாதன் ", "இந்த வையத்தில் உள்ள அரசர்கள் எல்லாரும் ", "தன் சொல்லுக்குப் பணிந்து நடக்கும் போகம் வேண்டும் எனக் கருதி, ", "எல்லா அரசர்களும் சமம்\nஎன்னும் பொதுச்சொல்லைப் பொறுக்காமல், ", "தன் நாடு சிறியது என்று ஊக்கம் கொண்டு ", "போராடி\nவென்று பெற்றதைத் ", "தனக்கென வைத்துக்கொள்ளாமல் கொடுத்து மகிழ்கிறான்.", "ஞாயிறே!", "இவனுக்கு நீ நிகராவாயா?", "காலம் கணித்துக்கொண்டு வருகிறாய். ", "பின்வாங்கிச்\nசெத்துவிடுகிறாய். ", "திரும்பவும் வருகிறாய். ", "மேகத்துக்குள் மறைந்துகொள்கிறாய். ", "அப்படி\nஇருந்தும் ", "வானத்தில் கதிர் வீசிக்கொண்டு பகட்டாக வருகிறாயே!", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "பாடல்", "\n", "\n", "\n", "\n", "வையம் காவலர் வழிமொழிந்து ஒழுக", ",", "\n", "\n", "போகம் வேண்டி", ", ", "பொதுச் சொல் பொறாஅது", ",", "\n", "\n", "இடம் சிறிது என்னும் ஊக்கம் துரப்ப", ",", "\n", "\n", "ஒடுங்கா உள்ளத்து", ", ", "ஓம்பா ஈகை", ",", "\n", "\n", "கடந்து அடு தானைச் சேரலாதனை", "\n", "\n", "யாங்கனம் ஒத்தியோ", "? ", "வீங்கு செலல் மண்டிலம்!", "\n", "\n", "பொழுது என வரைதி", "; ", "புறக்கொடுத்து இறத்தி", ";", "\n", "\n", "மாறி வருதி", "; ", "மலை மறைந்து ஒளித்தி", ";", "\n", "\n", "அகல் இரு விசும்பினானும்", "\n", "\n", "பகல் விளங்குதியால்", ", ", "பல் கதிர் விரித்தே.", "\n", "திணை பாடாண் திணை", "; ", "துறை இயன்மொழி", "; ", "பூவை நிலையும் ஆம்.", "சேரமான் கடுங்கோ வாழியாதனைக் ", "கபிலர் பாடியது.", "\n\n", "காலம்", "  : ", "கி", ".", "மு", ".\n3 ", "முதல் கி", ".", "பி", ". 2 (", "நூற்றாண்டு", ")", "\n", "\n", "\n", "\n", "\n", "ஞாயிறு மறைந்து எழும்", "\nசேரலாதனோ", "\nஇரவிலும்", "\nமறைந்துகொள்ளாமல்", "\nவழங்குவான்", "\n", "\n", "\n", "\n", "\n"]
        },
        "output":{
            "poem_number": 8,
            "poem_title": "சேரமான் கடுங்கோ வாழியாதன்",
            "poem_content": [
                "வையம் காவலர் வழிமொழிந்து ஒழுக,",
                "போகம் வேண்டி, பொதுச் சொல் பொறாஅது,",
                "இடம் சிறிது என்னும் ஊக்கம் துரப்ப,",
                "ஒடுங்கா உள்ளத்து, ஓம்பா ஈகை,",
                "கடந்து அடு தானைச் சேரலாதனை",
                "யாங்கனம் ஒத்தியோ? வீங்கு செலல் மண்டிலம்!",
                "பொழுது என வரைதி; புறக்கொடுத்து இறத்தி;",
                "மாறி வருதி;மலை மறைந்து ஒளித்தி;",
                "அகல் இரு விசும்பினானும்",
                "பகல் விளங்குதியால், பல் கதிர் விரித்தே."
            ],
            "poem_meaning": [
                "சேரலாதன்",
                "இந்த வையத்தில் உள்ள அரசர்கள் எல்லாரும்",
                "தன் சொல்லுக்குப் பணிந்து நடக்கும் போகம் வேண்டும் எனக் கருதி,",
                "எல்லா அரசர்களும் சமம் என்னும் பொதுச்சொல்லைப் பொறுக்காமல்,",
                "தன் நாடு சிறியது என்று ஊக்கம் கொண்டு",
                "போராடி வென்று பெற்றதைத்",
                "தனக்கென வைத்துக்கொள்ளாமல் கொடுத்து மகிழ்கிறான்.",
                "ஞாயிறே!",
                "இவனுக்கு நீ நிகராவாயா?",
                "காலம் கணித்துக்கொண்டு வருகிறாய்.",
                "பின்வாங்கிச் செத்துவிடுகிறாய்.",
                "திரும்பவும் வருகிறாய்.",
                "மேகத்துக்குள் மறைந்துகொள்கிறாய்.",
                "அப்படி இருந்தும்",
                "வானத்தில் கதிர் வீசிக்கொண்டு பகட்டாக வருகிறாயே!"
            ],
            "poem_context": [
                "திணை பாடாண் திணை",
                "துறை இயன்மொழி; பூவை நிலையும் ஆம்.",
                "சேரமான் கடுங்கோ வாழியாதனைக் கபிலர் பாடியது.",
                "காலம்  : கி. மு. 3 முதல் கி. பி. 2 (நூற்றாண்டு)",
                "ஞாயிறு மறைந்து எழும்",
                "சேரலாதனோ இரவிலும் மறைந்துகொள்ளாமல் வழங்குவான்"
            ]
        }
    },
    {
        "input": {
            "link": "https://vaiyan.blogspot.com/2014/09/003.html", "title": "புறநானூறு 3 Purananuru  3", "content": ["கருங் கை ஒள்வாட் பெரும்பெயர் வழுதி", "\n", "\n", "\n", "\n", "நீ கவுரியர் மரபில் வந்தவன்", ". ", "உன் மரபினர் முழுமதி போல் உருவம் கொண்ட ", "வெண்கொற்றக் குடைநிழலில் இருந்துகொண்டு நாடாண்டு", "மண்ணிலுள்ள அனைத்து மக்களுக்கும் நிழல் தந்தவர்கள்", ". ", "முரசு முழக்கத்துடன் ஆட்சிச் சக்கரத்தை உருட்டியவர்கள்", ". ", "நெஞ்சில் நேயம் கொண்டு ", "இல்லை என்று சொல்லாமல் கொடை வழங்கியவர்கள்", ".", "நீ கற்புக்கரசியின் கணவன்", ".", "உன்னைக் ", "கருங்கை ஒள்வாள் பெரும்பெயர் வழுதி", " என்பார்கள்", ". ", "ஏனென்றால்", " ", "நீ எப்போதும் உன் வலிமை மிக்க கையில் ", "வாள் வைத்திருப்பாய் ", "மருந்தில் கூற்றம் என்னும் நிலப்பகுதியை நீ வென்றாய்", ". ", "யானைத்\nதலையில் இருந்துகொண்டு போரிட்டு வென்றாய்", ". ", "அந்த யானை பொன்னாலான\nஓடைக் கவசத்தை நெற்றியில் கொண்டது", ". ", "வலிமை மிக்கது", ". ", "மதம் பொழிவது", ". ", "கயிற்றில் கட்டிய மணி கொண்டது", ". ", "அதனை உதைத்துக்கொண்டுதான் நீ அதன் தலையில் அமர்ந்திருந்தாய்", ".", "உன்னை ஒன்று வேண்டுகிறேன்", ". ", "நிலமே மாறினாலும் நீ சொன்ன சொல் தவறாமல்\nவாழவேண்டும்", ".", "நீ பொன்னாலான வீரக்கழலைக் காலில் அணிந்தவன்", ". ", "ஈரச் சந்தனம் புலர்ந்த மார்பை உடையவன்", ".", "உன்னை நயந்து இரவலர் வருவர்", ". ", "ஊர் இல்லாத", ", ", "வாழ முடியாத", ", ", "நீர் இல்லாத ", "நீண்ட வழியைக் கடந்து வருவர்", ". ", "வன்கண் ஆடவர் பதுங்கியிருந்து அம்பு விட ", "வீழ்ந்தவர்களை உண்ணும் பருந்து ", "உன்னமரத்தில் காத்திருக்கும் வழியில் வருவர்", ".", "அவர்களின் நிலைமையை எண்ணிப்பார்த்து ", "அவர்களின் வறுமையைப்\nபோக்குவதுதான் உன் வலிமை", ".", "\n", "\n", "பாடல் ", "\n", "\n", "உவவு\nமதி உருவின் ஓங்கல் வெண் குடை", "\n", "\n", "நிலவுக்\nகடல் வரைப்பின் மண்ணகம் நிழற்ற", ",", "\n", "\n", "ஏம\nமுரசம் இழுமென முழங்க", ",", "\n", "\n", "நேமி\nஉய்த்த நேஎ நெஞ்சின்", ",", "\n", "\n", "தவிரா\nஈகை", ",\n", "கவுரியர் மருக!", "\n", "\n", "செயிர்\nதீர் கற்பின் சேயிழை கணவ!", "\n", "\n", "பொன்\nஓடைப் புகர் அணி நுதல்", ",", "\n", "\n", "துன்\nஅருந் திறல்", ", ", "கமழ் கடாஅத்து", ",", "\n", "\n", "எயிறு\nபடையாக எயிற் கதவு இடாஅ", ",", "\n", "\n", "கயிறு\nபிணிக்கொண்ட கவிழ் மணி மருங்கின்", ",", "\n", "\n", "பெருங்\nகை", ",\n", "யானை இரும் பிடர்த் தலை இருந்து", ",", "\n", "\n", "மருந்து\nஇல் கூற்றத்து அருந் தொழில் சாயாக்", "\n", "\n", "கருங்\nகை ஒள் வாட் பெரும்பெயர் வழுதி!", "\n", "\n", "நிலம்\nபெயரினும்", ", ", "நின் சொல் பெயரல்", ";", "\n", "\n", "பொலங்\nகழற் கால்", ", ", "புலர் சாந்தின்", "\n", "\n", "விலங்கு\nஅகன்ற வியல் மார்ப!", "\n", "\n", "ஊர்\nஇல்ல", ",\n", "உயவு அரிய", ",", "\n", "\n", "நீர்\nஇல்ல", ",\n", "நீள் இடைய", ",", "\n", "\n", "பார்வல்\nஇருக்கை", ",\n", "கவி கண் நோக்கின்", ",", "\n", "\n", "செந்\nதொடை பிழையா வன்கண் ஆடவர்", "\n", "\n", "அம்பு\nவிட", ",\n", "வீழ்ந்தோர் வம்பப் பதுக்கை", ",", "\n", "\n", "திருந்து\nசிறை வளை வாய்ப் பருந்து இருந்து உயவும்", "\n", "\n", "உன்ன\nமரத்த துன் அருங் கவலை", ",", "\n", "\n", "நின்\nநசை வேட்கையின் இரவலர் வருவர் அது", "\n", "\n", "முன்னம்\nமுகத்தின் உணர்ந்து", ", ", "அவர்", "\n", "\n", "இன்மை\nதீர்த்தல் வன்மையானே.", "\n", "திணை\nபாடாண் திணை", "; ", "துறை செவியறிவுறூஉ", "; ", "வாழ்த்தியலும்\nஆம்.", "பாண்டியன்\nகருங் கை ஒள்வாட் பெரும்பெயர் வழுதியை ", "இரும்பிடர்த்தலையார்\nபாடியது. ", "இவர் பாடலிலுள்ள தொடரால் பெயர் பெற்ற புலவர்", ".", "\n", "\n\n\n", "காலம்", "  : ", "கி", ".", "மு", ".\n3 ", "முதல் கி", ".", "பி", ". 2 (", "நூற்றாண்டு", ")", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "கருங்கை ஒள்வாள்", "பெரும்பெயர் வழுதி", "\n", "\n", "பெருங்கை", ", ", "யானை", "இரும்பிடர்த் தலை", "இருந்து", "போரிட்டவன்", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "பாண்டியன்", "\n", "*", "\n", "வழுதி என்றால் ", "\n", "\n", "இவனையே குறிக்கும்", "\n", "\n", "*", "\n", "\n", "மருந்தில் கூற்றம் ", "\n", "\n", "போரில் ", "\n", "வெற்றி கண்டவன்", "\n", "\n", "\n", "\n", "\n", "\n", "\n"]
        },
        "output": {
                "poem_number": 3,
                "poem_title": "கருங் கை ஒள்வாட் பெரும்பெயர் வழுதி",
                "poem_content": [
                    "உவவு மதி உருவின் ஓங்கல் வெண் குடை",
                    "நிலவுக் கடல் வரைப்பின் மண்ணகம் நிழற்ற,",
                    "ஏம முரசம் இழுமென முழங்க,",
                    "நேமி உய்த்த நேஎ நெஞ்சின்,",
                    "தவிரா ஈகை, கவுரியர் மருக!",
                    "செயிர் தீர் கற்பின் சேயிழை கணவ!",
                    "பொன் ஓடைப் புகர் அணி நுதல்,",
                    "துன் அருந் திறல், கமழ் கடாஅத்து,",
                    "எயிறு படையாக எயிற் கதவு இடாஅ,",
                    "கயிறு பிணிக்கொண்ட கவிழ் மணி மருங்கின்,",
                    "பெருங் கை, யானை இரும் பிடர்த் தலை இருந்து,",
                    "மருந்து இல் கூற்றத்து அருந் தொழில் சாயாக்",
                    "கருங் கை ஒள் வாட் பெரும்பெயர் வழுதி!",
                    "நிலம் பெயரினும், நின் சொல் பெயரல்;",
                    "பொலங் கழற் கால், புலர் சாந்தின்",
                    "விலங்கு அகன்ற வியல் மார்ப!",
                    "ஊர் இல்ல, உயவு அரிய,",
                    "நீர் இல்ல, நீள் இடைய,",
                    "பார்வல் இருக்கை, கவி கண் நோக்கின்,",
                    "செந் தொடை பிழையா வன்கண் ஆடவர்",
                    "அம்பு விட, வீழ்ந்தோர் வம்பப் பதுக்கை,",
                    "திருந்து சிறை வளை வாய்ப் பருந்து இருந்து உயவும்",
                    "உன்ன மரத்த துன் அருங் கவலை,",
                    "நின் நசை வேட்கையின் இரவலர் வருவர் அது",
                    "முன்னம் முகத்தின் உணர்ந்து, அவர்",
                    "இன்மை தீர்த்தல் வன்மையானே."
                ],
                "poem_meaning": [
                    "நீ கவுரியர் மரபில் வந்தவன்.",
                    "உன் மரபினர் முழுமதி போல் உருவம் கொண்ட ",
                    "வெண்கொற்றக் குடைநிழலில் இருந்துகொண்டு நாடாண்டு",
                    "மண்ணிலுள்ள அனைத்து மக்களுக்கும் நிழல் தந்தவர்கள். ",
                    "முரசு முழக்கத்துடன் ஆட்சிச் சக்கரத்தை உருட்டியவர்கள். ",
                    "நெஞ்சில் நேயம் கொண்டு ",
                    "இல்லை என்று சொல்லாமல் கொடை வழங்கியவர்கள்.",
                    "நீ கற்புக்கரசியின் கணவன்.",
                    "உன்னைக் கருங்கை ஒள்வாள் பெரும்பெயர் வழுதி என்பார்கள். ",
                    "ஏனென்றால் ",
                    "நீ எப்போதும் உன் வலிமை மிக்க கையில் ",
                    "வாள் வைத்திருப்பாய் ",
                    "மருந்தில் கூற்றம் என்னும் நிலப்பகுதியை நீ வென்றாய். ",
                    "யானைத் தலையில் இருந்துகொண்டு போரிட்டு வென்றாய். ",
                    "அந்த யானை பொன்னாலான ஓடைக் கவசத்தை நெற்றியில் கொண்டது. ",
                    "வலிமை மிக்கது. ",
                    "மதம் பொழிவது. ",
                    "கயிற்றில் கட்டிய மணி கொண்டது. ",
                    "அதனை உதைத்துக்கொண்டுதான் நீ அதன் தலையில் அமர்ந்திருந்தாய்.",
                    "உன்னை ஒன்று வேண்டுகிறேன். ",
                    "நிலமே மாறினாலும் நீ சொன்ன சொல் தவறாமல் வாழவேண்டும்.",
                    "நீ பொன்னாலான வீரக்கழலைக் காலில் அணிந்தவன். ",
                    "ஈரச் சந்தனம் புலர்ந்த மார்பை உடையவன்.",
                    "உன்னை நயந்து இரவலர் வருவர். ",
                    "ஊர் இல்லாத, வாழ முடியாத, நீர் இல்லாத ",
                    "நீண்ட வழியைக் கடந்து வருவர். ",
                    "வன்கண் ஆடவர் பதுங்கியிருந்து அம்பு விட ",
                    "வீழ்ந்தவர்களை உண்ணும் பருந்து ",
                    "உன்னமரத்தில் காத்திருக்கும் வழியில் வருவர்.",
                    "அவர்களின் நிலைமையை எண்ணிப்பார்த்து ",
                    "அவர்களின் வறுமையைப் போக்குவதுதான் உன் வலிமை."
                ],
                "poem_context": [
                    "திணை பாடாண் திணை",
                    "பாண்டியன் கருங் கை ஒள்வாட் பெரும்பெயர் வழுதியை ",
                    "இரும்பிடர்த்தலையார் பாடியது.",
                    "இவர் பாடலிலுள்ள தொடரால் பெயர் பெற்ற புலவர்.",
                    "காலம் : கி.மு. 3 முதல் கி.பி. 2 (நூற்றாண்டு)",
                    "கருங்கை ஒள்வாள் பெரும்பெயர் வழுதி பெருங்கை, யானை இரும்பிடர்த் தலை இருந்து போரிட்டவன்",
                    "பாண்டியன் - வழுதி என்றால் இவனையே குறிக்கும்",
                    "மருந்தில் கூற்றம் போரில் வெற்றி கண்டவன்"
                ]
            }
    }
]


# Example function to clean text data using OpenAI's GPT-3
def clean_text(new_data):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who is helping a user to clean up a text document in Tamil language. Please do NOT make your own meaning or generate text of your own"},
            { 
                "role": "user", 
                "content": f"""
                    'input': <<input-start>>{example_data[0]['input']}<<input-end>>,
                    'output': <<output-start>>{example_data[0]['output']}<<output-end>>,
                """
            },
            { 
                "role": "user", 
                "content": f"""
                    'input': <<input-start>>{example_data[1]['input']}<<input-end>>,
                    'output': <<output-start>>{example_data[1]['output']}<<output-end>>,
                """
            },
            { 
                "role": "user", 
                "content": f"""
                    'input': <<inputstart>>{example_data[2]['input']}<<input-end>>,
                    'output': <<output-start>>{example_data[2]['output']}<<output-end>>,
                """
            },
            { 
                "role": "user", 
                "content": f"""
                    'input': <<input-start>>{new_data}<<input-end>>,
                    'output': <<output-start>>insert text in Tamil language here<<output-end>>,
                """
            },
        ],
        response_format=Poem
    )
    return completion.choices[0].message


# Example usage
if __name__ == "__main__":

    with open('aganaanuru_text.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Sort the data by the title field
    cleaned_data = []
    for item in data:
        cleaned_data.append(clean_text(item).content)
        print(f"cleaned {len(cleaned_data)} of {len(data)}\n")
        with open('aganaanuru_cleaned_attempt_3.json', 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

