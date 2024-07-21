def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import os

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/jibeombae/capstone/service_account_jibeom_key.json"


    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    print(f'\n"{texts[0].description}"')

    # for text in texts:
    #     print(f'\n"{text.description}"')

        # vertices = [
        #     f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        # ]

        # print("bounds: {}".format(",".join(vertices)))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

detect_text('book.jpg')


# {
#   "type": "service_account",
#   "project_id": "glowing-furnace-430104-p9",
#   "private_key_id": "c332ff981a0d3e3c02d65f0ad53515b9b22c0610",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC6109Gt33IE+be\nKXG9YoIEgCdekDre/EsTgZxdtV62BXGq0s3q3YGmDicWViV3alEtgFeiQng1bbE6\nyB7ucs34hs0pZrc+I14FyGwonTG1RQrd6XUXIFgA3GotRSHNzr8cXKAUrx0JepzT\n3eYfiaHbEDsqdy7BJjttNUYjfMTcx3Pff3Y+lcSOnneBik7G0Yej4LS7ARIIMbSc\nwEL/dfk6jqJZc7JTTOyWKMA0AV+YFyp/aS2sIujDGkxh53464jeNRISVuHCo8Kn/\neW26SH7katHTcfKIF/uzrqraSEMIwWWrcUJ/ZcCraX5jC/OWqohehNPuE/u4nVzV\nq43Dx8KbAgMBAAECggEAEIYiOLrZoOxBqrw3luwzW3qKAM74pefiK+N2lMMJkUeB\n+f2SwIa+hJUT1+HehmUcsM188pi2UONWnUA9nBEDLkudsV+oLRKrqg9DoYPldYaZ\no26WMGln3wufSEmo5661MCjw72NdSg1R+VrSk090xQ72bJcFx4c+EjZ38YODVZMX\nW95Ni+JQPeTLC7VQL4uGUxBYQYTppKYPifb4Aq1RfyoevKIbZOHO1zibckPjvZe6\n1KuWwTQqbAT95H8wguL/M5IopLXWLDRaewq3f66lP9sh+oFBWp+4BT4z5bqeTX1D\nLpiP2Oi5hbJ1hY/AizqUCIrPA45awL7mPFmc74HpAQKBgQDsL+r0tW30SRn0xsg/\nVsPzh79ibCVl/jrqnoUlMnPcvycYFC2NwOv6zpDxs4Fr7ytlLLGS440V3v94w/qX\nVvK7LYhE/I9AkEgpZyh9VEhMVrPk08vdq8FWYCJST23FxQmmfLp1Q3zLo+3VdjJl\nwHkJ7uhSYWxGaSZT9tQgbpzWoQKBgQDKg7EQi3VeIZtvzaVxoVuV8F+3oucxW8bm\n92gUt7+soFidlUUU5HqTCYRBNoC/H1DPMvxbJWL1VY4cKfrQia1RVDEFK1ZJ+iim\nE5TYnkPSgmP8Hsby8dhiUxjAQLdUcrttY4z/spv/K1k+NqSiuqvI2roHt4a+tr78\nXBwYqBQbuwKBgQDXl03THaFGcUveIW08U8j+DRVnk+v3U78X1qcWsx0LjPj0g8ap\nNEazY8buuboTefeUnN1ihY+NPUbZR5sAdf+PWBqhTiC9AHa+REmzTTHJbQM8hw/6\nQgNzAsGRfKto8VjDveq9i2Lox7QbO475Tl2t8YPjXsZk5ypzTkWHbTCAwQKBgGCi\n0NZtRddiQBLs1drQPazh5Drz0FC8U8CZJKBmQl+0sDSaKznaASey7dpUkMEix2Po\nF4XC5GLfrY2A9r+WQw9BFpc549YvOkBtraRkeUa1k9KWOSdrAm+A6ZmsCA+TJB8B\n1yGY8FmmLNLELnG8lAanYQgXqoPNHnu71GhrpBTLAoGAeFHqxWL7jKyGo4V3MWa1\nYvv7m2Rh36+IH123HyHquanofklm8rmxrADsYVAHrMsAenXtmTRes1N4hE+paHg3\nGOO1ORiD/9I+cHyIp6jPd/ZROPN7W74jlfKpWyEtRDfHecE15i8f5FRGvEH3g92J\n79h03sHuXVZVkWYJblVof/A=\n-----END PRIVATE KEY-----\n",
#   "client_email": "jibeom@glowing-furnace-430104-p9.iam.gserviceaccount.com",
#   "client_id": "102419720367561128902",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/jibeom%40glowing-furnace-430104-p9.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }