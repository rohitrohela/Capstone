import unittest
import json
from init import create_app


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        self.app = create_app("True")
        self.client = self.app.test_client

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_sample_test(self):
        return_value = True
        self.assertEqual(return_value, True)

    def test_create_movie(self):
        res = self.client().post('/movie', json={
            "title": "Test Movie2",
            "release_date": "23-08-1990"
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_movie(self):
        # first insert a movie and then delete it
        res = self.client().post('/movie', json={
            "title": "Test Movie Deletion",
            "release_date": "23-08-1990"
        })
        data = json.loads(res.data)

        if data['success']:  # If movie insertion is successful, then delete it
            movie_id = data['movie_id']
            deleteUrl = 'movie/' + str(movie_id)
            res = self.client().delete(deleteUrl)
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['recordDeleted'], 1)

    def test_create_actor(self):
        res = self.client().post('/actor', json={
            "name": "Rohit Rohela",
            "age": "33",
            "gender": "Male"
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor(self):
        # first insert a actor and then delete it
        res = self.client().post('/actor', json={
            "name": "Test Actor for Deletion",
            "age": "33",
            "gender": "Male"
        })
        data = json.loads(res.data)

        if data['success']:  # If actor insertion is successful, then delete it
            actor_id = data['actor_id']
            deleteUrl = 'actor/' + str(actor_id)
            res = self.client().delete(deleteUrl)
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['recordDeleted'], 1)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
