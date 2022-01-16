from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles 



LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Post(models.Model):

	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
	title  = models.CharField(max_length=255, db_index=True, verbose_name='Заголовок')
	content = models.TextField(default='Type something', verbose_name='Контент')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
	language = models.CharField(choices=LANGUAGE_CHOICES, default='Языки', verbose_name='Языки', max_length=100)
	style = models.CharField(choices=STYLE_CHOICES, default='Стиль', verbose_name='Стиль', max_length=100)

	class Meta:

		verbose_name_plural = 'Пост'
		ordering = ['-created_at']
	
	def __str__(self) -> str:
		return self.title
