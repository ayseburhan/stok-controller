# Ürün Stok Takip Programı

Bu Python programı, bir mağazanın ürün stok durumunu takip etmek için Selenium kütüphanesi kullanılarak geliştirilmiştir. Program, belirli bir ürünün stok durumunu kontrol eder ve ürün stokta olduğunda bildirim verir.

## Gereksinimler

Bu programı çalıştırmak için aşağıdaki gereksinimlere ihtiyacınız vardır:

- Python 3
- Selenium kütüphanesi
- Chrome WebDriver (Google Chrome tarayıcısı için)
  - WebDriver'ı [buradan](https://sites.google.com/a/chromium.org/chromedriver/downloads) indirebilirsiniz.
  - İndirdiğiniz WebDriver dosyasını sisteminizin PATH değişkenine eklemelisiniz.

## Kurulum

1. Python 3'ü indirin ve sisteminize kurun.
2. Selenium kütüphanesini yüklemek için aşağıdaki komutu kullanın:

   ```shell
   pip install selenium
    ```
3. Chrome WebDriver'ı indirin ve sisteminizin PATH değişkenine ekleyin.

## Kullanım
1. stok_takip.py adında bir Python dosyası oluşturun ve içeriğine yukarıdaki kodları yapıştırın.

2. 'url' değişkenini, takip etmek istediğiniz ürünün mağaza sayfasının URL'siyle güncelleyin.

3. Programı çalıştırmak için aşağıdaki komutu kullanın:

    ```shell
    python stok_takip.py
    ```
4. Program, belirli aralıklarla ürün stok durumunu kontrol edecektir. Stokta bulunursa, Ürün bulundu. Mesajını gösterir ve çalışmayı durdurur. Stokta yoksa, 'Ürün bulunamadı' mesajını gösterir ve belirli bir süre sonra yeniden kontrol etmek için sayfayı yeniden yükler.