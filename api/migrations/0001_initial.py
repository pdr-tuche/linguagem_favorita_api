# Generated by Django 4.2.4 on 2023-08-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('idade', models.IntegerField()),
                ('tempo_experiencia', models.CharField(max_length=255)),
                ('linguagem_favorita', models.CharField(max_length=255)),
            ],
        ),
    ]
