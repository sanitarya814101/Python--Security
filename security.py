import dropbox
import time
import random
import cv2

start_time = time.time()


def take_snapshot():
    number = random.randint(0, 100)

    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = 'img'+str(number) + '.png'
        cv2.imwrite(img_name, frame)

        startTime = time.time()
        result = False

    return(img_name)
    print('Snapshot taken...')
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "sl.A3YfvljFidU1zccrCgxrmmRZWTox-BA2ZkrTNjLT0dteyPW6HpUMq1ThPusimARtLBafh9brztQJwqVS06oU-1HkHyb-FwsaBRKraJVSWf-zk4fA9ATBGXHN_C2UUDcZFz0ft7I"
    file = img_name
    file_from = file
    file_to = '/New_From' + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.filesupload(f.read(), file_to,
                        mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded....")


def main():
    while(True):
        if((time.time() - start_time) >= 300):
            name = take_snapshot()
            upload_file(name)


main()
