Penjelasan:

Network data berupa weighteddirected graph dengan pemain sebagai node, hubungan assist sebagai edge dan jumlah assist sebagai weight.  Perlu diketahui bahwa dataset yang kami kumpulkan tidak mencakup seluruh gol Manchester United pada kompetisi Liga Inggris 20/21. Hal ini dikarenakan tidak semua gol memiliki assist (gol penalti, gol bunuh diri, gol dari kesalahan lawan, dll). Selain itu, terdapat kemungkinan bahwa web scraper yang kami kembangkan belum sempurna dan belum berhasil mengambil seluruh data.

File PLCrawler.ipynb = crawler yang dibuat untuk mengumpulkan data

File out.csv = Network Matrix dalam format csv. Data dalam file csv yang kami kumpulkan diinterpretasikan sebagai berikut:
Kolom berisi nama pemain disebelah kiri memberikan asisst sejumlah n pada pemain dengan nama di row teratas.