# Axle Tree Exercise

One of our clients wants to detect vehicles and axle trees from a video stream.
To do so, our client sent us many videos so that we could train our algorithms to execute this task.
The first step has been to extract images from those videos, and to annotate them with a given 
set of categories: `single_axle`, `car` and `other`. We annotated the images and generated the `annotations.json` file. Then, a first algorithm was trained with this data.

After discussing with the client, it was decided that we would add a new category `grouped_axles`. This new class would be a combination of `single_axle` next to each other.

Before training a new network, your mission is to transform the `annotations.json` file. The objective of this exercise is to merge several axle trees 
into a larger area in which the given axle trees are close enough. Below is an example of the transformation we want to make. Look closely at the purple boxe in the bottomg image, two separate axles have been merged.

![alt text](https://storage.googleapis.com/dp-missions/hiring-sa/single.jpg "Single axle trees")

![alt text](https://storage.googleapis.com/dp-missions/hiring-sa/grouped.jpg "Grouped axle trees")

To do so, you first need to decide on a criteria that you will use to merge axle trees, and then fill in the `merge_axle_trees` 
function in the `merge_axle_trees.py` script to implement your solution. The script takes the `annotations.json` file as input and outputs a new JSON file with the right format but with merged axle tree boxes.
The output JSON should contain only 4 tags: `car`, `other`, `single_axle`, and `grouped_axles`.