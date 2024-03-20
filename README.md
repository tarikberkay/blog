
# DRF GENERIC VIEW

Django Rest Framework Generic Views yapısı ile Blog projesi.



## Kurulum

Not: Sol taraftaki veriler Mac kurulumu için sağ taraftaki veriler Windows kurulumu içindir.

Projeyi Kurma  

```bash
  git clone https://github.com/tarikberkay/drf-genericview.git
```

Sanal Ortam Oluşturma
```bash
  python3 -m venv venv || python -m venv venv
```

Sanal Ortamı Aktif Etme
```bash
  source venv/bin/activate  ||  venv\Scripts\activate
```

Gerekli Paketleri Kurma
```bash
  pip3 install -r requirements.txt  ||  pip install -r requirements.txt
```


Projeyi Çalıştırma
```bash
  python3 manage.py runserver || python manage.py runserver
```

  
## API Kullanımı

#### Tüm öğeleri getir

```http
  http://127.0.0.1:8000/api/posts
```
Tüm Postları getirir.



#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/authors/
```

Tüm yazarları getirir.




#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/tags/
```

Tüm Tag'leri getirir.




#### Öğeyi getir

```http
  http://127.0.0.1:8000/api/swagger/
```

Swagger ile API belgelenmesi kısmıdır.






  
