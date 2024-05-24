import os
import telebot
from celery import shared_task

from habits.models import Habit
from users.models import User

TOKEN = os.getenv('TGTOKEN')

tb = telebot.TeleBot(TOKEN)

day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# tb.send_message(426795208, 'haha loh')


@shared_task
def send_notifications():
    user = User.objects.all()
    for u in user:
        habit = Habit.objects.filter(user=u)
        for h in habit:
            if u.telegram_id:
                tb.send_message(
                    u.telegram_id,
                    f"NOTIFICATION action:{h.action} place:{h.place} date:{h.time.date()} time:{h.time.time()} "
                    f"every {day[h.period]} {h.related_habit if h.reltaed_habit is not None else h.reward}")
