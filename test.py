import cv2

# Initialize the webcam
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Instructions:")
print(" - Press 'SPACE' to capture a photo")
print(" - Press 'q' to quit")

img_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
        
    # Optional mirror effect
    frame = cv2.flip(frame, 1)

    # Show the live preview
    cv2.imshow('Live Camera (Press Space to Shoot)', frame)

    # Wait for keypress
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        # Quit the application
        print("Closing camera...")
        break
        
    elif key == 32:  # 32 is the ASCII code for the Spacebar
        # Save the current frame as an image
        img_name = f"captured_photo_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print(f"📸 Photo saved as {img_name}!")
        img_counter += 1

# Clean up
cap.release()
cv2.destroyAllWindows()