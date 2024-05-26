from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitAPITest(APITestCase):

    def setUp(self) -> None:
        """create user for authentication and habit in db"""
        self.user = User.objects.create(
            email="test@test.com",
            password='12345'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            action="TestHabit",
            place="TestPlace",
            time="2024-05-27T00:00:00Z",
            is_published=True,
            user=self.user
        )

    def test_create_habit(self):
        """Testing creating habits"""
        data = {
            "action": self.habit.action,
            "place": self.habit.place,
            "time": self.habit.time,
            "user": self.user.id
        }

        response = self.client.post(
            '/habits/create/',
            data=data
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_habit(self):
        response = self.client.get('/habits/list/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 5, 'action': 'TestHabit', 'place': 'TestPlace', 'time': '2024-05-27T00:00:00Z', 'is_good': False,
                 'reward': None, 'period': None, 'time_to_complete': None, 'is_published': True, 'user': 4,
                 'related_habit': None}]}

        )

    def test_habit_list_public(self):
        response = self.client.get('/habits/list/public/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 4, 'action': 'TestHabit', 'place': 'TestPlace', 'time': '2024-05-27T00:00:00Z', 'is_good': False,
                 'reward': None, 'period': None, 'time_to_complete': None, 'is_published': True, 'user': 3,
                 'related_habit': None}]}
        )

    def test_update_habit(self):
        data = {
            'action': "TestUpdateAction"
        }

        response = self.client.patch(f'/habits/update/{self.habit.id}/', data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        # refresh database after updating
        self.habit.refresh_from_db()

        self.assertEqual(
            self.habit.action,
            data['action']
        )

    def test_delete_habit(self):
        response = self.client.delete(f'/habits/delete/{self.habit.id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
