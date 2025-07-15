# import os
# from openai import OpenAI

# # Set your API key here
# client = OpenAI(api_key="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")  # your key

# def chat_with_gpt(prompt):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response.choices[0].message.content

# # Test chatbot
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         break
#     reply = chat_with_gpt(user_input)
#     print("Bot:", reply)

import fitz  # PyMuPDF
from PIL import Image
from pyzbar.pyzbar import decode

# Open PDF
doc = fitz.open("your_file.pdf")
page = doc.load_page(0)
pix = page.get_pixmap()
pix.save("page.png")

# Scan barcode
img = Image.open("WhatsApp Image 2025-07-14 at 14.19.30")
results = decode(img)
for result in results:
    print("Type:", result.type)
    print("Data:", result.data.decode("utf-8"))






