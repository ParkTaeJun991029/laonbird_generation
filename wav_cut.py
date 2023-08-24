from pydub import AudioSegment
import os
import os.path as osp
from os.path import join as ospj
import argparse

def split_and_save(input_file, output_folder, segment_length):
    # Load the input file
    audio = AudioSegment.from_file(input_file)

    # Convert to WAV format
    audio = audio.set_channels(1)  # Convert to mono
    audio = audio.set_frame_rate(44100)  # Set frame rate to 44.1 kHz

    # Segment length in milliseconds
    segment_length_ms = segment_length * 1000

    # Split the audio into segments and save as WAV
    for i, start_time in enumerate(range(0, len(audio), segment_length_ms)):
        segment = audio[start_time:start_time + segment_length_ms]
        name = osp.splitext(osp.basename(input_file))[0]

        output_file = ospj(output_folder, f"ss_{name}_{i + 1}.wav")
        segment.export(output_file, format="wav")

def process_folder(input_folder, output_folder, segment_length):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):  # Assuming all input files are in WAV format
            input_file = ospj(input_folder, filename)
            split_and_save(input_file, output_folder, segment_length)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split audio files in a folder into segments.")
    parser.add_argument("--input_folder", required=True, help="Path to the input audio folder path")
    parser.add_argument("--output_folder", required=True, help="Path to the output folder for segments")
    parser.add_argument("--segment_length", type=int, default=15, help="Segment length in seconds")

    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder
    segment_length = args.segment_length

    process_folder(input_folder, output_folder, segment_length)
    print("Splitting and conversion completed.")
