

import os
import re
import ssl
from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube
LOCAL_DOWNLOAD_DIRECTORY='C:\\Users\\Kavya\\Pictures'
def design(request):
    return render(request, "app1/design-1.html")




def youtube(request):
    if request.method == 'POST':
        # Get the YouTube link and quality from the POST request
        link = request.POST.get('link')
        quality = request.POST.get('quality')

        # Check if the link is provided
        if not link:
            return HttpResponse('No link provided.', status=400)

        
        try:
            # Initialize YouTube object using pytube
            video = YouTube(link)

            # Get the stream based on the selected quality (360p, 720p, etc.)
            stream = video.streams.get_by_resolution(quality)

            # If the stream for the requested quality is unavailable, return an error
            if stream is None:
                return HttpResponse(f'No stream available for the selected quality: {quality}.', status=404)

            # Generate a unique filename for the video using the title
            download_filename = f"{video.title}.mp4"
            download_path = os.path.join(LOCAL_DOWNLOAD_DIRECTORY, download_filename)

            # Download the video only if it doesn't already exist
            if not os.path.exists(download_path):
                stream.download(output_path=LOCAL_DOWNLOAD_DIRECTORY, filename=download_filename)

            # Serve the file as a downloadable response
            if os.path.exists(download_path):
                with open(download_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="video/mp4")
                    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(download_path)}"'
                    return response

        except Exception as e:
            # Handle exceptions from pytube or file handling
            return HttpResponse(f'An error occurred: {e}', status=500)

    # Render the form page for GET requests
    return render(request, "app1/youtube.html")
