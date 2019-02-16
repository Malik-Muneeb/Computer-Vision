import sys
from zipfile import ZipFile

# more fine-grained control over ZIP files
with ZipFile(sys.argv[1]+"_corner_detection.zip", "w") as newzip:
    newzip.write("book_gray_res_rohr.png")
    newzip.write("book_gray_res_harris.png")
    newzip.write("checkmate_res_rohr.png")
    newzip.write("wooden_pool_res_rohr.png")
    newzip.write("detect_corners.py")
