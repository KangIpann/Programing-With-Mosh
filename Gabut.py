def total_belanjaan(total, pengiriman, diskon):
    harga_kedua = total + pengiriman
    harga_diskon = harga_kedua * diskon
    harga_akhir = harga_kedua - harga_diskon
    print(f'Total harga belanjaan anda: Rp.{harga_akhir}')
    return harga_akhir



total_belanjaan(total=float(input('Masukan belanjaan anda: RP.'.title())), pengiriman=float(input("Masukan total ongkir anda: RP.".title())), diskon=0.1)
