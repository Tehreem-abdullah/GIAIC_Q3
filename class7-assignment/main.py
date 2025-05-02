import cv2

class FaceDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                                  'haarcascade_frontalface_default.xml')
        self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                                   'haarcascade_smile.xml')

    def detect_faces(self, gray_frame):
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
        return faces

    def detect_smile(self, gray_face):
        smiles = self.smile_cascade.detectMultiScale(gray_face, scaleFactor=1.8, minNeighbors=20)
        return smiles


class EmotionRecognizer:
    def recognize_emotion(self, face_gray, detector):
        smiles = detector.detect_smile(face_gray)
        if len(smiles) > 0:
            return "Happy"
        else:
            return "Neutral"


class EmotionApp:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.detector = FaceDetector()
        self.recognizer = EmotionRecognizer()

    def run(self):
        print("Press 'q' to exit the app.")
        while True:
            ret, frame = self.camera.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.detector.detect_faces(gray)

            for (x, y, w, h) in faces:
                face_gray = gray[y:y+h, x:x+w]
                emotion = self.recognizer.recognize_emotion(face_gray, self.detector)

                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.9, (0, 255, 0), 2)

            cv2.imshow('Emotion Detector App', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = EmotionApp()
    app.run()