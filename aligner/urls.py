from django.urls import path
from . views import WordListView, fr_sentence_view, eng_sentence_view, lat_sentence_view

app_name = 'aligner'

urlpatterns = [
    path('',WordListView.as_view(), name="word_list_view"),
    path('fr_sentence/<int:index>/', fr_sentence_view, name='fr_sentence_view'),
    path('en_sentence/<int:index>/', eng_sentence_view, name='eng_sentence_view' ),
    path('lat_sentence/<int:index>/', lat_sentence_view, name='lat_sentence_view' )
]