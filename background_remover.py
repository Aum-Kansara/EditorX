import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
change_bg.change_bg_img(f_image_path = "static/res/Black_Adam.jpeg",b_image_path = "static/res/3.jpg", output_image_name="new_img.jpg")