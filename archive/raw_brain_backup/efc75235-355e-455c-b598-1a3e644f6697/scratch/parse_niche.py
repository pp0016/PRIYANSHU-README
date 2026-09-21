import json

with open(r'C:\Users\renu5\.gemini\antigravity\brain\efc75235-355e-455c-b598-1a3e644f6697\scratch\niche_overview.json','r',encoding='utf-8-sig') as f:
    data = json.load(f)

print("="*80)
print("NICHE OVERVIEW - KEY DATA")
print("="*80)

# Top-level non-channel fields
print("\n--- TOP-LEVEL METADATA ---")
for k,v in data.items():
    if k not in ('channels',):
        if isinstance(v, (dict, list)):
            if len(str(v)) < 500:
                print(f"{k}: {json.dumps(v, indent=2)}")
            else:
                print(f"{k}: [large data - {len(v)} items]")
        else:
            print(f"{k}: {v}")

# Channel summaries
print("\n--- ALL NICHE CHANNELS (COMPETITORS) ---")
channels = data.get('channels', [])
print(f"Total channels found: {len(channels)}")
print()

for i, ch in enumerate(channels):
    name = ch.get('channelName', '?')
    subs = ch.get('subscriptionCount', ch.get('subscriberCount', '?'))
    ch_id = ch.get('channelId', '?')
    videos = ch.get('videos', [])
    
    # Calculate total views and avg VPH from sampled videos
    total_views = sum(int(v.get('viewCount', 0)) for v in videos)
    avg_vph = 0
    if videos:
        vphs = [v.get('vph', 0) for v in videos if v.get('vph')]
        avg_vph = sum(vphs)/len(vphs) if vphs else 0
    
    max_outlier = max((v.get('outlierScore', 0) for v in videos), default=0)
    
    # Top video
    top_video = max(videos, key=lambda v: int(v.get('viewCount', 0)), default={})
    top_title = top_video.get('title', 'N/A')
    top_views = top_video.get('viewCount', '0')
    
    print(f"[{i+1}] {name}")
    print(f"    Subs: {subs:,}" if isinstance(subs, int) else f"    Subs: {subs}")
    print(f"    Channel ID: {ch_id}")
    print(f"    Sampled Videos: {len(videos)} | Total Views (sampled): {total_views:,}")
    print(f"    Avg VPH: {avg_vph:.2f} | Max Outlier Score: {max_outlier:.2f}")
    print(f"    Top Video: '{top_title}' ({top_views} views)")
    print()
