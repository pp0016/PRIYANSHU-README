import sys
import argparse

argv = sys.argv
if "--" in argv:
    argv = argv[argv.index("--") + 1:]
else:
    argv = []

parser = argparse.ArgumentParser(description="Test CLI Arg Parsing in Blender")
parser.add_argument("--start-frame", type=int, default=1)
parser.add_argument("--end-frame", type=int, default=60)
parser.add_argument("--text", type=str, default="Default Text")
parser.add_argument("--engine", type=str, default="CYCLES")

args = parser.parse_args(argv)
print("PARSED CLI ARGS SUCCESSFULLY:")
print(f"  start_frame: {args.start_frame}")
print(f"  end_frame: {args.end_frame}")
print(f"  text: {args.text}")
print(f"  engine: {args.engine}")
