# Generated by Django 2.2.10 on 2020-05-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baixa', '0004_auto_20200514_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baixa',
            name='baixa_produto',
            field=models.CharField(max_length=255, verbose_name='Baixa'),
        ),
    ]
