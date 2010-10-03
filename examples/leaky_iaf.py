import nineml.abstraction_layer as nineml


parameters = ["V", "t", "spike", "Isyn", "subthreshold", "refractory_end", "gL",
              "vL", "theta", "Vreset", "C", "trefractory", "tspike"]

subthreshold_regime = nineml.Sequence(
    nineml.ODE("V", "t", "(-gL*(V-vL) + Isyn)/C"),
    nineml.Assignment("spike", "V > theta")
    )


refractory_regime = nineml.Union(
    nineml.Assignment("V", "Vreset"),
    nineml.Assignment("refractory_end", "t >= tspike + trefractory")
    )

tspike_assignment = nineml.Assignment("tspike", "t")
spike_transition = nineml.Transition(subthreshold_regime,
                                     refractory_regime,
                                     "spike",
                                     tspike_assignment)

subthreshold_transition = nineml.Transition(refractory_regime,
                                            subthreshold_regime,
                                            "refractory_end")

c1 = nineml.Component("LeakyIAF", parameters,
                             transitions=(spike_transition, subthreshold_transition))


# write to file object f if defined
try:
    # This case is used in the test suite for examples.
    c1.write(f)
except NameError:
    c1.write("leaky_iaf.xml")
    c2 = parse("leaky_iaf.xml")
    assert c1==c2
