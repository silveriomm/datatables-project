from django.db import models

class Person(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField('email', null=True, blank=True)
    phone = models.CharField('telefone', max_length=15, null=True, blank=True)
    GENDER = {
        ('0', ''),
        ('man', 'homem'),
        ('woman', 'mulher'),
    }
    gender = models.CharField(
        'gênero',
        max_length = 5,
        choices = GENDER,
        null = True,
        blank = True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'gender': self.get_gender_display(),
        }