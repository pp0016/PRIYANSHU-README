import os
import math
from PIL import Image, ImageDraw, ImageFont

def render_frame(frame_num, width=1080, height=1920):
    """
    Renders a single frame for Scene 3 (Frames 540 to 809).
    Total duration: 270 frames (9 seconds at 30 fps).
    """
    # Normalize time t from 0.0 to 1.0 within this scene
    start_frame = 540
    end_frame = 809
    total_frames = end_frame - start_frame + 1
    t = (frame_num - start_frame) / float(total_frames)
    
    img = Image.new('RGB', (width, height), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)
    
    # Font setup
    try:
        font_title = ImageFont.truetype("arial.ttf", 70)
        font_text = ImageFont.truetype("arial.ttf", 50)
    except IOError:
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()
        
    # Draw Title
    title = "The 80/20 Rule in Action"
    try:
        bbox = draw.textbbox((0, 0), title, font=font_title)
        tw = bbox[2] - bbox[0]
    except AttributeError:
        tw = draw.textlength(title, font=font_title)
    draw.text(((width - tw)/2, 200), title, font=font_title, fill=(255, 255, 255))
    
    # Section 1: Effort (10 dots representing 100% effort, 2 highlighted representing 20%)
    effort_y = 450
    item_radius = 25
    spacing = 70
    total_w = 10 * spacing
    start_x = (width - total_w) / 2 + spacing / 2
    
    for i in range(10):
        x = start_x + i * spacing
        # First 2 are the "20% effort" (highlighted)
        color = (255, 80, 80) if i < 2 else (80, 80, 80)
        
        # Pop-in animation for dots
        anim_start = i * 0.02
        if t > anim_start:
            scale = min(1.0, (t - anim_start) * 10)
            # Bounce effect
            if scale < 1.0:
                scale += math.sin(scale * math.pi) * 0.2
            r = item_radius * scale
            draw.ellipse((x - r, effort_y - r, x + r, effort_y + r), fill=color)
            
    # Text for effort
    eff_txt = "20% Effort"
    if t > 0.2:
        try:
            bbox = draw.textbbox((0, 0), eff_txt, font=font_text)
            tw = bbox[2] - bbox[0]
        except AttributeError:
            tw = draw.textlength(eff_txt, font=font_text)
        draw.text(((width - tw)/2, 530), eff_txt, font=font_text, fill=(255, 80, 80))
    
    # Section 2: Results Visualization (Bar Chart)
    # The 2 highlighted efforts produce a massive 80% results bar.
    if t > 0.3:
        # Animate bars growing
        t_res = min(1.0, (t - 0.3) * 3.0) # Finishes growing by t=0.63
        t_res = 1.0 - (1.0 - t_res) ** 3 # Cubic ease-out
        
        # 80% results block (Huge)
        res_80_max_height = 500
        res_80_height = res_80_max_height * t_res
        res_80_x = width / 2 - 220
        res_80_y = 1300 - res_80_height
        draw.rectangle([res_80_x, res_80_y, res_80_x + 180, 1300], fill=(255, 80, 80))
        
        # 20% results block (Small)
        res_20_max_height = 125
        res_20_height = res_20_max_height * t_res
        res_20_x = width / 2 + 40
        res_20_y = 1300 - res_20_height
        draw.rectangle([res_20_x, res_20_y, res_20_x + 180, 1300], fill=(80, 80, 80))
        
        # Text for results
        if t > 0.4:
            res_txt = "80% Results"
            draw.text((res_80_x, res_80_y - 70), res_txt, font=font_text, fill=(255, 80, 80))
            
            res2_txt = "20% Results"
            draw.text((res_20_x, res_20_y - 70), res2_txt, font=font_text, fill=(80, 80, 80))

    # Connection line / arrow from 20% Effort to 80% Results
    if t > 0.6:
        arrow_alpha = int(min(1.0, (t - 0.6) * 5) * 255)
        # Using a polygon for an arrow
        arrow_color = (255, 255, 255, arrow_alpha)
        # We need an RGBA overlay for transparency
        overlay = Image.new('RGBA', img.size, (0,0,0,0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        # Simple downward arrow
        ax = width / 2 - 130
        ay1 = 650
        ay2 = 750
        overlay_draw.line((ax, ay1, ax, ay2), fill=arrow_color, width=8)
        overlay_draw.polygon([(ax - 20, ay2 - 20), (ax + 20, ay2 - 20), (ax, ay2 + 10)], fill=arrow_color)
        
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

    return img

def generate_scene():
    out_dir = "scene3_frames"
    os.makedirs(out_dir, exist_ok=True)
    
    start_frame = 540
    end_frame = 809
    
    print(f"Generating frames {start_frame} to {end_frame}...")
    for f in range(start_frame, end_frame + 1):
        img = render_frame(f)
        img.save(os.path.join(out_dir, f"frame_{f:04d}.png"))
        if (f - start_frame) % 20 == 0:
            print(f"Rendered frame {f}")
            
    print("Scene 3 rendering complete!")

if __name__ == "__main__":
    generate_scene()
