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

async def poll_job(status_tool, job_id, label, max_attempts=15):
    for attempt in range(max_attempts):
        print(f"[{label}] Poll {attempt+1}/{max_attempts}...", file=sys.stderr)
        try:
            result = await call_tool(status_tool, {"jobId": job_id})
            data = json.loads(result)
            status = data.get("status", "unknown")
            print(f"[{label}] Status: {status}", file=sys.stderr)
            if status == "completed":
                print(f"\n{'='*80}\nRESULT: {label}\n{'='*80}")
                print(result)
                return data
            elif status == "failed":
                print(f"[{label}] FAILED", file=sys.stderr)
                print(f"\n{'='*80}\nFAILED: {label}\n{'='*80}")
                print(result)
                return data
            else:
                await asyncio.sleep(8)
        except Exception as e:
            print(f"[{label}] Error: {e}", file=sys.stderr)
            await asyncio.sleep(5)
    print(f"[{label}] Timed out", file=sys.stderr)
    return None

async def main():
    niche = await poll_job("get_niche_overview_status", "5cf39cd7-c332-4e84-a2ff-a7e2227381d6", "NICHE_OVERVIEW")
    similar = await poll_job("get_similar_channels_status", "401e392e-ffa0-49fe-8553-d8fb36c64663", "SIMILAR_CHANNELS")
    print("\nALL DONE", file=sys.stderr)

if __name__ == "__main__":
    asyncio.run(main())
