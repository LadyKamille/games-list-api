from application.api.game.serializers import GameSerializer
from application.api.game.tests.test_setup import TestSetup


class GameTestSerializers(TestSetup):
    def test_contains_expected_fields(self):
        serializer = GameSerializer(instance=self.game)
        data = serializer.data
        self.assertEqual(set(data.keys()), {'id', 'title', 'description'})

    def test_title_field_content(self):
        serializer = GameSerializer(instance=self.game)
        data = serializer.data
        self.assertEqual(data['title'], self.game_data['title'])

    def test_description_field_content(self):
        serializer = GameSerializer(instance=self.game)
        data = serializer.data
        self.assertEqual(data['description'], self.game_data['description'])
