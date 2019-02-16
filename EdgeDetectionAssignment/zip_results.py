import sys
from zipfile import ZipFile

# more fine-grained control over ZIP files
with ZipFile(sys.argv[1]+"_edge_detection.zip", "w") as newzip:
    newzip.write("book_gray_e.png")
    newzip.write("checkmate_e.png")
    newzip.write("wooden_pool_e.png")
    newzip.write("detect_canny_edges.py")
