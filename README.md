A little yolov11 project to detect and distinct the 12 different ores in the game planet crafter<br>
(The purpose of this project was to get myself familiar with yolov11)

The entire project was divided in 3 parts:
1. Gathering training data<br>
   -using the screenshots.py file I took many screenshots of the game while playing for some time
   
3. Labelling the data & training<br>
   -Using makesense.ai I labelled the ~120 images I then used for the training of detecting the 12 different ores in the game<br>
   -120 is a very small number, usually you would take atleast 5-10x that, however it worked suprisingly well<br>
   -Sometimes there are false positives or it fails to detect an ore it should detect which is due to the small sample size
   -<a href="https://huggingface.co/minogo/yolov11-planetcrafter-ore-detector/resolve/main/detector.pt">Download Model</a>
   
5. Realtime detection<br>
   -using the prediction.py file I let the model run while playing

A few output images:
<img src="https://i.imgur.com/qXaRqq4.jpeg">

<img src="https://i.imgur.com/CM7KvXr.jpeg">

<img src="https://i.imgur.com/kf74dfJ.png">

<img src="https://i.imgur.com/sXTWHla.png">

<img src="https://i.imgur.com/CoPmRaY.png">
