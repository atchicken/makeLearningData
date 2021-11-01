import argparse
import csv
import cv2
import random

import numpy as np



def main():

    args = Parse()

    # 学習用
    makeData(args.trainSaveDir, args.trainNum, args.size)

    # 評価用
    makeData(args.evalSaveDir, args.evalNum, args.size)

    return




def makeData(imgDir, dataNum, size):

    
    for i_num in range(dataNum):
        
        img = np.zeros((size, size))
        corImg = np.zeros((size, size))
        
        x, y = random.randint(0, size - 8), random.randint(0, size - 8)
        cclSize = random.randint(3, 8)
        
        cv2.circle(img, (x, y), cclSize, 255, thickness=1)
        cv2.circle(corImg, (x, y), cclSize, 255, thickness=-1)
        
        inputPath = imgDir + "/inputs/" + str(i_num).zfill(4) + ".png"
        correctPath = imgDir + "/corrects/" + str(i_num).zfill(4) + ".png"
        cv2.imwrite(inputPath, img)
        cv2.imwrite(correctPath, corImg)
 
    return




def Parse():

    parser = argparse.ArgumentParser()
    parser.add_argument('-tn', '--trainNum', type=int, default=500)
    parser.add_argument('-en', '--evalNum', type=int, default=100)
    parser.add_argument('-ts', '--trainSaveDir', type=str, default="./data/train")
    parser.add_argument('-es', '--evalSaveDir', type=str, default="./data/test")
    parser.add_argument('-s', '--size', type=int, default=32)

    args = parser.parse_args()

    return args




if __name__ == "__main__":
    main()
