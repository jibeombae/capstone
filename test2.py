# import requests

# api_url = 'https://api.api-ninjas.com/v1/imagetotext'
# image_file_descriptor = open('book.jpg', 'rb')
# files = {'image': image_file_descriptor}
# r = requests.post(api_url, files=files)
# # print(r.json())

# out = []
# for j in r.json():
#     out.append(j["text"])

# print(out)

text = f"(UVA) Online Judge Manager\n\"Competitive Programming\" and Kattis share this motivating\nprinciple: to make learning computer science and programming\naccessible for everyone.\n- Fredrik Niemelä, Founder of Kattis\nCP-Book helped us to train many generations of ICPC and 10\nparticipants for Bolivia. It\'s the best source to start and reach a good\nlevel to be a competitive programmer. - Jhonatan Castro,\nICPC coach and Bolivia IO! Team coach\nMy memories about CP3 is me reading it in many places, the bus\nmy room, the library, the contest floor...not much time had passed\nsince I start in competitive programming reading CP3 until I got\nqualified to an ICPC World Final. - Javier Eduardo Ojeda Jorge\nICPC World Finalist, Software Engineer at dParadig, Chile\nI was able to compete in 101 and ICPC WF and I think CP3 played\na very big factor in igniting the interest and providing a strong\ntechnical foundation about all the essential topics required in CP.\n---Sidhant Bansal, National University of Singapore"

print(text)
