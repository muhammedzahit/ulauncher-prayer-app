from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from praying_info import get_praying_info
import logging  

class DemoExtension(Extension):

    def __init__(self, logger):
        super().__init__()
        self.logger = logger
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        location = extension.preferences["location"]
        language = extension.preferences["language"]
        items = []
        try:
            fajr_time, sunset_time, dhuhr_time, asr_time, maghrib_time, isha_time ,next_azan = \
            get_praying_info(location, language)

            logger.info(fajr_time)
        
            items.append(ExtensionResultItem(icon=next_azan["icon"],
                                                name=next_azan["text"],
                                                description="Next Azan",
                                                on_enter=HideWindowAction()))
            
            items.append(ExtensionResultItem(icon="./images/fajr.png",
                                                name=fajr_time,
                                                description="",
                                                on_enter=HideWindowAction()))
            
            items.append(ExtensionResultItem(icon="./images/fajr.png",
                                                name=sunset_time,
                                                description="",
                                                on_enter=HideWindowAction()))
            
            items.append(ExtensionResultItem(icon="./images/dhuhr.png",
                                                name=dhuhr_time,
                                                description="",
                                                on_enter=HideWindowAction()))
            
            items.append(ExtensionResultItem(icon="./images/asr.png",
                                                name=asr_time,
                                                description="",
                                                on_enter=HideWindowAction()))
            
            items.append(ExtensionResultItem(icon="./images/maghrib.png",
                                                name=maghrib_time,
                                                description="",
                                                on_enter=HideWindowAction()))
            
            items.append(ExtensionResultItem(icon="./images/isha.png",
                                                name=isha_time,
                                                description="",
                                                on_enter=HideWindowAction()))
            
        except:
            items.append(ExtensionResultItem(icon="./images/exclamation.jpeg",
                                                name="City Text ID Not Found, Please check file creating_city_folders.py from github !",
                                                description="",
                                                on_enter=HideWindowAction()))

        return RenderResultListAction(items)

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    DemoExtension(logger).run()