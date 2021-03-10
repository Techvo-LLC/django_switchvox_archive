import os
import time
import mysql.connector
from mysql.connector.errors import IntegrityError as IE
from xml.etree import ElementTree as ET
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler, FileSystemEventHandler


if __name__ == "__main__":

    # When a new file / directory is created do...
    def on_created(event):

        def load_data():
            import time
            print(f'event: {event}')
            # get the file path, remove the xml filetype and add wav to the filename in the path. This will give us the location of the recording without having to find it. 
            recording = ("/".join(event.src_path.split("/"))[0:-3] + "wav")
            print(f'recording: {recording}')
            filename = event.src_path.split("/")[-1]
            print(f'filename: {filename}')
            filetype = filename.split(".")[-1]
            print(f'filetype: {filetype}')

            # if the filetype is xml load the data
            if filetype == "xml":
                time.sleep(1)
                print("found an xml doc")
                new_record = {"recording": recording}
                print (new_record)
                # use the xml file and extract the info
                parser = ET.parse(event.src_path)
                for x in parser.getroot():
                    if (x.tag != 'date_created_secs'):
                        new_record[x.tag] = x.text
                        
                for k, v in new_record.items():
                    print (k,"-", v)

                sql = mysql.connector.connect(
                    host = os.environ['archiver_host'],
                    user = os.environ['archiver_user'],
                    password = os.environ['archiver_password'],
                    database = os.environ['archiver_db'],
                )
                
                cursor = sql.cursor()

                # SQL INSERT statement
                stmnt = "INSERT INTO recordings (recording, recording_tag, recorded_call_id, recorder_cid, recorded_cid, recorder_account_id, recorded_account_id, from_account_id, from_caller_id, to_account_id, to_caller_id, duration, date_created_ts) VALUES (%(recording)s, %(recording_tag)s, %(recorded_call_id)s, %(recorder_cid)s, %(recorded_cid)s, %(recorder_account_id)s, %(recorded_account_id)s, %(from_account_id)s, %(from_caller_id)s, %(to_account_id)s, %(to_caller_id)s, %(duration)s, %(date_created_ts)s)"

            
                cursor.execute(stmnt, new_record)
                sql.commit()
                print(cursor.rowcount, "record inserted")

        if event.is_directory == True:
            pass
        
        else:
            # load data from recording
            print("got a file")
            load_data()

    # Events
    recordings_event_handler = FileSystemEventHandler()
    recordings_event_handler.on_created = on_created 

    # Observer
    path = "./archiver/media"
    go_recursively = True
    recordings_observer = Observer()
    recordings_observer.schedule(recordings_event_handler, path, recursive = go_recursively)

    recordings_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
            pass