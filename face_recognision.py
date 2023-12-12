import cv2
import numpy as np
import face_recognition as fr

# Load the video capture
video_capture = cv2.VideoCapture(0)

# Load the image and compute its face encoding
image = fr.load_image_file('Jovian_Profile.PNG')
image_face_encoding = fr.face_encodings(image)[0]

# Create a list of known face encodings and names
known_face_encodings = [image_face_encoding]
known_face_names = ["Nambative"]

# Start the video capture loop
while True:
    # Read a frame from the video capture
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    # Detect faces in the frame
    fc_locations = fr.face_locations(rgb_frame)
    fc_encodings = fr.face_encodings(rgb_frame, fc_locations)

    # Process each face in the frame
    for (top, right, bottom, left), face_encoding in zip(fc_locations, fc_encodings):
        # Compare face encodings with known encodings
        matches = fr.compare_faces(known_face_encodings, face_encoding)
        name = "unknown"
        fc_distances = fr.face_distances(known_face_encodings, face_encoding)
        match_index = np.argmin(fc_distances)
        if matches[match_index]:
            name = known_face_names[match_index]

        # Draw bounding box and display name on the frame
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the frame
    cv2.imshow("Simplilearn face detection system", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
video_capture.release()
cv2.destroyAllWindows()


