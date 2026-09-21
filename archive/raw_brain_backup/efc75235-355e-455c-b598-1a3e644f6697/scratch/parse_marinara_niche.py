import json

with open(r'C:\Users\renu5\.gemini\antigravity\brain\efc75235-355e-455c-b598-1a3e644f6697\scratch\marinara_niche.json','r',encoding='utf-8') as f:
    data = json.load(f)

sc = data.get('similarChannels', [])
vids = data.get('videos', [])

print('=== SIMILAR CHANNELS ===')
for i, ch in enumerate(sc):
    print(f"  [{i+1}] {ch.get('channelName','?')} | Similarity: {ch.get('similarityScore',0)} | ID: {ch.get('channelId','?')}")

print(f'\n=== COMPETITOR DETAILS ({len(vids)} channels) ===')
for entry in vids:
    name = entry.get('channelName','?')
    subs = entry.get('subscriptionCount','?')
    ch_id = entry.get('channelId','?')
    ch_vids = entry.get('videos', [])
    total_views = sum(int(v.get('viewCount', 0)) for v in ch_vids)
    vphs = [v.get('vph', 0) for v in ch_vids if v.get('vph')]
    avg_vph = sum(vphs)/len(vphs) if vphs else 0
    top_video = max(ch_vids, key=lambda v: int(v.get('viewCount', 0)), default={})
    top_title = top_video.get('title', 'N/A')[:70]
    top_views = top_video.get('viewCount', '0')

    print(f'\n  {name}')
    print(f'    Subs: {subs:,}' if isinstance(subs, int) else f'    Subs: {subs}')
    print(f'    ID: {ch_id}')
    print(f'    Videos sampled: {len(ch_vids)} | Total views (sampled): {total_views:,}')
    print(f'    Avg VPH: {avg_vph:.2f}')
    print(f'    Top: "{top_title}" ({top_views} views)')

print(f'\ntotalChannels: {data.get("totalChannels")}')
print(f'totalVideos: {data.get("totalVideos")}')
