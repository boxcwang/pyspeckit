"""
===========
NH2D fitter: ortho- and para- in the same file, but not modeled together
===========
Reference for line params:

F. Daniel et al. (2016) line frequencies and line strengths.
It includes HFS due to D

"""
import hyperfine
import astropy.units as u

freq_dict_cen ={
                'o-1_01-1_11':  85.926263e9,
                'p-1_01-1_11': 110.153599e9,
                'o-1_01-0_00': 332.82251e9,
                'p-1_01-0_00': 332.78189e9,
               }

freq_dict={
    ####### ortho-NH2D J=1_01-1_11
    'o-1_01-1_11_01': 85.924692e9,
    'o-1_01-1_11_02': 85.924750e9,
    'o-1_01-1_11_03': 85.924782e9,
    'o-1_01-1_11_04': 85.925274e9,
    'o-1_01-1_11_05': 85.925371e9,
    'o-1_01-1_11_06': 85.925643e9,
    'o-1_01-1_11_07': 85.925662e9,
    'o-1_01-1_11_08': 85.925688e9,
    'o-1_01-1_11_09': 85.925694e9,
    'o-1_01-1_11_10': 85.925701e9,
    'o-1_01-1_11_11': 85.925733e9,
    'o-1_01-1_11_12': 85.926187e9,
    'o-1_01-1_11_13': 85.926188e9,
    'o-1_01-1_11_14': 85.926213e9,
    'o-1_01-1_11_15': 85.926226e9,
    'o-1_01-1_11_16': 85.926243e9,
    'o-1_01-1_11_17': 85.926245e9,
    'o-1_01-1_11_18': 85.926271e9,
    'o-1_01-1_11_19': 85.926282e9,
    'o-1_01-1_11_20': 85.926284e9,
    'o-1_01-1_11_21': 85.926289e9,
    'o-1_01-1_11_22': 85.926301e9,
    'o-1_01-1_11_23': 85.926315e9,
    'o-1_01-1_11_24': 85.926323e9,
    'o-1_01-1_11_25': 85.926333e9,
    'o-1_01-1_11_26': 85.926807e9,
    'o-1_01-1_11_27': 85.926826e9,
    'o-1_01-1_11_28': 85.926865e9,
    'o-1_01-1_11_29': 85.926878e9,
    'o-1_01-1_11_30': 85.926904e9,
    'o-1_01-1_11_31': 85.926923e9,
    'o-1_01-1_11_32': 85.927101e9,
    'o-1_01-1_11_33': 85.927140e9,
    'o-1_01-1_11_34': 85.927695e9,
    'o-1_01-1_11_35': 85.927721e9,
    'o-1_01-1_11_36': 85.927740e9,
    ####### ortho-NH2D J=1_01-0_00
    'o-1_01-0_00_01': 332.780878e9,
    'o-1_01-0_00_02': 332.780878e9,
    'o-1_01-0_00_03': 332.780878e9,
    'o-1_01-0_00_04': 332.781695e9,
    'o-1_01-0_00_05': 332.781695e9,
    'o-1_01-0_00_06': 332.781695e9,
    'o-1_01-0_00_07': 332.781734e9,
    'o-1_01-0_00_08': 332.781792e9,
    'o-1_01-0_00_09': 332.781792e9,
    'o-1_01-0_00_10': 332.782285e9,
    'o-1_01-0_00_11': 332.782285e9,
    'o-1_01-0_00_12': 332.782285e9,
    'o-1_01-0_00_13': 332.782317e9,
    'o-1_01-0_00_14': 332.782317e9,
    'o-1_01-0_00_15': 332.782375e9,
    ####### para-NH2D J=1_01-1_11
    'p-1_01-1_11_01': 110.151981e9,
    'p-1_01-1_11_02': 110.152039e9,
    'p-1_01-1_11_03': 110.152072e9,
    'p-1_01-1_11_04': 110.152566e9,
    'p-1_01-1_11_05': 110.152664e9,
    'p-1_01-1_11_06': 110.152933e9,
    'p-1_01-1_11_07': 110.152952e9,
    'p-1_01-1_11_08': 110.152978e9,
    'p-1_01-1_11_09': 110.152984e9,
    'p-1_01-1_11_10': 110.152991e9,
    'p-1_01-1_11_11': 110.153023e9,
    'p-1_01-1_11_12': 110.153479e9,
    'p-1_01-1_11_13': 110.153484e9,
    'p-1_01-1_11_14': 110.153505e9,
    'p-1_01-1_11_15': 110.153518e9,
    'p-1_01-1_11_16': 110.153533e9,
    'p-1_01-1_11_17': 110.153537e9,
    'p-1_01-1_11_18': 110.153563e9,
    'p-1_01-1_11_19': 110.153572e9,
    'p-1_01-1_11_20': 110.153577e9,
    'p-1_01-1_11_21': 110.153578e9,
    'p-1_01-1_11_22': 110.153591e9,
    'p-1_01-1_11_23': 110.153605e9,
    'p-1_01-1_11_24': 110.153616e9,
    'p-1_01-1_11_25': 110.153623e9,
    'p-1_01-1_11_26': 110.154099e9,
    'p-1_01-1_11_27': 110.154118e9,
    'p-1_01-1_11_28': 110.154157e9,
    'p-1_01-1_11_29': 110.154171e9,
    'p-1_01-1_11_30': 110.154197e9,
    'p-1_01-1_11_31': 110.154216e9,
    'p-1_01-1_11_32': 110.154397e9,
    'p-1_01-1_11_33': 110.154436e9,
    'p-1_01-1_11_34': 110.154991e9,
    'p-1_01-1_11_35': 110.155017e9,
    'p-1_01-1_11_36': 110.155036e9,
    ####### para-NH2D J=1_01-0_00
    'p-1_01-0_00_01': 332.821618e9,
    'p-1_01-0_00_02': 332.821618e9,
    'p-1_01-0_00_03': 332.821618e9,
    'p-1_01-0_00_04': 332.822438e9,
    'p-1_01-0_00_05': 332.822438e9,
    'p-1_01-0_00_06': 332.822438e9,
    'p-1_01-0_00_07': 332.822478e9,
    'p-1_01-0_00_08': 332.822536e9,
    'p-1_01-0_00_09': 332.822536e9,
    'p-1_01-0_00_10': 332.823031e9,
    'p-1_01-0_00_11': 332.823031e9,
    'p-1_01-0_00_12': 332.823031e9,
    'p-1_01-0_00_13': 332.823063e9,
    'p-1_01-0_00_14': 332.823063e9,
    'p-1_01-0_00_15': 332.823121e9,
    }


