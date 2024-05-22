from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        """
        1 if) check time_to_complete field should be less than 120 sec

        2 if) check if field is_good is true can add only field related_habit
        3 if) if field is_good is false user can add only field reward
        """
        if data['time_to_complete'] > 120:
            raise serializers.ValidationError({'time_to_complete': 'lead time should be less than 120'})

        if data['related_habit'].is_good is False:
            raise serializers.ValidationError({'related_habit': 'only good habits can be related_habit'})
        print(data)
        return data
