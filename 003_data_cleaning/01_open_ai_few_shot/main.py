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
            "poem_number": "1",
            "poem_title": "அருந்தவத்தோன்",
            "poem_meaning":[x for x in ["தலையில் கொன்றைப் பூ சூடியவன்.", "\n", "மார்பில் கொன்றை-மாலை அணிந்தவன்.", "\n", "அவனுக்கு ஊர்தி வெண்ணிறக் காளைமாடு.", "\n", "கொடியும் காளைமாடு என்று கூறுகின்றனர்.", "\n", "தொண்டையில் நஞ்சு தேங்கிய கறை.", "\n", "அந்தக் கறை அந்தணர் மறையில் போற்றப்படுகிறது.", "\n", "ஒருபாதி (இடப்புறம்) பெண்-உருவம்.", "\n", "அதனை அவன் தனக்குள் மறைத்துக்கொள்வதும் உண்டு.", "\n", "நெற்றியில் பிறை.", "\n", "அந்தப் பிறை 18 வகையான தேவ கணங்களாலும் போற்றி வணங்கப்படும்.", "\n", "அவன் எல்லா உயிரிங்களுக்கும் பாதுகாவலாக விளங்குபவன்.", "\n", "நீர் வற்றாத கரகத்தைக் கையில் வைத்திருப்பவன்.", "\n", "தாழ்ந்த சடைமுடியிலும் நீர் வற்றுவதில்லை.", "\n", "இந்தக் கோலத்தில் அவன் தவம் செய்துகொண்டிருக்கிறான்.", "\n", "\n",] if x != "\n"],
            "poem_content": [x for x in ["\n", "\n", "கண்ணி கார் நறுங் கொன்றை; காமர்", "\n", "வண்ண மார்பின் தாரும் கொன்றை:", "\n", "ஊர்தி வால் வெள் ஏறே; சிறந்த", "\n", "சீர் கெழு கொடியும் அவ் ஏறு என்ப:", "\n", "கறை மிடறு அணியலும் அணிந்தன்று; அக் கறை", "\n", "மறை நவில் அந்தணர் நுவலவும் படுமே:", "\n", "பெண் உரு ஒரு திறன் ஆகின்று; அவ் உருத்", "\n", "தன்னுள் அடக்கிக் கரக்கினும் கரக்கும்:", "\n", "பிறை நுதல் வண்ணம் ஆகின்று; அப் பிறை", "\n", "பதினெண் கணனும் ஏத்தவும் படுமே", "\n", "எல்லா உயிர்க்கும் ஏமம் ஆகிய,", "\n", "நீர் அறவு அறியாக் கரகத்து,", "\n", "தாழ் சடைப் பொலிந்த, அருந் தவத்தோற்கே."] if x != "\n"],
            "poem_context": [x for x in ["\n", "\n", "கடவுள் வாழ்த்து.", "\n", "பாரதம் பாடிய பெருந்தேவனார் பாடியது.", "\n", "\n", "காலம்", "      : ", "கி", ".", "பி", ".\n3 ", "ஆம் நூற்றாண்டு", "\n", "ஆங்கிலத்தில்இதன் செய்தி", "\n", "\n", "\n", "\n", "அருந்தவத்தோன்", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "நீர் அறவு அறியாக் கரகம்", "\n", "\n", "\n", "\n", "\n", "கொன்றை", "\n", "\n", "\n", "\n", "\n"] if x != "\n"],
        },
    },
        
    {
        "input": {
            "link": "https://vaiyan.blogspot.com/2014/09/008.html", "title": "புறநானூறு 8 Purananuru 8", "content": ["\n", "சேரமான் கடுங்கோ வாழியாதன்", "\n", "சேரலாதன் ", "இந்த வையத்தில் உள்ள அரசர்கள் எல்லாரும் ", "தன் சொல்லுக்குப் பணிந்து நடக்கும் போகம் வேண்டும் எனக் கருதி, ", "எல்லா அரசர்களும் சமம்\nஎன்னும் பொதுச்சொல்லைப் பொறுக்காமல், ", "தன் நாடு சிறியது என்று ஊக்கம் கொண்டு ", "போராடி\nவென்று பெற்றதைத் ", "தனக்கென வைத்துக்கொள்ளாமல் கொடுத்து மகிழ்கிறான்.", "ஞாயிறே!", "இவனுக்கு நீ நிகராவாயா?", "காலம் கணித்துக்கொண்டு வருகிறாய். ", "பின்வாங்கிச்\nசெத்துவிடுகிறாய். ", "திரும்பவும் வருகிறாய். ", "மேகத்துக்குள் மறைந்துகொள்கிறாய். ", "அப்படி\nஇருந்தும் ", "வானத்தில் கதிர் வீசிக்கொண்டு பகட்டாக வருகிறாயே!", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "பாடல்", "\n", "\n", "\n", "\n", "வையம் காவலர் வழிமொழிந்து ஒழுக", ",", "\n", "\n", "போகம் வேண்டி", ", ", "பொதுச் சொல் பொறாஅது", ",", "\n", "\n", "இடம் சிறிது என்னும் ஊக்கம் துரப்ப", ",", "\n", "\n", "ஒடுங்கா உள்ளத்து", ", ", "ஓம்பா ஈகை", ",", "\n", "\n", "கடந்து அடு தானைச் சேரலாதனை", "\n", "\n", "யாங்கனம் ஒத்தியோ", "? ", "வீங்கு செலல் மண்டிலம்!", "\n", "\n", "பொழுது என வரைதி", "; ", "புறக்கொடுத்து இறத்தி", ";", "\n", "\n", "மாறி வருதி", "; ", "மலை மறைந்து ஒளித்தி", ";", "\n", "\n", "அகல் இரு விசும்பினானும்", "\n", "\n", "பகல் விளங்குதியால்", ", ", "பல் கதிர் விரித்தே.", "\n", "திணை பாடாண் திணை", "; ", "துறை இயன்மொழி", "; ", "பூவை நிலையும் ஆம்.", "சேரமான் கடுங்கோ வாழியாதனைக் ", "கபிலர் பாடியது.", "\n\n", "காலம்", "  : ", "கி", ".", "மு", ".\n3 ", "முதல் கி", ".", "பி", ". 2 (", "நூற்றாண்டு", ")", "\n", "\n", "\n", "\n", "\n", "ஞாயிறு மறைந்து எழும்", "\nசேரலாதனோ", "\nஇரவிலும்", "\nமறைந்துகொள்ளாமல்", "\nவழங்குவான்", "\n", "\n", "\n", "\n", "\n"]
        },
        "output":{
            "poem_number": "8",
            "poem_title": "சேரமான் கடுங்கோ வாழியாதன",
            "poem_meaning":[x for x in ["சேரலாதன் ", "இந்த வையத்தில் உள்ள அரசர்கள் எல்லாரும் ", "தன் சொல்லுக்குப் பணிந்து நடக்கும் போகம் வேண்டும் எனக் கருதி, ", "எல்லா அரசர்களும் சமம்\nஎன்னும் பொதுச்சொல்லைப் பொறுக்காமல், ", "தன் நாடு சிறியது என்று ஊக்கம் கொண்டு ", "போராடி\nவென்று பெற்றதைத் ", "தனக்கென வைத்துக்கொள்ளாமல் கொடுத்து மகிழ்கிறான்.", "ஞாயிறே!", "இவனுக்கு நீ நிகராவாயா?", "காலம் கணித்துக்கொண்டு வருகிறாய். ", "பின்வாங்கிச்\nசெத்துவிடுகிறாய். ", "திரும்பவும் வருகிறாய். ", "மேகத்துக்குள் மறைந்துகொள்கிறாய். ", "அப்படி\nஇருந்தும் ", "வானத்தில் கதிர் வீசிக்கொண்டு பகட்டாக வருகிறாயே!", "\n", "\n", "\n", "\n", "\n", "\n", "\n" ] if x != "\n"],
            "poem_content": [x for x in [ "\n", "\n", "\n", "வையம் காவலர் வழிமொழிந்து ஒழுக", ",", "\n", "\n", "போகம் வேண்டி", ", ", "பொதுச் சொல் பொறாஅது", ",", "\n", "\n", "இடம் சிறிது என்னும் ஊக்கம் துரப்ப", ",", "\n", "\n", "ஒடுங்கா உள்ளத்து", ", ", "ஓம்பா ஈகை", ",", "\n", "\n", "கடந்து அடு தானைச் சேரலாதனை", "\n", "\n", "யாங்கனம் ஒத்தியோ", "? ", "வீங்கு செலல் மண்டிலம்!", "\n", "\n", "பொழுது என வரைதி", "; ", "புறக்கொடுத்து இறத்தி", ";", "\n", "\n", "மாறி வருதி", "; ", "மலை மறைந்து ஒளித்தி", ";", "\n", "\n", "அகல் இரு விசும்பினானும்", "\n", "\n", "பகல் விளங்குதியால்", ", ", "பல் கதிர் விரித்தே.", "\n", "திணை பாடாண் திணை", "; ", "துறை இயன்மொழி", "; ", "பூவை நிலையும் ஆம்."] if x != "\n"],
            "poem_context": [x for x in ["சேரமான் கடுங்கோ வாழியாதனைக் ", "கபிலர் பாடியது.", "\n\n", "காலம்", "  : ", "கி", ".", "மு", ".\n3 ", "முதல் கி", ".", "பி", ". 2 (", "நூற்றாண்டு", ")", "\n", "\n", "\n", "\n", "\n", "ஞாயிறு மறைந்து எழும்", "\nசேரலாதனோ", "\nஇரவிலும்", "\nமறைந்துகொள்ளாமல்", "\nவழங்குவான்"] if x != "\n"],

        },
    },
    {
        "input": {
            "link": "https://vaiyan.blogspot.com/2014/09/003.html", "title": "புறநானூறு 3 Purananuru  3", "content": ["கருங் கை ஒள்வாட் பெரும்பெயர் வழுதி", "\n", "\n", "\n", "\n", "நீ கவுரியர் மரபில் வந்தவன்", ". ", "உன் மரபினர் முழுமதி போல் உருவம் கொண்ட ", "வெண்கொற்றக் குடைநிழலில் இருந்துகொண்டு நாடாண்டு", "மண்ணிலுள்ள அனைத்து மக்களுக்கும் நிழல் தந்தவர்கள்", ". ", "முரசு முழக்கத்துடன் ஆட்சிச் சக்கரத்தை உருட்டியவர்கள்", ". ", "நெஞ்சில் நேயம் கொண்டு ", "இல்லை என்று சொல்லாமல் கொடை வழங்கியவர்கள்", ".", "நீ கற்புக்கரசியின் கணவன்", ".", "உன்னைக் ", "கருங்கை ஒள்வாள் பெரும்பெயர் வழுதி", " என்பார்கள்", ". ", "ஏனென்றால்", " ", "நீ எப்போதும் உன் வலிமை மிக்க கையில் ", "வாள் வைத்திருப்பாய் ", "மருந்தில் கூற்றம் என்னும் நிலப்பகுதியை நீ வென்றாய்", ". ", "யானைத்\nதலையில் இருந்துகொண்டு போரிட்டு வென்றாய்", ". ", "அந்த யானை பொன்னாலான\nஓடைக் கவசத்தை நெற்றியில் கொண்டது", ". ", "வலிமை மிக்கது", ". ", "மதம் பொழிவது", ". ", "கயிற்றில் கட்டிய மணி கொண்டது", ". ", "அதனை உதைத்துக்கொண்டுதான் நீ அதன் தலையில் அமர்ந்திருந்தாய்", ".", "உன்னை ஒன்று வேண்டுகிறேன்", ". ", "நிலமே மாறினாலும் நீ சொன்ன சொல் தவறாமல்\nவாழவேண்டும்", ".", "நீ பொன்னாலான வீரக்கழலைக் காலில் அணிந்தவன்", ". ", "ஈரச் சந்தனம் புலர்ந்த மார்பை உடையவன்", ".", "உன்னை நயந்து இரவலர் வருவர்", ". ", "ஊர் இல்லாத", ", ", "வாழ முடியாத", ", ", "நீர் இல்லாத ", "நீண்ட வழியைக் கடந்து வருவர்", ". ", "வன்கண் ஆடவர் பதுங்கியிருந்து அம்பு விட ", "வீழ்ந்தவர்களை உண்ணும் பருந்து ", "உன்னமரத்தில் காத்திருக்கும் வழியில் வருவர்", ".", "அவர்களின் நிலைமையை எண்ணிப்பார்த்து ", "அவர்களின் வறுமையைப்\nபோக்குவதுதான் உன் வலிமை", ".", "\n", "\n", "பாடல் ", "\n", "\n", "உவவு\nமதி உருவின் ஓங்கல் வெண் குடை", "\n", "\n", "நிலவுக்\nகடல் வரைப்பின் மண்ணகம் நிழற்ற", ",", "\n", "\n", "ஏம\nமுரசம் இழுமென முழங்க", ",", "\n", "\n", "நேமி\nஉய்த்த நேஎ நெஞ்சின்", ",", "\n", "\n", "தவிரா\nஈகை", ",\n", "கவுரியர் மருக!", "\n", "\n", "செயிர்\nதீர் கற்பின் சேயிழை கணவ!", "\n", "\n", "பொன்\nஓடைப் புகர் அணி நுதல்", ",", "\n", "\n", "துன்\nஅருந் திறல்", ", ", "கமழ் கடாஅத்து", ",", "\n", "\n", "எயிறு\nபடையாக எயிற் கதவு இடாஅ", ",", "\n", "\n", "கயிறு\nபிணிக்கொண்ட கவிழ் மணி மருங்கின்", ",", "\n", "\n", "பெருங்\nகை", ",\n", "யானை இரும் பிடர்த் தலை இருந்து", ",", "\n", "\n", "மருந்து\nஇல் கூற்றத்து அருந் தொழில் சாயாக்", "\n", "\n", "கருங்\nகை ஒள் வாட் பெரும்பெயர் வழுதி!", "\n", "\n", "நிலம்\nபெயரினும்", ", ", "நின் சொல் பெயரல்", ";", "\n", "\n", "பொலங்\nகழற் கால்", ", ", "புலர் சாந்தின்", "\n", "\n", "விலங்கு\nஅகன்ற வியல் மார்ப!", "\n", "\n", "ஊர்\nஇல்ல", ",\n", "உயவு அரிய", ",", "\n", "\n", "நீர்\nஇல்ல", ",\n", "நீள் இடைய", ",", "\n", "\n", "பார்வல்\nஇருக்கை", ",\n", "கவி கண் நோக்கின்", ",", "\n", "\n", "செந்\nதொடை பிழையா வன்கண் ஆடவர்", "\n", "\n", "அம்பு\nவிட", ",\n", "வீழ்ந்தோர் வம்பப் பதுக்கை", ",", "\n", "\n", "திருந்து\nசிறை வளை வாய்ப் பருந்து இருந்து உயவும்", "\n", "\n", "உன்ன\nமரத்த துன் அருங் கவலை", ",", "\n", "\n", "நின்\nநசை வேட்கையின் இரவலர் வருவர் அது", "\n", "\n", "முன்னம்\nமுகத்தின் உணர்ந்து", ", ", "அவர்", "\n", "\n", "இன்மை\nதீர்த்தல் வன்மையானே.", "\n", "திணை\nபாடாண் திணை", "; ", "துறை செவியறிவுறூஉ", "; ", "வாழ்த்தியலும்\nஆம்.", "பாண்டியன்\nகருங் கை ஒள்வாட் பெரும்பெயர் வழுதியை ", "இரும்பிடர்த்தலையார்\nபாடியது. ", "இவர் பாடலிலுள்ள தொடரால் பெயர் பெற்ற புலவர்", ".", "\n", "\n\n\n", "காலம்", "  : ", "கி", ".", "மு", ".\n3 ", "முதல் கி", ".", "பி", ". 2 (", "நூற்றாண்டு", ")", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "கருங்கை ஒள்வாள்", "பெரும்பெயர் வழுதி", "\n", "\n", "பெருங்கை", ", ", "யானை", "இரும்பிடர்த் தலை", "இருந்து", "போரிட்டவன்", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "பாண்டியன்", "\n", "*", "\n", "வழுதி என்றால் ", "\n", "\n", "இவனையே குறிக்கும்", "\n", "\n", "*", "\n", "\n", "மருந்தில் கூற்றம் ", "\n", "\n", "போரில் ", "\n", "வெற்றி கண்டவன்", "\n", "\n", "\n", "\n", "\n", "\n", "\n"]
        },
        "output": {
           "poem_number": "3",
           "poem_title": "சகருங் கை ஒள்வாட் பெரும்பெயர் வழுத",
           "poem_meaning":[x for x in ["நீ கவுரியர் மரபில் வந்தவன்", ". ", "உன் மரபினர் முழுமதி போல் உருவம் கொண்ட ", "வெண்கொற்றக் குடைநிழலில் இருந்துகொண்டு நாடாண்டு", "மண்ணிலுள்ள அனைத்து மக்களுக்கும் நிழல் தந்தவர்கள்", ". ", "முரசு முழக்கத்துடன் ஆட்சிச் சக்கரத்தை உருட்டியவர்கள்", ". ", "நெஞ்சில் நேயம் கொண்டு ", "இல்லை என்று சொல்லாமல் கொடை வழங்கியவர்கள்", ".", "நீ கற்புக்கரசியின் கணவன்", ".", "உன்னைக் ", "கருங்கை ஒள்வாள் பெரும்பெயர் வழுதி", " என்பார்கள்", ". ", "ஏனென்றால்", " ", "நீ எப்போதும் உன் வலிமை மிக்க கையில் ", "வாள் வைத்திருப்பாய் ", "மருந்தில் கூற்றம் என்னும் நிலப்பகுதியை நீ வென்றாய்", ". ", "யானைத்\nதலையில் இருந்துகொண்டு போரிட்டு வென்றாய்", ". ", "அந்த யானை பொன்னாலான\nஓடைக் கவசத்தை நெற்றியில் கொண்டது", ". ", "வலிமை மிக்கது", ". ", "மதம் பொழிவது", ". ", "கயிற்றில் கட்டிய மணி கொண்டது", ". ", "அதனை உதைத்துக்கொண்டுதான் நீ அதன் தலையில் அமர்ந்திருந்தாய்", ".", "உன்னை ஒன்று வேண்டுகிறேன்", ". ", "நிலமே மாறினாலும் நீ சொன்ன சொல் தவறாமல்\nவாழவேண்டும்", ".", "நீ பொன்னாலான வீரக்கழலைக் காலில் அணிந்தவன்", ". ", "ஈரச் சந்தனம் புலர்ந்த மார்பை உடையவன்", ".", "உன்னை நயந்து இரவலர் வருவர்", ". ", "ஊர் இல்லாத", ", ", "வாழ முடியாத", ", ", "நீர் இல்லாத ", "நீண்ட வழியைக் கடந்து வருவர்", ". ", "வன்கண் ஆடவர் பதுங்கியிருந்து அம்பு விட ", "வீழ்ந்தவர்களை உண்ணும் பருந்து ", "உன்னமரத்தில் காத்திருக்கும் வழியில் வருவர்", ".", "அவர்களின் நிலைமையை எண்ணிப்பார்த்து ", "அவர்களின் வறுமையைப்\nபோக்குவதுதான் உன் வலிமை"] if x != "\n"],
           "poem_content": [x for x in ["உவவு\nமதி உருவின் ஓங்கல் வெண் குடை", "\n", "\n", "நிலவுக்\nகடல் வரைப்பின் மண்ணகம் நிழற்ற", ",", "\n", "\n", "ஏம\nமுரசம் இழுமென முழங்க", ",", "\n", "\n", "நேமி\nஉய்த்த நேஎ நெஞ்சின்", ",", "\n", "\n", "தவிரா\nஈகை", ",\n", "கவுரியர் மருக!", "\n", "\n", "செயிர்\nதீர் கற்பின் சேயிழை கணவ!", "\n", "\n", "பொன்\nஓடைப் புகர் அணி நுதல்", ",", "\n", "\n", "துன்\nஅருந் திறல்", ", ", "கமழ் கடாஅத்து", ",", "\n", "\n", "எயிறு\nபடையாக எயிற் கதவு இடாஅ", ",", "\n", "\n", "கயிறு\nபிணிக்கொண்ட கவிழ் மணி மருங்கின்", ",", "\n", "\n", "பெருங்\nகை", ",\n", "யானை இரும் பிடர்த் தலை இருந்து", ",", "\n", "\n", "மருந்து\nஇல் கூற்றத்து அருந் தொழில் சாயாக்", "\n", "\n", "கருங்\nகை ஒள் வாட் பெரும்பெயர் வழுதி!", "\n", "\n", "நிலம்\nபெயரினும்", ", ", "நின் சொல் பெயரல்", ";", "\n", "\n", "பொலங்\nகழற் கால்", ", ", "புலர் சாந்தின்", "\n", "\n", "விலங்கு\nஅகன்ற வியல் மார்ப!", "\n", "\n", "ஊர்\nஇல்ல", ",\n", "உயவு அரிய", ",", "\n", "\n", "நீர்\nஇல்ல", ",\n", "நீள் இடைய", ",", "\n", "\n", "பார்வல்\nஇருக்கை", ",\n", "கவி கண் நோக்கின்", ",", "\n", "\n", "செந்\nதொடை பிழையா வன்கண் ஆடவர்", "\n", "\n", "அம்பு\nவிட", ",\n", "வீழ்ந்தோர் வம்பப் பதுக்கை", ",", "\n", "\n", "திருந்து\nசிறை வளை வாய்ப் பருந்து இருந்து உயவும்", "\n", "\n", "உன்ன\nமரத்த துன் அருங் கவலை", ",", "\n", "\n", "நின்\nநசை வேட்கையின் இரவலர் வருவர் அது", "\n", "\n", "முன்னம்\nமுகத்தின் உணர்ந்து", ", ", "அவர்", "\n", "\n", "இன்மை\nதீர்த்தல் வன்மையானே.", "\n", "திணை\nபாடாண் திணை", "; ", "துறை செவியறிவுறூஉ", "; ", "வாழ்த்தியலும்\nஆம்.",] if x != "\n"],
           "poem_context": [x for x in ["பாண்டியன்\nகருங் கை ஒள்வாட் பெரும்பெயர் வழுதியை ", "இரும்பிடர்த்தலையார்\nபாடியது. ", "இவர் பாடலிலுள்ள தொடரால் பெயர் பெற்ற புலவர்", ".", "\n", "\n\n\n", "காலம்", "  : ", "கி", ".", "மு", ".\n3 ", "முதல் கி", ".", "பி", ". 2 (", "நூற்றாண்டு", ")", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "கருங்கை ஒள்வாள்", "பெரும்பெயர் வழுதி", "\n", "\n", "பெருங்கை", ", ", "யானை", "இரும்பிடர்த் தலை", "இருந்து", "போரிட்டவன்", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "பாண்டியன்", "\n", "*", "\n", "வழுதி என்றால் ", "\n", "\n", "இவனையே குறிக்கும்", "\n", "\n", "*", "\n", "\n", "மருந்தில் கூற்றம் ", "\n", "\n", "போரில் ", "\n", "வெற்றி கண்டவன்"] if x != "\n"],
        },
    }
]

