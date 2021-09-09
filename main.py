import os
import sys
import boto3
import logging
from botocore.exceptions import ClientError
from os.path import isfile, join
from Helpers import csv_helper as ch

# ACCESS_KEY = sys.argv[1]
# SECRET_KEY = sys.argv[2]
#
# def upload_to_awsS3(file_name, bucket, object_name=None):
#     """Upload a file to an S3 bucket
#
#     :param file_name: File to upload
#     :param bucket: Bucket to upload to
#     :param object_name: S3 object name. If not specified then file_name is used
#     :return: True if file was uploaded, else False
#     """
#
#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = os.path.basename(file_name)
#
#     # Upload the file
#     s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
#     try:
#         response = s3.upload_file(file_name, bucket, object_name)
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True

# Creating temporary folders
if not os.path.exists("Output/Temp"):
    os.mkdir("Output/Temp")
if not os.path.exists("Resources/Temp"):
    os.mkdir("Resources/Temp")

# Unzip the basic data
# bigdata_zip = zipfile.ZipFile("Resources/BigData_raw.zip")
# bigdata_zip.extractall("Resources/Temp")
# bigdata_zip.close()

# Divide the data into segments of 20,000 units
full_paths = []
directories = os.listdir(r"Resources/Temp")
for directory in os.listdir(r"Resources/Temp"):
    full_paths = full_paths + [("Resources/Temp/" + directory + "/" + f) for f in os.listdir("Resources/Temp/" + directory) if isfile(join("Resources/Temp/" + directory, f))]
for full_path in full_paths:
    ch.bigdata_segmentation_csv(full_path, full_path.split('/')[3][16:-15], full_path.split('/')[3][5:-15])

# Delete the temporary folder with the main data
# shutil.rmtree("Resources/Temp")

# Archiving the processed data
# shutil.make_archive("Output/Archives/BigData", 'zip', "Output/Temp")

# Delete the temporary folder with the processed data
# shutil.rmtree("Output/Temp")

# Upload the resulting archive to AWS S3
# uploaded = upload_to_awsS3("Output/Archives/BigData.zip", 'bigdata-to-s3')

# Delete the resulting archive
# os.remove("Output/Archives/BigData.zip")