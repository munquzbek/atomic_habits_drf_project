from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        """
        1 if) check time_to_complete field should be less than 120 sec
        2 if) check that related_habit can only be with is_good field
        3 if) check period field can be 1-7
        """
        for d in data:
            if 'time_to_complete' == d:
                if data['time_to_complete'] > 120:
                    raise serializers.ValidationError({'time_to_complete': 'lead time should be less or equal 120'})

            if 'related_habit' == d:
                if data['related_habit'].is_good is False:
                    raise serializers.ValidationError({'related_habit': 'only good habits can be related_habit'})

            if 'period' == d:
                if data['period'] == 0 or data['period'] > 7:
                    raise serializers.ValidationError({'period': 'period should repeat at least 1 times in week '
                                                                 'or everyday during the week'})

        return data
