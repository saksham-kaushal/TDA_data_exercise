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

o1_fwhm = np.array([
78.714,
54.016,
40.734,
34.328,
27.558,
28.294,
27.210,
27.340,
33.103,
25.836])

o1_fwhm_err = np.array([
0.634,
0.461,
0.431,
0.425,
1.143,
1.528,
2.297,
5.240,
5.612,
7.491])

halpha_fwhm = np.array([
51.444,
34.377,
25.816,
21.706,
18.785,
18.681,
18.759,
18.760,
18.822,
18.884])

halpha_fwhm_err = np.array([
0.219,
0.129,
0.107,
0.097,
0.120,
0.110,
0.114,
0.129,
0.133,
0.138])

hbeta_fwhm = np.array([
47.185,
32.503,
24.359,
20.642,
17.328,
16.260,
16.619,
16.319,
16.453,
16.123])

hbeta_fwhm_err = np.array([
0.393,
0.395,
0.347,
0.335,
0.367,
0.368,
0.381,
0.445,
0.458,
0.404])

hgamma_fwhm = np.array([
51.671,
40.518,
27.682,
24.232,
21.666,
22.766,
15.875,
19.282,
23.854,
23.214])

hgamma_fwhm_err = np.array([
0.620,
0.826,
0.525,
0.518,
1.342,
1.578,
1.816,
1.116,
2.776,
1.677])

hdelta_fwhm = np.array([
51.791,
46.489,
33.247,
25.271,
12.441,
12.364,
12.843,
34.943,
15.605,
8.028,])

hdelta_fwhm_err = np.array([
0.723,
1.218,
0.947,
0.750,
1.722,
4.088,
27.378,
37.214,
6.468,
33.176])

sns.set(font_scale=0.85)
plt.errorbar(x=time, y=o1_fwhm*c/wavelength[0], fmt='o', yerr=o1_fwhm_err*c/wavelength[0], markersize=4, capsize=5, label=r'O I (7773 $\mathrm{\AA}$)')
plt.errorbar(x=time, y=halpha_fwhm*c/wavelength[1], fmt='o', yerr=halpha_fwhm_err*c/wavelength[1], markersize=4, capsize=5, label=r'H $\alpha$ (6563 $\mathrm{\AA}$)')
plt.errorbar(x=time, y=hbeta_fwhm*c/wavelength[2], fmt='o', yerr=hbeta_fwhm_err*c/wavelength[2], markersize=4, capsize=5, label=r'H $\beta$ (4861 $\mathrm{\AA}$)')
plt.errorbar(x=time, y=hgamma_fwhm*c/wavelength[3], fmt='o', yerr=hgamma_fwhm_err*c/wavelength[3], markersize=4, capsize=5, label=r'H $\gamma$ (4340 $\mathrm{\AA}$)')
plt.errorbar(x=time, y=hdelta_fwhm*c/wavelength[4], fmt='o', yerr=hdelta_fwhm_err*c/wavelength[4], markersize=4, capsize=5, label=r'H $\delta$ (4102 $\mathrm{\AA}$)')
plt.legend(title='Spectral Line')
plt.xlabel('Time since eruption (days)')
plt.ylabel('FWHM (km/s)')
# plt.show()
plt.savefig('./plots/line_width_evolution_kmps.png', dpi=550,bbox_inches='tight')

plt.clf()
sns.set(font_scale=0.85)
plt.errorbar(x=np.log10(time), y=np.log10(o1_fwhm), fmt='o', yerr=o1_fwhm_err, markersize=4, capsize=5, label=r'O I (7773 $\mathrm{\AA}$)')
plt.errorbar(x=np.log10(time), y=np.log10(halpha_fwhm), fmt='o', yerr=halpha_fwhm_err, markersize=4, capsize=5, label=r'H $\alpha$ (6563 $\mathrm{\AA}$)')
plt.errorbar(x=np.log10(time), y=np.log10(hbeta_fwhm), fmt='o', yerr=hbeta_fwhm_err, markersize=4, capsize=5, label=r'H $\beta$ (4861 $\mathrm{\AA}$)')
plt.errorbar(x=np.log10(time), y=np.log10(hgamma_fwhm), fmt='o', yerr=hgamma_fwhm_err, markersize=4, capsize=5, label=r'H $\gamma$ (4340 $\mathrm{\AA}$)')
plt.errorbar(x=np.log10(time), y=np.log10(hdelta_fwhm), fmt='o', yerr=hdelta_fwhm_err, markersize=4, capsize=5, label=r'H $\delta$ (4102 $\mathrm{\AA}$)')
plt.legend(title='Spectral Line')
plt.xlabel('Time since eruption (days)')
plt.ylabel(r'FWHM ($\AA$)')
# plt.show()
plt.savefig('./plots/line_width_evolution_angstrom.png', dpi=550,bbox_inches='tight')
