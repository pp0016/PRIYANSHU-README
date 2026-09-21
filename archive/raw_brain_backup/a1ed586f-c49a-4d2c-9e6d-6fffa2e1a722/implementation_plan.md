# Cloud-Based Avatar Video Generation Pipeline

Since local rendering on a laptop CPU would be too slow, we are pivoting to a cloud-based pipeline. We will use the **Super Video Maker** skill to automate the entire process remotely. 

## Proposed Changes

We will use my built-in video making tools to perform the following steps:

### 1. Script & Planning
- I will automatically generate a compelling 15-second faceless channel script.
- I will design a storyboard and assign visual jobs (like Proof, Mechanism, Action) to each beat of the script.

### 2. Avatar Generation
- We will use the concept digital avatar image I generated earlier.
- I will process it through the `super-video-maker` pipeline to ensure it matches the strict hyperrealistic requirements.

### 3. Voice & Video Rendering
- We will send the script and the avatar image to a cloud rendering service (like HeyGen and ElevenLabs) to synthesize the voice and animate the lip-syncing perfectly.
- We will export the final `.mp4` video.

## User Review Required

> [!WARNING]
> **API Keys are Strictly Required**
> While platforms like Groq are completely free, they only process text (like ChatGPT), not video. Platforms that render high-quality video (like HeyGen, Seedance, or Runway) cost an immense amount of server power and **do not** offer completely free, keyless API access that I can use automatically. 
>
> The `super-video-maker` skill you asked me to use is hardcoded to fail unless it detects the following API keys in your environment:
> - `HEYGEN_API_KEY`
> - `OPENAI_API_KEY`
> - `ELEVENLABS_API_KEY`
> - `FALAI_API_KEY`

## Open Questions
1. **Can you generate free-tier API keys for HeyGen, OpenAI, and ElevenLabs?** (They all offer free trials/credits upon sign-up, which is enough to render this video. Once you paste the keys here, I can immediately trigger the pipeline).
2. If you cannot provide API keys, would you like me to just generate the script and the audio file locally (using your CPU, which only takes a few minutes for audio), and leave the video rendering part out?
