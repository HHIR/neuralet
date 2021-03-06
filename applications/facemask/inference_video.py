from configs.config_handler import Config
import cv2 as cv
import numpy as np
from argparse import ArgumentParser
import os


def main():
    """
    Read input video and process it, the output video will be exported output_video path
     which can be set by input arguments.
    Example: python inference_video.py --config configs/config.json --input_video_path data/video/sample.mov
     --output_video data/videos/output.avi
    """
    argparse = ArgumentParser()
    argparse.add_argument('--config', type=str, help='json config file path')
    argparse.add_argument('--input_video_path', type=str, help='the path of input video', default='')
    argparse.add_argument('--output_video', type=str, help='the name of output video file',
                          default='face_mask_output.avi')
    args = argparse.parse_args()

    config_path = args.config
    cfg = Config(path=config_path)

    if args.input_video_path == '':
        input_path = cfg.APP_VIDEO_PATH
    else:
        input_path = args.input_video_path

    print("INFO: Input video is: ", input_path)
    output_path = args.output_video
    file_name_size = len(output_path.split('/')[-1])
    output_dir = output_path[:-file_name_size]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("INFO: The output video will be exported at: ", output_path)

    detector_input_size = (cfg.DETECTOR_INPUT_SIZE[0], cfg.DETECTOR_INPUT_SIZE[1], 3)
    classifier_img_size = (cfg.CLASSIFIER_INPUT_SIZE, cfg.CLASSIFIER_INPUT_SIZE, 3)

    device = cfg.DEVICE
    detector = None
    classifier = None
    output_vidwriter = None

    if device == "x86":
        from libs.detectors.x86.detector import Detector
        from libs.classifiers.x86.classifier import Classifier

    elif device == "EdgeTPU":
        from libs.detectors.edgetpu.detector import Detector
        from libs.classifiers.edgetpu.classifier import Classifier
    elif device == "Jetson":
        from libs.detectors.jetson.detector import Detector
        from libs.classifiers.jetson.classifier import Classifier
    else:
        raise ValueError('Not supported device named: ', device)

    detector = Detector(cfg)
    classifier_model = Classifier(cfg)
    input_cap = cv.VideoCapture(input_path)

    print("INFO: Start inferencing")
    frame_id = 0
    while (input_cap.isOpened()):
        ret, raw_img = input_cap.read()
        if output_vidwriter is None:
            output_vidwriter = cv.VideoWriter(output_path, cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 24,
                                              (raw_img.shape[1], raw_img.shape[0]))
            height, width = raw_img.shape[:2]

        if ret == False:
            break
        _, cv_image = input_cap.read()
        if np.shape(cv_image) != ():
            resized_image = cv.resize(cv_image, tuple(detector_input_size[:2]))
            rgb_resized_image = cv.cvtColor(resized_image, cv.COLOR_BGR2RGB)
            objects_list = detector.inference(rgb_resized_image)
            faces = []
            cordinates = []
            cordinates_head = []
            for obj in objects_list:
                if 'bbox' in obj.keys():
                    face_bbox = obj['bbox']  # [ymin, xmin, ymax, xmax]
                    xmin, xmax = np.multiply([face_bbox[1], face_bbox[3]], width)
                    ymin, ymax = np.multiply([face_bbox[0], face_bbox[2]], height)
                    croped_face = cv_image[int(ymin):int(ymin) + (int(ymax) - int(ymin)),
                                  int(xmin):int(xmin) + (int(xmax) - int(xmin))]
                    # Resizing input image
                    croped_face = cv.resize(croped_face, tuple(classifier_img_size[:2]))
                    croped_face = cv.cvtColor(croped_face, cv.COLOR_BGR2RGB)
                    # Normalizing input image to [0.0-1.0]
                    croped_face = croped_face / 255.0
                    faces.append(croped_face)
                    cordinates.append([int(xmin), int(ymin), int(xmax), int(ymax)])
                if 'bbox_head' in obj.keys():
                    head_bbox = obj['bbox_head']  # [ymin, xmin, ymax, xmax]
                    xmin, xmax = np.multiply([head_bbox[1], head_bbox[3]], width)
                    ymin, ymax = np.multiply([head_bbox[0], head_bbox[2]], height)
                    cordinates_head.append([int(xmin), int(ymin), int(xmax), int(ymax)])

            faces = np.array(faces)
            face_mask_results, scores = classifier_model.inference(faces)
            for i, cor in enumerate(cordinates):
                if face_mask_results[i] == 1:
                    color = (0, 0, 255)
                elif face_mask_results[i] == 0:
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 0)

                cv.rectangle(raw_img, (cor[0], cor[1]), (cor[2], cor[3]), color, 2)

            for cor in cordinates_head:
                cv.rectangle(raw_img, (cor[0], cor[1]), (cor[2], cor[3]), (200,200,200), 2)
            output_vidwriter.write(raw_img)
            print('{} Frames number are processed. {} fps'.format(frame_id, detector.fps))
            frame_id = frame_id + 1
        else:
            continue

    input_cap.release()
    output_vidwriter.release()
    print('INFO: Finish:) Output video is exported at: ', output_path)


if __name__ == '__main__':
    main()
