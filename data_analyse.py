
# -----------------------------------------------
data = [16.16, 17.72, 19.94, 20.28, 21.02, 21.17, 21.55, 21.88, 
        22.36, 22.43, 22.50, 22.77, 23.08, 23.26, 24.05, 24.3, 
        24.45, 24.52, 24.62, 25.18, 25.2, 25.23, 25.55, 25.7, 
        25.81, 25.95, 26.09, 26.44, 26.77, 26.8, 27.13, 27.34,
        27.74, 27.91, 28.1, 28.34, 28.47, 29.29, 29.34, 31.77]
class_beginn = 16 # kleinster Klassenbeginn (exlusive)
class_ends = [19, 21, 23, 25, 27, 29, 32] # alle Klassenenden (inklusive)
standard_accuracy = 4
# -----------------------------------------------

def calculate_table(data, class_beginn, class_ends):
    n = len(data)
    c = len(class_ends)
    class_beginns = [class_beginn] + class_ends[:-1]
    frequency = [0] * c
    for value in data:
        for i in range(c):
            if class_beginns[i] < value <= class_ends[i]: # beginn exlusiv, end inclusiv
                frequency[i] += 1
                break
    class_widths = [class_ends[i] - class_beginns[i] for i in range(c)]
    class_mid = [class_beginns[i] + (class_widths[i] / 2) for i in range(c)]
    rel_fre = [frequency[i] / n for i in range(c)]
    rel_density = [rel_fre[i] / class_widths[i] for i in range(c)]
    return class_beginns, class_ends, class_widths, class_mid, frequency, rel_fre, rel_density, n

def calculate_stats(data):
    n = len(data)
    total = 0
    for value in data:
        total += value
    
    average = total / n

    emp_dev = 0 # empirical standard deviation
    for value in data:
        emp_dev += (value - average)**2
    
    emp_dev = (emp_dev / (n - 1)) ** (1/2) # important to use count-1

    return total, average, emp_dev, n

def calculate_boxplot_stats(data):
    data.sort()
    pos_q1 = len(data) // 4 -1
    pos_q2 = len(data) * 2 // 4 -1
    pos_q3 = len(data) * 3 // 4 -1
    quartil_1 = 0
    quartil_2 = 0
    quartil_3 = 0
    if len(data) % 4 == 0:
        quartil_1 = (data[pos_q1] + data[pos_q1+1]) / 2
        quartil_2 = (data[pos_q2] + data[pos_q2+1]) / 2
        quartil_3 = (data[pos_q3] + data[pos_q3+1]) / 2
    else:
        quartil_1 = data[pos_q1]
        quartil_2 = data[pos_q2]
        quartil_3 = data[pos_q3]


    iqa = quartil_3 - quartil_1 # Interquartilsabstand
    max_probe_length = iqa * 1.5 # Maximale Fühlerlänge
    min_probe_start = quartil_1 - max_probe_length
    max_probe_end = quartil_3 + max_probe_length
    probe_start = quartil_1
    probe_end = quartil_3
    
    outliers_sub_min = []
    outliers_above_max = []

    for value in data:
        if value < min_probe_start:
            outliers_sub_min.append(value)
        elif value > max_probe_end:
            outliers_above_max.append(value)
        elif min_probe_start <= value < quartil_1 and value < probe_start:
            probe_start = value
        elif max_probe_end >= value > quartil_3 and value > probe_end:
            probe_end = value

    return quartil_1, quartil_2, quartil_3, iqa, max_probe_length, probe_start, probe_end, outliers_sub_min, outliers_above_max

def text_table_output(class_beginns, class_ends, class_widths, class_mid, frequency, rel_fre, rel_density, n):
    title = "Histrogramm Tabelle"
    tableTitle = "| Klasse   | K.breite | K.mitte | abs. H | rel. H  | rel. H.Dichte |"
    print("=" * len(tableTitle))
    print(title)
    print("=" * len(tableTitle))
    print("Anz. =", n)
    print("-" * len(tableTitle))
    print(tableTitle)
    print("-" * len(tableTitle))
    for i in range(len(class_ends)):
        str_classes     = "]" + str(class_beginns[i]) + ";" + str(class_ends[i]) + "]"
        str_width       = str(class_widths[i])
        str_class_mid   = str(round(class_mid[i], standard_accuracy))
        str_fre         = str(frequency[i])
        str_rel_fre     = str(round(rel_fre[i], standard_accuracy + 1))
        str_rel_density = str(round(rel_density[i], standard_accuracy + 2))

        print(
            str_classes,
            "|",
            str_width,
            "|",
            str_class_mid,
            "|",
            str_fre,
            "|",
            str_rel_fre,
            "|",
            str_rel_density
        )

    print("=" * len(tableTitle))

def text_stats_output(sum, average, emp_dev, n):
    title = "Statistiken"
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print("Anzahl                           = ", n)
    print("Summe                            = ", round(sum, standard_accuracy))
    print("Arithmetisches Mittel            = ", round(average, standard_accuracy))
    print("Empirische Standardabweichung    = ", round(emp_dev, standard_accuracy))
    print("=" * len(title))

def text_boxplot_output(quartil_1, quartil_2, quartil_3, iqa, max_probe_length, probe_start, probe_end, outliers_sub_min, outliers_above_max):
    title = "Statistiken fuer Boxplot"
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print("1. Quartil               = ", round(quartil_1, standard_accuracy))
    print("2. Quratil/Median        = ", round(quartil_2, standard_accuracy))
    print("3. Quartil               = ", round(quartil_3, standard_accuracy))
    print("Interquatilabstand       = ", round(iqa, standard_accuracy))
    print("Maximale Fuehlerlaenge   = ", round(max_probe_length, standard_accuracy))
    print("Fuehlerstart             = ", round(probe_start, standard_accuracy))
    print("Fuehlerende              = ", round(probe_end, standard_accuracy))
    print("Ausreisser unter Fuehler : ", outliers_sub_min)
    print("Ausreisser ueber Fuehler : ", outliers_above_max)
    print("=" * len(title))  


# -----------------------------------------------
# HAUPTPROGRAMM
# -----------------------------------------------
data.sort() # wichtig, um für Statisiken
cb, ce, cw, cm, fr, rf, rd, n = calculate_table(data, class_beginn, class_ends)
text_table_output(cb, ce, cw, cm, fr, rf, rd, n)
sm, ag, ed, n = calculate_stats(data)
text_stats_output(sm, ag, ed, n)
q1, q2, q3, iqa, mp, ps, pe, qs, qa = calculate_boxplot_stats(data)
text_boxplot_output(q1, q2, q3, iqa, mp, ps, pe, qs, qa)
