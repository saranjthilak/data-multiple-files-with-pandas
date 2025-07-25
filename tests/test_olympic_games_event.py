from nbresult import ChallengeResultTestCase
import pytest


@pytest.mark.optional
class TestOlympicGamesEvent(ChallengeResultTestCase):
    def test_top_10_events_shape(self):
        self.assertEqual(self.result.top_country_event_shape, (10, 1))

    def test_top_events_1(self):
        self.assertEqual(self.result.top_country_1_event, 949)

    def test_top_events_10(self):
        self.assertEqual(self.result.top_country_10_event, 259)
