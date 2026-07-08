import json
import os

classes = ["yogurt"]

for filename in os.listdir("data"):
    
    
    if not filename.endswith(".json"):
        continue
        
    
    json_path = "data/" + filename
    txt_path = "data/" + filename.replace(".json", ".txt")
    
    
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    img_w = data["imageWidth"]
    img_h = data["imageHeight"]
    
    # Open a blank text file to save the final YOLO numbers
    with open(txt_path, "w") as txt_file:
        
        # Loop through every bounding box you drew inside this image
        for shape in data["shapes"]:
            label = shape["label"]
            
            # Find the ID number (0 or 1) for this label
            class_id = classes.index(label)
            
            # Get the two raw corner points of your box from Labelme
            p1 = shape["points"][0]
            p2 = shape["points"][1]
            
            # Calculate the box limits (Left, Right, Top, Bottom)
            xmin = min(p1[0], p2[0])
            xmax = max(p1[0], p2[0])
            ymin = min(p1[1], p2[1])
            ymax = max(p1[1], p2[1])
            
            # Turn raw pixel values into percentages (0.0 to 1.0)
            x_center = ((xmin + xmax) / 2.0) / img_w
            y_center = ((ymin + ymax) / 2.0) / img_h
            box_width = (xmax - xmin) / img_w
            box_height = (ymax - ymin) / img_h
            
            # Write the single line of numbers YOLO needs into the text file
            txt_file.write(f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}\n")

print("[✓] All JSON files converted to TXT files directly inside your data folder!")