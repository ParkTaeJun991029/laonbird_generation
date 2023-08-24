#!/bin/bash
source activate tj_rvc



read -p "Enter the path to the input audio path:  " input_folder
read -p "Enter the path to the output folder:  " output_folder
read -p "Enter the path to the segement_length:  " segment_length 
python wav_cut.py --input_folder "$input_folder" --output_folder "$output_folder" --segment_length "$segment_length"

conda deactivate

