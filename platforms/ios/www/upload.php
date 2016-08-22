<?php
print_r($_FILES);
$new_image_name = "myimg.jpg";
move_uploaded_file($_FILES["file"]["tmp_name"], "uploads/".$new_image_name);
?>
