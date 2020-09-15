from rest_framework.test import APITestCase
from django.urls import reverse

from application.api.game.models import Game


class TestSetup(APITestCase):
    def setUp(self):
        self.game_list_url = reverse('game-list')
        self.game_detail_url = reverse('game-detail', kwargs={'pk': 1})
        self.game_detail_invalid_url = reverse('game-detail', kwargs={'pk': 2})

        self.game_data = {
            'title': 'Civilization VI',
            'description': 'Turn-based strategy game.',
        }

        self.game = Game.objects.create(title=self.game_data['title'],
                                        description=self.game_data['description'])

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
