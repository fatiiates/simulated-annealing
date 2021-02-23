- [EN description](#en)  
- [TR açıklama](#tr)



# Tavlama Benzetimi(Simulated Annealing)

# [TR]

## Tavlama Benzetimi Nedir ?
&emsp;&emsp;Tavlama benzetimi belirli bir fonksiyonun global optimum değerini stokastik olarak tahmin etmek için kullanılan meta-sezgisel yöntemdir.
 
# Nasıl Çalışır ?
&emsp;&emsp;Tavlama(Annealing), metalürjide sıkça kullanılan işlemlerden biri olan metali belirli bir seviyeye kadar ısıtıp kontrollü olarak soğutarak yapısının sağlamlaştırıldığı bir teknikten gelmektedir. Aynı tekniği algoritmaya döküp fonksiyonlara uygulayarak fonksiyonların global minimumlarını elde edebiliriz.

- Adım 1: Başlangıç çözümü, başlangıç sıcaklığı, başlangıç çözümü belirlenir.
- Adım 2: Mevcut x,y değerlerine karşın rassal olarak yeni komşu x,y değerleri üretilir.
- Adım 3: Mevcut çözüm ile yeni komşu değerler ile hesaplanan çözüm karşılaştırılır.
- Adım 4: Eğer yeni çözüm > mevcut çözüm ise; Boltzmann dağılımı hesaplanır.
   - Adım 4.1: Rastgele bir değer hesaplanır ve hesaplanan değer > Boltzmann dağılımı ise değerler güncellenir.
- Adım 5: Eğer yeni çözüm <= mevcut çözüm ise değerler güncellenir.
- Adım 6: Sıcaklık fraksiyona bağlı olarak düşürülür.
- Adım 7: Eğer iterasyona devam edilecekse Adım 2'den devam edilir.
- Adım 8: İterasyon sonlandıysa değerler ekrana verilir ve program sonlanır.
 
 ### Sonuçlar
 
 &emsp;&emsp;TB algoritması metafor bazlı dört farklı fonksiyon üzerinde test edilmiş ve sonuçları aşağıdaki gibidir. Tüm testlerde 'simulatedAnnealing' fonksiyonu için aşağıdaki parametreler kullanılmıştır.

- startedLocation=[0.5, -0.5],
- numberOfIterations=[50, 500],
- temperatureValues=700,
- fraction=.88,
- functionToOptimize=[İLGİLİ_FONKSİYON],
- functionRange=[İLGİLİ_FONKSİYON_ARALIĞI]
 
 #### Ackley Fonksiyonu
 
- Fonksiyon: ![\Large x=f(x,y)={-20exp[-0.2\sqrt{0.5(x^2+y^2)}]-exp[0.5(cos2{\pi}x+cos2{\pi}y)]+e+20}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,y)={-20exp[-0.2\sqrt{0.5(x^2+y^2)}]-exp[0.5(cos2{\pi}x+cos2{\pi}y)]+e+20}) 
- Global minimum: ![\Large x=f(0,0)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(0,0)={0})
- Değer aralığı: ![\Large x=-5%20\leq%20x,y%20\leq%205](https://latex.codecogs.com/svg.latex?\Large&space;-5%20\leq%20x,y%20\leq%205)

Elde edilen değerler

- En iyi çözüm için x ve y: -0.0017175650567326506, -0.001767226084160134
- En iyi x ve y için sonuç: 0.007132000788232062
- 50 iterasyon sonucunda elde edilen grafikler;

![ackley](https://user-images.githubusercontent.com/51250249/108876819-ab922200-760f-11eb-9a6b-a01f2da187f6.png)

 #### Beale Fonksiyonu
 
-

 #### Goldstein-Price Fonksiyonu


 #### Levi Fonksiyonu
 
