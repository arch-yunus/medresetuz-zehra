

## 💡 “Context” Ne Demek?

“Context”, bir olayın **geçtiği ortam, koşullar veya anlam çerçevesi** demek.
Yani bilgi *tek başına* değil, **nerede, kim tarafından, hangi durumda kullanıldığına göre** anlam kazanıyor.

Örnek:

* “Python” kelimesi bir yazılımcı için programlama dili, bir zoolog için yılandır.
  👉 Aynı kelime ama **farklı context = farklı anlam**

---

## 🧠 Context Engineering Nedir?

Kısaca:
**Veri, sistem veya insan davranışlarını doğru yorumlayabilmek için bağlamın (context’in) modellenmesi, yönetilmesi ve mühendislik düzeyinde işlenmesidir.**

Yani context engineering, “veriyi anlamlandırma sanatı”dır diyebiliriz.
Veriyi sadece toplamakla kalmaz, o verinin hangi koşulda, hangi anlamda ve ne işe yarayacağını da sistematik hale getirir.

---

## ⚙️ Nerelerde Kullanılır?

### 1. **Yapay Zekâ & NLP (Doğal Dil İşleme)**

* ChatGPT gibi modeller, sorunu anlamak için bağlamı işler.
* “Kedi masanın üstüne çıktı, sonra düştü. Kim düştü?”
  → Doğru cevap için model bağlamı çözümlemek zorunda.

### 2. **IoT (Nesnelerin İnterneti)**

* Sensör verilerini anlamlandırmak için “ortam koşulları” (sıcaklık, konum, zaman) gerekir.
* Bağlam mühendisliği burada cihazların çevreyle etkileşimini yönetir.

### 3. **Kullanıcı Deneyimi (UX) ve Arayüz Tasarımı**

* Kullanıcının konumuna, cihazına, saatine göre farklı öneriler sunmak (örneğin YouTube’un akşam sakin müzikler önermesi).

### 4. **Siber Güvenlik**

* Sistem davranışlarını izlerken “anormal” durumları anlamak için bağlama ihtiyaç vardır.
* Örneğin: Gecenin bir yarısı giriş yapan bir kullanıcı → sistem “context-aware” bir uyarı verebilir.

---

## 🧩 Context Engineering’in Temel Bileşenleri

| Bileşen                    | Açıklama                                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Context Modeling**       | Bağlamın hangi verilerden oluştuğunu tanımlamak (örneğin zaman, yer, cihaz türü, kullanıcı profili). |
| **Context Representation** | Bağlamı sistemin anlayacağı biçimde modellemek (örneğin ontolojiler, veri şemaları).                 |
| **Context Reasoning**      | Bu bağlamdan anlam çıkarmak (örneğin: “kullanıcı sabah işe gidiyor” sonucunu üretmek).               |
| **Context Adaptation**     | Sistem davranışını bağlama göre uyarlamak.                                                           |

---

## 🚀 Neden Önemli?

Çünkü **geleceğin sistemleri “bağlam farkında” olmak zorunda.**
Artık sadece *ne söylendiğini* değil, *neden, nerede, kime, hangi şartlarda söylendiğini* de anlayan sistemler kazandırıyor.

---

## 💬 Örnekle Bitirelim:

**Durum:**
Bir akıllı ev sistemi “ışıkları kapat” komutunu duyuyor.

* **Context’siz mühendislik:** Her yerdeki ışıkları kapatır.
* **Context engineering’li sistem:** Komutu kimin verdiğini, hangi odada olduğunu, saat kaç olduğunu, kimlerin uyuduğunu bilir → sadece gerekli odanın ışığını kapatır.
  👉 Daha akıllı, insan gibi davranan sistemler.

---
Harika! 🔥 O zaman senin gibi yazılım kökenli biri için **Context Engineering Öğrenme Yol Haritası**’nı iki parçaya ayıracağım:
1️⃣ Temel mantık ve teori kısmı (bağlam kavramını derin anlamak)
2️⃣ Uygulamalı yazılım tarafı (bağlamı sistemlerde gerçekten kullanmak)

---

## 🧭 1. TEMEL MANTIĞI ANLAMA (Bağlamın Anatomisi)

### 🎯 Hedef:

Bir sistemin veya insanın “duruma göre karar verme” mekanizmasını anlamak.
Burası temel, çünkü context engineering sadece kod değil — **algı, anlam ve etkileşim mühendisliği**.

### 📚 Öğrenilmesi Gerekenler:

| Konu                                      | Ne işe yarar                                                          |
| ----------------------------------------- | --------------------------------------------------------------------- |
| **Context kavramı (bağlam farkındalığı)** | Sistemlerin neden bağlam bilincine sahip olması gerektiğini anlarsın. |
| **Semantic Web & Ontologies**             | Veriyi anlamlı hale getirmenin temeli (RDF, OWL gibi).                |
| **Knowledge Representation**              | Bilgiyi makinelerin anlayabileceği biçimde temsil etmeyi öğretir.     |
| **Context Reasoning**                     | Bağlamdan sonuç çıkarma (örneğin mantıksal çıkarım motorları).        |

