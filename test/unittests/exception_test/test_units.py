import unittest
from nineml.units import (Dimension, Unit, Quantity)
from nineml.utils.testing.comprehensive import instances_of_all_types
from nineml.exceptions import (NineMLDimensionError, NineMLNameError, NineMLRuntimeError)


class TestDimensionExceptions(unittest.TestCase):

    def test_from_sympy_ninemlruntimeerror(self):
        """
        line #: 237
        message: Cannot convert '{}' dimension, must be 1 or sympy expression

        context:
        --------
    def from_sympy(self, expr):
        if expr == 1:
            return dimensionless
        elif not isinstance(expr, sympy.Basic):
        """

        self.assertRaises(
            NineMLRuntimeError,
            Dimension.from_sympy,
            expr=None)


class TestUnitExceptions(unittest.TestCase):

    def test_to_SI_units_str_exception(self):
        """
        line #: 306
        message: Cannot convert to SI units string as offset is not zero ({})

        context:
        --------
    def to_SI_units_str(self):
        if self.offset != 0.0:
        """

        unit = next(instances_of_all_types['Unit'].itervalues())
        self.assertRaises(
            Exception,
            unit.to_SI_units_str)

    def test___mul___ninemlruntimeerror(self):
        """
        line #: 366
        message: Can't multiply units with nonzero offsets ({} and {})

        context:
        --------
    def __mul__(self, other):
        "self * other"
        try:
            if (self.offset != 0 or other.offset != 0):
        """

        unit = next(instances_of_all_types['Unit'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            unit.__mul__,
            other=None)

    def test___truediv___ninemlruntimeerror(self):
        """
        line #: 379
        message: Can't divide units with nonzero offsets ({} and {})

        context:
        --------
    def __truediv__(self, other):
        "self / expr"
        try:
            if (self.offset != 0 or other.offset != 0):
        """

        unit = next(instances_of_all_types['Unit'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            unit.__truediv__,
            other=None)

    def test___pow___ninemlruntimeerror(self):
        """
        line #: 395
        message: Can't raise units to power with nonzero offsets ({})

        context:
        --------
    def __pow__(self, power):
        "self ** expr"
        if self.offset != 0:
        """

        unit = next(instances_of_all_types['Unit'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            unit.__pow__,
            power=None)


class TestQuantityExceptions(unittest.TestCase):

    def test___init___exception(self):
        """
        line #: 450
        message: Units ({}) must of type <Unit>

        context:
        --------
    def __init__(self, value, units=None):
        super(Quantity, self).__init__()
        if isinstance(value, Quantity):
            if units is not None:
                value = value.in_units(units)
            else:
                units = value.units
                value = value.value
        elif not isinstance(value, (SingleValue, ArrayValue, RandomValue)):
            try:
                # Convert value from float
                value = SingleValue(float(value))
            except TypeError:
                # Convert value from iterable
                value = ArrayValue(value)
        if units is None:
            units = unitless
        elif not isinstance(units, Unit):
        """

        quantity = next(instances_of_all_types['Quantity'].itervalues())
        self.assertRaises(
            Exception,
            quantity.__init__,
            value=None,
            units=None)

    def test___getitem___ninemlruntimeerror(self):
        """
        line #: 482
        message: Cannot get item from random distribution

        context:
        --------
    def __getitem__(self, index):
        if self.is_array():
            return self._value.values[index]
        elif self.is_single():
            return self._value.value
        else:
        """

        quantity = next(instances_of_all_types['Quantity'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            quantity.__getitem__,
            index=None)

    def test_set_units_ninemldimensionerror(self):
        """
        line #: 487
        message: Can't change dimension of quantity from '{}' to '{}'

        context:
        --------
    def set_units(self, units):
        if units.dimension != self.units.dimension:
        """

        quantity = next(instances_of_all_types['Quantity'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            quantity.set_units,
            units=None)

    def test_in_units_ninemldimensionerror(self):
        """
        line #: 499
        message: Can't change convert quantity dimension from '{}' to '{}'

        context:
        --------
    def in_units(self, units):
        \"\"\"
        Returns a float value in terms of the given units (dimensions must be
        equivalent)
        \"\"\"
        if units.dimension != self.units.dimension:
        """

        quantity = next(instances_of_all_types['Quantity'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            quantity.in_units,
            units=None)

    def test_from_xml_ninemlruntimeerror(self):
        """
        line #: 525
        message: {} element '{}' is missing 'units' attribute (found '{}')

        context:
        --------
    def from_xml(cls, element, document, **kwargs):  # @UnusedVariable
        value = BaseValue.from_parent_xml(element, document, **kwargs)
        try:
            units_str = get_xml_attr(element, 'units', document, **kwargs)
        except KeyError:
        """

        self.assertRaises(
            NineMLRuntimeError,
            Quantity.from_xml,
            element=None,
            document=None)

    def test_from_xml_ninemlnameerror(self):
        """
        line #: 532
        message: Did not find definition of '{}' units in the current document.

        context:
        --------
    def from_xml(cls, element, document, **kwargs):  # @UnusedVariable
        value = BaseValue.from_parent_xml(element, document, **kwargs)
        try:
            units_str = get_xml_attr(element, 'units', document, **kwargs)
        except KeyError:
            raise NineMLRuntimeError(
                "{} element '{}' is missing 'units' attribute (found '{}')"
                .format(element.tag, element.get('name', ''),
                        "', '".join(element.attrib.iterkeys())))
        try:
            units = document[units_str]
        except KeyError:
        """

        self.assertRaises(
            NineMLNameError,
            Quantity.from_xml,
            element=None,
            document=None)

    def test__scaled_value_ninemldimensionerror(self):
        """
        line #: 593
        message: Cannot scale value as dimensions do not match ('{}' and '{}')

        context:
        --------
    def _scaled_value(self, qty):
        try:
            if qty.units.dimension != self.units.dimension:
        """

        quantity = next(instances_of_all_types['Quantity'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            quantity._scaled_value,
            qty=None)

    def test__scaled_value_ninemldimensionerror2(self):
        """
        line #: 602
        message: Can only add/subtract numbers from dimensionless quantities

        context:
        --------
    def _scaled_value(self, qty):
        try:
            if qty.units.dimension != self.units.dimension:
                raise NineMLDimensionError(
                    "Cannot scale value as dimensions do not match ('{}' and "
                    "'{}')".format(self.units.dimension.name,
                                   qty.units.dimension.name))
            return qty.value * 10 ** (self.units.power - qty.units.power)
        except AttributeError:
            if self.units == unitless:
                return float(qty.value)
            else:
        """

        quantity = next(instances_of_all_types['Quantity'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            quantity._scaled_value,
            qty=None)

    def test_parse_ninemlruntimeerror(self):
        """
        line #: 636
        message: Cannot '{}' to nineml.Quantity (can only convert quantities.Quantity and numeric objects)

        context:
        --------
    def parse(cls, qty):
        \"\"\"
        Parses ints and floats as dimensionless quantities and
        python-quantities Quantity objects into 9ML Quantity objects
        \"\"\"
        if not isinstance(qty, cls):
            # Assume it is a python quantities quantity and convert to
            # 9ML quantity
            try:
                unit_name = str(qty.units).split()[1].replace(
                    '/', '_per_').replace('**', '').replace('*', '_')
                if unit_name.startswith('_per_'):
                    unit_name = unit_name[1:]  # strip leading underscore
                powers = dict(
                    (cls._pq_si_to_dim[type(u).__name__], p)
                    for u, p in
                    qty.units.simplified._dimensionality.iteritems())
                dimension = Dimension(unit_name + 'Dimension', **powers)
                units = Unit(
                    unit_name, dimension=dimension,
                    power=int(math.log10(float(qty.units.simplified))))
                value = SingleValue(qty)
            except AttributeError:
                if isinstance(qty, (int, float)):
                    value = SingleValue(qty)
                else:
                    try:
                        value = ArrayValue(qty)
                    except NineMLValueError:
        """

        self.assertRaises(
            NineMLRuntimeError,
            Quantity.parse,
            qty=None)