new_data = [
    {"link": "https://vaiyan.blogspot.com/2014/09/007.html", "title": "புறநானூறு 7 Purananuru 7", "content": ["\n", "சோழன் கரிகாற் பெருவளத்தான்", "\n", "களிற்றுப்படை", ", ", "காலாள்படை ", "ஆகியவற்றின் வளத்தால் காலால்\nமிதித்தும்", ", ", "கை வளத்தால் அம்பு தொடுத்தும் ", "பகைநாட்டை அழித்தாய்", ".", "விரும்பி வந்த திருமகளை ஏற்க மறுத்த\nமலர்ந்த மார்பில் ", "தோல் என்னும் போர்க் கவசத்தை அணிந்திருக்கும் ", "வலிமை மிக்க மார்பினை உடையவன்\nநீ", ".", "இரவு பகல் என்று பார்க்காமல் ", "பகைநாட்டைச்\nசுட்டு ", "அது எரியும் விளக்கில் ", "அவர் நாட்டு மக்கள் அழுகுரலைக் கேட்பவன் நீ", ".", "இயல்தேர் வளவ", "!", "இது நல்லது அன்று", ".", "புனல் பாயும் வளநாட்டைக் காப்பதில் கவனம் செலுத்தாமல்", "பகைவரின் மீன் வளம் மிக்க நாட்டில் இப்படிச் செய்யலாமா", "?", "\n", "\n", "சேர நாட்டை அழித்தான் போலும் ", "\n", "\n", "\n", "\n", "\n", "பாடல்", "\n", "\n", "\n", "\n", "\n", "களிறு கடைஇய தாள்", ",", "\n", "\n", "கழல் உரீஇய திருந்து அடி", ",", "\n", "\n", "கணை பொருது கவி வண் கையால்", ",", "\n", "\n", "கண் ஒளிர்வரூஉம் கவின் சாபத்து", ",", "\n", "\n", "மா மறுத்த மலர் மார்பின்", ",", "\n", "\n", "தோல் பெயரிய எறுழ் முன்பின்", ",", "\n", "\n", "எல்லையும் இரவும் எண்ணாய்", ", ", "பகைவர்", "\n", "\n", "ஊர் சுடு விளக்கத்து அழு விளிக் கம்பலைக்", "\n", "\n", "கொள்ளை மேவலை", "; ", "ஆகலின்", ", ", "நல்ல", "\n", "\n", "இல்ல ஆகுபவால் இயல் தேர் வளவ!", "\n", "\n", "தண் புனல் பரந்த பூசல் மண் மறுத்து", "\n", "\n", "மீனின் செறுக்கும் யாணர்ப்", "\n", "\n", "பயன் திகழ் வைப்பின் பிறர் அகன் தலை நாடே.", "\n", "திணை வஞ்சி", "; ", "துறை கொற்றவள்ளை", "; ", "மழபுல வஞ்சியும் ஆம்.", "சோழன் கரிகாற் பெருவளத்தானைக் ", "கருங்குழலாதனார் பாடியது.", "\n", "\n\n", "காலம்", "  : ", "கி", ".", "மு", ".\n3 ", "முதல் கி", ".", "பி", ". 2 (", "நூற்றாண்டு", ")", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "இயல்தேர் வளவன்", "\nகற்பனை", "\n", "\n", "\n", "\n", "சோழன்", "\nகரிகால் வளவன்", "\nபுனல்நாடன்", "\nமீன்-நாட்டை வென்று", "\nதீ மூட்டி", "\nமக்களின்", "\nஅழுகுரலைக்", "\nகேட்டான்", "\n*", "\nஇச்செயல்", "\nநன்று அன்று", "\nஎன்று", "\nபுலவர்", "\nகுறிப்பிட்டு", "\nஅரசனைத்", "\nதிருத்துகிறார்", "\n", "\n", "\n", "\n", "\n", "\n"]},
    {"link": "https://vaiyan.blogspot.com/2014/09/006.html", "title": "புறநானூறு 6 Purananuru 6", "content": ["\n", "பாண்டியன் பல்யாகசாலை முதுகுடுமிப் பெருவழுதி", "\n", "\n", "\n", "உன்\nஉருவமும்", ",\n", "புகழும் பரவ வேண்டும்", ". ", "வடக்கில் இமயமலைக்கு அப்பாலும்", ", ", "தெற்கில் குமரிமுனைக்குத் தென்பாலும்", ", ", "கிழக்கில்\nதோண்டப்பட்ட கடலுக்கு அப்பாலும்", ", ", "மேற்கில் பழமையான கடலுக்கு அப்பாலும்", ", ", "மூன்றாக அடுக்கப்பட்டுள்ள உலகங்களில் கீழே உள்ள உலகம்", ", ", "மேலே உள்ள உலகம் ஆகியவற்றிற்கு அப்பாலும் பரவ வேண்டும்", ".", "உன்\nசெங்கோல் ஒருபுறமும் சாயாமல் ", "நடுவுநிலைமை கொண்டிருக்க வேண்டும்", ".", "இப்படி\nஉன் திறமை வெளிப்பட வேண்டும்", ".", "உன்\nசெயல்பாட்டுக்கு மாறுபட்ட பகைவர் நாட்டில்மீது உன் ", "கடற்படையையும்", " யானைப்படையையும் ஏவி", ", ", "அவர்களது பாசி பிடித்த அகழியையும்", ", ", "மதிலையும் கடந்து", ", ", "அவர்களின் நாட்டில் பெற்ற அணிகலன்களை ", "உன்னிடம் பரிசில் நாடி வரும் மக்களுக்கு ", "அவர்களின் தரம் அறிந்து வழங்க வேண்டும்", ".", "சிவபெருமான்\nஊர்வலம் வரும்போது ", "உன் குடை வணங்க வேண்டும்", ".", "நான்மறை\nமுதல்வர் உன்னிடம் கையேந்தும்போது ", "நீ தலைவணங்க வேண்டும்", ".", "நீ\nதலையில் சூடியுள்ள பூ ", "நீ பகைவர் நாட்டை எரிக்கும் புகையால் மட்டுமே வாடவேண்டும்", ".", "உன்\nசினம் உன் மனைவியர் ஊடும் முகத்தின்முன் ", "காணாமல் போக வேண்டும்", ".", "இப்படிப்பட்ட\nவெற்றியோடு ", "தடையின்றி வழங்கும் தகைமை மிக்க", " ‘", "குடுமி", "’ ", "என்னும் பெயர் கொண்ட அரசே", "!", "நீ\nகுளுமையான நிலவு போலவும் ", "ஒளி மிக்க ஞாயிறு போலவும் ", "இந்த நிலவுலகில் நிலைபெற்று வாழ்வாயாக", "!", "\n", "\n", "\n", "\n", "பாடல்", "\n", "வடாஅது\nபனி படு நெடு வரை வடக்கும்", ",", "\n", "\n", "தெனாஅது\nஉரு கெழு குமரியின் தெற்கும்", ",", "\n", "\n", "குணாஅது\nகரை பொரு தொடு கடற் குணக்கும்", ",", "\n", "\n", "குடாஅது\nதொன்று முதிர் பௌவத்தின் குடக்கும்", ",", "\n", "\n", "கீழது\nமுப் புணர் அடுக்கிய முறை முதற் கட்டின்", "\n", "\n", "நீர்\nநிலை நிவப்பின் கீழும்", ", ", "மேலது", "\n", "\n", "ஆனிலை\nஉலகத்தானும்", ", ", "ஆனாது", ",", "\n", "\n", "உருவும்\nபுகழும் ஆகி", ", ", "விரி சீர்த்", "\n", "\n", "தெரி\nகோல் ஞமன் போல", ", ", "ஒரு திறம்", "\n", "\n", "பற்றல்\nஇலியரோ! நின் திறம் சிறக்க!", "\n", "\n", "செய்\nவினைக்கு எதிர்ந்த தெவ்வர் தேஎத்து", ",", "\n", "\n", "கடல்\nபடை குளிப்ப மண்டி", ", ", "அடர் புகர்ச்", "\n", "\n", "சிறு\nகண் யானை செவ்விதின் ஏவி", ",", "\n", "\n", "பாசவல்\nபடப்பை ஆர் எயில் பல தந்து", ",", "\n", "\n", "அவ்\nஎயில் கொண்ட செய்வுறு நன் கலம்", "\n", "\n", "பரிசில்\nமாக்கட்கு வரிசையின் நல்கி", ",", "\n", "\n", "பணியியர்\nஅத்தை", ",\n", "நின் குடையே முனிவர்", "\n", "\n", "முக்\nகட் செல்வர் நகர் வலம் செயற்கே!", "\n", "\n", "இறைஞ்சுக", ", ", "பெரும! நின் சென்னி சிறந்த", "\n", "\n", "நான்மறை\nமுனிவர் ஏந்து கை எதிரே!", "\n", "\n", "வாடுக", ", ", "இறைவ! நின் கண்ணி ஒன்னார்", "\n", "\n", "நாடு\nசுடு கமழ் புகை எறித்தலானே!", "\n", "\n", "செலியர்\nஅத்தை", ",\n", "நின் வெகுளி வால் இழை", "\n", "\n", "மங்கையர்\nதுனித்த வாள் முகத்து எதிரே!", "\n", "\n", "ஆங்க", ", ", "வென்றி எல்லாம் வென்று அகத்து அடக்கிய", "\n", "\n", "தண்டா\nஈகைத் தகை மாண் குடுமி!", "\n", "\n", "தண்\nகதிர் மதியம் போலவும்", ", ", "தெறு சுடர்", "\n", "\n", "ஒண்\nகதிர் ஞாயிறு போலவும்", ",", "\n", "\n", "மன்னிய", ", ", "பெரும! நீ நிலமிசையானே!", "\n", "திணை\nபாடாண்திணை", "; ", "துறை செவியறிவுறூஉ", "; ", "பொருண்மொழிக்\nகாஞ்சியும் ஆம்.  துறை வாழ்த்தியலும் ஆம்.", "பாண்டியன்\nபல்யாகசாலை முதுகுடுமிப் பெருவழுதியைக் ", "காரி கிழார் பாடியது.", "\n", "\n\n", "காலம்", "  : ", "கி", ".", "மு", ".\n3 ", "முதல் கி", ".", "பி", ". 2 (", "நூற்றாண்டு", ")", "\n", "\n", "ஆங்கிலத்தில்இதன் செய்தி", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\nஅரசனின்", "\n", "\nகொற்றக்குடை", "\n", "\nசிவபெருமான்", "\n", "\nஊர்வலத்தின்போது", "\n", "\nமட்டும்", "\n", "\nவணங்க வேண்டுமாம்", "\n", "\n", "\n", "\n", "\n", "பாண்டியன்", "\nகுடுமி வழுதி", "\nபரிவேள்வி", "\n(அஸ்வமேத யாகம்)", "\nசெய்தான்", "\n", "\n", "\n", "\n", "\n", "\n"]},
]

# Example function to clean text data using OpenAI's GPT-3
def clean_text(new_data):
    completion = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who is helping a user to clean up a text document in Tamil language."},
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

    with open('puranaanuru_text.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Sort the data by the title field
    cleaned_data = []
    for item in data:
        cleaned_data.append(clean_text(item).content)
        print(f"cleaned {len(cleaned_data)} of {len(data)}\n")
        with open('puranaanuru_cleaned.json', 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

