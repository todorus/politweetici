import unittest
import tests.lib.utils as utils


class ImportTweets(unittest.TestCase):

    def setUp(self):
        # TODO connect to db
        # TODO wipe db
        stub = True

    def test_empty_db(self):
        # Given there is a json file containing a feed from the twitter api
        # TODO define data input

        # When the TweetConverter processes this data
        # TODO process data with tweet converter

        # Then It will have added these tweets to the db
        # TODO define expected data in db
        # TODO check against db
        self.fail('test not implemented')

    def test_duplicate_id(self):
        # Given there is a json file containing a feed from the twitter api
        # TODO define data input
        # And some of these tweets are already in the db
        # TODO write a few tweets to the db

        # When the TweetConverter processes this data
        # TODO process data with tweet converter

        # Then It will have added the non-duplicate tweets to the db
        # TODO define expected data in db
        # TODO check against db
        self.fail('test not implemented')
