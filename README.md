# Flask based application for Animal Recognition using Transfer Learning
 This flask based application for Animal Recognition uses uses transfer learning over Google's Inception CNN for prediciton.

### Please use the requirments.txt to install dependencies:
> pip install -r requirements.txt

## To run the application:
>1.flask db migrate
>2.flask db upgrade
>3.flask run

## For Training the model on new animals:
1. Update the images with the animal name inside tf_files/animals
2. Run the following command on the .console
> python -m scripts.retrain --bottleneck_dir=tf_files/bottlenecks --how_many_training_steps 500 --model_dir=tf_files/inception --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --image_dir tf_files/animals
