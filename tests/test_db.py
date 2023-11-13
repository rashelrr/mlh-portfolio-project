import unittest
from peewee import *

'''from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memorv SOLite for tests
test_db = SqliteDatabase(': memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
    # Bind model classes to test db. Since we have a complete list of
    # all models, we do not need to recursively bind dependencies
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
    # Not strictly necessary since SOLite in-memory databases only live
    # for the duration of the connection. and in the next step we close
    # the connection... but a good practice all the same
        test_db.drop_tables(MODELS)
    # Close connection to db
        test_db.close()

    def test_timeline_post(self):
    # Create 2 timeline posts
        first_post = TimelinePost.create(name='John Doe',
        email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe',
        email='jame@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

        posts = TimelinePost.select()

        for i in range(len(posts)):
            if posts[i].id == 1:
                assert posts[i].id == 1
                assert posts[i].name == 'John Doe'
                assert posts[i].email == 'john@example.com'
                assert posts[i].content == 'Hello world, I\'m John!'
            else:
                assert posts[i].id == 2
                assert posts[i].name == 'Jane Doe'
                assert posts[i].email == 'jame@example.com'
                assert posts[i].content == 'Hello world, I\'m Jane!'
'''