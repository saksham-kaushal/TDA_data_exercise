import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

mjd = [57585.079220,
57586.081891,
57587.071763,
57588.067123,
57591.107611,
57594.062194,
57596.066012,
57603.135421,
57609.055383,
57617.059846,
57619.090142,
57621.120495,
57627.062642,
57629.125938,
57637.102795,
57644.994801,
57655.102315,
57659.120519]

airmass = [1.7258910,
1.6665240,
1.7491860,
1.7721150,
1.3530670,
1.6443790,
1.5562500,
1.1115970,
1.3717510,
1.2355820,
1.1156090,
1.0482370,
1.1306350,
1.0244450,
1.0250930,
1.1904340,
1.0329910,
1.0706010]

nova_mag_and_err = [(-8.06917,0.00554),
(-8.11788,0.00477),
(-7.78778,0.00655),
(-7.7492,0.00711),
(-7.01378,0.01582),
(-6.7958,0.01559),
(-6.22505,0.02621),
(-6.00348,0.00998),
(-5.19026,0.03097),
(-5.31643,0.04588),
(-4.58417,0.07163),
(0.351068,0.28434),
(-4.08713,0.03827),
(-3.75681,0.03747),
(-3.27988,0.05617),
(-3.37124,0.19267),
(-2.69049,0.10301),
(-1.99732,0.1288)]


stars_mag_and_err = [ [(-8.79153,0.00311),
(-9.08614,0.00228),
(-8.94943,0.00261),
(-9.06624,0.00248),
(-8.67234,0.00379),
(-8.76096,0.00302),
(-8.4437,0.0039),
(-8.78424,0.00191),
(-8.44701,0.00266),
(-9.07027,0.0021),
(-8.58765,0.00271),
(-7.62915,0.00734),
(-8.71743,0.00193),
(-8.40337,0.00228),
(-8.46164,0.00225),
(-8.81852,0.00219),
(-8.5127,0.00143),
(-8.08944,0.0018)]

, [(-8.19322,0.00501),
(-8.49188,0.00355),
(-8.34755,0.00414),
(-8.47205,0.00392),
(-8.0789,0.00621),
(-8.16958,0.00477),
(-7.86253,0.00628),
(-8.19902,0.00259),
(-7.86816,0.00381),
(-8.47533,0.00321),
(-8.00687,0.00403),
(-7.06545,0.01171),
(-8.13829,0.00256),
(-7.81135,0.00305),
(-7.89683,0.00291),
(-8.2141,0.00324),
(-7.91725,0.00196),
(-7.49395,0.00242)]

, [(-8.43167,0.00413),
(-8.72659,0.00296),
(-8.58463,0.00344),
(-8.70987,0.00324),
(-8.32961,0.00501),
(-8.41133,0.00394),
(-8.09466,0.00516),
(-8.44785,0.00226),
(-8.10531,0.00328),
(-8.72066,0.00267),
(-8.26852,0.00333),
(-7.29312,0.00969),
(-8.38544,0.00226),
(-8.07205,0.00267),
(-8.15279,0.00256),
(-8.4636,0.00275),
(-8.17252,0.0017),
(-7.76262,0.00208)]

, [(-6.81993,0.01639),
(-7.11721,0.01104),
(-6.95411,0.01345),
(-7.09267,0.1257),
(-6.72892,0.02037),
(-6.80057,0.01552),
(-6.45922,0.02131),
(-6.83937,0.00566),
(-6.48753,0.01046),
(-7.124,0.00931),
(-6.63258,0.01166),
(-5.63848,0.04075),
(-6.7756,0.00543),
(-6.45187,0.00618),
(-6.5255,0.00592),
(-6.86197,0.00885),
(-6.53396,0.00448),
(-6.09845,0.00533)]

, [(-9.23457,0.00222),
(-9.52156,0.00168),
(-9.37925,0.00192),
(-9.50961,0.0018),
(-9.10936,0.00268),
(-9.20142,0.00218),
(-8.86995,0.00281),
(-9.23819,0.00152),
(-8.89045,0.00205),
(-9.51246,0.00158),
(-9.03455,0.00204),
(-8.08902,0.00511),
(-9.16339,0.00156),
(-8.85114,0.00185),
(-8.93343,0.00178),
(-9.25069,0.00169),
(-8.95882,0.00114),
(-8.51768,0.00149)]]

