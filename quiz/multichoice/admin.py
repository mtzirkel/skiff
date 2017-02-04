
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from models import *
#######
#Admin#
#######
"""
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 2


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'creation', 'possible',)
    search_fields = ('name', 'creator')
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    search_fields = ('question', 'quiz', 'value',)
    list_display = ('question', 'quiz', 'value',)

admin.site.register(MCQuestion, QuestionAdmin)
"""

#class QuestionAttemptInline(admin.StackedInline):
#    model = QuestionAttempt
           
#class QuizAttemptAdmin(admin.ModelAdmin):
#    inlines = [QuestionAttemptInline]
#    search_fields = ('quiz', 'student', 'date')
#    list_display = ('quiz', 'student', 'date', 'score', 'possible')

#admin.site.register(QuizAttempt, QuizAttemptAdmin)
#admin.site.register(QuestionAttempt)
