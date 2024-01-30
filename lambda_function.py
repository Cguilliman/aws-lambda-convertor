import boto3
import os
from io import BytesIO
from PIL import Image

# Initialize S3 client
s3 = boto3.client('s3')

def convert_image(image_data, image_format):
    image = Image.open(BytesIO(image_data))
    buffer = BytesIO()
    image.save(buffer, format=image_format)
    return buffer.getvalue()

def lambda_handler(event, context):
    # Get the bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Download the JPEG image from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    jpeg_data = response['Body'].read()
    
    # Convert to BMP
    bmp_data = convert_image(jpeg_data, 'BMP')
    bmp_key = os.path.splitext(key)[0] + '.bmp'
    
    # Convert to GIF
    gif_data = convert_image(jpeg_data, 'GIF')
    gif_key = os.path.splitext(key)[0] + '.gif'
    
    # Convert to PNG
    png_data = convert_image(jpeg_data, 'PNG')
    png_key = os.path.splitext(key)[0] + '.png'
    
    # Upload the converted images back to S3
    s3.put_object(Bucket=bucket, Key=bmp_key, Body=bmp_data)
    s3.put_object(Bucket=bucket, Key=gif_key, Body=gif_data)
    s3.put_object(Bucket=bucket, Key=png_key, Body=png_data)
    
    return {
        'statusCode': 200,
        'body': 'Images converted and saved successfully.'
    }
