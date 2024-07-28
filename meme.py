from PIL import Image, ImageDraw, ImageFont
# import matplotlib.pyplot as plt

# Load the images
cat_image = Image.open("./cat.jpeg")

# URL to a sample image of Bill Murray for demonstration
bill_murray_image = Image.open("BillMurray.webp")

# Resize images to match
bill_murray_image = bill_murray_image.resize(cat_image.size)

# Create a new blank image to combine both images
combined_image = Image.new("RGB", (cat_image.width * 2, cat_image.height))
combined_image.paste(cat_image, (0, 0))
combined_image.paste(bill_murray_image, (cat_image.width, 0))

# Add text to the image
draw = ImageDraw.Draw(combined_image)
font = ImageFont.truetype("Impact.ttf", 128)
# font = ImageFont.truetype("/Users/justin.heyes-jones/Library/Fonts/HackNerdFont-Bold.ttf", 92)

# Text settings
top_text = "When your plans go awry..."
bottom_text = "...and you're just trying to act cool about it."

# Draw the text in white
text_color = (255, 255, 255)

w, h = combined_image.size
top_text_bbox = draw.textbbox((0, 0), top_text, font=font)
bottom_text_bbox = draw.textbbox((0, 0), bottom_text, font=font)

top_text_width = top_text_bbox[2] - top_text_bbox[0]
top_text_height = top_text_bbox[3] - top_text_bbox[1]
bottom_text_width = bottom_text_bbox[2] - bottom_text_bbox[0]
bottom_text_height = bottom_text_bbox[3] - bottom_text_bbox[1]

top_text_position = ((w - top_text_width) // 2, 50)
bottom_text_position = ((w - bottom_text_width) // 2, h - bottom_text_height - 120)

# Draw the text
draw.text(top_text_position, top_text, font=font, fill=text_color)
draw.text(bottom_text_position, bottom_text, font=font, fill=text_color)

# Save the result
combined_image_path = "./cat_bill_murray_meme.jpeg"
combined_image.save(combined_image_path)

combined_image.show()
# # Display the result
# plt.imshow(combined_image)
# plt.axis('off')
# plt.show()
