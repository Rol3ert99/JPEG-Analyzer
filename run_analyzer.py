from classes.Jpeg_Image import JpegImage


jpeg = JpegImage("JPEG_JFIF.jpg")
jpeg.read_markers()
# jpeg.display_image()
# jpeg.DFT_magnitude()
# jpeg.DFT_phase()
# jpeg.parse_app0()
# jpeg.parse_exif()
# jpeg.save_anon()
for marker in jpeg.markers:
    print(marker)
for dht in jpeg.dht:
    print(dht)
    