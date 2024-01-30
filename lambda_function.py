import os
from io import BytesIO
from PIL import Image

def lambda_handler(event, context):
    # Get the image data from the event
    image_data = event['image_data']
    
    # Open the image using PIL
    image = Image.open(BytesIO(image_data))
    
    # Convert to BMP
    bmp_buffer = BytesIO()
    image.save(bmp_buffer, format='BMP')
    bmp_data = bmp_buffer.getvalue()
    
    # Convert to GIF
    gif_buffer = BytesIO()
    image.save(gif_buffer, format='GIF')
    gif_data = gif_buffer.getvalue()
    
    # Convert to PNG
    png_buffer = BytesIO()
    image.save(png_buffer, format='PNG')
    png_data = png_buffer.getvalue()
    
    # You can now do something with the converted images
    # For example, save them to S3
    
    return {
        'bmp_data': bmp_data,
        'gif_data': gif_data,
        'png_data': png_data
    }