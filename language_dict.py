from enum import Enum

class LanguageDict(Enum):
    FAJR_TIME = "Fajr-Time"
    SUNRISE_TIME = "Sunrise-Time"
    DHUHR_TIME = "Dhuhr-Time"
    ASR_TIME = "Asr-Time"
    MAGHRIB_TIME = "Maghrib-Time"
    ISHA_TIME = "Isha-Time"
    FAJR = "Fajr"
    SUNRISE = "Sunrise"
    DHUHR = "Dhuhr"
    ASR = "Asr"
    MAGHRIB = "Maghrib"
    ISHA = "Isha"

def get_language_dict():
    language_dict={
        "Fajr-Time" : {
            "tr" : "İmsak vaktine {h} S, {m} D, {s} S kaldı.",
            "en" : "{h} H, {m} M, {s} S left until the Fajr time.",
        },
        "Sunrise-Time" : {
            "tr" : "Güneşin Doğmasına {h} S, {m} D, {s} S kaldı.",
            "en" : "{h} H, {m} M, {s} S left until Sunrise."
        },
        "Dhuhr-Time" : {
            "tr": "Öğle Ezanına {h} S, {m} D, {s} S kaldı.",
            "en": "{h} H, {m} M, {s} S left until the Dhuhr Azan."
        },
        "Asr-Time" : {
            "tr" : "İkindi Ezanına {h} S, {m} D, {s} S kaldı.",
            "en": "{h} H, {m} M, {s} S left until the Asr Azan."
        },
        "Maghrib-Time": {
            "tr" : "Akşam Ezanına {h} S, {m} D, {s} S kaldı.",
            "en": "{h} H, {m} M, {s} S left until the Maghrib Azan."
        },
        "Isha-Time" : {
            "tr" : "Yatsı Ezanına {h} S, {m} D, {s} S kaldı.",
            "en": "{h} H, {m} M, {s} S left until the Isha Azan."
        },
        "Fajr" : {
            "tr" : "İmsak vakti : {h}:{m}",
            "en" : "Fajr time : {h}:{m}",
        },
        "Sunrise" : {
            "tr" : "Güneş vakti : {h}:{m}",
            "en" : "Sunrise time : {h}:{m}",
        },
        "Dhuhr" : {
            "tr" : "Öğle vakti : {h}:{m}",
            "en" : "Dhuhr time : {h}:{m}",
        },
        "Asr" : {
            "tr" : "İkindi vakti : {h}:{m}",
            "en" : "Asr time : {h}:{m}",
        },
        "Maghrib": {
            "tr" : "Akşam vakti : {h}:{m}",
            "en" : "Maghrib time : {h}:{m}",
        },
        "Isha" : {
            "tr" : "Yatsı vakti : {h}:{m}",
            "en" : "Isha time : {h}:{m}",
        }
    }
    return language_dict
