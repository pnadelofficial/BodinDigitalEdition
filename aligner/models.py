from django.db import models
from email.policy import default

# Create your models here.
class FrenchWord(models.Model):
    word_text = models.CharField(max_length=30, default='None Provided')
    word_id = models.IntegerField()
    en_sent_id = models.IntegerField(null=True, blank=True, default='None Provided')
    la_sent_id = models.IntegerField(null=True, blank=True, default='None Provided')
    unaligned_id = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    en_sent_aligned = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    la_sent_aligned = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    lemma = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    PartOfSpeech = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    UDRelation = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    features = models.CharField(max_length=30, null=True, blank=True, default='None Provided')

    def __str__(self):
        return f'{self.word_text}'

class EnglishWord(models.Model):
    word_text = models.CharField(max_length=30, default='None Provided')
    word_id = models.IntegerField()
    sent_id = models.IntegerField()
    unaligned_id = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    sent_aligned = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    align_id = models.CharField(max_length=30, default='None Provided')
    lemma = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    PartOfSpeech = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    UDRelation = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    features = models.CharField(max_length=30, null=True, blank=True, default='None Provided')

    def __str__(self):
        return f'{self.word_text}'

class LatinWord(models.Model):
    word_text = models.CharField(max_length=30, default='None Provided')
    word_id = models.IntegerField()
    sent_id = models.IntegerField()
    unaligned_id = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    sent_aligned = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    align_id = models.CharField(max_length=30, default='None Provided')
    lemma = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    PartOfSpeech = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    UDRelation = models.CharField(max_length=30, null=True, blank=True, default='None Provided')
    features = models.CharField(max_length=30, null=True, blank=True, default='None Provided')

    def __str__(self):
        return f'{self.word_text}'