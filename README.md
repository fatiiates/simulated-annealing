- [EN description](#en)  
- [TR açıklama](#tr)
- [Paper(Bildiri)](https://www.fatiiates.com/doc/notice_optimization.pdf)

# Tavlama Benzetimi(Simulated Annealing, SA)

# [EN]

## What is the Simulated Annealing ?
&emsp;&emsp;SA is the meta-heuristic method used to stochastically estimate the global optimum of a given function.

## How SA Works ? 
&emsp;&emsp;Annealing comes from a technique in which the structure of metal is strengthened by heating the metal to a certain level and cooling it in a controlled, which is one of the frequently used processes in metallurgy. We can create the algorithm of the same technique, we can apply this algorithm to functions and obtain global minimum values of the functions.

- Step 1: The initial solution and initial temperature are determined.
- Step 2: New neighboring x, y values are generated randomly against existing x, y values.
- Step 3: The current solution is compared with the new neighboring values and the calculated solution.
- Step 4: If new solution > existing solution; The Boltzmann distribution is calculated.
   - Step 4.1: A random value is calculated and the values are updated if the calculated value is > Boltzmann distribution.
- Step 5: If new solution <= existing solution; the values are updated
- Step 6: Temperature is lowered depending on fraction value.
- Step 7: If the iteration is to continue, continue from Step 2.
- Step 8: If the iteration is completed, the values ​​are displayed and the program is terminated.
 
### Results
 
 &emsp;&emsp;The SA algorithm has been tested on four different metaphor-based functions and the results are as follows. The following parameters are used for the 'simulatedAnnealing' function in all tests.

- startedLocation=[0.5, -0.5]
- numberOfIterations=[50, 500]
- temperatureValues=700
- fraction=.88
- functionToOptimize=[RELATED_FUNCTION]
- functionRange=[RELATED_FUNCTION_RANGE]


 #### Ackley Function
 
- Function: ![\Large x=f(x,%20y)={-20exp[-0.2\sqrt{0.5(x^2%20+%20y^2)}]-exp[0.5(cos2{\pi}x%20+%20cos2{\pi}y)]%20+%20e%20+%20{20}}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={-20exp[-0.2\sqrt{0.5(x^2%20+%20y^2)}]-exp[0.5(cos2{\pi}x%20+%20cos2{\pi}y)]%20+%20e%20+%20{20}}) 
- Global minimum: ![\Large x=f(0,%200)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(0,%200)={0})
- Search domain: ![\Large x=-5%20\leq%20x,y%20\leq%205](https://latex.codecogs.com/svg.latex?\Large&space;-5%20\leq%20x,y%20\leq%205)

The obtained values

- For the best solution, x and y: -0.0017175650567326506, -0.001767226084160134
- The result for best x and y: 0.007132000788232062
- Graphs obtained as a result of 50 iterations;

![ackley](https://user-images.githubusercontent.com/51250249/108876819-ab922200-760f-11eb-9a6b-a01f2da187f6.png)

 #### Beale Function

- Function: ![\Large x=f(x,%20y)={(1.5%20-%20x%20+%20xy)^2%20+%20(2.25%20-%20x%20+%20xy^2)^2%20+%20(2.625%20-%20x%20+%20xy^3)^2}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={(1.5%20-%20x%20+%20xy)^2%20+%20(2.25%20-%20x%20+%20xy^2)^2%20+%20(2.625%20-%20x%20+%20xy^3)^2}) 
- Global minimum: ![\Large x=f(3,%200.5)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(3,%20{0.5})={0})
- Search domain: ![\Large x=-4.5%20\leq%20x,y%20\leq%204.5](https://latex.codecogs.com/svg.latex?\Large&space;-4.5%20\leq%20x,y%20\leq%204.5)

The obtained values

- For the best solution, x and y: 3.0756646925140005, 0.5286730640983099
- The result for best x and y: 0.003704091519416439
- Graphs obtained as a result of 50 iterations;

![beale](https://user-images.githubusercontent.com/51250249/108878274-27d93500-7611-11eb-8590-d3d3ef23f0fc.png)

 #### Goldstein-Price Function

- Function: ![\Large x=f(x,%20y)={[1%20+%20(x%20+%20y%20+%201)^2(19%20-%2014x%20+%203x^2%20-%2014y%20+%206xy%20+%203y^2)][30%20+%20(2x%20-%203y)^2(18%20-%2032x%20+%2012x^2%20+%2048y%20-%2036xy%20+%2027y^2)]}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={[1%20+%20(x%20+%20y%20+%201)^2(19%20-%2014x%20+%203x^2%20-%2014y%20+%206xy%20+%203y^2)][30%20+%20(2x%20-%203y)^2(18%20-%2032x%20+%2012x^2%20+%2048y%20-%2036xy%20+%2027y^2)]}) 
- Global minimum: ![\Large x=f(0,%20-1)={3}](https://latex.codecogs.com/svg.latex?\Large&space;f(0,%20-1)={3})
- Search domain: ![\Large x=-2%20\leq%20x,y%20\leq%202](https://latex.codecogs.com/svg.latex?\Large&space;-2%20\leq%20x,y%20\leq%202)

The obtained values

- For the best solution, x and y: -0.003973639126817308, -1.0052460061942456
- The result for best x and y: 3.011428548092107
- Graphs obtained as a result of 50 iterations;

![gsp](https://user-images.githubusercontent.com/51250249/108879024-e09f7400-7611-11eb-90da-a1e1527c7a7b.png)


 #### Lévi Function

- Function: ![\Large x=f(x,%20y)={sin^23{\pi}x%20+%20(x%20-%201)^2(1%20+%20sin^23{\pi}y)%20+%20(y%20-%201)^2(1%20+%20sin^22{\pi}y)}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={sin^23{\pi}x%20+%20(x%20-%201)^2(1%20+%20sin^23{\pi}y)%20+%20(y%20-%201)^2(1%20+%20sin^22{\pi}y)}) 
- Global minimum: ![\Large x=f(1,%201)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(1,%201)={0})
- Search domain: ![\Large x=-10%20\leq%20x,y%20\leq%2010](https://latex.codecogs.com/svg.latex?\Large&space;-10%20\leq%20x,y%20\leq%2010)

The obtained values

- For the best solution, x and y: 0.9921885050472286, 1.0427844298879307
- The result for best x and y: 0.007440404165127328
- Graphs obtained as a result of 50 iterations;

![levi](https://user-images.githubusercontent.com/51250249/108880852-b9e23d00-7613-11eb-8fca-52da14e66610.png)

# [TR]

## Tavlama Benzetimi Nedir ?
&emsp;&emsp;TB belirli bir fonksiyonun global optimum değerini stokastik olarak tahmin etmek için kullanılan meta-sezgisel yöntemdir.
 
# Nasıl Çalışır ?
&emsp;&emsp;Tavlama(Annealing), metalürjide sıkça kullanılan işlemlerden biri olan metali belirli bir seviyeye kadar ısıtıp kontrollü olarak soğutarak yapısının sağlamlaştırıldığı bir teknikten gelmektedir. Aynı tekniği algoritmaya döküp fonksiyonlara uygulayarak fonksiyonların global minimum değerlerini elde edebiliriz.

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
 
- Fonksiyon: ![\Large x=f(x,%20y)={-20exp[-0.2\sqrt{0.5(x^2%20+%20y^2)}]-exp[0.5(cos2{\pi}x%20+%20cos2{\pi}y)]%20+%20e%20+%20{20}}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={-20exp[-0.2\sqrt{0.5(x^2%20+%20y^2)}]-exp[0.5(cos2{\pi}x%20+%20cos2{\pi}y)]%20+%20e%20+%20{20}}) 
- Global minimum: ![\Large x=f(0,%200)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(0,%200)={0})
- Değer aralığı: ![\Large x=-5%20\leq%20x,y%20\leq%205](https://latex.codecogs.com/svg.latex?\Large&space;-5%20\leq%20x,y%20\leq%205)

Elde edilen değerler

- En iyi çözüm için x ve y: -0.0017175650567326506, -0.001767226084160134
- En iyi x ve y için sonuç: 0.007132000788232062
- 50 iterasyon sonucunda elde edilen grafikler;

![ackley](https://user-images.githubusercontent.com/51250249/108876819-ab922200-760f-11eb-9a6b-a01f2da187f6.png)

 #### Beale Fonksiyonu

- Fonksiyon: ![\Large x=f(x,%20y)={(1.5%20-%20x%20+%20xy)^2%20+%20(2.25%20-%20x%20+%20xy^2)^2%20+%20(2.625%20-%20x%20+%20xy^3)^2}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={(1.5%20-%20x%20+%20xy)^2%20+%20(2.25%20-%20x%20+%20xy^2)^2%20+%20(2.625%20-%20x%20+%20xy^3)^2}) 
- Global minimum: ![\Large x=f(3,%200.5)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(3,%20{0.5})={0})
- Değer aralığı: ![\Large x=-4.5%20\leq%20x,y%20\leq%204.5](https://latex.codecogs.com/svg.latex?\Large&space;-4.5%20\leq%20x,y%20\leq%204.5)

Elde edilen değerler

- En iyi çözüm için x ve y: 3.0756646925140005, 0.5286730640983099
- En iyi x ve y için sonuç: 0.003704091519416439
- 50 iterasyon sonucunda elde edilen grafikler;

![beale](https://user-images.githubusercontent.com/51250249/108878274-27d93500-7611-11eb-8590-d3d3ef23f0fc.png)

 #### Goldstein-Price Fonksiyonu

- Fonksiyon: ![\Large x=f(x,%20y)={[1%20+%20(x%20+%20y%20+%201)^2(19%20-%2014x%20+%203x^2%20-%2014y%20+%206xy%20+%203y^2)][30%20+%20(2x%20-%203y)^2(18%20-%2032x%20+%2012x^2%20+%2048y%20-%2036xy%20+%2027y^2)]}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={[1%20+%20(x%20+%20y%20+%201)^2(19%20-%2014x%20+%203x^2%20-%2014y%20+%206xy%20+%203y^2)][30%20+%20(2x%20-%203y)^2(18%20-%2032x%20+%2012x^2%20+%2048y%20-%2036xy%20+%2027y^2)]}) 
- Global minimum: ![\Large x=f(0,%20-1)={3}](https://latex.codecogs.com/svg.latex?\Large&space;f(0,%20-1)={3})
- Değer aralığı: ![\Large x=-2%20\leq%20x,y%20\leq%202](https://latex.codecogs.com/svg.latex?\Large&space;-2%20\leq%20x,y%20\leq%202)

Elde edilen değerler

- En iyi çözüm için x ve y: -0.003973639126817308, -1.0052460061942456
- En iyi x ve y için sonuç: 3.011428548092107
- 50 iterasyon sonucunda elde edilen grafikler;

![gsp](https://user-images.githubusercontent.com/51250249/108879024-e09f7400-7611-11eb-90da-a1e1527c7a7b.png)


 #### Lévi Fonksiyonu

- Fonksiyon: ![\Large x=f(x,%20y)={sin^23{\pi}x%20+%20(x%20-%201)^2(1%20+%20sin^23{\pi}y)%20+%20(y%20-%201)^2(1%20+%20sin^22{\pi}y)}](https://latex.codecogs.com/svg.latex?\Large&space;f(x,%20y)={sin^23{\pi}x%20+%20(x%20-%201)^2(1%20+%20sin^23{\pi}y)%20+%20(y%20-%201)^2(1%20+%20sin^22{\pi}y)}) 
- Global minimum: ![\Large x=f(1,%201)={0}](https://latex.codecogs.com/svg.latex?\Large&space;f(1,%201)={0})
- Değer aralığı: ![\Large x=-10%20\leq%20x,y%20\leq%2010](https://latex.codecogs.com/svg.latex?\Large&space;-10%20\leq%20x,y%20\leq%2010)

Elde edilen değerler

- En iyi çözüm için x ve y: 0.9921885050472286, 1.0427844298879307
- En iyi x ve y için sonuç: 0.007440404165127328
- 50 iterasyon sonucunda elde edilen grafikler;

![levi](https://user-images.githubusercontent.com/51250249/108880852-b9e23d00-7613-11eb-8fca-52da14e66610.png)

