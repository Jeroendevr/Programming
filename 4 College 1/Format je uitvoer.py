__author__ = 'jeroendevries'
naam = ['jan', 'achmed', 'alice', 'mohammed', 'truus', 'eva', 'matthijs', 'marleen']
salaris = [900, 1300, 3000, 4100, 3400, 5000, 2800, 10000]
z = 0
for name in naam:
    print('Salaris: {1:8d} Naam: {0:8s}'.format(name, salaris[z]))
    z += 1