import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


class CreditCardApprover:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def load_data(self):
        # carica il dataset
        header = [f'A{i}' for i in range(1, 16)] + ['Class']
        self.df = pd.read_csv(self.data_path, header=None, names=header, na_values='?')
        print("  - Dati caricati con successo.")
        print(f"  - Shape del dataset: {self.df.shape}")
        print("  - Info sul dataset:")
        self.df.info(verbose=False)
        print("  - Valori mancanti prima della pulizia:")
        print(self.df.isnull().sum())
        print("-" * 20)
        
    def preprocess_data(self):
        # eseguiamo il preprocessing dei dati, cioè la pulizia e la normalizzazione
        
        for col in self.df.columns:
            if self.df[col].isnull().any():
                if self.df[col].dtype == 'object':
                    valore_frequente = self.df[col].mode()[0]
                    self.df[col] = self.df[col].fillna(valore_frequente)
                else:
                    media = self.df[col].mean()
                    self.df[col] = self.df[col].fillna(media)
        print("  - Valori mancanti dopo la pulizia:")
        print(self.df.isnull().sum())
        print("-" * 20)
        
        # codifica delle variabili categoriche (One-Hot Econding)
        col_categoriche = self.df.select_dtypes(include=['object']).columns.tolist()
        col_categoriche.remove('Class')  # variabile target
        self.df = pd.get_dummies(self.df, columns=col_categoriche, drop_first=True)
        print("  - Variabili categoriche codificate:")
        print(self.df.head())
        
        # mappatura della colonna target
        self.df['Class'] = self.df['Class'].map({'+': 1, '-': 0})
        
        # divisione in features e target
        X = self.df.drop('Class', axis=1)
        y = self.df['Class']
        
        # suddivisione in set di addestramento e test
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        
        # scaling delle features numeriche
        scaler = StandardScaler()
        self.X_train = scaler.fit_transform(self.X_train)
        self.X_test = scaler.transform(self.X_test)
        
        
    def build_model(self):
        # creazione del modello di rete neurale
        self.model = Sequential([
            Dense(64, activation='relu'),
            Dense(32, activation='relu'),
            Dense(16, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        
    def train_model(self):
        # allena e valuta il modello
        history = self.model.fit(
            self.X_train,
            self.y_train,
            epochs = 10,
            batch_size = 32,
            validation_split = 0.2,
            verbose=1
        )
        
        print("Riepilogo dell'addestramento:")   
        self.model.summary()
        
        # valutazione del modello
        loss, accuracy = self.model.evaluate(self.X_test, self.y_test, verbose=1)
        print(f"  - Loss: {loss:.4f}")
        print(f"  - Accuracy: {accuracy:.4f}")
        
    def run(self):
        # eseguiaamo il flusso di lavoro completo
        self.load_data()
        self.preprocess_data()
        self.build_model()
        self.train_model()
        
# input del percorso del dataset
if __name__ == "__main__":
    data_file = 'crx.data'
    approver = CreditCardApprover(data_path=data_file)
    approver.run()