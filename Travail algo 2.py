# -- coding: utf-8 --

class Client:
    def _init_(self, nom, date_naissance, tel, facture):
        self.nom = nom
        self.date_naissance = date_naissance
        self.tel = tel
        self.facture = facture

class DetailCall:
    def _init_(self, chemin):
        self.chemin = chemin
        self.data = []
        self.res = []
        self.nombre = 0

    def lire_cdr(self):
        with open(self.chemin, "r") as f:
            for i in f:
                self.i.append(self.data.strip())
            self.pile_dict()
            self.nombre = self.res[0]["Appelant"]

    def pile_dict(self):
        a = []
        b = ["ID", 'type', 'Hour', 'appelant', 'appelé', 'Temps', 'Taxe', 'Total volume']
        for i in self.data:
            a = i.split('|')
            self.res.append(dict(zip(b, a)))

class Payment:
    def _init_(self, liste_dict):
        self.liste_dict = liste_dict
        self.amount = 0

    def description(self):
        for i in self.liste_dict:
            type_call = float(i['type call'])
            num2 = i['appelé']
            if i['durée'] != '':
                dure = float(i['durée'])
            else:
                dure = 0
            total_vol = float(i['total volume'])
            taxe = float(i['taxe'])
            amount = 0
            if type_call == 0:
                if num2[0:4] == '24381' or num2[0:4] == '24382':
                    amount += 0.025 * dure / 60
                else:
                    amount += 0.05 * dure / 60
            elif type_call == 1:
                if num2[0:4] == '24381' or num2[0:4] == '24382':
                    # Ajoutez ici la logique manquante pour le type d'appel 1
                    pass