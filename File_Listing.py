import _thread

from watchdog.events import FileSystemEventHandler

import Loader


class MyDirEventHandler(FileSystemEventHandler):
    def __init__(self, loader):
        FileSystemEventHandler.__init__(self)
        self.loader = loader

    def on_moved(self, event):

        if event.is_directory:
            print(
                "directory moved from {0} to {1}".format(
                    event.src_path, event.dest_path
                )
            )
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            self.loader.FileName = event.src_path
            Loader.Loader.load(self.loader)
            print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:

            # Loader.Loader.load(self.loader)
            print("file modified:{0}".format(event.src_path))
