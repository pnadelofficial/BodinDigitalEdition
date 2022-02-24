import json
from aligner.models import FrenchWord, EnglishWord, LatinWord

en = open('en_data_stanza.json', encoding="utf8")
fr = open('fr_data_stanza.json', encoding="utf8")
la = open('lat_data_stanza.json', encoding="utf8")

def process_eng_data(file):
    data = json.load(file)
    for index in data:
        for sent in data[index]:
            for word in sent:
                if 'lemma' in list(word[1][0].keys()):
                    lemma = word[1][0]['lemma']
                else:
                    lemma = None

                if 'upos' in list(word[1][0].keys()):
                    upos = word[1][0]['upos']
                else:
                    upos = None
                
                if 'deprel' in list(word[1][0].keys()):
                    deprel = word[1][0]['deprel']
                else:
                    deprel = None

                if 'feats' in list(word[1][0].keys()):
                    feats = word[1][0]['feats']
                else:
                    feats = None
                
                EnglishWord.objects.create(
                    word_text=word[1][0]['word_text'],
                    word_id=word[1][0]['word_id'],
                    align_id=word[1][0]['align_id'],
                    sent_id=word[1][0]['sent_id'],
                    unaligned_id=word[1][0]['unaligned_id'],
                    sent_aligned=word[1][0]['sent_aligned'],
                    lemma=lemma,
                    PartOfSpeech=upos,
                    UDRelation=deprel,
                    features=feats
                )

def process_lat_data(file):
    data = json.load(file)
    for index in data:
        for sent in data[index]:
            for word in sent:
                if 'lemma' in list(word[1][0].keys()):
                    lemma = word[1][0]['lemma']
                else:
                    lemma = None

                if 'upos' in list(word[1][0].keys()):
                    upos = word[1][0]['upos']
                else:
                    upos = None
                
                if 'deprel' in list(word[1][0].keys()):
                    deprel = word[1][0]['deprel']
                else:
                    deprel = None

                if 'feats' in list(word[1][0].keys()):
                    feats = word[1][0]['feats']
                else:
                    feats = None
                
                LatinWord.objects.create(
                    word_text=word[1][0]['word_text'],
                    word_id=word[1][0]['word_id'],
                    align_id=word[1][0]['align_id'],
                    sent_id=word[1][0]['sent_id'],
                    unaligned_id=word[1][0]['unaligned_id'],
                    sent_aligned=word[1][0]['sent_aligned'],
                    lemma=lemma,
                    PartOfSpeech=upos,
                    UDRelation=deprel,
                    features=feats
                )

def process_fre_data(file):
    data = json.load(file)
    for index in data:
        for sent in data[index]:
            for word in sent:
                if 'lemma' in list(word[1][0].keys()):
                    lemma = word[1][0]['lemma']
                else:
                    lemma = None

                if 'upos' in list(word[1][0].keys()):
                    upos = word[1][0]['upos']
                else:
                    upos = None
                
                if 'deprel' in list(word[1][0].keys()):
                    deprel = word[1][0]['deprel']
                else:
                    deprel = None

                if 'feats' in list(word[1][0].keys()):
                    feats = word[1][0]['feats']
                else:
                    feats = None

                if 'la_sent_id' in list(word[1][0].keys()):
                    lat_sent_id = word[1][0]['la_sent_id']
                else:
                    lat_sent_id = None
                
                if 'la_sent_aligned' in list(word[1][0].keys()):
                    lat_sent_aligned = word[1][0]['la_sent_aligned']
                else:
                    lat_sent_aligned = None

                if 'en_sent_aligned' in list(word[1][0].keys()):
                    eng_sent_aligned = word[1][0]['en_sent_aligned']
                else:
                    eng_sent_aligned = None

                FrenchWord.objects.create(
                    word_text=word[1][0]['word_text'],
                    word_id=word[1][0]['word_id'],
                    en_sent_id=word[1][0]['sent_id'],
                    unaligned_id=word[1][0]['unaligned_id'],
                    la_sent_id=lat_sent_id,
                    en_sent_aligned=eng_sent_aligned,
                    la_sent_aligned=lat_sent_aligned,
                    lemma=lemma,
                    PartOfSpeech=upos,
                    UDRelation=deprel,
                    features=feats
                )