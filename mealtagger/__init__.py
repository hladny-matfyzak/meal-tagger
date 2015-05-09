# -*- coding: utf8 -*-
import lemmsk
import re

GRAMMS_RE = re.compile(r"[0-9/]+g", re.UNICODE)
ENDSPACE_RE = re.compile(r"\s+$", re.UNICODE)
MULTISPACE_RE = re.compile(r"\s+", re.UNICODE)


def preprocess(desc):
    repls = {
        'Kur.': 'Kuracie ',
        'Dus.': 'Dusená ',
        'Hov.': 'Hovädzí ',
        'Vypr.': 'Vyprážaný ',
        'gul.': 'guláš '
    }
    for k, v in repls.iteritems():
        desc = desc.replace(k, v)

    desc = GRAMMS_RE.sub('', desc)
    desc = MULTISPACE_RE.sub(' ', desc)
    desc = ENDSPACE_RE.sub('', desc)

    return desc.lower()


def tag(desc):
    desc = preprocess(desc)
    tags = []
    for word in desc.split(' '):
        lemm = lemmsk.lemmatize(unicode(word))
        if lemmsk.is_lemma(lemm):
            tags.append(lemm)

    return tags
