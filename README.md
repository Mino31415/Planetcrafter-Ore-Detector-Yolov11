A little yolov11 project to detect and distinct the 12 different ores in the game planet crafter
(The purpose of this project was to get myself familiar with yolov11)

The entire project was divided in 3 parts:
1. Gathering training data
   -using the screenshots.py file I took many screenshots of the game while playing for some time
   
3. Labelling the data & training
   -Using makesense.ai I labelled the ~120 images I then used for the training of detecting the 12 different ores in the game
   -120 is a very small number, usually you would take atleast 5-10x that, however it worked suprisingly well
   -Sometimes there are false positives or it fails to detect an ore it should detect which is due to the small sample size
   
5. Realtime detection
   -using the prediction.py file I let the model run while playing

A few output images:
<img src="https://i.imgur.com/qXaRqq4.jpeg">

<img src="https://i.imgur.com/CM7KvXr.jpeg">

<img src="https://i.imgur.com/kf74dfJ.png">

<img src="https://i.imgur.com/sXTWHla.png">

<img src="https://i.imgur.com/CoPmRaY.png">
