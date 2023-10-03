from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['id']

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    tags = models.ManyToManyField(Tag, related_name='tags', through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='+')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='+', verbose_name='Раздел')
    is_main = models.BooleanField(verbose_name='Основной')

    def __str__(self):
        return self.article.title + " " + self.tag.name

    class Meta:
        verbose_name_plural = 'Тематики статьи'
        ordering = ['-is_main', 'tag__name']
