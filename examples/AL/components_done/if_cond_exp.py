"""
A composite leaky integrate-and-fire with conductance-based, exponential
synapses, like the IF_cond_exp standard cell model in PyNN

"""

import nineml.abstraction_layer as al

def get_component():
    regimes = [
        al.Regime(
            name = "sub-threshold-regime",
            time_derivatives = [
                "dV/dt = (v_rest - V)/tau_m + (gE*(e_rev_E - V) + gI*(e_rev_I - V) + i_offset)/cm",
                "dgE/dt = -gE/tau_syn_E",
                "dgI/dt = -gI/tau_syn_I",],
            transitions = (al.On("V > v_thresh",
                                     do=["t_spike = t",
                                         "V = v_reset",
                                         al.OutputEvent('spikeoutput')],
                                     to="refractory-regime"),
                           al.On('excitatory', do="gE=gE+q"),
                           al.On('inhibitory', do="gI=gI+q"),
                          ),
        ),
        al.Regime(
            name = "refractory-regime",
            time_derivatives = [
                "dgE/dt = -gE/tau_syn_E",
                "dgI/dt = -gI/tau_syn_I",],
            transitions = (al.On("t >= t_spike + tau_refrac", to="sub-threshold-regime"),
                           al.On('excitatoryspike', do="gE=gE+q"),
                           al.On('inhibitoryspike', do="gI=gI+q"),
                           ),
        )]


    analog_ports = [al.SendPort("V"), al.SendPort("gE"), al.SendPort("gI"),
             al.RecvPort("q")]

    c1 = al.ComponentClass("IF_cond_exp", regimes=regimes, analog_ports=analog_ports)
    return c1

