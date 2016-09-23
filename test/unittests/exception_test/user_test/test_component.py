import unittest
from nineml.user.component import (Definition, DynamicsProperties, Component)
from nineml.utils.testing.comprehensive import instances_of_all_types
from nineml.exceptions import (NineMLUnitMismatchError, NineMLNameError, NineMLRuntimeError)


class TestDefinitionExceptions(unittest.TestCase):

    def test___init___ninemlruntimeerror(self):
        """
        line #: 35
        message: Cannot provide name, document or url arguments with explicit component class

        context:
        --------
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            BaseNineMLObject.__init__(self)
            self._referred_to = args[0]
            if kwargs:
        """

        definition = next(instances_of_all_types['Definition'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            definition.__init__)

    def test___init___ninemlruntimeerror2(self):
        """
        line #: 44
        message: Wrong number of arguments ({}), provided to Definition __init__, can either be one (the component class) or zero

        context:
        --------
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            BaseNineMLObject.__init__(self)
            self._referred_to = args[0]
            if kwargs:
                raise NineMLRuntimeError(
                    "Cannot provide name, document or url arguments with "
                    "explicit component class")
            self._url = None
        elif not args:
            super(Definition, self).__init__(
                name=kwargs['name'], document=kwargs['document'],
                url=kwargs['url'])
        else:
        """

        definition = next(instances_of_all_types['Definition'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            definition.__init__)

    def test_to_xml_ninemlruntimeerror(self):
        """
        line #: 61
        message: Cannot create reference for '{}' {} in the provided document due to name clash with existing {} object

        context:
        --------
    def to_xml(self, document, E=E, **kwargs):  # @UnusedVariable
        if self.url is None:
            # If definition was created in Python, add component class
            # reference to document argument before writing definition
            try:
                doc_obj = document[self._referred_to.name]
                if doc_obj != self._referred_to:
        """

        definition = next(instances_of_all_types['Definition'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            definition.to_xml,
            document=None,
            E=E)


class TestDynamicsPropertiesExceptions(unittest.TestCase):

    def test_check_initial_values_exception(self):
        """
        line #: 520
        message: BinOp(left=Str(s='Initial value not specified for %s'), op=Mod(), right=Attribute(value=Name(id='var', ctx=Load()), attr='name', ctx=Load()))

        context:
        --------
    def check_initial_values(self):
        for var in self.definition.component_class.state_variables:
            try:
                initial_value = self.initial_value(var.name)
            except KeyError:
        """

        dynamicsproperties = next(instances_of_all_types['DynamicsProperties'].itervalues())
        self.assertRaises(
            Exception,
            dynamicsproperties.check_initial_values)

    def test_check_initial_values_ninemlruntimeerror(self):
        """
        line #: 526
        message: Dimensions for '{}' initial value, {}, in '{}' don't match that of its definition in '{}', {}.

        context:
        --------
    def check_initial_values(self):
        for var in self.definition.component_class.state_variables:
            try:
                initial_value = self.initial_value(var.name)
            except KeyError:
                raise Exception("Initial value not specified for %s" %
                                var.name)
            initial_units = initial_value.units
            initial_dimension = initial_units.dimension
            var_dimension = var.dimension
            if initial_dimension != var_dimension:
        """

        dynamicsproperties = next(instances_of_all_types['DynamicsProperties'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            dynamicsproperties.check_initial_values)

    def test_initial_value_ninemlnameerror(self):
        """
        line #: 554
        message: No initial value named '{}' in component class

        context:
        --------
    def initial_value(self, name):
        try:
            return self._initial_values[name]
        except KeyError:
            try:
                return self.definition.component.initial_value(name)
            except AttributeError:
        """

        dynamicsproperties = next(instances_of_all_types['DynamicsProperties'].itervalues())
        self.assertRaises(
            NineMLNameError,
            dynamicsproperties.initial_value,
            name=None)

    def test_set_ninemlnameerror(self):
        """
        line #: 565
        message: '{}' Dynamics does not have a Parameter or StateVariable named '{}'

        context:
        --------
    def set(self, prop):
        try:
            super(DynamicsProperties, self).set(prop)
        except NineMLNameError:
            try:
                state_variable = self.component_class.state_variable(prop.name)
            except NineMLNameError:
        """

        dynamicsproperties = next(instances_of_all_types['DynamicsProperties'].itervalues())
        self.assertRaises(
            NineMLNameError,
            dynamicsproperties.set,
            prop=None)

    def test_set_ninemlunitmismatcherror(self):
        """
        line #: 569
        message: Dimensions for '{}' property ('{}') don't match that of component_class class ('{}').

        context:
        --------
    def set(self, prop):
        try:
            super(DynamicsProperties, self).set(prop)
        except NineMLNameError:
            try:
                state_variable = self.component_class.state_variable(prop.name)
            except NineMLNameError:
                raise NineMLNameError(
                    "'{}' Dynamics does not have a Parameter or StateVariable "
                    "named '{}'".format(self.component_class.name, prop.name))
            if prop.units.dimension != state_variable.dimension:
        """

        dynamicsproperties = next(instances_of_all_types['DynamicsProperties'].itervalues())
        self.assertRaises(
            NineMLUnitMismatchError,
            dynamicsproperties.set,
            prop=None)


class TestComponentExceptions(unittest.TestCase):

    def test___init___valueerror(self):
        """
        line #: 150
        message: 'definition' must be either a 'Definition' or 'Prototype' element

        context:
        --------
    def __init__(self, name, definition, properties={}, document=None):
        \"\"\"
        Create a new component_class with the given name, definition and
        properties, or create a prototype to another component_class that will
        be resolved later.
        \"\"\"
        ensure_valid_identifier(name)
        self._name = name
        BaseULObject.__init__(self)
        DocumentLevelObject.__init__(self, document)
        ContainerObject.__init__(self)
        if isinstance(definition, basestring):
            if "#" in definition:
                defn_url, name = definition.split("#")
            else:
                defn_url, name = definition, path.basename(
                    definition).replace(".xml", "")
            definition = Definition(
                name=name,
                document=document,
                url=defn_url)
        elif (isinstance(definition, ComponentClass) or
              definition.nineml_type in ('Dynamics', 'MultiDynamics')):
            definition = Definition(definition)
        elif (isinstance(definition, Component) or
              definition.nineml_type in ('DynamicsProperties',
                                         'MultiDynamicsProperties')):
            definition = Prototype(definition)
        elif definition.nineml_type not in ('Definition', 'Prototype'):
        """

        component = next(instances_of_all_types['Component'].itervalues())
        self.assertRaises(
            ValueError,
            component.__init__,
            name=None,
            definition=None,
            properties={},
            document=None)

    def test_set_ninemlunitmismatcherror(self):
        """
        line #: 201
        message: Dimensions for '{}' property ('{}') don't match that of component_class class ('{}').

        context:
        --------
    def set(self, prop):
        param = self.component_class.parameter(prop.name)
        if prop.units.dimension != param.dimension:
        """

        component = next(instances_of_all_types['Component'].itervalues())
        self.assertRaises(
            NineMLUnitMismatchError,
            component.set,
            prop=None)

    def test_check_properties_ninemlruntimeerror(self):
        """
        line #: 248
        message: . 

        context:
        --------
    def check_properties(self):
        # First check the names
        properties = set(self.property_names)
        parameters = set(self.component_class.parameter_names)
        msg = []
        diff_a = properties.difference(parameters)
        diff_b = parameters.difference(properties)
        if diff_a:
            msg.append("User properties of '{}' ({}) contain the following "
                       "parameters that are not present in the definition of "
                       "'{}' ({}): {}\n\n".format(
                           self.name, self.url, self.component_class.name,
                           self.component_class.url, ",".join(diff_a)))
        if diff_b:
            msg.append("Definition of '{}' ({}) contains the following "
                       "parameters that are not present in the user properties"
                       " of '{}' ({}): {}".format(
                           self.component_class.name, self.component_class.url,
                           self.name, self.url, ",".join(diff_b)))
        if msg:
            # need a more specific type of Exception
        """

        component = next(instances_of_all_types['Component'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            component.check_properties)

    def test_check_properties_ninemlruntimeerror2(self):
        """
        line #: 255
        message: Dimensions for '{}' property, {}, in '{}' don't match that of its definition in '{}', {}.

        context:
        --------
    def check_properties(self):
        # First check the names
        properties = set(self.property_names)
        parameters = set(self.component_class.parameter_names)
        msg = []
        diff_a = properties.difference(parameters)
        diff_b = parameters.difference(properties)
        if diff_a:
            msg.append("User properties of '{}' ({}) contain the following "
                       "parameters that are not present in the definition of "
                       "'{}' ({}): {}\n\n".format(
                           self.name, self.url, self.component_class.name,
                           self.component_class.url, ",".join(diff_a)))
        if diff_b:
            msg.append("Definition of '{}' ({}) contains the following "
                       "parameters that are not present in the user properties"
                       " of '{}' ({}): {}".format(
                           self.component_class.name, self.component_class.url,
                           self.name, self.url, ",".join(diff_b)))
        if msg:
            # need a more specific type of Exception
            raise NineMLRuntimeError(". ".join(msg))
        # Check dimensions match
        for param in self.component_class.parameters:
            prop_units = self.property(param.name).units
            prop_dimension = prop_units.dimension
            param_dimension = param.dimension
            if prop_dimension != param_dimension:
        """

        component = next(instances_of_all_types['Component'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            component.check_properties)

    def test_property_ninemlnameerror(self):
        """
        line #: 380
        message: No property named '{}' in component class

        context:
        --------
    def property(self, name):
        try:
            return self._properties[name]
        except KeyError:
            try:
                return self.definition.component.property(name)
            except AttributeError:
        """

        component = next(instances_of_all_types['Component'].itervalues())
        self.assertRaises(
            NineMLNameError,
            component.property,
            name=None)

