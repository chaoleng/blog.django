# Generated by Django 2.1.3 on 2018-12-11 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='queston_text',
            new_name='question_text',
        ),
    ]