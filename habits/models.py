from django.conf import settings
from django.db import models

from rest_framework import serializers

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='user', **NULLABLE)
    action = models.CharField(max_length=300, verbose_name='action')
    place = models.CharField(max_length=50, verbose_name='place of action')
    time = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='time of action')

    is_good = models.BooleanField(default=False, verbose_name='is good habit')
    related_habit = models.ForeignKey('Habit', on_delete=models.CASCADE, verbose_name='related habit',
                                      **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name='reward after completed action', **NULLABLE)

    period = models.PositiveIntegerField(verbose_name='periodicity of habit', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(verbose_name='time to complete action', **NULLABLE)

    is_published = models.BooleanField(default=False, verbose_name='is published')

    def save(self, *args, **kwargs):
        """
        1. if is_good is true you cant add related_habit and reward
        2. check that object can have only one field related_habit or reward
        """
        if self.is_good and (self.related_habit or self.reward):
            raise serializers.ValidationError(
                {'is_good': 'if is_good field is True you cant fill reward and related_habit'})

        if self.related_habit is not None and self.reward is not None:
            raise serializers.ValidationError('Need to fill only one field related_habit or reward')

        return super().save()

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'
