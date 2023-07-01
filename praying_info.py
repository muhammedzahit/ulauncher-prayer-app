import requests
from bs4 import BeautifulSoup
import datetime
from language_dict import get_language_dict, LanguageDict

def get_city_id(city_text):
    try:
        with open("./cities/" + city_text + "/value.txt", "r") as f:
            text = f.readline();
            return text
    except:
        return "-1"

def get_praying_info(city_text, language):
    city_id = get_city_id(city_text)
    if(city_id == -1) :
        raise Exception("City Not Found")
    url = "https://namazvakitleri.diyanet.gov.tr/tr-TR/" + city_id # Replace with your desired URL

    # Send a GET request to the URL and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Save the HTML content to a file
    #with open("output.html", "wb") as file:
    #    file.write(html_content)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all the option tags
    #option_tags = soup.find_all("option")

    # Loop through the option tags and extract their attributes
    #for option in option_tags:
    #    value = option.get("value")
    #    text = option.text
    #    print(sehir_text + text  + "' :" + value + ",")

    # Find the script tag containing the variables
    script_tag = soup.find("script", text=lambda text: text and "var langCode" in text)

    # Extract the variables from the script tag using regex
    import re
    try:
        script_text = script_tag.text
    except:
        print("s:", city_text.strip(), city_text==city_text.strip())
        print("l:", language.strip(), language==language.strip())
        print("id:", city_id)
    imsak_time = re.search(r'var _imsakTime = "(\d{2}:\d{2})";', script_text).group(1)
    gunes_time = re.search(r'var _gunesTime = "(\d{2}:\d{2})";', script_text).group(1)
    ogle_time = re.search(r'var _ogleTime = "(\d{2}:\d{2})";', script_text).group(1)
    ikindi_time = re.search(r'var _ikindiTime = "(\d{2}:\d{2})";', script_text).group(1)
    aksam_time = re.search(r'var _aksamTime = "(\d{2}:\d{2})";', script_text).group(1)
    yatsi_time = re.search(r'var _yatsiTime = "(\d{2}:\d{2})";', script_text).group(1)
    next_imsak_time = re.search(r'var nextImsakTime = "(\d{2}:\d{2})";', script_text).group(1)

    # Get the current time
    now = datetime.datetime.now().time()

    # Convert the prayer times to datetime objects that include the current date
    imsak_datetime = datetime.datetime.combine(datetime.date.today(), datetime.datetime.strptime(imsak_time, "%H:%M").time())
    gunes_datetime = datetime.datetime.combine(datetime.date.today(), datetime.datetime.strptime(gunes_time, "%H:%M").time())
    ogle_datetime = datetime.datetime.combine(datetime.date.today(), datetime.datetime.strptime(ogle_time, "%H:%M").time())
    ikindi_datetime = datetime.datetime.combine(datetime.date.today(), datetime.datetime.strptime(ikindi_time, "%H:%M").time())
    aksam_datetime = datetime.datetime.combine(datetime.date.today(), datetime.datetime.strptime(aksam_time, "%H:%M").time())
    yatsi_datetime = datetime.datetime.combine(datetime.date.today(), datetime.datetime.strptime(yatsi_time, "%H:%M").time())
    next_imsak_datetime = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), datetime.datetime.strptime(next_imsak_time, "%H:%M").time())

    # Calculate the intervals between the current time and the prayer times
    imsak_interval = (imsak_datetime - datetime.datetime.combine(datetime.date.today(), now)).total_seconds() / 60
    gunes_interval = (gunes_datetime - datetime.datetime.combine(datetime.date.today(), now)).total_seconds() / 60
    ogle_interval = (ogle_datetime - datetime.datetime.combine(datetime.date.today(), now)).total_seconds() / 60
    ikindi_interval = (ikindi_datetime - datetime.datetime.combine(datetime.date.today(), now)).total_seconds() / 60
    aksam_interval = (aksam_datetime - datetime.datetime.combine(datetime.date.today(), now)).total_seconds() / 60
    yatsi_interval = (yatsi_datetime - datetime.datetime.combine(datetime.date.today(), now)).total_seconds() / 60
    next_imsak_interval = (next_imsak_datetime - datetime.datetime.combine(datetime.date.today(), now)).total_seconds() / 60


    # Print the intervals
    # print("Imsak interval:", imsak_interval)
    # print("Gunes interval:", gunes_interval)
    # print("Ogle interval:", ogle_interval)
    # print("Ikindi interval:", ikindi_interval)
    # print("Aksam interval:", aksam_interval)
    # print("Yatsi interval:", yatsi_interval)
    # print("Next Imsak interval:", next_imsak_interval)

    def get_minutes_and_second_from_interval(interval):
        minutes = int(interval // 1.00);
        hours = minutes // 60;
        minutes = minutes % 60
        seconds = int((interval % 1.00) * 60);
        return hours, minutes, seconds;

    def next_pray_time(intervalText , interval):
        hours, minutes, seconds = get_minutes_and_second_from_interval(interval=interval)
        return intervalText.format(h = hours, m = minutes, s = seconds)
    
    language_texts = get_language_dict()
    next_pray_info = {"text" : "", "icon" : ""}


    if now < datetime.datetime.strptime(imsak_time, "%H:%M").time():
        next_pray_info["text"] = next_pray_time(language_texts.get(LanguageDict.FAJR_TIME.value).get(language), imsak_interval)
        next_pray_info["icon"] = "./images/fajr.png"
    elif now < datetime.datetime.strptime(gunes_time, "%H:%M").time():
        next_pray_info["text"] = next_pray_time(language_texts.get(LanguageDict.SUNRISE_TIME.value).get(language), gunes_interval)
        next_pray_info["icon"] = "./images/fajr.png"
    elif now < datetime.datetime.strptime(ogle_time, "%H:%M").time():
        next_pray_info["text"] = next_pray_time(language_texts.get(LanguageDict.DHUHR_TIME.value).get(language), ogle_interval)
        next_pray_info["icon"] = "./images/dhuhr.png"
    elif now < datetime.datetime.strptime(ikindi_time, "%H:%M").time():
        next_pray_info["text"] = next_pray_time(language_texts.get(LanguageDict.ASR_TIME.value).get(language), ikindi_interval)
        next_pray_info["icon"] = "./images/asr.png"
    elif now < datetime.datetime.strptime(aksam_time, "%H:%M").time():
        next_pray_info["text"] = next_pray_time(language_texts.get(LanguageDict.MAGHRIB_TIME.value).get(language), aksam_interval)
        next_pray_info["icon"] = "./images/maghrib.png"
    elif now < datetime.datetime.strptime(yatsi_time, "%H:%M").time():
        next_pray_info["text"] = next_pray_time(language_texts.get(LanguageDict.ISHA_TIME.value).get(language), yatsi_interval)
        next_pray_info["icon"] = "./images/isha.png"
    else:
        next_pray_info["text"] = next_pray_time(language_texts.get(LanguageDict.FAJR_TIME.value).get(language), next_imsak_interval)
        next_pray_info["icon"] = "./images/fajr.png"

    return language_texts.get(LanguageDict.FAJR.value).get(language).format(h = imsak_time.split(':')[0], m = imsak_time.split(':')[1]), \
            language_texts.get(LanguageDict.SUNRISE.value).get(language).format(h = gunes_time.split(':')[0], m = gunes_time.split(':')[1]),\
            language_texts.get(LanguageDict.DHUHR.value).get(language).format(h = ogle_time.split(':')[0], m = ogle_time.split(':')[1]), \
            language_texts.get(LanguageDict.ASR.value).get(language).format(h = ikindi_time.split(':')[0], m = ikindi_time.split(':')[1]), \
            language_texts.get(LanguageDict.MAGHRIB.value).get(language).format(h = aksam_time.split(':')[0], m = aksam_time.split(':')[1]), \
            language_texts.get(LanguageDict.ISHA.value).get(language).format(h = yatsi_time.split(':')[0], m = yatsi_time.split(':')[1]), \
            next_pray_info                
            
            
print(get_praying_info("TÜRKİYE/SAMSUN/ÇARŞAMBA", "tr"))