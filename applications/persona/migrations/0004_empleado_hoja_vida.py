# Generated by Django 3.2 on 2024-01-05 21:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_auto_20240105_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]
