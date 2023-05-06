import unittest
import json
from init import create_app
from token_auth import getRoleBasedToken


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    castingAssistantToken = ""
    castingDirectorToken = ""
    executiveProducerToken = ""

    def setUp(self):
        self.app = create_app("True")
        self.client = self.app.test_client

        TriviaTestCase.castingAssistantToken = getRoleBasedToken(TriviaTestCase.castingAssistantToken,
                                                                 "castingAssistant")
        TriviaTestCase.castingDirectorToken = getRoleBasedToken(TriviaTestCase.castingDirectorToken,
                                                                "castingDirector")
        TriviaTestCase.executiveProducerToken = getRoleBasedToken(TriviaTestCase.executiveProducerToken,
                                                                  "executiveProducer")

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_getMovie_success(self):
        res = self.client().post('/movie', json={
            "title": "Test Movie get",
            "release_date": "23-08-1990"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)

        if data['success']:  # If movie insertion is successful, then get it
            movie_id = data['movie_id']
            getUrl = 'movie/' + str(movie_id)
            res = self.client().get(getUrl,
                                    headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['movie']['title'], 'Test Movie get')
            self.assertEqual(data['movie']['id'], movie_id)

    def test_getMovie_fail(self):
        getUrl = 'movie/' + str(99999999)
        res = self.client().get(getUrl,
                                headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_createMovie_success(self):
        res = self.client().post('/movie', json={
            "title": "Test Movie2",
            "release_date": "23-08-1990"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_createMovie_fail(self):
        res = self.client().post('/movie', json={
            "title": "Test Movie2",
            "release_date": "hellow"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['description'], 'Date format is not correct')

    def test_deleteMovie_success(self):
        # first insert a movie and then delete it
        res = self.client().post('/movie', json={
            "title": "Test Movie Deletion",
            "release_date": "23-08-1990"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)

        if data['success']:  # If movie insertion is successful, then delete it
            movie_id = data['movie_id']
            deleteUrl = 'movie/' + str(movie_id)
            res = self.client().delete(deleteUrl,
                                       headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['recordDeleted'], 1)

    def test_deleteMovie_fail(self):
        deleteUrl = 'movie/' + str(9999999)
        res = self.client().delete(deleteUrl,
                                   headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)

    def test_editMovie_success(self):
        # first insert a movie and then edit it
        res = self.client().post('/movie', json={
            "title": "Test Movie Deletion",
            "release_date": "23-08-1990"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)

        if data['success']:  # If movie insertion is successful, then edit it
            movie_id = data['movie_id']
            editUrl = 'movie/' + str(movie_id)
            res = self.client().patch(editUrl, json={
                "title": "Test Movie paching",
            }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['recordUpdated'], 1)

    def test_editMovie_fail(self):
        editUrl = 'movie/' + str(9999999)
        res = self.client().patch(editUrl, json={
            "title": "Test Movie paching",
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['description'], 'No Movie Found')

    def test_getActor_success(self):
        # first insert a actor and then assert it
        res = self.client().post('/actor', json={
            "name": "Test Actor for get",
            "age": "33",
            "gender": "Male"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)

        if data['success']:  # If actor insertion is successful, then get the details
            actor_id = data['actor_id']
            getUrl = 'actor/' + str(actor_id)
            res = self.client().get(getUrl,
                                    headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['actor']['name'], 'Test Actor for get')
            self.assertEqual(data['actor']['age'], 33)

    def test_getActor_fail(self):
        getUrl = 'actor/' + str(99999999)
        res = self.client().get(getUrl,
                                headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_createActor_success(self):
        res = self.client().post('/actor', json={
            "name": "Rohit Rohela",
            "age": "33",
            "gender": "Male"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_createActor_fail(self):
        res = self.client().post('/actor', json={
            "name": "Rohit Rohela",
            "age": "thirty three",
            "gender": "Male"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)

    def test_deleteActor_success(self):
        # first insert a actor and then delete it
        res = self.client().post('/actor', json={
            "name": "Test Actor for Deletion",
            "age": "33",
            "gender": "Male"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)

        if data['success']:  # If actor insertion is successful, then delete it
            actor_id = data['actor_id']
            deleteUrl = 'actor/' + str(actor_id)
            res = self.client().delete(deleteUrl,
                                       headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['recordDeleted'], 1)

    def test_deleteActor_fail(self):
        deleteUrl = 'actor/' + str(99999999)
        res = self.client().delete(deleteUrl,
                                   headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['recordDeleted'], 0)

    def test_editActor_success(self):
        # first insert a actor and then delete it
        res = self.client().post('/actor', json={
            "name": "Test Actor for Deletion",
            "age": "33",
            "gender": "Male"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)

        if data['success']:  # If actor insertion is successful, then edit it
            actor_id = data['actor_id']
            editUrl = 'actor/' + str(actor_id)
            res = self.client().patch(editUrl,
                                      json={
                                          "name": "Rohit",
                                          "age": "30"
                                      },
                                      headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['recordPatched'], 1)

    def test_editActor_fail(self):
        # first insert a actor and then delete it
        res = self.client().post('/actor', json={
            "name": "Test Actor for Deletion",
            "age": "33",
            "gender": "Male"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)

        if data['success']:  # If actor insertion is successful, then edit it
            actor_id = data['actor_id']
            editUrl = 'actor/' + str(actor_id)
            res = self.client().patch(editUrl,
                                      json={
                                          "name": "Rohit",
                                          "age": "Thirty"
                                      },
                                      headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['recordPatched'], 0)

    def test_editActorNotFound_fail(self):
        editUrl = 'actor/' + str(9999999)
        res = self.client().patch(editUrl,
                                  json={
                                      "name": "Rohit"
                                  },
                                  headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['description'], 'No actor Found')

    def test_getMovieForAssistantRole_success(self):
        res = self.client().post('/movie', json={
            "title": "Test Movie get",
            "release_date": "23-08-1990"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.castingAssistantToken})
        data = json.loads(res.data)

        if data['success']:  # If movie insertion is successful, then get it
            movie_id = data['movie_id']
            getUrl = 'movie/' + str(movie_id)
            res = self.client().get(getUrl,
                                    headers={'Authorization': 'Bearer ' + TriviaTestCase.castingAssistantToken})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['movie']['title'], 'Test Movie get')
            self.assertEqual(data['movie']['id'], movie_id)

    def test_createMovieForAssistantRole_fail(self):
        res = self.client().post('/movie', json={
            "title": "Test Movie2",
            "release_date": "hellow"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.castingAssistantToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Requested permission not found')

    def test_createMovieForCastingDirector_fail(self):
        res = self.client().post('/movie', json={
            "title": "Test Movie2",
            "release_date": "23-08-1990"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.castingDirectorToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Requested permission not found')

    def test_createActorForCastingDirector_success(self):
        res = self.client().post('/actor', json={
            "name": "Rohit Rohela",
            "age": "33",
            "gender": "Male"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.castingDirectorToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_createMovieForExecutiveProducer_success(self):
        res = self.client().post('/movie', json={
            "title": "Test Movie2",
            "release_date": "23-08-1990"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_deleteMovieForExecutiveProducer_success(self):
        # first insert a movie and then delete it
        res = self.client().post('/movie', json={
            "title": "Test Movie Deletion",
            "release_date": "23-08-1990"
        }, headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
        data = json.loads(res.data)

        if data['success']:  # If movie insertion is successful, then delete it
            movie_id = data['movie_id']
            deleteUrl = 'movie/' + str(movie_id)
            res = self.client().delete(deleteUrl,
                                       headers={'Authorization': 'Bearer ' + TriviaTestCase.executiveProducerToken})
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
            self.assertEqual(data['recordDeleted'], 1)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
