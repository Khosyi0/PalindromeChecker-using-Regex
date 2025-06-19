import re

class PalindromeRecognizer:
    """
    Kelas untuk mengenali string palindrom yang terdiri dari kombinasi huruf dan angka.
    Menggunakan konsep finite automata untuk memvalidasi input.
    """
    
    def __init__(self):
        self.valid_pattern = re.compile(r'^[a-zA-Z0-9]*$')
    
    def is_valid_input(self, string):
        """
        Memvalidasi apakah string hanya terdiri dari huruf dan angka.
        Sesuai dengan pola (letter + digit)*
        """
        return bool(self.valid_pattern.match(string))
    
    def is_palindrome(self, string):
        """
        Mengenali apakah string adalah palindrom.
        Menggunakan pendekatan two-pointer (finite automata approach).
        """
        if not self.is_valid_input(string):
            return False, "Input tidak valid! Hanya huruf dan angka yang diperbolehkan."
        
        # Konversi ke lowercase untuk case-insensitive comparison
        string = string.lower()
        
        # Implementasi finite automata dengan two-pointer
        left = 0
        right = len(string) - 1
        
        while left < right:
            if string[left] != string[right]:
                return False, f"Bukan palindrom: karakter '{string[left]}' ≠ '{string[right]}'"
            left += 1
            right -= 1
        
        return True, "String adalah palindrom!"
    
    def analyze_palindrome(self, string):
        """
        Menganalisis string dan memberikan informasi detail.
        """
        print(f"\n{'='*50}")
        print(f"Analisis String: '{string}'")
        print(f"{'='*50}")
        
        # Validasi input
        if not self.is_valid_input(string):
            print("Input TIDAK VALID!")
            print("   Hanya huruf (a-z, A-Z) dan angka (0-9) yang diperbolehkan.")
            return
        
        print("Input VALID (sesuai pola (letter + digit)*)")
        
        # Informasi string
        print(f"Panjang string: {len(string)}")
        print(f"String lowercase: {string.lower()}")
        
        # Cek palindrom
        is_pal, message = self.is_palindrome(string)
        
        if is_pal:
            print("HASIL: PALINDROM")
        else:
            print("HASIL: BUKAN PALINDROM")
        
        print(f"Detail: {message}")
        
        # Tampilkan perbandingan karakter
        string_lower = string.lower()
        print(f"\nPerbandingan karakter:")
        print(f"Maju:     {' '.join(string_lower)}")
        print(f"Mundur:   {' '.join(string_lower[::-1])}")


def main():
    """
    Fungsi utama untuk menjalankan program.
    """
    recognizer = PalindromeRecognizer()
    
    print("PROGRAM PENGENALAN STRING PALINDROM")
    print("Input: (letter + digit)* - kombinasi huruf dan angka")
    print("="*60)
    
    # Test cases
    test_strings = [
        "aba",                  # palindrom huruf
        "121",                  # palindrom angka
        "a1a",                  # palindrom campuran
        "Madam",                # palindrom case-insensitive
        "A1B2B1A",              # palindrom campuran panjang
        "racecar",              # palindrom klasik
        "hello",                # bukan palindrom
        "12321",                # palindrom angka
        "a1b2c",                # bukan palindrom
        "Was1it1a1rat1I1saw",   # palindrom kompleks
        "abc@123",              # input tidak valid
        "",                     # string kosong
        "a",                    # single character
        "12"                    # dua karakter tidak palindrom
    ]
    
    print("TESTING DENGAN BERBAGAI CONTOH:")
    for test_string in test_strings:
        recognizer.analyze_palindrome(test_string)
    
    print("\n" + "="*60)
    print("INPUT MANUAL:")
    
    while True:
        try:
            user_input = input("\nMasukkan string (atau 'quit' untuk keluar): ").strip()
            
            if user_input.lower() == 'quit':
                print("Yahh, keluar... Salam dari U38")
                break
            
            recognizer.analyze_palindrome(user_input)
            
        except KeyboardInterrupt:
            print("\n\nKok maksa keluar")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()