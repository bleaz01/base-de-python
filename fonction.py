def facture_avec_tva(client, montantHt):
    montant_avec_tva = montantHt *1.21
    print("cher Monsieur "+ client)
    print("vous nous devez la somme de " + str(montant_avec_tva) +"euros.")
    print("bien avous")

facture_avec_tva("jeason", 250)
