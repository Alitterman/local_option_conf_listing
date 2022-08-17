import json
import time

import watchdog.events as we
from watchdog.observers import Observer

from File_Listing import MyDirEventHandler


class Loader:
    def __init__(self, FilePath, FileName, *args):
        self.FilePath = FilePath
        self.Obs = []
        self.FileData = {}
        self.FileName = FileName
        # 初始化
        self.initload(args)

    """
    初始化函数
    """

    def initload(self, args):
        for i in args:
            self.Obs.append(i)
        self.load()
        self.listing()

    def load(self):
        with open(self.FilePath + self.FileName, encoding="utf-8") as f:
            self.FileData = json.loads(f.read())
        self.notitier()
        print(self.FilePath)

    def listing(self):
        # 创建观察者对象
        observer = Observer()
        # 创建事件处理对象
        fileHandler = MyDirEventHandler(self)
        # 为观察者设置观察对象与处理事件对象
        observer.schedule(fileHandler, "./", False)
        observer.start()
        try:
            while True:
                time.sleep(3)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def notitier(self):
        for i in self.Obs:
            i.callback(self.FileData)