line_strength_dict = {
    ####### ortho-NH2D J=1_01-1_11
    'o-1_01-1_11_01': 9.24e-7,
    'o-1_01-1_11_02': 4.37e-6,
    'o-1_01-1_11_03': 2.51e-6,
    'o-1_01-1_11_04': 1.12e-8,
    'o-1_01-1_11_05': 2.44e-8,
    'o-1_01-1_11_06': 1.13e-6,
    'o-1_01-1_11_07': 7.44e-7,
    'o-1_01-1_11_08': 1.80e-6,
    'o-1_01-1_11_09': 1.72e-6,
    'o-1_01-1_11_10': 4.54e-8,
    'o-1_01-1_11_11': 3.92e-7,
    'o-1_01-1_11_12': 3.94e-6,
    'o-1_01-1_11_13': 1.11e-11,
    'o-1_01-1_11_14': 8.09e-7,
    'o-1_01-1_11_15': 1.65e-6,
    'o-1_01-1_11_16': 5.63e-7,
    'o-1_01-1_11_17': 8.40e-7,
    'o-1_01-1_11_18': 5.23e-6,
    'o-1_01-1_11_19': 1.53e-6,
    'o-1_01-1_11_20': 6.03e-7,
    'o-1_01-1_11_21': 2.68e-6,
    'o-1_01-1_11_22': 6.59e-7,
    'o-1_01-1_11_23': 4.79e-7,
    'o-1_01-1_11_24': 4.62e-6,
    'o-1_01-1_11_25': 3.82e-7,
    'o-1_01-1_11_26': 3.26e-7,
    'o-1_01-1_11_27': 2.41e-6,
    'o-1_01-1_11_28': 2.82e-6,
    'o-1_01-1_11_29': 2.95e-6,
    'o-1_01-1_11_30': 1.38e-7,
    'o-1_01-1_11_31': 9.77e-7,
    'o-1_01-1_11_32': 6.50e-10,
    'o-1_01-1_11_33': 4.09e-9,
    'o-1_01-1_11_34': 2.21e-6,
    'o-1_01-1_11_35': 2.55e-6,
    'o-1_01-1_11_36': 2.85e-6,
    ####### ortho-NH2D J=1_01-0_00
    'o-1_01-0_00_01': 4.62e-6,
    'o-1_01-0_00_02': 2.29e-6,
    'o-1_01-0_00_03': 1.23e-6,
    'o-1_01-0_00_04': 4.96e-9,
    'o-1_01-0_00_05': 3.07e-6,
    'o-1_01-0_00_06': 5.07e-6,
    'o-1_01-0_00_07': 8.14e-6,
    'o-1_01-0_00_08': 2.52e-6,
    'o-1_01-0_00_09': 5.62e-6,
    'o-1_01-0_00_10': 2.78e-6,
    'o-1_01-0_00_11': 3.52e-6,
    'o-1_01-0_00_12': 1.84e-6,
    'o-1_01-0_00_13': 2.52e-6,
    'o-1_01-0_00_14': 5.62e-6,
    'o-1_01-0_00_15': 8.14e-6,
    ####### para-NH2D J=1_01-1_11
    'p-1_01-1_11_01': 1.95e-6,
    'p-1_01-1_11_02': 9.21e-6,
    'p-1_01-1_11_03': 5.30e-6,
    'p-1_01-1_11_04': 2.36e-8,
    'p-1_01-1_11_05': 5.15e-8,
    'p-1_01-1_11_06': 2.38e-6,
    'p-1_01-1_11_07': 1.57e-6,
    'p-1_01-1_11_08': 3.81e-6,
    'p-1_01-1_11_09': 3.62e-6,
    'p-1_01-1_11_10': 9.57e-8,
    'p-1_01-1_11_11': 8.29e-7,
    'p-1_01-1_11_12': 8.30e-6,
    'p-1_01-1_11_13': 2.34e-11,
    'p-1_01-1_11_14': 1.71e-6,
    'p-1_01-1_11_15': 3.49e-6,
    'p-1_01-1_11_16': 1.19e-6,
    'p-1_01-1_11_17': 1.77e-6,
    'p-1_01-1_11_18': 1.10e-5,
    'p-1_01-1_11_19': 3.22e-6,
    'p-1_01-1_11_20': 1.27e-6,
    'p-1_01-1_11_21': 5.65e-6,
    'p-1_01-1_11_22': 1.39e-6,
    'p-1_01-1_11_23': 1.01e-6,
    'p-1_01-1_11_24': 9.75e-6,
    'p-1_01-1_11_25': 8.05e-7,
    'p-1_01-1_11_26': 6.87e-7,
    'p-1_01-1_11_27': 5.09e-6,
    'p-1_01-1_11_28': 5.95e-6,
    'p-1_01-1_11_29': 6.23e-6,
    'p-1_01-1_11_30': 2.90e-7,
    'p-1_01-1_11_31': 2.06e-6,
    'p-1_01-1_11_32': 1.37e-9,
    'p-1_01-1_11_33': 8.61e-9,
    'p-1_01-1_11_34': 4.66e-6,
    'p-1_01-1_11_35': 5.38e-6,
    'p-1_01-1_11_36': 6.01e-6,
    ####### para-NH2D J=1_01-0_00
    'p-1_01-0_00_01': 4.31e-6,
    'p-1_01-0_00_02': 2.14e-6,
    'p-1_01-0_00_03': 1.15e-6,
    'p-1_01-0_00_04': 4.66e-9,
    'p-1_01-0_00_05': 2.86e-6,
    'p-1_01-0_00_06': 4.73e-6,
    'p-1_01-0_00_07': 7.60e-6,
    'p-1_01-0_00_08': 2.35e-6,
    'p-1_01-0_00_09': 5.24e-6,
    'p-1_01-0_00_10': 2.60e-6,
    'p-1_01-0_00_11': 3.29e-6,
    'p-1_01-0_00_12': 1.72e-6,
    'p-1_01-0_00_13': 2.35e-6,
    'p-1_01-0_00_14': 5.24e-6,
    'p-1_01-0_00_15': 7.60e-6,
}

