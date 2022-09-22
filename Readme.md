# API Link
### Swagger Link
- http://ilabapi.cdf8g6g4aeb4e7c2.westeurope.azurecontainer.io:8188/docs
### Base Link
- http://ilabapi.cdf8g6g4aeb4e7c2.westeurope.azurecontainer.io:8188

# Docker Run

- docker build -t ilab:v2 .
- docker run -d -p 8188:8188 ilab:v2

# Colab
- https://colab.research.google.com/drive/1_3HgOqTfliNtt_6TQd21NFrJRswMiOn1?usp=sharing

# Bonus

1.   Üretilen product_idleri trie gibi bir yapıya leaf düğüme kadar ilerleyip en yakın item üzerinden kontrol sağlanabilir
2.   Hiç emin olmamakla birlikte yazmak istedim.Sepetteki ilişkileri kurmak için kullanılan Associaiton ve apriori algoritması kullanılabilir.(Muhtemelen hatalı mantığında eksiklikler bulunuyor)
3.   Kullanıcının geçirdiği süre, ne kadar tıklandığı, tıklanılan dönemler/mevsimsellik, aldığı yıldız, satış oranı, sepette hangi ürünlerle bulunduğu, kategorisi gibi verileri toplayarak kmeans gibi algoritmalara dahil edilebilir
4.   Unknown word problemine çözüm olarak üretilen FastText kullanılabilir

