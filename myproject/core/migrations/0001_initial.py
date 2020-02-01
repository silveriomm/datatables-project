# Generated by Django 2.2.8 on 2020-01-31 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='telefone')),
                ('gender', models.CharField(blank=True, choices=[('woman', 'mulher'), ('0', ''), ('man', 'homem')], max_length=5, null=True, verbose_name='gênero')),
            ],
            options={
                'verbose_name': 'contato',
                'verbose_name_plural': 'contatos',
                'ordering': ('name',),
            },
        ),
    ]