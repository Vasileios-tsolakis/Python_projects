import random

print("Στο σημερινό παιχνίδι πρέπει να μαντέψεις ένα τυχαίο αριθμό μεταξύ του 1 και του 100. '\n' Αν θές να παραιτηθείς γράψε stop")

r1= random.randint(1, 100)
tries = 0
while answer != "stop" :
    try:
        answer = int(input('Μάντεψε τον αριθμό μεταξύ 1 και 100\n'))
        if 1 <= answer <= 100:
            break
        raise ValueError()
    except ValueError:
        if(answer!= 'stop'):
            print("Παρακαλώ επιλέξτε ένα ακέραιο αριθμό μεταξύ 1 και 100!!!\n")
    try:
        print ('hi')

if r1 == answer:
    print("Συηχαρητήρια μάντεξες τον σωστό αριθμό\n")
    tries += 1
else:
    while r1:
        if answer>r1:
            print("Ο κρυμμένος αριθμός είναι μικρότερος\n")
            tries +=1
            while True:
                try:
                    answer = int(input('Μάντεψε τον αριθμό μεταξύ 1 και 100\n'))
                    if 1 <= answer <= 100:
                        break
                    raise ValueError()
                except ValueError:
                    print("Παρακαλώ επιλέξτε ένα ακέραιο αριθμό μεταξύ 1 και 100!!!\n")
        if answer<r1:
            print("Ο κρυμμένος αριθμός είναι μεγαλύτερος\n")
            tries += 1
            while True:
                try:
                    answer = int(input('Μάντεψε τον αριθμό μεταξύ 1 και 100\n'))
                    if 1 <= answer <= 100:
                        break
                    raise ValueError()
                except ValueError:
                    print("Παρακαλώ επιλέξτε ένα ακέραιο αριθμό μεταξύ 1 και 100!!!\n")
        else:
            print("Συγχαρητήρια μάντεψες τον σωστό αριθμό!!!!\n")
            break
    Grade= 100-10*tries
    if Grade>0:
        print("Οι προσπάθειες σου ήταν:",tries,"και η βαθμολογία σου ήταν", Grade)
    else:
        print("Οι προσπάθειες σου ήταν:",tries,"και η βαθμολογία σου ήταν 0", )


