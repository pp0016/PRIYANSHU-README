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

async def submit_and_poll(submit_tool, status_tool, args, label, max_polls=20):
    print(f"\n[{label}] Submitting {submit_tool}...", flush=True)
    try:
        result = await call_tool(submit_tool, args)
        print(f"[{label}] Submit response: {result}", flush=True)
        data = json.loads(result)
        
        # Check if result came back directly (not async)
        if data.get("status") == "completed" or "jobId" not in data:
            print(f"\n{'='*80}", flush=True)
            print(f"RESULT: {label}", flush=True)
            print(f"{'='*80}", flush=True)
            print(result, flush=True)
            return data
        
        job_id = data["jobId"]
        print(f"[{label}] Got jobId: {job_id}", flush=True)
        
        # Poll
        for attempt in range(max_polls):
            await asyncio.sleep(10)
            print(f"[{label}] Poll {attempt+1}/{max_polls}...", flush=True)
            try:
                poll_result = await call_tool(status_tool, {"jobId": job_id})
                poll_data = json.loads(poll_result)
                status = poll_data.get("status", "unknown")
                print(f"[{label}] Status: {status}", flush=True)
                
                if status == "completed":
                    print(f"\n{'='*80}", flush=True)
                    print(f"RESULT: {label}", flush=True)
                    print(f"{'='*80}", flush=True)
                    print(poll_result, flush=True)
                    return poll_data
                elif status == "failed":
                    print(f"[{label}] FAILED: {poll_result}", flush=True)
                    return poll_data
            except Exception as e:
                print(f"[{label}] Poll error: {e}", flush=True)
        
        print(f"[{label}] Timed out after {max_polls} polls", flush=True)
        return None
    except Exception as e:
        print(f"[{label}] Submit error: {e}", flush=True)
        return None

async def main():
    channel_id = "UCqO9SfF4QKw94DvHMaXbP2A"
    
    # 1. Niche overview
    niche = await submit_and_poll(
        "get_niche_overview", "get_niche_overview_status",
        {"channelId": channel_id},
        "NICHE_OVERVIEW"
    )
    
    # 2. Similar channels
    similar = await submit_and_poll(
        "get_similar_channels", "get_similar_channels_status",
        {"channelId": channel_id},
        "SIMILAR_CHANNELS"
    )
    
    print("\n\nALL COMPLETE", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
