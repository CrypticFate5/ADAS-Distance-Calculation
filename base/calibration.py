# Camera Calibration

# Most commonly width is used as parameter, but after checking some edge cases like a vechicles side view, I've come to the conclusion that height would be a more suitable parameter because width would change for an object in a normal perspective, but height would remain the same in every horizontal approach.

# So at first, I'll assign some common heights to common objects seen on the roads.

# Object Height(in meters) Calibration

objects_heights = {
    "person": 1.5,
    "bicyle": 0.6,
    "car": 1.5,
    "motorcycle": 0.65,
    "bus": 4,
    "truck": 4,
    "bird": 0.12,
    "cat": 0.25,
    "dog": 0.45,
    "horse": 1.5,
    "sheep": 0.85,
    "cow": 1.4
}

# Choose a reference object of known height and distance from the camera, then measure the height of image after the capture and calculate the focal length in pixels using the below given function


image_height_of_object_pxl_val = 175
actual_distance_of_object_meters_val = 12
actual_height_of_object_meters_val = objects_heights["car"]


def focalLengthPxl(image_height_of_object_pxl, actual_distance_of_object_meters, actual_height_of_object_meters):
    return (image_height_of_object_pxl*actual_distance_of_object_meters)/actual_height_of_object_meters


focal_length = focalLengthPxl(image_height_of_object_pxl_val,
                              actual_distance_of_object_meters_val, actual_height_of_object_meters_val)
