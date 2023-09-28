#!/bin/bash

VIDEOS_PATH="./videos/"
METADATA_PATH="./metadata.csv"
H5_PATH="./how2100m_tsp_features.h5"

# Generate metadata
python generate_metadata_csv.py --video-folder $VIDEOS_PATH --output-csv $METADATA_PATH


RELEASED_CHECKPOINT=r2plus1d_34-tsp_on_activitynet # choose one of the models above
STRIDE=16
SHARD_ID=0
NUM_SHARDS=1
DEVICE=cuda:0
OUTPUT_DIR=./pkl/${RELEASED_CHECKPOINT}_features/stride_${STRIDE}/

mkdir -p $OUTPUT_DIR

python extract_features.py \
--data-path $DATA_PATH \
--metadata-csv-filename $METADATA_CSV_FILENAME \
--released-checkpoint $RELEASED_CHECKPOINT \
--stride $STRIDE \
--shard-id $SHARD_ID \
--num-shards $NUM_SHARDS \
--device $DEVICE \
--output-dir $OUTPUT_DIR

python merge_pkl_files_into_one_h5_feature_file.py --features-folder $OUTPUT_DIR --output-h5 $H5_PATH