# freq_dict = {
#     'J2-1': (voff_lines_dict['J2-1']*u.km/u.s).to(u.GHz, equivalencies=u.doppler_radio(freq_dict_cen['J2-1']*u.Hz)).value,
#     'J3-2': (voff_lines_dict['J3-2']*u.km/u.s).to(u.GHz, equivalencies=u.doppler_radio(freq_dict_cen['J3-2']*u.Hz)).value,
# }
# Get offset velocity dictionary in km/s based on the lines frequencies and rest frequency
conv_o1_1=u.doppler_radio(freq_dict_cen['o-1_01-1_11']*u.Hz)
conv_p1_1=u.doppler_radio(freq_dict_cen['p-1_01-1_11']*u.Hz)
conv_o1_0=u.doppler_radio(freq_dict_cen['o-1_01-0_00']*u.Hz)
conv_p1_0=u.doppler_radio(freq_dict_cen['p-1_01-0_00']*u.Hz)

voff_lines_dict = {
    name: ((freq_dict[name]*u.Hz).to(u.km/u.s, equivalencies=conv_o1_1).value) for name in freq_dict.keys() if "o-1_01-1_11" in name
    }
voff_lines_dict.update({
	name: ((freq_dict[name]*u.Hz).to(u.km/u.s, equivalencies=conv_p1_1).value) for name in freq_dict.keys() if "p-1_01-1_11" in name
    })
