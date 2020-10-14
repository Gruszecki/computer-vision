from simple_image_download import simple_image_download as simp


def download_images(keywords, limit):
    response = simp.simple_image_download

    try:
        response().download(keywords, limit)
        print(response().urls(keywords, limit))
    except FileNotFoundError:
        pass


download_images('horse, lion', 10)

'''
Obejście problemu z google_images_download

W terminalu:
pip install tqdm
git clone https://github.com/ ultralytics/google-images-download
cd google-images-download
python bing_scraper.py --search "horse" --limit 600 --download --chromedriver C:\Apps\chromedriver.exe

Po --search podajemy termin o jaki chcemy zapytać, 
po --limit limit zdjęć do pobrania oraz 
po --chrmedriver odpowiednią ścieżkę do chromedriver.exe
'''