import math

R2 = 45
r2 = 38
R3 = 115
r3 = 94
def main(t):
    S1 = 40+98*(t**2)
    V1 = 196 * t * 10**(-3)
    a1 = 0.196
    w2 = V1/(r2*10**(-3))
    e2 = a1/(r2*10**(-3))
    Vb = w2*(R2*10**(-3))
    ab = e2*(R2*10**(-2))
    w3 = Vb/(r3*10**(-3))
    e3 = ab/(r3*10**(-3))
    Vm = w3*(R3*10**(-3))
    am1 = e3*(R3*10**(-3))
    anm = Vm**2/(R3*10**(-3))
    am2 = math.sqrt(anm**2 + am1**2)

    # print(f'S1 = {S1}\nV1 = {V1}\na1 = {a1}\nw2 = {w2}\ne2 = {e2}\nVb = {Vb}\nab = {ab}'
    #       f'\nw3 = {w3}\ne3 = {e3}\nVm = {Vm}\nam1 = {am1}\nanm = {anm}\nam2 = {am2}')

    answer = (f'В момент времени t = {t}с:\n'
          f'путь = {S1}мм\n'
          f'нормальное ускорение = {anm}\n'
          f'тангенциальное ускорение = {am1}\n'
          f'полное ускорение = {am2}\n')

    return [S1, anm, am1, am2 ,answer]

print('формула: y1 = 40 + 98t^2')
print('R2 = 45, r2 = 38, R3 = 115, r3 = 94')
print()

from PIL import Image
img = Image.open('img.png')
img.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = {'секунда':[], 'путь':[],'нормальное ускорение':[], 'тангенсальное ускорение':[], 'полное ускорение':[] }

for i in range(1,100):
    df['секунда'].append(i)
    df['путь'].append(main(i)[0])
    df['нормальное ускорение'].append(main(i)[1])
    df['тангенсальное ускорение'].append(main(i)[2])
    df['полное ускорение'].append(main(i)[3])
df = pd.DataFrame(df)

print(df.to_string())
sns.pairplot(data = df, y_vars=["путь", "нормальное ускорение", "тангенсальное ускорение", "полное ускорение"], x_vars=["секунда"])
sns.pairplot(data = df, corner=True)

plt.show()

