from application.api.game.models import Game
from application.api.game.tests.test_setup import TestSetup


class GameTestModels(TestSetup):
    def test_title_label(self):
        title = Game.objects.get(id=1)
        field_label = title._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        title = Game.objects.get(id=1)
        max_length = title._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_description_label(self):
        description = Game.objects.get(id=1)
        field_label = description._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        description = Game.objects.get(id=1)
        max_length = description._meta.get_field('description').max_length
        self.assertEqual(max_length, 500)

