

import os
import re
import ssl
from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube
from urllib.error import HTTPError 
LOCAL_DOWNLOAD_DIRECTORY='C:\\Users\\Kavya\\Pictures'
def design(request):
    return render(request, "app1/design-1.html")

# importing all the required modules 
from django.shortcuts import render, redirect 
from pytube import *
YOUTUBE_REGEX = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=)?(\S+)'

import yt_dlp

# defining function 

def youtube_page(request):
    return render(request, 'app1/youtube.html')

def youtube(request): 
    ydl_opts = {
    'format': 'best',
    'outtmpl': 'C:\\Users\\Kavya\\Pictures\\%(title)s.%(ext)s',  # Specify your download path
    }

    link = 'https://youtu.be/CH50zuS8DD0?si=_FveBOE6o8oD68Ri'  # Your video link here
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
     ydl.download([link])

    return redirect('youtube_page')
def facebook_page(request):
    return render(request, 'app1/facebook.html')

def facebook(request):
    if request.method == 'POST':

        # Get the YouTube link and quality from the POST request
            video_url= request.POST.get('url')
           

    
   # Define the directory where you want to save the video
    save_directory = 'C:/Users/Kavya/Downloads/'  # Change this path as needed

    # Ensure the directory exists
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Define download options
    ydl_opts = {
        'format': 'best',  # Choose best quality
        'outtmpl': os.path.join(save_directory, 'video.mp4'),  # Save the video to the desired directory
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

   
    return redirect('facebook_page')
