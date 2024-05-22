from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        """
        check if field is_good is true can add only field related_habit
        if field is_good is false user can add only field reward
        """
        if data['is_good']:
            if data['reward']:
                raise serializers.ValidationError({'reward': 'Change habit to is good to add reward'})
        elif not data['is_good']:
            if data['related_habit']:
                raise serializers.ValidationError({'related_habit': 'Change habit to is not good to add related_habit'})
        return data
