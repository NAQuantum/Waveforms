import sys
get_ipython().system("{sys.executable} -m pip install lalsuite=='6.48.1.dev20180620' pycbc")
from pycbc.waveform import get_td_waveform
import pylab

event = '150914' # Date of event

wavedata = {'150914':(35.6,30.6,430),'151012':(23.3,13.6,1060),'151226':(13.7,7.7,440),'170104':(31.0,20.1,960),
            '170608':(10.9,7.6,320),'170729':(50.6,34.3,2750),'170809':(35.2,23.8,990),'170814':(30.7,25.3,580),
           '170817':(1.46,1.27,40),'170818':(35.5,26.8,1020),'170823':(39.6,29.4,1850)}
(m1,m2,dist)=wavedata[event]
hp, hc = get_td_waveform(approximant="SEOBNRv4_opt",
                         mass1=m1,
                         mass2=m2,
                         delta_t=1.0/4096,
                         f_lower=10,
                        distance=dist)
pylab.plot(hp.sample_times, hp, label='Plus Polarization')
pylab.plot(hp.sample_times, hc, label='Cross Polarization')
pylab.xlabel('Time (s)')
pylab.legend()
pylab.grid()
pylab.show()

