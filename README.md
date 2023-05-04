# Vimoa
Vimoa, short for video motion amplification is a program that uses frame differencing to detect motion and then amplifies the motion in the output video by scaling the pixel intensities.
It is inspired from Video magnification program developed by MIT you can visit their site http://people.csail.mit.edu/mrub/vidmag/ to know more about it.
this programm is created by pratyush ganguly (pratyushganguly@hotmail.com) with the help of chatGPT.
Any improvements and suggestions are most welcome

How to use this tool :
1. Download Zip file, Extract, and open this as a new folder in VScode (other text editors may also work)
2. Click on Vimoa.py from explorer, You will see the code, Run that code, you can see the sample videos side by side.
3. To amplify your own Videos, Rename any video you want to amplify to "input_video.mp4" (should be an mp4 video) and replace it with the sample video
    (input_video.mp4) in the Vimoa folder. dont change anything else
4. Run the code as usual, your video along with amplified version will play.(a copy of your amplified video wil be saved as "output_video.avi") in the folder.

Note that this program will require OpenCV.
