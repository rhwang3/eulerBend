# eulerBend

eulerBend takes in inputs and outputs your Euler bend of interest. 

# packages

This code requires scipy, numpy, datetime, matplotlib, and gdspy. The assignment specified either using KLayout or IPKISS; however, I could not obtain IPKISS because it is proprietary and in my opinion, gdspy has better documentation than the KLayout python API. If you would like to see this in IPKISS, I am waiting on an approval for a free trial license. 

# derivation 

Given the Euler bend can be described by the Fresnel integrals [1], we use the scipy.special.fresnel [2] to describe our bend of interest. However, note that the argument for the Fresnel integral in scipy is different than that from [1]. Therefore, we must scale the argument appropriately, which is done so in the function eulerBend. 

We also note that this Euler bend is not symmetric -- so, as recommended by [3] we calculate an Euler bend for half of the desired angle (let us call this 'Bend A'). We then make a copy of this structure, flip it across the y axis and rotate the flipped bend by the desired angle. We then shift this flipped and rotated structure ('Bend B') such that Bend B touches Bend A. We now have a completed Euler bend structure. 


[1] https://en.wikipedia.org/wiki/Euler_spiral#Formulation
[2] https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.fresnel.html
[3] Cherchi, M., Ylinen, S., Harjanne, M., Kapulainen, M., Vehmas, T., & Aalto, T. (2014). The Euler bend: Paving the way for High-density integration on Micron-scale Semiconductor platforms. Silicon Photonics IX. doi:10.1117/12.2039912
