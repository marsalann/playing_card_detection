# playing_card_detection
This is part of a computer vision project using YOLOv5 to correctly identify the playing card drawn in front of the camera, display the count, and check the cards already displayed.

The dataset comprises 60,000 images of playing cards with different backgrounds, lighting, and orientation. 
The dataset is prepared by recording the videos of all 52 cards in different lighting conditions. 
OpenCV is then used to extract frames from the videos.
The image augmentation library is used to delimit negative spaces, create bounding boxes, and translate, rotate, and scale the cards on different backgrounds extracted from DTD (describable textures dataset).
Once the dataset is prepared, YOLOv5 is used to train the data for 52 classes.
After acquiring satisfactory results, a simple user interface is created to detect cards shown on a real-time camera where the count of cards drawn (from a single deck) is updated along with the checks on the cards drawn.
