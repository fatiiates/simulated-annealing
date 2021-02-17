import random
import math
import matplotlib
import matplotlib.pyplot as plt

def createPlot(OBJECTIVE_ARRAY, LOCATION_ARRAY):
    fig = plt.figure() # Yeni bir figür oluşturuluyor
    ax1 = fig.add_subplot(211) # Yeni bir alan oluşturuluyor row = 2, col = 1, index = 1
    ax1.plot(OBJECTIVE_ARRAY,'g.-') # Objective değerleri ax1 alanına dahil ediliyor, yeşil renk
    ax1.legend(['Objective']) # Objective grafiğine özel başlık veriliyor

    ax2 = fig.add_subplot(212) # Yeni bir alan oluşturuluyor row = 2, col = 3, index = 2
    LOCATION_X = [] # X lokasyon değerleri için başlangıç dizisi oluşturuluyor
    LOCATION_Y = [] # Y lokasyon değerleri için başlangıç dizisi oluşturuluyor
    for i in range(len(LOCATION_ARRAY)):
        # X lokasyon değerleri güncelleniyor
        LOCATION_X.append(LOCATION_ARRAY[i][0])
        # Y lokasyon değerleri güncelleniyor
        LOCATION_Y.append(LOCATION_ARRAY[i][1])

    # X lokasyon değerleri ax2 alanına dahil ediliyor, mavi renk
    ax2.plot(LOCATION_X, 'b.-')
    # Y lokasyon değerleri ax2 alanına dahil ediliyor, kırmızı renk
    ax2.plot(LOCATION_Y, 'r--')
    # X ve Y grafiklerine özel başlık veriliyor
    ax2.legend(['x','y'])

    # Alanlar ekrana çizdiriliyor
    plt.show()

