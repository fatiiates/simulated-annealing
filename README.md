# Tavlama Benzetimi(Simulated Annealing)
 Tavlama benzetimi belirli bir fonksiyonun global optimum değerini olasılıksal olarak tahmin etmek kullanılan meta-sezgisel tekniktir.
 
# Nasıl Çalışır ?
Annealing, metalürjide kullanılan işlemlerden biri olan metali ısıtıp kontrollü olarak soğutma tekniğinden gelmektedir. Dolayısıyla aynı teknik algoritmada da mevcuttur.

- Adım 1: Başlangıç çözümü, başlangıç sıcaklığı, başlangıç çözümü belirlenir.
- Adım 2: Mevcut x,y değerlerine karşın rassal olarak yeni komşu x,y değerleri üretilir.
- Adım 3: Mevcut çözüm ile yeni komşu değerler ile hesaplanan çözüm karşılaştırılır.
- Adım 4: Eğer yeni çözüm > mevcut çözüm ise; Boltzmann dağılımı hesaplanır.
- Adım 4.1: Rastgele bir değer hesaplanır ve hesaplanan değer > Boltzmann dağılımı ise değerler güncellenir.
- Adım 5: Eğer yeni çözüm <= mevcut çözüm ise değerler güncellenir.
- Adım 6: Sıcaklık fraksiyona bağlı olarak düşürülür.
- Adım 7: Eğer iterasyona devam edilecekse Adım 2'den devam edilir.
- Adım 8: İterasyon sonlandıysa değerler ekrana verilir ve program sonlanır.
 
 ### Metafor bazlı fonksiyonlar üzerinde Tavlama Benzetimi algoritmasının incelenmesi
 
 #### Ackley Fonksiyonu
 
 - 700 derece başlangıç sıcaklığı ve 500*50 tekrarlanan bir döngü sonucunda;
 - 0 - 53 arası iterasyon değerleri
 ![Ekran görüntüsü 2020-12-20 18-33-19](https://user-images.githubusercontent.com/51250249/102717243-1bbfb700-42f2-11eb-96f9-089d2050930c.png)
 - 449 - 499 arası iterasyon değerleri ve nihai sonuçlar
 ![Ekran görüntüsü 2020-12-20 18-33-22](https://user-images.githubusercontent.com/51250249/102717279-5de8f880-42f2-11eb-9b9a-89d70a2ac8b9.png)
 
 #### Beale Fonksiyonu
 
- 700 derece başlangıç sıcaklığı ve 500*50 tekrarlanan bir döngü sonucunda;
- 0 - 53 arası iterasyon değerleri
![Ekran görüntüsü 2020-12-20 18-39-08](https://user-images.githubusercontent.com/51250249/102717331-ae605600-42f2-11eb-996f-dd286d634242.png)
- 449 - 499 arası iterasyon değerleri ve nihai sonuçlar
![Ekran görüntüsü 2020-12-20 18-39-13](https://user-images.githubusercontent.com/51250249/102717335-b02a1980-42f2-11eb-91cd-78bd5a262b2e.png)

 #### Goldstein-Price Fonksiyonu
 
- 700 derece başlangıç sıcaklığı ve 500*50 tekrarlanan bir döngü sonucunda;
- 0 - 53 arası iterasyon değerleri
![Ekran görüntüsü 2020-12-20 18-40-56](https://user-images.githubusercontent.com/51250249/102717364-ec5d7a00-42f2-11eb-8cb2-d2825a1dc261.png)
- 449 - 499 arası iterasyon değerleri ve nihai sonuçlar
![Ekran görüntüsü 2020-12-20 18-40-59](https://user-images.githubusercontent.com/51250249/102717367-ee273d80-42f2-11eb-9f83-516a31d753ae.png)

 #### Levi Fonksiyonu
 
- 700 derece başlangıç sıcaklığı ve 500*50 tekrarlanan bir döngü sonucunda;
- 0 - 53 arası iterasyon değerleri
![Ekran görüntüsü 2020-12-20 18-42-56](https://user-images.githubusercontent.com/51250249/102717418-35153300-42f3-11eb-884e-2de580c3deb1.png)
- 449 - 499 arası iterasyon değerleri ve nihai sonuçlar
![Ekran görüntüsü 2020-12-20 18-42-59](https://user-images.githubusercontent.com/51250249/102717419-36def680-42f3-11eb-8cd5-8ea69c779796.png)
