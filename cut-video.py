import argparse
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def cut_video(rute, start_time, end_time, final_rute):
	ffmpeg_extract_subclip(rute, start_time, end_time, targetname=final_rute)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description="Cut a section of the selected video from START to END")
	parser.add_argument(
		"rute", help="The rute/name of the video file", type=str)
	parser.add_argument(
		"start", help="The start time to cut in seconds", type=float)
	parser.add_argument(
		"end", help="The start time to cut in seconds", type=float)
	parser.add_argument(
		"--name", help="name or rute of the final cutted video", type=str, default="test.mp4")
	args = parser.parse_args()

	cut_video(args.rute, args.start, args.end, args.name)