# ackley
def ackley(x, y):
    val = - 20 * math.exp(-0.2 * math.sqrt(0.5*(x**2 + y**2)))
    val += - math.exp(0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.e + 20
    return val

ackley_test_range = [5, -5]

# beale
def beale(x, y):
    val = (1.5 - x + x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2
    return val


beale_test_range = [4.5, -4.5]

# gold-stein price
def gold_stein_price(x, y):
    val = 1 + ((x + y + 1)**2)*(19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)
    val *= 30 + ((2*x - 3*y)**2)*(18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)
    return val

gold_stein_price_test_range = [2, -2]

# Levi
def levi(x, y):
    val = math.sin(3*math.pi*x)**2 + ((x - 1)**2)*(1 + math.sin(3 * math.pi*y)**2)
    val += ((y - 1)**2)*(1 + math.sin(2*math.pi*y)**2)
    return val

levi_test_range = [10, -10]

def simulatedAnneling(startedLocation=[0.5, -0.5],
                      numberOfIterations=[10, 10],
                      temperatureValues=700,
                      fraction=.88,
                      functionToOptimize=None,
                      functionRange=[1, -1]
                      ):

    if startedLocation[0] > functionRange[0] or startedLocation[0] < functionRange[1]:
        raise Exception(
            "Başlangıç konumu(x) fonksiyon aralığına ait olmalıdır.")
    elif startedLocation[1] > functionRange[0] or startedLocation[1] < functionRange[1]:
        raise Exception(
            "Başlangıç konumu(y) fonksiyon aralığına ait olmalıdır.")
    elif numberOfIterations[0] < 1 or numberOfIterations[1] < 1:
        raise Exception("İterasyon sayıları 1'den daha yüksek olmalıdır.")
    elif temperatureValues < 1:
        raise Exception(
            "Sıcaklık değeri 1'den büyük olmalıdır.")
    elif fraction < .8 or fraction > .95:
        raise Exception(
            "Fraksiyon değeri 0.8 ve 0.95 değerleri arasında olmalıdır.")
    elif functionToOptimize == None:
        raise Exception("Optimize edilecek bir fonksiyon bulunamadı.")
    elif functionRange[0] < functionRange[1]:
        raise Exception(
            "Fonksiyon değerlerinin formatı: [MAX, MİN] şeklinde olmalıdır.")

# ---- SABİT DEĞİŞKEN TANIMLAMALARI - BAŞLANGIÇ

    #  X VE Y BAŞLANGIÇ NOKTALARIMIZ
    START_POINT_X = startedLocation[0]
    START_POINT_Y = startedLocation[1]

    #  Maximum iterasyon sayımız
    N = numberOfIterations[0]

    #  Bir iterasyonda kaç kez komşu bulma denemesi yapacağını belirleyen sayımız
    M = numberOfIterations[1]

    #  Başlangıç sıcaklığı
    TEMPERATURE_MAX = temperatureValues

    #  ALPHA DEĞERİ
    ALPHA = fraction

    #  Optimize edilecek fonksiyon
    FUNCTION_TO_OPTIMIZE = functionToOptimize

    #  Optimize edilecek fonksiyonun değer aralığı
    FUNCTION_RANGE_MAX = functionRange[0]
    FUNCTION_RANGE_MIN = functionRange[1]

# ---- SABİT DEĞİŞKEN TANIMLAMALARI - SON

# ---- BAŞLANGIÇ DEĞERLERİ OLUŞTURMA - BAŞLANGIÇ
    T = TEMPERATURE_MAX
    accept_x = START_POINT_X
    accept_y = START_POINT_Y
    accept_solution = FUNCTION_TO_OPTIMIZE(START_POINT_X, START_POINT_Y)
    # Grafik çizimi için verilerin tutulduğu diziler
    ALL_OBJECTIVE = []
    ALL_OBJECTIVE_LOCATION = []
# ---- BAŞLANGIÇ DEĞERLERİ OLUŞTURMA - SON

# ---- EN İYİ DEĞERLERİ HESAPLAMAK İÇİN İTERASYON BAŞLATILIYOR
    for i in range(N):

        for j in range(M):
            # Yeni ve rassal olarak x, y noktaları üretiliyor
            x1 = accept_x + random.gauss(0.5, .1*(FUNCTION_RANGE_MAX - FUNCTION_RANGE_MIN))
            y1 = accept_y + random.gauss(-0.5, .1*(FUNCTION_RANGE_MAX - FUNCTION_RANGE_MIN))
            # Eğer ki aralık dışında bir değer üretildiyse aralık sınırlarına sabitleniyor
            x1 = min(x1, FUNCTION_RANGE_MAX) if x1 > 0 else max(x1, FUNCTION_RANGE_MIN)
            y1 = min(y1, FUNCTION_RANGE_MAX) if y1 > 0 else max(y1, FUNCTION_RANGE_MIN)
            delta = FUNCTION_TO_OPTIMIZE(x1, y1) - accept_solution
            # Fonksiyon değeri eski fonksiyon değerinden yüksek ise (kötü ise)
            if (FUNCTION_TO_OPTIMIZE(x1, y1) > accept_solution):
                # Boltzmann sabiti
                # Normalde = 1.38064852e-23
                kB = 1.38064852e-3
                # Boltzmann dağılımı
                distribution = math.exp(-abs(delta)/(kB*T))
                # Eğer rassal olarak üretilen sayı dağılımdan küçük ise [0, 1) -> rassal değer
                if (random.random() < distribution):
                    # Kötü sonuç kabul edilir. Veriler yenileriyle güncellenir.
                    accept_x = x1
                    accept_y = y1
                    accept_solution = FUNCTION_TO_OPTIMIZE(accept_x, accept_y)
            else:
                # Sonuç zaten iyidir. Veriler yenileriyle güncellenir.
                accept_x = x1
                accept_y = y1
                accept_solution = FUNCTION_TO_OPTIMIZE(accept_x, accept_y)

        # Alfa ile sıcaklık düşürülür.
        T = ALPHA * T
        print('İterasyon {0}: {1}, {2}'.format(i + 1, [accept_x, accept_y], accept_solution))
        ALL_OBJECTIVE.append(accept_solution)
        ALL_OBJECTIVE_LOCATION.append([accept_x, accept_y])

    print('En iyi çözüm için x ve y: ' + str(accept_x) + ', ' + str(accept_y))
    print('En iyi x ve y için sonuç: ' + str(accept_solution))

    # Hesaplanan değerlere bağlı olarak grafikler çizdiriliyor
    createPlot(ALL_OBJECTIVE, ALL_OBJECTIVE_LOCATION)


def main():
    try:
        simulatedAnneling(
            numberOfIterations=[50, 500],
            functionToOptimize=gold_stein_price,
            functionRange=gold_stein_price_test_range
        )
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
