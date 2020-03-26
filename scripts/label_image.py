import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf, sys
import os
# image_path = sys.argv[1]
def predict(image_path):

    print(os.path.exists(image_path))
    # Read in the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    print(os.path.exists("tf_files/retrained_labels.txt"))

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                    in tf.gfile.GFile("tf_files/retrained_labels.txt")]

    # Unpersists graph from file

    print(os.path.exists("tf_files/retrained_graph.pb"))
    with tf.gfile.FastGFile("tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        result={}
        for node_id in top_k:
            human_string = label_lines[node_id].title()
            score = predictions[0][node_id]
            result[human_string]="%.5f"%(score*100)
        return result