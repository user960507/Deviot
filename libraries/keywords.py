#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals


class Keyword(object):

    def __init__(self, _id, word_type, ref):
        self.id = _id
        self.word_type = word_type
        self.ref = ref

    def get_id(self):
        return self.id

    def get_type(self):
        return self.word_type

    def get_ref(self):
        return self.ref


class KeywordsFile(object):

    def __init__(self, path):
        self.path = path
        self.load()

    def load(self):
        self.keywords = []
        with open(self.path) as text:
            for line in text:
                line = line.strip()
                if(line and not line.startswith('#') and
                   not line.startswith('//')):
                    word_list = line.split()
                    if len(word_list) > 3:
                        continue
                    elif len(word_list) == 2:
                        if not ('LITERAL' in word_list[1] or
                                'KEYWORD' in word_list[1]):
                            word_list.insert(1, '')
                        else:
                            word_list.append('')
                    elif len(word_list) == 1:
                        word_list += ['', '']
                    keyword = Keyword(*word_list)
                    self.keywords.append(keyword)
            self.keyword_ids = [k.id for k in self.keywords]
            self.id_keyword_dict = dict(zip(self.keyword_ids, self.keywords))

    def get_id_keyword_dict(self):
        return self.id_keyword_dict

    def get_keywords(self):
        return self.keywords

    def get_keyword_ids(self):
        return self.keyword_ids
