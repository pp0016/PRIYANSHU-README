import os
from PIL import Image, ImageDraw, ImageFont
import math

def create_scene_4(output_dir="scene4_frames", start_frame=810, end_frame=1079):
    os.makedirs(output_dir, exist_ok=True)
    
    width, height = 1080, 1920
    
    try:
        # Attempt to load a default Windows font
        font_large = ImageFont.truetype("arial.ttf", 120)
        font_medium = ImageFont.truetype("arial.ttf", 80)
    except IOError:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()

    total_frames = end_frame - start_frame + 1
    
    for i, frame_num in enumerate(range(start_frame, end_frame + 1)):
        # Use RGBA for transparency support
        img = Image.new('RGBA', (width, height), color=(20, 20, 30, 255))
        draw = ImageDraw.Draw(img)
        
        progress = i / total_frames
        
        # Draw background elements (animated circles)
        bg_circle_radius = 500 + math.sin(progress * math.pi * 2) * 50
        draw.ellipse([width/2 - bg_circle_radius, height/2 - bg_circle_radius, 
                      width/2 + bg_circle_radius, height/2 + bg_circle_radius], 
                     fill=(30, 30, 45, 255))
        
        # Text Logic
        if progress < 0.33:
            # Phase 1: Work Smarter
            alpha = int(min(1.0, progress / 0.1) * 255)
            y_pos = height/2 - 100 - (1 - min(1.0, progress/0.1)) * 50
            text = "WORK SMARTER"
            text_bbox = draw.textbbox((0, 0), text, font=font_large)
            draw.text(((width - (text_bbox[2] - text_bbox[0]))/2, y_pos), 
                      text, font=font_large, fill=(255, 200, 50, alpha))
                      
        elif progress < 0.66:
            # Phase 2: Not Harder
            alpha = int(min(1.0, (progress - 0.33) / 0.1) * 255)
            y_pos = height/2 - 100
            text1 = "WORK SMARTER,"
            text_bbox1 = draw.textbbox((0, 0), text1, font=font_large)
            draw.text(((width - (text_bbox1[2] - text_bbox1[0]))/2, y_pos - 100), 
                      text1, font=font_large, fill=(255, 200, 50, 255))
                      
            text2 = "NOT HARDER"
            text_bbox2 = draw.textbbox((0, 0), text2, font=font_large)
            draw.text(((width - (text_bbox2[2] - text_bbox2[0]))/2, y_pos + 50), 
                      text2, font=font_large, fill=(255, 100, 100, alpha))
                      
        else:
            # Phase 3: Final CTA
            alpha = int(min(1.0, (progress - 0.66) / 0.1) * 255)
            y_pos = height/2 - 150
            
            text1 = "Apply the 80/20 Rule"
            text_bbox1 = draw.textbbox((0, 0), text1, font=font_medium)
            draw.text(((width - (text_bbox1[2] - text_bbox1[0]))/2, y_pos), 
                      text1, font=font_medium, fill=(255, 255, 255, alpha))
                      
            text2 = "TODAY!"
            text_bbox2 = draw.textbbox((0, 0), text2, font=font_large)
            # Bounce effect
            bounce = abs(math.sin((progress - 0.66) * math.pi * 5)) * 30
            draw.text(((width - (text_bbox2[2] - text_bbox2[0]))/2, y_pos + 120 - bounce), 
                      text2, font=font_large, fill=(50, 255, 100, alpha))
        
        # Progress bar at the bottom
        bar_width = width * 0.8
        bar_height = 15
        bar_x = (width - bar_width) / 2
        bar_y = height - 150
        
        draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], fill=(50, 50, 50, 255))
        draw.rectangle([bar_x, bar_y, bar_x + bar_width * progress, bar_y + bar_height], fill=(0, 255, 150, 255))
        
        # Convert back to RGB if necessary, or just save RGBA as PNG
        img.save(os.path.join(output_dir, f"frame_{frame_num:04d}.png"))
        
        if i % 50 == 0:
            print(f"Generated frame {frame_num} / {end_frame}")
            
    print("Scene 4 rendering complete.")

if __name__ == '__main__':
    create_scene_4()