voff_lines_dict.update({
	name: ((freq_dict[name]*u.Hz).to(u.km/u.s, equivalencies=conv_p1_1).value) for name in freq_dict.keys() if "o-1_01-0_00" in name
    })
voff_lines_dict.update({
	name: ((freq_dict[name]*u.Hz).to(u.km/u.s, equivalencies=conv_p1_1).value) for name in freq_dict.keys() if "p-1_01-0_00" in name
    })

# I don't know yet how to use this parameter... in CLASS it does not exist
# Note to Jaime: this is the sum of the degeneracy values for all hyperfines
# for a given line; it gives the relative weights between the J=2-1 and J=3-2
# lines, for example (the hyperfine weights are treated as normalized within
# one rotational transition)
wo1_1 = sum(val for name,val in line_strength_dict.items() if 'o-1_01-1_11' in name)
wp1_1 = sum(val for name,val in line_strength_dict.items() if 'p-1_01-1_11' in name)
wo1_0 = sum(val for name,val in line_strength_dict.items() if 'o-1_01-0_00' in name)
wp1_0 = sum(val for name,val in line_strength_dict.items() if 'p-1_01-0_00' in name)
relative_strength_total_degeneracy = {
    name : wo1_1 for name  in line_strength_dict.keys() if "o-1_01-1_11" in name
    }
relative_strength_total_degeneracy.update({
    name : wp1_1 for name  in line_strength_dict.keys() if "p-1_01-1_11" in name
    })
relative_strength_total_degeneracy.update({
    name : wo1_0 for name  in line_strength_dict.keys() if "o-1_01-0_00" in name
    })
relative_strength_total_degeneracy.update({
    name : wp1_0 for name  in line_strength_dict.keys() if "p-1_01-0_00" in name
    })
# Get the list of line names from the previous lists
line_names = [name for name in voff_lines_dict.keys()]

nh2d_vtau = hyperfine.hyperfinemodel(line_names, voff_lines_dict, freq_dict,
                                     line_strength_dict,
                                     relative_strength_total_degeneracy)
nh2d_vtau_fitter = nh2d_vtau.fitter
nh2d_vtau_vheight_fitter = nh2d_vtau.vheight_fitter
nh2d_vtau_tbg_fitter = nh2d_vtau.background_fitter
