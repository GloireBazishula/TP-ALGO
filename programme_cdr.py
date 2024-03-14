

class Client:
    """ Classe description du client """
    def __init__(self,nom,date_naissance,tel,facture):
        self.nom = nom
        self.date_naissance = date_naissance
        self.tel = tel
        self.facture = facture
        
class detailCall:

    """ classe pour gerer le call detail """    
    def __init__(self, chemin):
        self.chemin = chemin
        self.data = []
        self.res = []
        self.nombre = 0
        
        
        
    def lire_cdr(self):
        """ lecture du fichier call detail record """
        
        with open(self.chemin, "r") as f:
            for i in f:
                self.i.append(self.data.strip())
            self.pile_dict()
            self.nombre = self.res[0]["Appelant"]
            
                
    def pile_dict(self):
        a = []
        b = ["ID", 'type', 'Hour','appelant', 'appelé', 'Temps', 'Taxe', 'Total volume']
        for i in self.data:
            a = i.split('|')
            self.res.append(dict(zip(b, a)))
            
            
class Payement:
    
    def __init__(self,liste_dict):
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
                    amount += 0.025*dure/60
                else:
                    amount += 0.05*dure/60
            elif type_call == 1:
                if num2[0:4] == '24381' or num2[0:4] == '24382':
                    amount  += 0.001
                else:
                    amount += 0.002
            else:
                amount += total_vol*0.03
            if taxe == 1:
                amount =amount + amount *5/100
            elif taxe == 2:
                amount = amount + amount *16/100
            self.amount += amount
            
            
class Statistique:
    def __init__(self, liste_dict):
        self.liste_dict = liste_dict
        self.nbr_appel = 0
        self.nbr_sms = 0
        self.giga = 0 
        self.dure_appel = 0
        self.statistique = []
        self.stat_dict = {}
    def stat(self):
        for i in self.liste_dict:
            type_call = float(i['type call'])
            
            if i['durée'] != '':
            	dure = float(i['durée'])
            else:
            	dure = 0
            total_vol = float(i['total volume'])
            
            if type_call == 0:
                self.nbr_appel += 1
                self.dure_appel += dure
                
            elif type_call == 1:
                self.nbr_sms += 1
            else:
                self.giga += total_vol
        
        self.statistique = [self.nbr_appel, self.dure_appel, self.nbr_sms, self.giga]
        self.have_stat()
    def have_stat(self):
        a = ["Nombre d'appels", "Durée d'appel", "Nombre de sms", "Nombre de Gigabytes"]
        self.stat_dict = dict(zip(a, self.statistique))
        
if __name__ =='__main__' :
    print("Hello")
        
            
            
            
