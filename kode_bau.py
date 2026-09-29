"""Contoh kode yang telah diperbaiki agar memenuhi standar Pylint."""


def calculate_result(first_value, second_value):
    """Menghitung hasil penjumlahan dua nilai."""
    return first_value + second_value


def main():
    """Menjalankan program utama."""
    first_value = 10
    second_value = 20

    result = calculate_result(first_value, second_value)
    print(f"Hasil perhitungan: {result}")


if __name__ == "__main__":
    main()