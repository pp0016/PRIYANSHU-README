import json

with open(r'C:\Users\renu5\.gemini\antigravity\brain\efc75235-355e-455c-b598-1a3e644f6697\scratch\niche_overview.json','r',encoding='utf-8-sig') as f:
    data = json.load(f)

sc = data.get('similarChannels', [])
print('=== SIMILAR CHANNELS (sorted by similarity) ===')
for i, ch in enumerate(sc):
    score = ch.get('similarityScore', 0)
    name = ch.get('channelName', '?')
    ch_id = ch.get('channelId', '?')
    print(f'  [{i+1}] {name} | Similarity: {score:.4f} | ID: {ch_id}')

vids = data.get('videos', [])
print(f'\n=== NICHE VIDEOS DATA ({len(vids)} channel entries) ===')
for entry in vids:
    ch_name = entry.get('channelName', '?')
    ch_id = entry.get('channelId', '?')
    subs = entry.get('subscriptionCount', '?')
    ch_vids = entry.get('videos', [])
    total_views = sum(int(v.get('viewCount', 0)) for v in ch_vids)
    
    vphs = [v.get('vph', 0) for v in ch_vids if v.get('vph')]
    avg_vph = sum(vphs)/len(vphs) if vphs else 0
    
    top_video = max(ch_vids, key=lambda v: int(v.get('viewCount', 0)), default={})
    top_title = top_video.get('title', 'N/A')[:60]
    top_views = top_video.get('viewCount', '0')
    
    print(f'\n  {ch_name}')
    print(f'    Subs: {subs} | Channel ID: {ch_id}')
    print(f'    Sampled Videos: {len(ch_vids)} | Total Views (sampled): {total_views:,}')
    print(f'    Avg VPH: {avg_vph:.2f}')
    print(f'    Top: "{top_title}" ({top_views} views)')
