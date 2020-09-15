import json
from application.api.game.tests.test_setup import TestSetup


class TestViews(TestSetup):
    def test_get_game_list(self):
        response = self.client.get(self.game_list_url)
        self.assertEqual(response.status_code, 200)

    def test_cannot_create_game_without_data(self):
        response = self.client.post(self.game_list_url)
        self.assertEqual(response.status_code, 400)

    def test_creates_game_with_data(self):
        response = self.client.post(self.game_list_url, self.game_data, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], self.game_data['title'])
        self.assertEqual(response.data['description'], self.game_data['description'])

    def test_cannot_update_without_valid_id(self):
        response = self.client.put(self.game_detail_invalid_url)
        self.assertEqual(response.status_code, 404)

    def test_updates_game_with_valid_id(self):
        response = self.client.put(self.game_detail_url, {'title': 'Civilization V'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content),
                         {'title': 'Civilization V',
                          'id': 1,
                          'description': self.game_data['description']})

    def test_cannot_delete_without_valid_id(self):
        response = self.client.delete(self.game_detail_invalid_url)
        self.assertEqual(response.status_code, 404)

    def test_deletes_game_with_valid_id(self):
        response = self.client.delete(self.game_detail_url)
        self.assertEqual(response.status_code, 204)
