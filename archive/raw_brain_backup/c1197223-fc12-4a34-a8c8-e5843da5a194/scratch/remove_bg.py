import cv2
import numpy as np
import os

img_path = r"C:\Users\renu5\.gemini\antigravity\brain\c1197223-fc12-4a34-a8c8-e5843da5a194\.user_uploaded\media_1788285703286.png"
out_dir = r"C:\Users\renu5\.gemini\antigravity\brain\c1197223-fc12-4a34-a8c8-e5843da5a194\scratch"

# Read image with alpha channel
img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
if img.shape[2] == 3:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

# Convert to HSV to easily select the yellow/brown background
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# The character is white/gray with black outlines.
# The background is yellow/tan and brown stones.
# Let's create a mask for anything that is NOT white, gray, or black.
# White/Gray/Black have very low saturation.
# So we can mask out high saturation pixels (the yellow wall/brown floor).
# Lower bound for saturation
lower_sat = np.array([0, 30, 0])
upper_sat = np.array([180, 255, 255])
bg_mask = cv2.inRange(hsv, lower_sat, upper_sat)

# There might also be some low-saturation brownish floor parts.
# Let's also do a simple floodfill from the top-left corner to get the main wall.
h, w = img.shape[:2]
# Floodfill approach skipped in favor of thresholding.

# Simpler approach: 
# Stickman is mostly white (V > 200, S < 30) and black lines (V < 50).
# Let's just create a mask for the stickman.
stickman_mask = np.zeros((h, w), dtype=np.uint8)

# Condition for white-ish pixels (body fill)
white_cond = (hsv[:,:,1] < 40) & (hsv[:,:,2] > 200)
# Condition for black-ish pixels (lines)
black_cond = (hsv[:,:,2] < 100)

stickman_mask[white_cond | black_cond] = 255

# Clean up the mask using morphological operations
kernel = np.ones((3,3), np.uint8)
stickman_mask = cv2.morphologyEx(stickman_mask, cv2.MORPH_CLOSE, kernel)

# Apply mask to alpha channel
img[:,:,3] = stickman_mask

# Save the bored state
bored_path = os.path.join(out_dir, "stickman_bored.png")
cv2.imwrite(bored_path, img)

# --- Create Laughing State ---
laugh_img = img.copy()
# The mouth is a straight line. 
# Let's find the mouth. It's a horizontal black line in the middle of the head.
# Head is roughly from y=50 to y=200.
# Mouth is roughly around y=140 to 160, x=130 to 230.
# Let's just draw a big laughing mouth over that area!
# Draw a white filled rectangle to erase the old mouth.
cv2.rectangle(laugh_img, (130, 140), (230, 170), (255, 255, 255, 255), -1)

# Draw a laughing mouth (a wide 'D' shape)
# Arc
cv2.ellipse(laugh_img, (181, 145), (40, 20), 0, 0, 180, (0, 0, 0, 255), 4)
# Top line
cv2.line(laugh_img, (141, 145), (221, 145), (0, 0, 0, 255), 4)

laugh_path = os.path.join(out_dir, "stickman_laugh.png")
cv2.imwrite(laugh_path, laugh_img)

print("Saved", bored_path)
print("Saved", laugh_path)
