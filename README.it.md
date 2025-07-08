[Read in English](README.md)

# Sistema di predizione per carte di credito
[![Licenza: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Questo progetto implementa un sistema di machine learning per prevedere l'approvazione delle richieste di carte di credito. L'applicazione utilizza una rete neurale costruita con TensorFlow e Keras, è scritta in Python con un approccio orientato agli oggetti (OOP) e può essere eseguita sia localmente che tramite un container Docker.

## Sommario

- [Scopo del Progetto](#scopo-del-progetto)
- [Tecnologie Utilizzate](#tecnologie-utilizzate)
- [Struttura del Progetto](#struttura-del-progetto)
- [Guida all'Installazione e all'Esecuzione](#guida-allinstallazione-e-allesecuzione)
  - [Prerequisiti](#prerequisiti)
  - [Opzione 1: Esecuzione tramite Docker (Consigliata)](#opzione-1-esecuzione-tramite-docker-consigliata)
  - [Opzione 2: Esecuzione in Locale](#opzione-2-esecuzione-in-locale)
- [Dettagli dell'Implementazione](#dettagli-dellimplementazione)
  - [Dataset](#dataset)
  - [Preprocessing dei Dati](#preprocessing-dei-dati)
  - [Modello di Rete Neurale](#modello-di-rete-neurale)
- [Autore](#autore)

## Scopo del Progetto

Le banche ricevono numerose richieste di carte di credito, e la loro valutazione manuale è un processo lento e soggetto a errori. Questo progetto automatizza il processo di approvazione costruendo un modello predittivo che analizza i dati dei richiedenti per determinare la probabilità di approvazione.

## Tecnologie Utilizzate

- **Linguaggio**: Python 3.11
- **Machine Learning**: TensorFlow, Keras
- **Manipolazione Dati**: Pandas, NumPy
- **Preprocessing**: Scikit-learn
- **Containerizzazione**: Docker

## Struttura del Progetto

```
credit-approval-system/
├── .venv/                # Ambiente virtuale locale (ignorato da Git e Docker)
├── app.py                # Script principale con la logica dell'applicazione
├── crx.data              # Il dataset grezzo
├── requirements.txt      # Elenco delle dipendenze Python
├── Dockerfile            # Istruzioni per costruire l'immagine Docker
├── .dockerignore         # File e cartelle da escludere dal build Docker
└── README.md             # Questo file
```

## Guida all'Installazione e all'Esecuzione

### Prerequisiti

- [Git](https://git-scm.com/)
- [Python 3.11](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (per l'opzione Docker)

### Opzione 1: Esecuzione tramite Docker (Consigliata)

Questo è il modo più semplice e veloce per eseguire l'applicazione, poiché non richiede alcuna configurazione manuale dell'ambiente Python.

1.  **Clona il repository:**
    ```bash
    git clone https://github.com/aciluca/credit-approval-system.git
    cd credit-approval-system
    ```

2.  **Costruisci l'immagine Docker:**
    Il comando `docker build` legge il `Dockerfile` e crea un'immagine contenente l'applicazione e tutte le sue dipendenze.
    ```bash
    docker build -t credit-approver-app .
    ```

3.  **Esegui il container:**
    Lancia l'applicazione all'interno del container. Il flag `--rm` assicura che il container venga rimosso dopo l'esecuzione.
    ```bash
    docker run --rm credit-approver-app
    ```
    Vedrai l'output del processo di training e valutazione stampato direttamente nel tuo terminale.

### Opzione 2: Esecuzione in Locale

Segui questi passaggi per configurare l'ambiente ed eseguire lo script sul tuo computer.

1.  **Clona il repository:**
    ```bash
    git clone https://github.com/aciluca/credit-approval-system.git
    cd credit-approval-system
    ```

2.  **Scarica il dataset:**
    Il dataset originale proviene dall'UCI Machine Learning Repository. Puoi scaricarlo con `curl` (su macOS/Linux) o `wget`.
    ```bash
    # Su Linux/macOS
    curl -o crx.data http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data

    # Su Windows (usando PowerShell)
    Invoke-WebRequest -Uri http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data -OutFile crx.data
    ```

3.  **Crea e attiva un ambiente virtuale:**
    È una best practice isolare le dipendenze del progetto.
    ```bash
    # Crea l'ambiente virtuale
    python -m venv .venv

    # Attiva l'ambiente
    # Su Windows
    .\.venv\Scripts\activate
    # Su macOS/Linux
    source .venv/bin/activate
    ```

4.  **Installa le dipendenze:**
    Il file `requirements.txt` contiene tutte le librerie necessarie.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Esegui lo script Python:**
    Ora che l'ambiente è configurato, puoi lanciare l'applicazione.
    ```bash
    python app.py
    ```

## Dettagli dell'Implementazione

### Dataset

Il progetto utilizza il [Credit Approval Data Set](http://archive.ics.uci.edu/ml/datasets/Credit+Approval) dall'UCI Repository. Per proteggere la privacy, i nomi delle feature e i valori sono stati resi anonimi.

### Preprocessing dei Dati

Lo script `app.py` esegue i seguenti passaggi di preprocessing:
1.  **Gestione dei Valori Mancanti**: I valori mancanti (indicati con `?`) vengono imputati usando la media per le colonne numeriche e la moda per quelle categoriche.
2.  **Codifica delle Variabili Categoriche**: Le feature categoriche vengono trasformate in numeriche tramite One-Hot Encoding.
3.  **Scaling**: Tutte le feature vengono standardizzate (media 0, varianza 1) usando `StandardScaler` per ottimizzare le performance del modello.

### Modello di Rete Neurale

È stata implementata una rete neurale sequenziale con Keras, composta da:
-   Un layer di input
-   Due layer nascosti (`Dense`) con attivazione `ReLU`.
-   Un layer di output con attivazione `Sigmoid`, ideale per problemi di classificazione binaria.

Il modello viene compilato con l'ottimizzatore `Adam` e la funzione di loss `binary_crossentropy`.

## Autore

- **Luca Acerbi** - [aciluca](https://github.com/aciluca)

## Licenza

Questo progetto è distribuito con licenza MIT. Per maggiori dettagli, vedere il file [LICENSE](LICENSE).