🧠 Tavsiye kaynaklar:

* 📘 *“Context-Aware Computing” — Guanling Chen, David Kotz*
* 📗 *“Context in Computing: A Cross-Disciplinary Approach for Modeling the Real World” — Anind K. Dey*
* 🎓 Coursera’da: “**Context-Aware Computing for IoT**” kursu

---

## 💻 2. UYGULAMALI TARAF (Gerçek Sistemlerde Context)

### 🎯 Hedef:

Bir uygulamanın kullanıcı, cihaz, ortam veya zaman gibi bilgileri kullanarak **davranışını değiştirebilmesini sağlamak**.

### 🧩 Öğrenmen Gereken Teknolojiler:

| Alan                               | Teknolojiler / Araçlar                                     |
| ---------------------------------- | ---------------------------------------------------------- |
| **Veri Toplama (Context Sources)** | Sensors, APIs, GPS, kullanıcı davranışı logları            |
| **Veri Modelleme**                 | JSON-LD, RDF, OWL, Graph Databases (Neo4j 🔥)              |
| **Veri İşleme**                    | Python (Pandas, NumPy), Node.js, Stream processing (Kafka) |
| **Yapay Zekâ**                     | NLP (Hugging Face), Reasoning AI, Context Embedding        |
| **Context-Aware Frameworks**       | Context Toolkit (MIT), CoBrA Framework, IoTivity           |
| **API Tasarımı**                   | REST + GraphQL + Context metadata                          |

---

## 🧠 3. UYGULAMA PROJE FİKİRLERİ (Pratikle Pekiştir)

| Proje                                | Amaç                                                                                             |
| ------------------------------------ | ------------------------------------------------------------------------------------------------ |
| 🕵️ **Akıllı Mesaj Asistanı**        | Kullanıcının ruh halini (metin tonu + zaman + cihaz) analiz edip cevap öneren sistem.            |
| 🏠 **Context-Aware Ev Otomasyonu**   | Hangi odada kim varsa ona göre ışık/ses ayarını değiştiren IoT sistemi.                          |
| 📅 **Kontekstli Takvim Asistanı**    | “Bugün dışarısı yağmurlu, dersin 9’da başlıyor, otobüs geç kalıyor.” → erken uyarı veren sistem. |
| 👩‍💻 **Bağlam Duyarlı Kod Editörü** | Kullanıcının kod stilini, hata geçmişini ve proje türünü öğrenip öneri veren mini IDE plugin’i.  |

---

## 🧠 4. YAPAY ZEKÂ İLE BİRLEŞTİRME (En Güçlü Seviye)

Burada “context” artık veriden çıkarılıyor.
Örneğin ChatGPT gibi modeller **prompt context** üzerinden yanıt verir.
Bu aşamada öğreneceğin konular:

| Konu                                           | Açıklama                                                                  |
| ---------------------------------------------- | ------------------------------------------------------------------------- |
| **Context Embeddings**                         | Metin, görsel veya sensör verisinden “anlam” çıkarma.                     |
| **Retrieval-Augmented Generation (RAG)**       | Yapay zekâyı gerçek dünyadaki bağlamla birleştirme.                       |
| **Multi-Agent Systems**                        | Birden fazla yapay zekâ ajanının context paylaşımıyla birlikte çalışması. |
| **LLM Prompt Engineering (Context Injection)** | Modellerin cevaplarını yönlendirmek için bağlam tasarımı.                 |

---

## ⚙️ 5. UZMANLIK YÖNLERİ (İleri Düzey)

Artık yönünü seçebilirsin 👇

* 🔹 **Context-Aware AI Engineer** – yapay zekâ modellerine bağlam farkındalığı kazandırır.
* 🔹 **IoT Context Engineer** – akıllı cihazların çevresini algılamasını sağlar.
* 🔹 **Context Data Scientist** – bağlam verilerini analiz eder ve çıkarım modelleri kurar.
* 🔹 **Human-Context Interaction Designer** – insanın psikolojik ve çevresel bağlamını sistemlere taşır.



## 🧭 1. Temel Kavramları Öğren

Context engineering’in temeli **veriyi, ortamı ve anlamı** birlikte düşünebilmektir.
Bu yüzden önce şu konuları sağlam öğrenmelisin:

### 🔹 Gerekli Alanlar:

* **Yapay zekâ temelleri** (AI, ML, Deep Learning mantığı)
* **Veri bilimi** (Python + pandas, numpy, scikit-learn)
* **Ontoloji & Semantik web** kavramları
* **Bilgi temsili (Knowledge Representation)**
* **Sistem tasarımı ve mimarisi**

### 🔹 Tavsiye kaynaklar:

* *“Artificial Intelligence: A Modern Approach”* – Russell & Norvig
* *Coursera: Context-Aware Computing*
* *MIT OpenCourseWare: Knowledge Systems*

