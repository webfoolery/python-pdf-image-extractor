from pikepdf import Pdf, PdfImage
import os

pwd = os.path.abspath(os.path.dirname(__file__))
# print (pwd)

for filename in os.listdir(pwd):
	if filename.endswith( 'pdf' ):
		# print(filename)
		# filename = "GSC 30 Cardiff Rd 2022-02-26.pdf"
		example = Pdf.open(filename)
		# mylist = list(enumerate(example.pages))
		# print(len(mylist))

		counter = 1
		for i, page in enumerate(example.pages):
			# print (i, page)
			for j, (name, raw_image) in enumerate(page.images.items()):
				image = PdfImage(raw_image)
				out = image.extract_to(fileprefix=f"{filename.replace('.pdf', '')}-p{i+1:03}-i{j+1:03}")
				# Optional: print info about image
				w = raw_image.stream_dict.Width
				h = raw_image.stream_dict.Height
				f = raw_image.stream_dict.Filter
				size = raw_image.stream_dict.Length
				
				# print (f'{w}x{h}')
				# print (repr(f))

				# print(f"Wrote {name} {w}x{h} {repr(f)} {size:,}B {image.colorspace} to {out}")
				print(f"{counter}. {out}: {name} {w}x{h} {size:,}B {image.colorspace} {repr(f)}")
				counter = counter + 1