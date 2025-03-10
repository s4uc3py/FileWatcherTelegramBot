import os
import time
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


TELEGRAM_TOKEN = '8180763206:AAGHaylwj6u7aOjeH0vuG78duOAbqqABjnQ'
CHAT_ID = '1635479253'


WATCH_PATH = r'C:\Users\e.nechaev\Nextcloud\Versions\Public\manuals'

event_cache = {}
DEBOUNCE_TIME = 2  


def send_telegram_message(message):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        response = requests.post(url, json={'chat_id': CHAT_ID, 'text': message})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка отправки сообщения: {e}")


class ChangeHandler(FileSystemEventHandler):


    def handle_event(self, event):

        if event.is_directory:
            return

        file_path = event.src_path
        file_name = os.path.basename(file_path)  


        current_time = time.time()
        if file_path in event_cache and (current_time - event_cache[file_path]) < DEBOUNCE_TIME:
            return  


        event_cache[file_path] = current_time

        if event.event_type == 'modified':
            send_telegram_message(f"Файл изменен: {file_name}")
        elif event.event_type == 'created':
            send_telegram_message(f"Новый файл создан: {file_name}")

    def on_modified(self, event):
        self.handle_event(event)

    def on_created(self, event):
        self.handle_event(event)


if __name__ == "__main__":
    if not TELEGRAM_TOKEN or not CHAT_ID or not WATCH_PATH:
        raise ValueError("Необходимо заполнить все настройки!")

    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_PATH, recursive=True)

    print(f"Начинаю мониторинг папки {WATCH_PATH}...")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()