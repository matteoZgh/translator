import sys
import re

from googletrans import Translator
from fileutils import *


class Trans :
    def __init__(self) :
        self.path = '/home/matteo/Downloads/translator/dictionary.txt'
        self.zedb, self.ezdb = self.__loaddb(path=self.path)
        self.adb = {}


    def trans(self, source) :
        self.source = source
        self.text = self.__translate()
        self.__savedb(path=self.path)


    @Read
    def __loaddb(self, file) :
        zh_en = {}
        en_zh = {}
        for line in file.readlines() :
            word = line.replace('\n','').split(':')
            if word[0] in zh_en :
                tmp = zh_en[word[0]]
                zh_en[word[0]] = tmp + ', ' + word[1]
            else :
                zh_en[word[0]] = word[1]
            if word[1] in en_zh :
                tmp = en_zh[word[1]]
                en_zh[word[1]] = tmp + ', ' + word[0]
            else :
                en_zh[word[1]] = word[0]
        return zh_en, en_zh


    @Add
    def __savedb(self, file) :
        if self.adb :
            for zh, en in self.adb.items() :
                s = zh + ':' + en + '\n'
                file.write(s)


    def getdb(self) :
        for zh, en in self.zedb.items() :
            print(zh, en)


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


if __name__ == '__main__' :
    cmd = sys.argv[1]
    if cmd == 'gdb' :
        trans = Trans()
        trans.getdb()
    else :
        trans = Trans()
        trans.trans(cmd)
        print(trans.text)
