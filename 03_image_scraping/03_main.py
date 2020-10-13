from simple_image_download import simple_image_download as simp


def download_images(keywords, limit):
    response = simp.simple_image_download

    try:
        response().download(keywords, limit)
        print(response().urls(keywords, limit))
    except FileNotFoundError:
        pass


download_images('horse, lion', 10)