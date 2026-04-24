import unittest
from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetector(unittest.TestCase):
    #test for emotion detector
    def test_emotion_detector(self):
        #testing for joy
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
        #testing for anger
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
        #testing for disgust
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        #testing for sadness
        result = emotion_detector("I am sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        #testing for fear
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')
if __name__ == '__main__':
    unittest.main()