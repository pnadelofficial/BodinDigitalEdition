from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView
from aligner.models import FrenchWord, EnglishWord, LatinWord
import json

## Helper objects
## Index look-up tables
fren_aligned_indices = open('FrEn_aligned_indices.json')
fren_aligned_data = json.load(fren_aligned_indices) 

frla_aligned_indices = open('FrLa_aligned_indices.json')
frla_aligned_data = json.load(frla_aligned_indices) 

enla_aligned_indices = open('EnLa_aligned_indices.json')
enla_aligned_data = json.load(enla_aligned_indices) 

fr_unaligned_list = FrenchWord.objects.order_by().values('unaligned_id').distinct()
fr_aligned_list = FrenchWord.objects.order_by().values('en_sent_id').distinct()

## Unaligned/aligned dict updates
for i in fr_unaligned_list:
    for word in FrenchWord.objects.all():
        if int(word.unaligned_id) == int(i['unaligned_id']):
            for j in fr_aligned_list:
                if j['en_sent_id'] == int(word.en_sent_id):
                    i['en_sent_id'] = j['en_sent_id']

en_unaligned_list = EnglishWord.objects.order_by().values('unaligned_id').distinct()
en_aligned_list = EnglishWord.objects.order_by().values('sent_id').distinct()

for i in en_unaligned_list:
    for word in EnglishWord.objects.all():
        if int(word.unaligned_id) == int(i['unaligned_id']):
            for j in en_aligned_list:
                if j['sent_id'] == int(word.sent_id):
                    i['sent_id'] = j['sent_id']

la_unaligned_list = LatinWord.objects.order_by().values('unaligned_id').distinct()
la_aligned_list = LatinWord.objects.order_by().values('sent_id').distinct()

for i in la_unaligned_list:
    for word in LatinWord.objects.all():
        if int(word.unaligned_id) == int(i['unaligned_id']):
            for j in la_aligned_list:
                if j['sent_id'] == int(word.sent_id):
                    i['sent_id'] = j['sent_id']

## Unaligned id string --> int
fr_unaligned_int = [dict([a, int(x)] for a, x in b.items()) for b in FrenchWord.objects.order_by().values('unaligned_id').distinct()]
en_unaligned_int = [dict([a, int(x)] for a, x in b.items()) for b in EnglishWord.objects.order_by().values('unaligned_id').distinct()]
la_unaligned_int = [dict([a, int(x)] for a, x in b.items()) for b in LatinWord.objects.order_by().values('unaligned_id').distinct()]

def home_view(request):
    return render(request, 'aligner/home.html')

def ack_view(request):
    return render(request, 'aligner/acknowledgements.html')

def fr_sentence_view(request, index):
    context_dict = {
        'index':index,
        'unaligned_aligned':fr_unaligned_list,
        'french_sents': fr_unaligned_int,
        'french_words': FrenchWord.objects.all(),
        'english_sents': EnglishWord.objects.order_by().values('sent_id').distinct(),
        'english_words': EnglishWord.objects.all(),
        'latin_sents': LatinWord.objects.order_by().values('sent_id').distinct(),
        'latin_words': LatinWord.objects.all(),
        'fren_aligned_indices': fren_aligned_data,
        'frla_aligned_indices': frla_aligned_data
    }
    return render(request, 'aligner/fr_sentence.html', context_dict)

def eng_sentence_view(request, index):
    fren_aligned_data_rev = [(t[1],t[0]) for t in fren_aligned_data]

    context_dict = {
        'index':index,
        'french_sents': FrenchWord.objects.order_by().values('en_sent_id').distinct(),
        'french_words': FrenchWord.objects.all(),
        'english_sents': en_unaligned_int,
        'english_words': EnglishWord.objects.all(),
        'latin_sents': LatinWord.objects.order_by().values('sent_id').distinct(),
        'latin_words': LatinWord.objects.all(),
        'fren_aligned_indices': fren_aligned_data_rev,
        'frla_aligned_indices': frla_aligned_data
    }
    return render(request, 'aligner/eng_sentence.html', context_dict)

def lat_sentence_view(request, index):
    fren_aligned_data_rev = [(t[1],t[0]) for t in fren_aligned_data]
    frla_aligned_data_rev = [(t[1],t[0]) for t in frla_aligned_data]

    context_dict = {
        'index':index,
        'french_sents': FrenchWord.objects.order_by().values('la_sent_id').distinct(),
        'french_words': FrenchWord.objects.all(),
        'english_sents': EnglishWord.objects.order_by().values('sent_id').distinct(),
        'english_words': EnglishWord.objects.all(),
        'latin_sents': la_unaligned_int,
        'latin_words': LatinWord.objects.all(),
        'fren_aligned_indices': fren_aligned_data,
        'frla_aligned_indices': frla_aligned_data_rev
    }
    return render(request, 'aligner/lat_sentence.html', context_dict)

# Create your views here.
class WordListView(ListView):
    #model_list.html
    model = FrenchWord

    def get_context_data(self, **kwargs):
        context = super(WordListView, self).get_context_data(**kwargs)
        context['fr_unaligned_aligned'] = fr_unaligned_list
        context['en_unaligned_aligned'] = en_unaligned_list
        context['la_unaligned_aligned'] = la_unaligned_list
        context['french_sents'] = FrenchWord.objects.order_by().values('unaligned_id').distinct()
        context['french_words'] = FrenchWord.objects.all()
        context['english_sents'] = EnglishWord.objects.order_by().values('unaligned_id').distinct()
        context['english_words'] = EnglishWord.objects.all()
        context['latin_sents'] = LatinWord.objects.order_by().values('unaligned_id').distinct()
        context['latin_words'] = LatinWord.objects.all()
        return context