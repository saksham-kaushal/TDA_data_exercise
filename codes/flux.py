import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 

c = 3e5

time = np.array([
2.48,
5.33,
10.44,
15.73,
30.23,
34.71,
43.55,
43.58,
48.19,
59.03])

wavelength = np.array([
7773,
6563,
4861,
4340,
4102])

o1_flux = np.array([
1.968e-13,
2.985e-14,
1.558e-14,
1.126e-14,
7.303e-15,
6.702e-15,
5.837e-15,
5.881e-15,
6.599e-15,
5.217e-15])

o1_flux_err = np.array([
0.019e-13,
0.030e-14,
0.019e-14,
0.016e-14,
0.351e-15,
0.411e-15,
0.534e-15,
1.159e-15,
1.156e-15,
1.526e-15])

halpha_flux = np.array([
4.959e-13,
2.755e-13,
1.704e-13,
1.271e-13,
8.415e-14,
7.874e-14,
7.238e-14,
7.259e-14,
7.073e-14,
6.777e-14])

halpha_flux_err = np.array([
0.026e-13,
0.013e-13,
0.009e-13,
0.007e-13,
0.066e-14,
0.057e-14,
0.054e-14,
0.061e-14,
0.061e-14,
0.061e-14])

hbeta_flux = np.array([
7.585e-14,
4.081e-14,
2.492e-14,
1.855e-14,
1.195e-14,
1.082e-14,
1.002e-14,
1.012e-14,
9.503e-15,
9.140e-15])

hbeta_flux_err = np.array([
0.074e-14,
0.060e-14,
0.043e-14,
0.037e-14,
0.031e-14,
0.029e-14,
0.027e-14,
0.032e-14,
0.313e-15,
0.270e-15])

hgamma_flux = np.array([
3.180e-14,
1.889e-14,
1.090e-14,
8.255e-15,
5.503e-15,
5.517e-15,
3.805e-15,
4.478e-15,
5.096e-15,
4.743e-15])

hgamma_flux_err = np.array([
0.043e-14,
0.045e-14,
0.024e-14,
0.203e-15,
0.388e-15,
0.427e-15,
0.464e-15,
0.297e-15,
0.630e-15,
0.382e-15])

hdelta_flux = np.array([
2.087e-14,
1.501e-14,
8.932e-15,
6.127e-15,
2.740e-15,
2.394e-15,
2.256e-15,
5.712e-15,
2.575e-15,
4.123e-15])

hdelta_flux_err = np.array([
0.032e-14,
0.045e-14,
0.290e-15,
0.205e-15,
0.407e-15,
0.817e-15,
4.815e-15,
6.099e-15,
1.085e-15,
6.909e-15])

o1_yerr 	= (o1_flux_err/o1_flux + o1_flux_err[0]/o1_flux[0])*o1_flux/o1_flux[0]
halpha_yerr 	= (halpha_flux_err/halpha_flux + halpha_flux_err[0]/halpha_flux[0])*halpha_flux/halpha_flux[0]
hbeta_yerr  	= (hbeta_flux_err/hbeta_flux + hbeta_flux_err[0]/hbeta_flux[0])*hbeta_flux/hbeta_flux[0]
hgamma_yerr 	= (hgamma_flux_err/hgamma_flux + hgamma_flux_err[0]/hgamma_flux[0])*hgamma_flux/hgamma_flux[0]
hdelta_yerr 	= (hdelta_flux_err/hdelta_flux + hdelta_flux_err[0]/hdelta_flux[0])*hdelta_flux/hdelta_flux[0]

sns.set(font_scale=0.85)
plt.errorbar(x=time, y=o1_flux/o1_flux[0], fmt='o', yerr=o1_yerr, markersize=4, capsize=5, label=r'O I (7773 $\mathrm{\AA}$)')
plt.errorbar(x=time, y=halpha_flux/halpha_flux[0], fmt='o', yerr=halpha_yerr, markersize=4, capsize=5, label=r'H $\alpha$ (6563 $\mathrm{\AA}$)')
plt.errorbar(x=time, y=hbeta_flux/hbeta_flux[0], fmt='o', yerr=hbeta_yerr, markersize=4, capsize=5, label=r'H $\beta$ (4861 $\mathrm{\AA}$)')
plt.errorbar(x=time, y=hgamma_flux/hgamma_flux[0], fmt='o', yerr=hgamma_yerr, markersize=4, capsize=5, label=r'H $\gamma$ (4340 $\mathrm{\AA}$)')
plt.errorbar(x=time, y=hdelta_flux/hdelta_flux[0], fmt='o', yerr=hdelta_yerr, markersize=4, capsize=5, label=r'H $\delta$ (4102 $\mathrm{\AA}$)')
plt.legend(title='Spectral Line')
plt.xlabel('Time since eruption (days)')
plt.ylabel('Flux Ratios')
plt.show()

plt.clf()
sns.set(font_scale=0.85)
plt.errorbar(x=np.log10(time), y=np.log10(o1_flux), fmt='o', yerr=o1_flux_err, markersize=4, capsize=5, label=r'O I (7773 $\mathrm{\AA}$)')
plt.errorbar(x=np.log10(time), y=np.log10(halpha_flux), fmt='o', yerr=halpha_flux_err, markersize=4, capsize=5, label=r'H $\alpha$ (6563 $\mathrm{\AA}$)')
plt.errorbar(x=np.log10(time), y=np.log10(hbeta_flux), fmt='o', yerr=hbeta_flux_err, markersize=4, capsize=5, label=r'H $\beta$ (4861 $\mathrm{\AA}$)')
plt.errorbar(x=np.log10(time), y=np.log10(hgamma_flux), fmt='o', yerr=hgamma_flux_err, markersize=4, capsize=5, label=r'H $\gamma$ (4340 $\mathrm{\AA}$)')
plt.errorbar(x=np.log10(time), y=np.log10(hdelta_flux), fmt='o', yerr=hdelta_flux_err, markersize=4, capsize=5, label=r'H $\delta$ (4102 $\mathrm{\AA}$)')
plt.legend(title='Spectral Line')
plt.xlabel('Time since eruption (days)')
plt.ylabel('Flux')
plt.show()