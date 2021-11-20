from pybmrb import Spectra, Histogram

import plotly.io as pio
pio.renderers.default = "browser"

peak_list=Spectra.n15hsqc(bmrb_ids=15060, legend='residue')

peak_list=Spectra.c13hsqc(bmrb_ids=15060, legend='residue')

peak_list=Spectra.tocsy(bmrb_ids=15060, legend='residue')