---

## 🧩 2. Programlama ve Teknik Temel

Context Engineering genelde **Python + semantic web + veri sistemleri** üçgeninde yürür.

### Öğrenmen gereken teknolojiler:

| Alan                    | Teknoloji / Kütüphane                          |
| ----------------------- | ---------------------------------------------- |
| Veri İşleme             | `Python`, `pandas`, `numpy`                    |
| AI & NLP                | `transformers`, `spaCy`, `langchain`, `openai` |
| Ontoloji / Semantik Web | `OWL`, `RDF`, `SPARQL`, `Protégé`              |
| Veri tabanı             | `Neo4j (graph)`, `MongoDB`, `PostgreSQL`       |
| Sistem Entegrasyonu     | `RESTful APIs`, `JSON-LD`, `GraphQL`           |

---

## 🧠 3. Context Modeling Aşaması

Burada amaç: *bağlamı tanımlamak.*

### Öğrenmen gereken şeyler:

* **Context modelleme yöntemleri:** key-value, ontoloji tabanlı, çok katmanlı modeller
* **Context lifecycle:** acquisition → modeling → reasoning → adaptation
* **Use case geliştirme:** örneğin “akıllı kampüs” veya “kişisel asistan” gibi projelerde context senaryosu yazmak.

### Uygulama fikri:

> “Kullanıcının bulunduğu yere, saate ve ruh haline göre müzik öneren bir sistem”
> (Buradaki bağlam: konum, zaman, ruh hali)

---

## ⚙️ 4. Context Reasoning (Bağlamdan Anlam Çıkarma)

Yapay zekânın işin içine girdiği asıl bölüm bu.

### Öğren:

* Kural tabanlı sistemler (rule-based reasoning)
* Makine öğrenimi ile context çıkarımı
* Hibrit context reasoning modelleri
* NLP tabanlı anlam çıkarımı

### Örnek araçlar:

* **OWL Reasoner (Hermit, Pellet)**
* **LangChain** ile context-aware LLM entegrasyonu
* **Prolog** (mantıksal çıkarım için)

---

## 🧰 5. Context Adaptation (Bağlama Göre Uyum)

Sistemin davranışını değiştirmen gereken aşama.

### Öğren:

* Kullanıcı profili yönetimi
* Dinamik servis seçimi (service orchestration)
* Context-aware API mimarisi
* Adaptif UI/UX (örneğin: kullanıcı gece modunda → sade arayüz)

---

## 🌍 6. Gerçek Proje Uygulamaları

### Yapabileceğin mini projeler:

1. **Context-aware chatbot** – Konuşmanın önceki mesajlarına göre anlam kurar.
2. **Akıllı ortam asistanı** – Sensör verilerini yorumlayarak ışık, sıcaklık, müzik ayarlar.
3. **Kişisel öneri sistemi** – Zaman, konum, ruh hali gibi bağlamlara göre film önerir.
4. **Akıllı güvenlik sistemi** – Kullanıcının alışkanlıklarına göre “şüpheli girişleri” tespit eder.

---

## 🧩 7. Gelişmiş Konular (İleri Seviye)

Burada artık gerçek anlamda **context engineer** oluyorsun 🔥

* **Context Ontology Design (OWL2, RDF Schema)**
* **Multi-agent Systems** (bağlam paylaşımı)
* **Edge AI & IoT Context Handling**
* **LLM’lerle Context Fusion** (örneğin GPT + sensör verisi birleşimi)
* **Context Privacy & Security**

---

## 📚 Öğrenme Stratejisi

> Her hafta bir alan, her ay bir proje.

### Örnek plan:

| Hafta | Hedef                                                        |
| ----- | ------------------------------------------------------------ |
| 1–2   | Context kavramını, semantik web temellerini öğren            |
| 3–4   | Python + veri işleme + ontoloji denemeleri yap               |
| 5–8   | Kendi mini context-aware sistemini yaz (örneğin öneri botu)  |
| 9+    | LLM ve sensör verisini birleştir, gerçek bağlam çıkarımı yap |



---

## 📂 Çekirdek Ders Ağacı
Akademik sistem entegrasyonu kapsamında bu bölüm için önerilen ve standartlaştırılmış ders/çalışma klasörleri:

- [01 Temel Bilimler ve Seminerler](01_Temel_Bilimler_ve_Giris/)
- [02 Alan Dersleri ve Pratik](02_Alan_Dersleri/)
- [03 Seçmeli, İleri ve Uzmanlık Dersleri](03_Secmeli_ve_Ileri_Uygulama/)
- [04 Bitirme, Araştırma ve Çapraz Projeler](04_Arastirma_ve_Bitirme/)

> [!TIP]
> Yeni bir ders eklerken ana dizindeki `DERS_SABLONU.md` dosyasını kopyalayarak ilgili alt klasörün içine koyabilir ve kolayca kendi not şablonunuzu oluşturabilirsiniz!
