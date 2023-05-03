# VIMOA 
# (Video Motion Amplification) version 1.00
import cv2

# Open the input video file
input_video = cv2.VideoCapture('input_video.mp4')

# Get the frames per second (fps) and frame size of the input video
fps = int(input_video.get(cv2.CAP_PROP_FPS))
frame_size = (int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Create the VideoWriter object to write the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('output_video.avi', fourcc, fps, frame_size, isColor=True)

while True:
    # Read a frame from the input video
    ret, frame = input_video.read()

    if not ret:
        # Break the loop if end of video
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (21, 21), 0)

    # Set the previous frame as the background for frame differencing
    if 'background' not in locals():
        background = blurred.copy()

    # Compute the absolute difference between the current frame and the background
    frame_diff = cv2.absdiff(background, blurred)

    # Threshold the frame difference to create a binary motion mask
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    # Amplify the motion by scaling the pixel intensities
    amplified_frame = cv2.addWeighted(frame, 1.5, cv2.merge([thresh, thresh, thresh]), -0.5, 0)

    # Write the amplified frame to the output video
    output_video.write(amplified_frame)

    # Display the input and output frames
    cv2.imshow('Input Video', frame)
    cv2.imshow('Output Video', amplified_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the input and output video objects
input_video.release()
output_video.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
