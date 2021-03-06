# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-20 00:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_question'),
        ('multichoice', '0004_auto_20161203_0653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mcanswer',
            name='question_answer',
        ),
        migrations.RenameField(
            model_name='mcquestion',
            old_name='iscorrect',
            new_name='a_is_correct',
        ),
        migrations.RemoveField(
            model_name='mcquestion',
            name='id',
        ),
        migrations.RemoveField(
            model_name='mcquestion',
            name='inquiz',
        ),
        migrations.RemoveField(
            model_name='mcquestion',
            name='point_value',
        ),
        migrations.RemoveField(
            model_name='mcquestion',
            name='question_text',
        ),
        migrations.AddField(
            model_name='mcquestion',
            name='answer_a',
            field=models.CharField(default='Empty', max_length=200),
        ),
        migrations.AddField(
            model_name='mcquestion',
            name='answer_b',
            field=models.CharField(default='Empty', max_length=200),
        ),
        migrations.AddField(
            model_name='mcquestion',
            name='answer_c',
            field=models.CharField(default='Empty', max_length=200),
        ),
        migrations.AddField(
            model_name='mcquestion',
            name='answer_d',
            field=models.CharField(default='Empty', max_length=200),
        ),
        migrations.AddField(
            model_name='mcquestion',
            name='b_is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mcquestion',
            name='c_is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mcquestion',
            name='d_is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mcquestion',
            name='question_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.Question'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MCAnswer',
        ),
        migrations.DeleteModel(
            name='MCChoice',
        ),
    ]
