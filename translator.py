import sys
import re

from googletrans import Translator
from fileutils import *


class Trans :
    def __init__(self) :
        self.zedb, self.ezdb = self.__loaddb(path='/home/matteo/Code/python/dictionary.txt')
        self.adb = {}


    def trans(self, source) :
        self.source = source
        self.text = self.__translate()
        self.__savedb(path='/home/matteo/Code/python/dictionary.txt')


    @Read
    def __loaddb(self, file) :
        zh_en = {}
        en_zh = {}
        for line in file.readlines() :
            word = line.replace('\n','').split(':')
            zh_en[word[0]] = word[1]
            en_zh[word[1]] = word[0]
        return zh_en, en_zh


    def __translate(self) :
        text = ''
        if re.match(r'[a-z]+|[A-Z]+', self.source) :
            if self.source in self.ezdb :
                text = self.ezdb[self.source]
            else :
                text = self.__googletranslate('en', 'zh-cn')
                self.adb[text] = self.source
        else :
            if self.source in self.zedb :
                text = self.zedb[self.source]
            else :
                text = self.__googletranslate('zh-cn', 'en')
                self.adb[self.source] = text
        return text


    def __googletranslate(self, src, dest) :
        translator = Translator(service_urls=['translate.google.cn'])
        text = translator.translate(self.source,src=src,dest=dest).text
        return text


    @Add
    def __savedb(self, file) :
        if self.adb :
            for zh, en in self.adb.items() :
                s = zh + ':' + en + '\n'
                file.write(s)


    def getdb(self) :
        for zh, en in self.zedb.items() :
            print(zh, en)


if __name__ == '__main__' :
    cmd = sys.argv[1]
    if cmd == 'g' :
        trans = Trans()
        trans.getdb()
    else :
        trans = Trans()
        trans.trans(cmd)
        print(trans.text)
