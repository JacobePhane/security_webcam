import cv2
import numpy as np
import time

# Set your webcam index (usually 0 for the built-in webcam)
webcam_index = 0

# Set the threshold for change detection
threshold = 10**6

# Initialize the webcam
cap = cv2.VideoCapture(webcam_index)

# Read the first frame for reference
_, prev_frame = cap.read()

print("Sleeeping for 1 minute...")
time.sleep(60)
count = 0
while count < 50:
    # Read the current frame
    _, current_frame = cap.read()
   # current_frame = cv2.GaussianBlur(current_frame, (5, 5), 0)
   # prev_frame = cv2.GaussianBlur(prev_frame, (5, 5), 0)
    # Compute the absolute difference between the current and previous frames
    frame_diff = cv2.absdiff(prev_frame, current_frame)

    # Convert the difference to grayscale
    gray_diff = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)

    # Compute the total pixel difference
    total_diff = np.sum(gray_diff)

    # Print the total difference (optional)
    print(f"Total Difference: {total_diff}")
    
    
    # If the difference exceeds the threshold, take a snapshot
    if total_diff > threshold:
        print("Change detected! Taking a snapshot...")
        count += 1
        # Save the snapshot with a timestamp
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        snapshot_filename = f"snapshot_{timestamp}.png"
        cv2.imwrite(snapshot_filename, current_frame)
        print(f"Snapshot saved as {snapshot_filename}")

    # Update the previous frame
    prev_frame = current_frame

    # Wait for 1 second
    time.sleep(1)

# Release the webcam
cap.release()