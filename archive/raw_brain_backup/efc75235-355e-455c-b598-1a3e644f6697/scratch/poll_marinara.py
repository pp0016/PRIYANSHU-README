import asyncio, json, sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession

NEXLEV_MCP_URL = "https://prod.dashboard.nexlev.io/api/claude-mcp"

async def call_tool(tool_name, arguments):
    server_params = StdioServerParameters(command="npx.cmd", args=["-y", "mcp-remote", NEXLEV_MCP_URL])
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, arguments)
            texts = []
            for content in result.content:
                if hasattr(content, 'text'):
                    texts.append(content.text)
            return "\n".join(texts)

async def main():
    job_id = "cc1d8dc3-e110-4afc-a700-a7ccaec58f3d"
    for attempt in range(20):
        await asyncio.sleep(10)
        print(f"Poll {attempt+1}/20...", flush=True)
        try:
            result = await call_tool("get_niche_overview_status", {"jobId": job_id})
            data = json.loads(result)
            status = data.get("status", "unknown")
            print(f"Status: {status}", flush=True)
            if status == "completed":
                # Save to file
                with open(r'C:\Users\renu5\.gemini\antigravity\brain\efc75235-355e-455c-b598-1a3e644f6697\scratch\marinara_niche.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
                print("SAVED to marinara_niche.json", flush=True)
                
                # Print summary
                sc = data.get('similarChannels', [])
                vids = data.get('videos', [])
                print(f"\nSimilar channels: {len(sc)}")
                for i, ch in enumerate(sc[:5]):
                    print(f"  [{i+1}] {ch.get('channelName','?')} | Similarity: {ch.get('similarityScore',0)}")
                print(f"\nVideo entries: {len(vids)}")
                for entry in vids[:5]:
                    name = entry.get('channelName','?')
                    subs = entry.get('subscriptionCount','?')
                    v = entry.get('videos',[])
                    print(f"  {name} | Subs: {subs} | Videos: {len(v)}")
                return
            elif status == "failed":
                print(f"FAILED: {result}", flush=True)
                return
        except Exception as e:
            print(f"Error: {e}", flush=True)
    print("Timed out", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
