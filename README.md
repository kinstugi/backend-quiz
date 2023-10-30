# DIJI.TECH Backend Quiz

Lütfen aşşağıdaki yönergeleri takip ederek görevleri tamamlayın.

## Kurulum
1. Python env oluşturun
2. Requirements.txt oluşturun
3. .gitignore dosyası oluşturun
4. Aşağıdaki Kütüphanelerin Son Versiyonlarını Kurun
   1. Django
   2. Django Rest Framework
      * Başka kütüphaneye ihtiyacınız varsa kurablirsiniz.
5. Django projesi oluşturun
6. Yeni app oluşturun `location` 
7. Modelleri Ekleyin
   1. Country
      1. name
      2. search_text
      3. search_count
      4. code
      5. phone_code
   2. City
      1. name
      2. search_text
      3. search_count
      4. country
   3. Airport
      1. name
      2. search_text
      3. search_count
      4. code
      5. country
      6. city
8. Fixture dosyasındaki verileri data migration oluşturarak yükleyin

## Ortak Görevler (Tüm modeller için Geçerli)

1.  Location Modellerdeki `name`,`search_text` ve `search_count` zorunlu olmalı eklenmediğinde uygulama hata vermeli
2.  Location appte `search_text` alanı için bir management komudu oluşturun.
    1.  `python manage.py XXX`
    2.  Bu command ile tüm location modeller için search text oluşmalı.
    3.  Search text kendi ve üst ilişkideki modellerin name alanını içermeli
           1.  Airport => 'airport.name,airport.city.name,airport.country.name'
3.  Location modelleri için `XXX.objects.search('Ankara')` gibi bir arama yapıldığında en doğru sonuçları getiren `.search` fonksiyonunu yazın.`(models.Manager ve models.QuerySet)`
    1.  Fonksiyon küçük büyük harf duyarlı olmalı
    2.  Unaccent aramalardada sonuç verebilmeli
        1.  Örn: Niğde ve NİgDe aynı sonuçları verebilmeli
4.  Aşağıdaki endpointleri oluşturun (Rest Framework)
    1. Tüm Location Modeller için Search End Point
       1. Yukarıda belirtilen search fonksiyonunu kullanarak en fazla 20 tane sonuç getirecek.
    2. Tüm Location Modeller için Select End Point
       1. Bir lokasyonun seçilmesi sağlanır.
       2. Select olduğunda request içine Cookie ile seçili model ve lokasyonun id'si kayıt edilir.
    3. Deselect End Point
       1. Cookieden seçili olan lokasyonu temizler.
5.  Bir lokasyon seçildiğinde search_count'u artmalı
    1. Aynı Zamanda üst ilişkilerininde search_countu artmalı
6.  Eğer atılan request cookilerinde bir lokasyon seçilmiş ise search_count artmalı
    1. Aynı Zamanda üst ilişkilerininde search_countu artmalı
    2. Response 200 kodu ile dönmüyorsa search_count artmamalı.
7. Eğer yeni bir lokasyon modeli eklenirse örn: `Stations` tüm yapı bu model içinde çalışmalı

## Görevler

1. Counry Most Searched Cities End Point
   1. Ülke kodu gönderilir ve en çok aranan 5 şehiri listelenir
   2. 1 den fazla ülke kodu gönderilebilir.
   3. Sonuçlar ülkeye göre gruplu gelmelidir.
2. Country Search Ratio
   1. Ülke kodu gönderilir ve toplam şehir araması sayısı toplam airport arama sayısına bölünüp bir oran çıkarılır.
   2. Bu oranla birlikte ülke bilgileri geri dönülür.
   3. 1 den fazla ülke kodu gönderilebilir.

## Notlar
1. 1 kullanıcı sadece 1 lokasyon seçebilir.

## Başlarken
1. Projeyi fork edip kendi reponuzu oluşturun
2. `gitignore` ve `requirements.txt` dosyanızın doğru bir şekilde oluşturun.
3. Kodlarınızı olabildiğince temiz ve anlaşılır yazmaya özen gösterin.
4. Kodlarınızı yazarken bildiğiniz en iyi yöntemler ile yazmaya çalışın.
5. Görevlerden çok yazdığınız kodun önemli olduğunu unutmayın.