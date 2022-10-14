import csv

# creazione di due liste rispettivamente di paesi e continenti da popolare

italia = []
gran_bretagna = []

europa = []
nord_america = []

with open('owid-covid-data.csv', 'r', newline='') as csv_file:
    dataset = csv.DictReader(csv_file)

    #creazione di un ciclo che inserisce in lista italia tutte le row interessate come dictionary ed esclude i paesi diversi da ITA

    for row in dataset:
        if row['iso_code'] == 'ITA':
            italia.append({'data': row['date'],
                           'nuovi_casi_per_milione': row['new_cases_per_million'],
                           'casi_tot_per_milione': row['total_cases_per_million'],
                           'nuove_morti_per_milione': row['new_deaths_per_million'],
                           'morti_tot_per_milione': row['total_deaths_per_million'],
                           'percentuale_vaccinati': row['people_vaccinated_per_hundred'],
                           'abitanti': row['population'],
                           'paese': row['location']})
            if row['iso_code'] != 'ITA':
                break

        #creazione di un ciclo che inserisce in lista gran bretagna tutte le row interessate come dictionary ed esclude i paesi diversi da GBR

        if row['iso_code'] == 'GBR':
            gran_bretagna.append({'data': row['date'],
                                  'nuovi_casi_per_milione': row['new_cases_per_million'],
                                  'casi_tot_per_milione': row['total_cases_per_million'],
                                  'nuove_morti_per_milione': row['new_deaths_per_million'],
                                  'morti_tot_per_milione': row['total_deaths_per_million'],
                                  'percentuale_vaccinati': row['people_vaccinated_per_hundred'],
                                  'abitanti': row['population'],
                                  'paese': row['location']})
            if row['iso_code'] != 'GBR':
                break

        #creazione di un ciclo che inserisce in lista europa tutte le row interessate come dictionary ed esclude i continenti diversi da europa

        if row['continent'] == 'Europe':
            europa.append({'data': row['date'],
                           'nuovi_casi_per_milione': row['new_cases_per_million'],
                           'casi_tot_per_milione': row['total_cases_per_million'],
                           'nuove_morti_per_milione': row['new_deaths_per_million'],
                           'morti_tot_per_milione': row['total_deaths_per_million'],
                           'percentuale_vaccinati': row['people_vaccinated_per_hundred'],
                           'abitanti': row['population'],
                           'paese': row['continent']})
            if row['continent'] != 'Europe':
                break

        #creazione di un ciclo che inserisce in lista nord america tutte le row interessate come dictionary ed esclude i continenti diversi da nord america

        if row['continent'] == 'North America':
            nord_america.append({'data': row['date'],
                                 'nuovi_casi_per_milione': row['new_cases_per_million'],
                                 'casi_tot_per_milione': row['total_cases_per_million'],
                                 'nuove_morti_per_milione': row['new_deaths_per_million'],
                                 'morti_tot_per_milione': row['total_deaths_per_million'],
                                 'percentuale_vaccinati': row['people_vaccinated_per_hundred'],
                                 'abitanti': row['population'],
                                 'paese': row['continent']})
            if row['continent'] != 'North America':
                break


#confronta il numero di nuovi casi giornalieri e morti giornalieri fra i due paesi Italia e Gran Bretagna

def media_in(lista_paese,arg2):      #definizione di funzione chiamata media_in con due argomenti, lista_paese e la key da analizzare
    totale = 0              #variabile che conterrà la somma dei nuovi casi o dei morti
    giorni = len(italia)    #ogni lista_paese contiene tanti dizionari quanti sono i giorni considerati

    if arg2 == 'nuovi_casi_per_milione':
        unita_di_misura = ' nuovi casi'  #unità di misura varia il proprio valore da nuovi casi a morti a seconda della key utilizzata
    else:
        unita_di_misura = ' morti'

    for i in lista_paese:  #qui si applica 0 per ogni volta che il valore è una stringa vuota
        if i[arg2] == '':
            i[arg2] = 0
        totale += float(i[arg2])  #ad ogni ciclo incrementa il totale del valore in numero float

    media = round(totale / giorni)  #calcola la media arrotondata

    print("In " + lista_paese[0]['paese'] + " c'è una media di " + str(media) + unita_di_misura + " al giorno per ogni milione di abitanti.")

#chiamate alla funzione media_in per italia e gran bretagna

media_in(italia, 'nuovi_casi_per_milione')
media_in(gran_bretagna, 'nuovi_casi_per_milione')
media_in(italia, 'nuove_morti_per_milione')
media_in(gran_bretagna, 'nuove_morti_per_milione')

#chiamate alla funzione media_in per europa e nord america

media_in(europa, 'nuovi_casi_per_milione')
media_in(nord_america, 'nuovi_casi_per_milione')  # chiamate alla funzione media_in
media_in(europa, 'nuove_morti_per_milione')
media_in(nord_america, 'nuove_morti_per_milione')

#creazione di due liste di Paesi da popolare con la percentuale dei vaccinati


def picco_vacc(arg1):
    liste_vacc = []
    for row in arg1:
        if row['percentuale_vaccinati'] == '':
            row['percentuale_vaccinati'] = 0
        liste_vacc.append({'percentuale': float(row['percentuale_vaccinati']), 'data': row['data']})
    sorted_list = sorted(liste_vacc, key=lambda x: x['percentuale'], reverse=True)
    perc = sorted_list[0].get('percentuale')

    first_occurence = next(item for item in sorted_list if item['percentuale'] == perc)
    if arg1 == italia or gran_bretagna:
        luogo = (arg1[0].get('paese'))
    else:
        luogo = (arg1[0].get('continente'))

    data_split = first_occurence['data'].split("-")
    data_reverse = []
    data_reverse.append(data_split[2])
    data_reverse.append(data_split[1])
    data_reverse.append(data_split[0])
    data_join = "-".join(data_reverse)
    print(f'La massima percentuale di vaccinati in {luogo} è di: {perc} e si è raggiunta in data {data_join}')

picco_vacc(gran_bretagna)
picco_vacc(italia)
picco_vacc(europa)
picco_vacc(nord_america)

def mediana_in(lista_paese,arg2):      #definizione di funzione chiamata media_in con due argomenti, lista_paese e la key da analizzare

    if arg2 == 'nuovi_casi_per_milione':
        unita_di_misura = ' nuovi casi'  #unità di misura varia il proprio valore da nuovi casi a morti a seconda della key utilizzata
    else:
        unita_di_misura = ' morti'

    for i in lista_paese:  #qui si applica 0 per ogni volta che il valore è una stringa vuota
        if i[arg2] == '':
            i[arg2] = 0
    sorted_list = sorted(lista_paese, key=lambda x: x[arg2])

    indice = len(sorted_list)/2
    print(indice)

mediana_in(italia, 'nuovi_casi_per_milione')