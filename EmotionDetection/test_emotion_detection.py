"""
python module to test the emotion dection app
"""
# import the required modules to test, stadard unittest and the module for emotion detection 
import unittest
from emotion_detection import emotion_detector

## Create class to hold the function for the tests.
class TestEmotionDetector(unittest.TestCase):
    """ Class to hold the functions to be tested."""

    def test_emotion_detector(self):
        """ Function testing the funciton emotion_detector contained within the emotion_detection module"""
        #unit tests
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], "disgust")
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotion"], "fear")

if __name__=='__main__':
    unittest.main()