r_error = np.array([0.0044,
0.0065,
0.0066,
0.0062,
0.0020])

g_error = np.array([0.0052,
0.0059,
0.0034,
0.0049,
0.0042])

phot_days_num 	= 18
stars_num 		= len(stars_mag_and_err)
mag_std 		= [16.194, 16.777, 16.525, 18.118, 15.731]
mag_std_err 	= r_error+g_error+0.004

z_mag 			= dict()
z_err 			= dict()
linearfit 		= dict()
linearfit_fn 	= dict()
linearfit_cov 	= dict()
linearfit_std 	= dict()
slope 			= dict()
z_mag_airmass_1 = dict()

nova_mag = [mag for (mag,err) in nova_mag_and_err]
nova_err = [err for (mag,err) in nova_mag_and_err]

for i in range(stars_num) :

	z_mag['star'+str(i+1)] 			= [mag_std[i]-mag_inst for (mag_inst,mag_inst_err) \
									in stars_mag_and_err[i]]

	z_err['star'+str(i+1)] 			= [mag_std_err[i]+mag_inst_err for (mag_inst,mag_inst_err) \
									in stars_mag_and_err[i]]

	linearfit['star'+str(i+1)], linearfit_cov['star'+str(i+1)] \
							  		= np.polyfit(airmass,z_mag['star'+str(i+1)],1,cov=True)

	linearfit_fn['star'+str(i+1)] 	= np.poly1d(linearfit['star'+str(i+1)])

	linearfit_std['star'+str(i+1)]	= np.sqrt(np.diag(linearfit_cov['star'+str(i+1)]))

	slope['star'+str(i+1)]			= (linearfit_fn['star'+str(i+1)](max(airmass))\
									-linearfit_fn['star'+str(i+1)](1.0))/(max(airmass)-1)

	z_mag_airmass_1['star'+str(i+1)]= linearfit_fn['star'+str(i+1)](1.00)

# print(np.diag(linearfit_cov['star1']))
# sns.set()
# for i in range(stars_num):
# 	print(slope['star'+str(i+1)])
# 	plt.scatter(airmass,z_mag['star'+str(i+1)])
# 	x=np.arange(1.0,max(airmass),0.001)
# 	plt.plot(x,linearfit_fn['star'+str(i+1)](x),'r')
# 	plt.show()

mag_star 		= dict()
mag_star_err 	= dict()
for i in range(stars_num):
	airmass_correction = np.array(slope['star'+str(i+1)]) * (np.array(airmass)-1)
	# print(slope['star'+str(i+1)])
	# print(airmass_correction)
	# print(z_mag_airmass_1['star'+str(i+1)])
	mag_star['star'+str(i+1)] = z_mag_airmass_1['star'+str(i+1)] + np.array(nova_mag)\
								- airmass_correction
	mag_star_err['star'+str(i+1)] = np.array(z_err['star'+str(i+1)]) + np.array(nova_err)

# for i in range(stars_num):
# 	for j in range(phot_days_num):
# 		print(f"{mag_star['star'+str(i+1)][j]:.5f}, {mag_star_err['star'+str(i+1)][j]:.5f}")
# 	print('\n')

app_mag_nova 		= list()
app_mag_err_nova 	= list()
for j in range(phot_days_num):
	total = 0
	sq_err=0
	for i in range(stars_num):
		total 	+= mag_star['star'+str(i+1)][j]
		sq_err 	+= (mag_star_err['star'+str(i+1)][j])**2
	mean = total/stars_num
	app_mag_nova.append(mean)
	app_mag_err_nova.append(np.sqrt(sq_err)/np.sqrt(stars_num))
	print(f"{app_mag_nova[j]:.5f}, {app_mag_err_nova[j]:.5f}")

sns.set()
plt.errorbar(x=mjd, y=app_mag_nova, fmt='o', yerr=app_mag_err_nova, markersize=3, capsize=3, ecolor='grey')
# plt.scatter(mjd, app_mag_nova,s=7)
plt.gca().invert_yaxis()
plt.show()

'''
Linear fit, followed by slope calculation. 
Plot of linear fit overlaid on scatter of Z with airmass.
All calculations for single secondary star.
'''
