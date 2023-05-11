from .RenderMetadata import RenderMetadata
import os

def render_video(data:RenderMetadata):
    command = f"ffmpeg -f image2 -r 29.97 -i {data.input_image_format} -c:v libx265 -pix_fmt yuv420p10le -x265-params colorprim=bt709 -b:v 50000k -maxrate 50000k -bufsize 100000k -pass 1 -crf 0 -b:a 192k -acodec aac {data.output_video_format}"
    print(f"COMMAND : {command}")
    return os.system(command)