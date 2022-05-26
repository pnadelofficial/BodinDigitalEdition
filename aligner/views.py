from itertools import chain
from django.shortcuts import get_object_or_404, render
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView
from aligner.models import FrenchWord, EnglishWord, LatinWord
import json
import glob

## Helper objects
## Index look-up tables
def generateFrEnAlignedIndices(chapter_number):
    for FrEn in list(glob.glob("aligner\static\FrEn_aligned_indices*.json")):
        if str(chapter_number) in FrEn:
            fren_aligned_indices = open(FrEn)
            fren_aligned_data = json.load(fren_aligned_indices)
            return fren_aligned_data

def generateFrLaAlignedIndices(chapter_number):
    for FrLa in list(glob.glob("aligner\static\FrLa_aligned_indices*.json")):
        if str(chapter_number) in FrLa:
            frla_aligned_indices = open(FrLa)
            frla_aligned_data = json.load(frla_aligned_indices)
            return frla_aligned_data

# fren_aligned_indices = open(r'aligner\static\FrEn_aligned_indices.json')
# fren_aligned_data = json.load(fren_aligned_indices) 

# frla_aligned_indices = open(r'aligner\static\FrLa_aligned_indices.json')
# frla_aligned_data = json.load(frla_aligned_indices) 

# enla_aligned_indices = open(r'aligner\static\EnLa_aligned_indices.json')
# enla_aligned_data = json.load(enla_aligned_indices) 

## Unaligned/aligned dict updates
fr_unaligned_list = FrenchWord.objects.order_by().values('unaligned_id').distinct()
# fr_aligned_list = FrenchWord.objects.order_by().values('en_sent_id').distinct()

# for i in fr_unaligned_list:
#     for word in FrenchWord.objects.all():
#         if int(word.unaligned_id) == int(i['unaligned_id']):
#             for j in fr_aligned_list:
#                 if j['en_sent_id'] == int(word.en_sent_id):
#                     i['en_sent_id'] = j['en_sent_id']

# en_unaligned_list = EnglishWord.objects.order_by().values('unaligned_id').distinct()
# en_aligned_list = EnglishWord.objects.order_by().values('sent_id').distinct()

# for i in en_unaligned_list:
#     for word in EnglishWord.objects.all():
#         if int(word.unaligned_id) == int(i['unaligned_id']):
#             for j in en_aligned_list:
#                 if j['sent_id'] == int(word.sent_id):
#                     i['sent_id'] = j['sent_id']

# la_unaligned_list = LatinWord.objects.order_by().values('unaligned_id').distinct()
# la_aligned_list = LatinWord.objects.order_by().values('sent_id').distinct()

# for i in la_unaligned_list:
#     for word in LatinWord.objects.all():
#         if int(word.unaligned_id) == int(i['unaligned_id']):
#             for j in la_aligned_list:
#                 if j['sent_id'] == int(word.sent_id):
#                     i['sent_id'] = j['sent_id']

## Unaligned id string --> int
# fr_unaligned_int = [dict([a, int(x)] for a, x in b.items()) for b in FrenchWord.objects.order_by().values('unaligned_id').distinct()]
# en_unaligned_int = [dict([a, int(x)] for a, x in b.items()) for b in EnglishWord.objects.order_by().values('unaligned_id').distinct()]
# la_unaligned_int = [dict([a, int(x)] for a, x in b.items()) for b in LatinWord.objects.order_by().values('unaligned_id').distinct()]

def home_view(request):
    return render(request, 'aligner/home.html')

def ack_view(request):
    return render(request, 'aligner/acknowledgements.html')

def chapter_choices(request):
    return render(request, 'aligner/chapter_choices.html')

def fr_sentence_view(request, index, chapter_number):
    context_dict = {
        'index':str(index),
        'chapter_number':chapter_number,
        'unaligned_aligned':fr_unaligned_list,
        'french_sents': [dict([a, int(x)] for a, x in b.items()) for b in FrenchWord.objects.order_by().values('unaligned_id').distinct()],
        'french_words': FrenchWord.objects.all(),
        'english_sents': EnglishWord.objects.order_by().values('sent_id').distinct(),
        'english_words': EnglishWord.objects.all(),
        'latin_sents': LatinWord.objects.order_by().values('sent_id').distinct(),
        'latin_words': LatinWord.objects.all(),
        'fren_aligned_indices': generateFrEnAlignedIndices(chapter_number),
        'frla_aligned_indices': generateFrLaAlignedIndices(chapter_number)
    }
    return render(request, 'aligner/fr_sentence.html', context_dict)

