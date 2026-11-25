Ti propongo un progetto che copre tutti e quattro i ruoli (Data Analyst, BI Specialist, Business Analyst e controller con Power BI) e sfrutta anche quello che hai studiato in ML. Così mostri qualcosa in più rispetto al classico "dashboard fatta seguendo un tutorial".

## Il progetto: analisi commerciale e previsione vendite di un e-commerce

**Dataset:** *Brazilian E-Commerce Public Dataset by Olist*, gratuito su Kaggle. Contiene circa 100.000 ordini reali (anonimizzati) dal 2016 al 2018, divisi in 9 tabelle collegate: ordini, righe d'ordine, clienti, venditori, prodotti, pagamenti, recensioni e geolocalizzazione. Va bene per un motivo pratico: in azienda i dati non arrivano mai in un unico file pulito, e qui devi collegare più tabelle e costruire un modello dati, proprio come faresti nel lavoro vero.

**Scenario:** immagina di essere l'analista interno appena assunto. La direzione ti chiede:

1. Come va il fatturato? Cresce? Quali sono i mesi forti e quelli deboli?
2. Quali categorie e quali venditori portano più margine e volume?
3. I ritardi nelle consegne peggiorano le recensioni? Di quanto?
4. Chi sono i nostri clienti migliori e quanti sono a rischio di non tornare?
5. Quanto venderemo nei prossimi 3 mesi?

Le domande 1 e 2 sono il lavoro da BI e da controller, la 3 da business analyst, la 4 e la 5 da data scientist.

## Le fasi

**1. SQL: modello dati (circa 1 settimana)**
- Carica i CSV in PostgreSQL (oppure SQLite, se vuoi partire leggero).
- Costruisci uno **schema a stella**: una tabella dei fatti `fact_order_items` e le dimensioni `dim_customer`, `dim_product`, `dim_seller` e `dim_date`.
- Scrivi query di controllo: duplicati, valori nulli, ordini senza pagamento.
- È la competenza che chiedono quasi tutti gli annunci, quindi metti gli script `.sql` bene in vista nel repo.

**2. Python: pulizia, analisi e ML (circa 1 settimana)**
- Analisi esplorativa con pandas e grafici essenziali.
- **Segmentazione RFM** (Recency, Frequency, Monetary) + K-Means, per creare segmenti come "Campioni", "A rischio" e "Persi".
- **Previsione** delle vendite mensili con Prophet o SARIMA, da confrontare con un modello di base semplice (per esempio "come l'anno scorso").
- **Effetto ritardo sulle recensioni**: confronta il voto medio con e senza ritardo, e aggiungi una regressione semplice.
- Esporta i risultati (segmenti e previsioni) in tabelle che Power BI legge.

**3. Power BI: il report (circa 1–2 settimane)**

Quattro pagine:
- **Executive overview:** indicatori principali (fatturato, ordini, valore medio dell'ordine, crescita anno su anno), andamento mensile, previsione.
- **Prodotti e venditori:** classifica delle categorie, analisi di Pareto (il 20% dei venditori fa l'80% del fatturato?), filtri.
- **Logistica:** tempi di consegna per stato, % di ordini in ritardo, legame con le recensioni, mappa.
- **Clienti:** i segmenti RFM, quanti clienti ci sono in ogni segmento, quanto valgono.

Misure DAX da dimostrare di saper scrivere: `Fatturato`, `Fatturato AP` con `SAMEPERIODLASTYEAR`, `YoY %`, `Valore medio ordine`, `% Consegne in ritardo`, cumulato da inizio anno con `TOTALYTD`. Ti serve anche una tabella date marcata come tabella di calendario: è una delle prime cose che guardano ai colloqui.

**4. Documentazione (2–3 giorni)**

Il README conta quanto la dashboard. Deve avere:
- il problema di business;
- 4–5 **insight** concreti, per esempio "gli ordini in ritardo hanno in media 1,7 stelle in meno";
- screenshot o una GIF della dashboard;
- istruzioni per riprodurre il progetto.

## Struttura del repository

```
olist-sales-analytics/
├── README.md
├── data/            # solo link al dataset, non i CSV (troppo pesanti)
├── sql/             # creazione schema, pulizia, viste
├── notebooks/       # 01_eda, 02_rfm_clustering, 03_forecast, 04_delivery_reviews
├── src/             # funzioni Python riutilizzabili
├── powerbi/         # report salvato in formato .pbip
├── images/          # screenshot per il README
└── requirements.txt
```

## Consigli pratici

- **Salva il report come progetto Power BI (.pbip)** e non solo come .pbix. Il .pbip salva il modello come file di testo, quindi su GitHub si vedono le misure DAX e le modifiche nel tempo. Da BI Specialist fai una bella figura.
- **Power BI Desktop gira solo su Windows.** Se hai un Mac ti serve una macchina virtuale.
- **Su GitHub non si può vedere la dashboard dal vivo** senza un account aziendale. Per questo screenshot e GIF nel README sono fondamentali.
- **Scrivi il README in inglese** (o in entrambe le lingue). Le aziende friulane e venete con reparti internazionali lo apprezzano.
- **Su LinkedIn pubblica gli insight, non lo strumento.** "Ho scoperto che il 3% dei venditori genera il 40% del fatturato" colpisce più di "ho fatto una dashboard in Power BI".

## Dopo questo

Se ti interessa anche il ruolo di **controller**, il secondo progetto potrebbe essere un report di **budget vs consuntivo** con conto economico, analisi degli scostamenti e previsioni a fine anno (con dati finanziari simulati). È il tipo di report che le PMI chiedono di più.

Se vuoi, posso prepararti la base di partenza: la struttura del repo, la bozza del README da completare con i tuoi risultati e lo script SQL dello schema a stella. Il lavoro di analisi resterebbe tuo.