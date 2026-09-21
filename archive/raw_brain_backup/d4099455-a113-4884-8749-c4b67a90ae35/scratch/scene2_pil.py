import os
import math
from PIL import Image, ImageDraw, ImageFont

def ease_in_out(t):
    return t * t * (3.0 - 2.0 * t)

def create_scene2(output_dir="scene2_frames", start_frame=270, end_frame=539):
    os.makedirs(output_dir, exist_ok=True)
    width, height = 1080, 1920
    
    # Try to load a standard font
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 100)
        font_subtitle = ImageFont.truetype("arial.ttf", 60)
    except:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        
    bg_color = (20, 20, 30)
    color_20 = (255, 204, 0)     # Golden yellow for the vital 20% effort
    color_80 = (100, 100, 120)   # Grey for the trivial 80% effort
    color_res_80 = (0, 204, 102) # Green for 80% results
    color_res_20 = (80, 120, 80) # Dull green for 20% results
    
    # Initial grid of efforts
    start_x = width // 2 - 300
    start_y = height // 2 - 400
    spacing_x = 150
    spacing_y = 150
    
    for f in range(start_frame, end_frame + 1):
        t = f - start_frame
        img = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(img)
        
        # 1. Title
        title_text = "The 80/20 Rule"
        if font_title != ImageFont.load_default():
            bbox = draw.textbbox((0, 0), title_text, font=font_title)
            tw = bbox[2] - bbox[0]
        else:
            tw = 100
        draw.text(((width - tw) // 2, 150), title_text, font=font_title, fill=(255, 255, 255))
        
        # Progress calculations for different phases
        p1_prog = min(max(t / 30.0, 0), 1)             # 0-30: Fade in efforts (10 blocks)
        p2_prog = min(max((t - 40) / 30.0, 0), 1)      # 40-70: Highlight 20% (2 blocks turn yellow)
        p3_prog = min(max((t - 80) / 40.0, 0), 1)      # 80-120: Split 20% to left and 80% to right
        p3_e = ease_in_out(p3_prog)
        p4_prog = min(max((t - 130) / 60.0, 0), 1)     # 130-190: Grow results bars
        p4_e = ease_in_out(p4_prog)
        
        # Draw 10 effort boxes
        for i in range(10):
            row = i // 5
            col = i % 5
            
            # Initial grid position
            ix = start_x + col * spacing_x
            iy = start_y + row * spacing_y
            
            is_vital = (i < 2)
            if is_vital:
                # Target for 20% effort (Left side)
                tx = width // 4 - 60
                ty = height // 3 + (i * 90) - 50
                # Color transition to golden yellow
                r = int(color_80[0] + (color_20[0] - color_80[0]) * p2_prog)
                g = int(color_80[1] + (color_20[1] - color_80[1]) * p2_prog)
                b = int(color_80[2] + (color_20[2] - color_80[2]) * p2_prog)
                color = (r, g, b)
            else:
                # Target for 80% effort (Right side)
                tx = 3 * width // 4 - 60
                ty = height // 3 + ((i - 2) * 90) - 150
                color = color_80
                
            # Interpolate position
            cx = ix + (tx - ix) * p3_e
            cy = iy + (ty - iy) * p3_e
            
            size = 80 * p1_prog
            if size > 0:
                draw.rectangle([cx, cy, cx + size, cy + size], fill=color, outline=(255,255,255), width=3)
                
        # Draw labels for efforts once split
        if p3_prog > 0.8:
            if font_subtitle != ImageFont.load_default():
                bbox1 = draw.textbbox((0, 0), "20% Effort", font=font_subtitle)
                w1 = bbox1[2] - bbox1[0]
                bbox2 = draw.textbbox((0, 0), "80% Effort", font=font_subtitle)
                w2 = bbox2[2] - bbox2[0]
            else:
                w1, w2 = 100, 100
                
            draw.text((width // 4 - w1 // 2, height // 3 - 130), "20% Effort", font=font_subtitle, fill=color_20)
            draw.text((3 * width // 4 - w2 // 2, height // 3 - 230), "80% Effort", font=font_subtitle, fill=color_80)
                
        # Draw Result Bars
        if p4_prog > 0:
            bar_w = 180
            
            # 80% Results Bar (from 20% effort)
            max_h_vital = 600
            cur_h_vital = max_h_vital * p4_e
            bx1 = width // 4 - bar_w // 2
            by1 = height - 250
            draw.rectangle([bx1, by1 - cur_h_vital, bx1 + bar_w, by1], fill=color_res_80)
            
            # 20% Results Bar (from 80% effort)
            max_h_triv = 150
            cur_h_triv = max_h_triv * p4_e
            bx2 = 3 * width // 4 - bar_w // 2
            by2 = height - 250
            draw.rectangle([bx2, by2 - cur_h_triv, bx2 + bar_w, by2], fill=color_res_20)
            
            # Results Text
            if p4_prog > 0.8:
                if font_subtitle != ImageFont.load_default():
                    bbox_r1 = draw.textbbox((0, 0), "80% Results", font=font_subtitle)
                    wr1 = bbox_r1[2] - bbox_r1[0]
                    bbox_r2 = draw.textbbox((0, 0), "20% Results", font=font_subtitle)
                    wr2 = bbox_r2[2] - bbox_r2[0]
                else:
                    wr1, wr2 = 100, 100
                    
                draw.text((bx1 + bar_w // 2 - wr1 // 2, by1 + 30), "80% Results", font=font_subtitle, fill=(255, 255, 255))
                draw.text((bx2 + bar_w // 2 - wr2 // 2, by2 + 30), "20% Results", font=font_subtitle, fill=(180, 180, 180))
        
        img.save(os.path.join(output_dir, f"frame_{f:04d}.png"))
        
if __name__ == "__main__":
    create_scene2(start_frame=270, end_frame=539)