def eng_sentence_view(request, index, chapter_number):
    fren_aligned_data_rev = [(t[1],t[0]) for t in generateFrEnAlignedIndices(chapter_number)]

    context_dict = {
        'index':index,
        'chapter_number':chapter_number,
        'french_sents': FrenchWord.objects.order_by().values('en_sent_id').distinct(),
        'french_words': FrenchWord.objects.all(),
        'english_sents': [dict([a, int(x)] for a, x in b.items()) for b in EnglishWord.objects.order_by().values('unaligned_id').distinct()],
        'english_words': EnglishWord.objects.all(),
        'latin_sents': LatinWord.objects.order_by().values('sent_id').distinct(),
        'latin_words': LatinWord.objects.all(),
        'fren_aligned_indices': fren_aligned_data_rev,
        'frla_aligned_indices': generateFrLaAlignedIndices(chapter_number)
    }
    return render(request, 'aligner/eng_sentence.html', context_dict)

def lat_sentence_view(request, index, chapter_number):
    frla_aligned_data_rev = [(t[1],t[0]) for t in generateFrLaAlignedIndices(chapter_number)]

    context_dict = {
        'index':index,
        'chapter_number':chapter_number,
        'french_sents': FrenchWord.objects.order_by().values('la_sent_id').distinct(),
        'french_words': FrenchWord.objects.all(),
        'english_sents': EnglishWord.objects.order_by().values('sent_id').distinct(),
        'english_words': EnglishWord.objects.all(),
        'latin_sents': [dict([a, int(x)] for a, x in b.items()) for b in LatinWord.objects.order_by().values('unaligned_id').distinct()],
        'latin_words': LatinWord.objects.all(),
        'fren_aligned_indices': generateFrEnAlignedIndices(chapter_number),
        'frla_aligned_indices': frla_aligned_data_rev
    }
    return render(request, 'aligner/lat_sentence.html', context_dict)

# Create your views here.
class WordListView(ListView):
    #model_list.html
    model = FrenchWord

    ## NEED TO LINK CHAPTER NUMBER FROM CHAPTER_CHOICES.HTML ##

    def makeFrAlignedUnaligned(self):
        fr_unaligned_list = FrenchWord.objects.filter(chapter_number=self.kwargs['chapter_number']).order_by().values('unaligned_id').distinct()
        fr_aligned_list = FrenchWord.objects.filter(chapter_number=self.kwargs['chapter_number']).order_by().values('en_sent_id').distinct()

        for i in fr_unaligned_list:
            for word in FrenchWord.objects.filter(chapter_number=self.kwargs['chapter_number']):
                if int(word.unaligned_id) == int(i['unaligned_id']):
                    for j in fr_aligned_list:
                        if j['en_sent_id'] == int(word.en_sent_id):
                            i['en_sent_id'] = j['en_sent_id']
        return fr_unaligned_list

    def makeEnLaAlignedUnaligned(self, word_object):
        unaligned_list = word_object.objects.filter(chapter_number=self.kwargs['chapter_number']).order_by().values('unaligned_id').distinct()
        aligned_list = word_object.objects.filter(chapter_number=self.kwargs['chapter_number']).order_by().values('sent_id').distinct()

        for i in unaligned_list:
            for word in word_object.objects.filter(chapter_number=self.kwargs['chapter_number']):
                if int(word.unaligned_id) == int(i['unaligned_id']):
                    for j in aligned_list:
                        if j['sent_id'] == int(word.sent_id):
                            i['sent_id'] = j['sent_id']
        return unaligned_list

    def get_context_data(self, **kwargs):
        context = super(WordListView, self).get_context_data(**kwargs)
        context['chapter_number'] = self.kwargs['chapter_number']
        context['fr_unaligned_aligned'] = self.makeFrAlignedUnaligned()
        context['en_unaligned_aligned'] = self.makeEnLaAlignedUnaligned(EnglishWord)
        context['la_unaligned_aligned'] = self.makeEnLaAlignedUnaligned(LatinWord)
        context['french_sents'] = FrenchWord.objects.filter(chapter_number=self.kwargs['chapter_number']).order_by().values('unaligned_id').distinct()
        context['french_words'] = FrenchWord.objects.filter(chapter_number=self.kwargs['chapter_number'])
        context['english_sents'] = EnglishWord.objects.filter(chapter_number=self.kwargs['chapter_number']).order_by().values('unaligned_id').distinct()
        context['english_words'] = EnglishWord.objects.filter(chapter_number=self.kwargs['chapter_number'])
        context['latin_sents'] = LatinWord.objects.filter(chapter_number=self.kwargs['chapter_number']).order_by().values('unaligned_id').distinct()
        context['latin_words'] = LatinWord.objects.filter(chapter_number=self.kwargs['chapter_number'])
        return context