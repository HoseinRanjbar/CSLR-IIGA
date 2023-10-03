import argparse
import cv2
import mediapipe as mp
import numpy as np
import os
import pickle
import progressbar
import json
import gzip

mp_holistic = mp.solutions.holistic


parser = argparse.ArgumentParser(description='Remove background of images')

parser.add_argument('--data_path', type=str, help='location of the data corpus')

parser.add_argument('--des_path', type=str)

args = parser.parse_args()

dataset_path = args.data_path
des_path = args.des_path

with mp_holistic.Holistic(
    static_image_mode=False,
    model_complexity=2,
    enable_segmentation=True,
    smooth_segmentation=False,
    refine_face_landmarks=False,
    min_detection_confidence=0.4,
    min_tracking_confidence=0.5) as holistic:

    bar = progressbar.ProgressBar(maxval=len(os.listdir(dataset_path)), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    cnt_bar = 0

    for video in os.listdir(dataset_path):

        cnt_bar += 1
        bar.update(cnt_bar)
        
        video_path = os.path.join(dataset_path,video,'1')

        for img_name in os.listdir(video_path):

  
            image = cv2.imread(os.path.join(video_path,img_name))
            image = cv2.resize(image , (224,224))
            results = holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            array=(results.segmentation_mask>0.5).astype(int)

            #array.flatten()

            if not os.path.exists(os.path.join(des_path,video)):
                os.makedirs(os.path.join(des_path,video))


            f = gzip.GzipFile(os.path.join(des_path,video,'{}.npy.gz'.format(img_name[:-4])), "wb")
            np.save(file=f, arr=array)
            f.close()