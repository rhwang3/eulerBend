# eulerBend

eulerBend takes in inputs and outputs your Euler bend of interest. 

# packages

This code requires scipy, numpy, datetime, matplotlib, and gdspy. The assignment specified either using KLayout or IPKISS; however, I could not obtain IPKISS because it is proprietary and in my opinion, gdspy has better documentation than the KLayout python API. If you would like to see this in IPKISS, I am waiting on an approval for a free trial license. 

# derivation 

Given the Euler bend can be described by the Fresnel integrals, [1]..... we use the scipy.special.fresnel [2] to describe our bend of interest. However, note that the argument for the Fresnel integral in scipy is different than that from [1]. Therefore, we must scale the argument appropriately, which is done so in the function eulerBend. 

We also note that this Euler bend is not symmetric [3, that paper on EB symmetry]. So, in our second iteration of designing the Euler bend function, we try a slightly modified approach. 
