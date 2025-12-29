class BlumBlumShub:
    def __init__(self, seed=None):
        # BBS için iki büyük asal sayı gerekir: p ve q
        # Bu asalların özelliği: 4'e bölündüğünde 3 kalanını vermelidir.
        
        # Gerçek hayatta bunlar 1024 bitlik asallar olmalı.
        self.p = 30000000091 # Örnek büyük bir asal
        self.q = 40000000003 # Örnek diğer asal
        self.M = self.p * self.q # Modülümüz (p * q)
        
        # Seed (tohum) değeri M ile aralarında asal olmalı.
        # Basitlik için rastgele bir başlangıç değeri atayalım.
        if seed is None:
            self.state = 123456789
        else:
            self.state = seed

        # İlk durumu ayarla (x0)
        self.state = (self.state ** 2) % self.M

    def next(self):
        """Bir sonraki rastgele sayıyı üretir."""
        # Formül: X(n+1) = X(n)^2 mod M
        self.state = (self.state ** 2) % self.M
        return self.state

    def get_random_bit(self):
        """BBS genelde bit bit sayı üretmek için kullanılır."""
        # Sayının tek mi çift mi olduğuna bakarak 0 veya 1 döndürür (parity bit)
        return self.state % 2

# Test Kısmı
if __name__ == "__main__":
    bbs = BlumBlumShub(seed=3)
    print(f"Modül (M): {bbs.M}")
    print("--- Rastgele Sayılar ---")
    
    # 5 tane rastgele sayı üret
    for i in range(5):
        print(f"Sayı {i+1}: {bbs.next()}")

    print("\n--- Rastgele Bitler (Daha güvenli kullanım) ---")
    # 8 bit üretip yan yana yazalım (1 byte)
    bits = ""
    for _ in range(8):
        bits += str(bbs.get_random_bit())
    print(f"Üretilen 8-bitlik dizi: {bits}")