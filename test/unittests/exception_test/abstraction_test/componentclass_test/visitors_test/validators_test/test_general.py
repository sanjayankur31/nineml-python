import unittest
from nineml.abstraction.componentclass.visitors.validators.general import (DimensionalityComponentValidator, CheckNoLHSAssignmentsToMathsNamespaceComponentValidator, AliasesAreNotRecursiveComponentValidator, NoUnresolvedSymbolsComponentValidator)
from nineml.utils.testing.comprehensive import instances_of_all_types
from nineml.exceptions import (NineMLDimensionError, NineMLRuntimeError)


class TestDimensionalityComponentValidatorExceptions(unittest.TestCase):

    def test__get_dimensions_ninemlruntimeerror(self):
        """
        line #: 208
        message: Did not find '{}' in '{}' dynamics class (scopes: {})

        context:
        --------
    def _get_dimensions(self, element):
        if isinstance(element, (sympy.Symbol, basestring)):
            if element == sympy.Symbol('t'):  # Reserved symbol 't'
                return sympy.Symbol('t')  # representation of the time dim.
            name = Expression.symbol_to_str(element)
            # Look back through the scope stack to find the referenced
            # element
            element = None
            for scope in reversed(self._scopes):
                try:
                    element = scope.element(
                        name,
                        class_map=self.class_to_visit.class_to_member)
                except KeyError:
                    pass
            if element is None:
        """

        dimensionalitycomponentvalidator = next(instances_of_all_types['DimensionalityComponentValidator'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            dimensionalitycomponentvalidator._get_dimensions,
            element=None)

    def test__flatten_dims_ninemldimensionerror(self):
        """
        line #: 252
        message: self

        context:
        --------
    def _flatten_dims(self, expr, element):
        if isinstance(expr, (sympy.Integer, sympy.Float, int, float)):
            dims = 1
        elif isinstance(expr, (BooleanTrue, BooleanFalse)):
            dims = 0
        elif isinstance(expr, sympy.Symbol):
            dims = self._get_dimensions(expr)
        elif isinstance(expr, sympy.Mul):
            dims = reduce(operator.mul,
                          (self._flatten_dims(a, element) for a in expr.args))
            if isinstance(dims, sympy.Basic):
                dims = dims.powsimp()
        elif isinstance(expr, sympy.Pow):
            base = expr.args[0]
            exponent = expr.args[1]
            exp_dims = self._flatten_dims(exponent, element)
            if exp_dims != 1:
        """

        dimensionalitycomponentvalidator = next(instances_of_all_types['DimensionalityComponentValidator'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            dimensionalitycomponentvalidator._flatten_dims,
            expr=None,
            element=None)

    def test__flatten_dims_ninemldimensionerror2(self):
        """
        line #: 259
        message: self

        context:
        --------
    def _flatten_dims(self, expr, element):
        if isinstance(expr, (sympy.Integer, sympy.Float, int, float)):
            dims = 1
        elif isinstance(expr, (BooleanTrue, BooleanFalse)):
            dims = 0
        elif isinstance(expr, sympy.Symbol):
            dims = self._get_dimensions(expr)
        elif isinstance(expr, sympy.Mul):
            dims = reduce(operator.mul,
                          (self._flatten_dims(a, element) for a in expr.args))
            if isinstance(dims, sympy.Basic):
                dims = dims.powsimp()
        elif isinstance(expr, sympy.Pow):
            base = expr.args[0]
            exponent = expr.args[1]
            exp_dims = self._flatten_dims(exponent, element)
            if exp_dims != 1:
                raise NineMLDimensionError(self._construct_error_message(
                    "Exponents are required to be dimensionless arguments,"
                    " which was not the case in", exp_dims, expr, element))
            base_dims = self._flatten_dims(base, element)
            if base_dims != 1:
                if not isinstance(exponent, (sympy.Integer, int,
                                             sympy.numbers.NegativeOne)):
        """

        dimensionalitycomponentvalidator = next(instances_of_all_types['DimensionalityComponentValidator'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            dimensionalitycomponentvalidator._flatten_dims,
            expr=None,
            element=None)

    def test__flatten_dims_ninemldimensionerror3(self):
        """
        line #: 271
        message: self

        context:
        --------
    def _flatten_dims(self, expr, element):
        if isinstance(expr, (sympy.Integer, sympy.Float, int, float)):
            dims = 1
        elif isinstance(expr, (BooleanTrue, BooleanFalse)):
            dims = 0
        elif isinstance(expr, sympy.Symbol):
            dims = self._get_dimensions(expr)
        elif isinstance(expr, sympy.Mul):
            dims = reduce(operator.mul,
                          (self._flatten_dims(a, element) for a in expr.args))
            if isinstance(dims, sympy.Basic):
                dims = dims.powsimp()
        elif isinstance(expr, sympy.Pow):
            base = expr.args[0]
            exponent = expr.args[1]
            exp_dims = self._flatten_dims(exponent, element)
            if exp_dims != 1:
                raise NineMLDimensionError(self._construct_error_message(
                    "Exponents are required to be dimensionless arguments,"
                    " which was not the case in", exp_dims, expr, element))
            base_dims = self._flatten_dims(base, element)
            if base_dims != 1:
                if not isinstance(exponent, (sympy.Integer, int,
                                             sympy.numbers.NegativeOne)):
                    raise NineMLDimensionError(self._construct_error_message(
                        "Integer exponents are required for non-dimensionless "
                        "bases, which was not the case in", exp_dims, expr,
                        element))
            dims = (self._flatten_dims(base, element) ** exponent)
        elif isinstance(expr, sympy.Add):
            dims = None
            for arg in expr.args:
                arg_dims = self._flatten_dims(arg, element)
                if dims is None:
                    dims = arg_dims
                elif arg_dims - dims != 0:
        """

        dimensionalitycomponentvalidator = next(instances_of_all_types['DimensionalityComponentValidator'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            dimensionalitycomponentvalidator._flatten_dims,
            expr=None,
            element=None)

    def test__flatten_dims_ninemldimensionerror4(self):
        """
        line #: 280
        message: self

        context:
        --------
    def _flatten_dims(self, expr, element):
        if isinstance(expr, (sympy.Integer, sympy.Float, int, float)):
            dims = 1
        elif isinstance(expr, (BooleanTrue, BooleanFalse)):
            dims = 0
        elif isinstance(expr, sympy.Symbol):
            dims = self._get_dimensions(expr)
        elif isinstance(expr, sympy.Mul):
            dims = reduce(operator.mul,
                          (self._flatten_dims(a, element) for a in expr.args))
            if isinstance(dims, sympy.Basic):
                dims = dims.powsimp()
        elif isinstance(expr, sympy.Pow):
            base = expr.args[0]
            exponent = expr.args[1]
            exp_dims = self._flatten_dims(exponent, element)
            if exp_dims != 1:
                raise NineMLDimensionError(self._construct_error_message(
                    "Exponents are required to be dimensionless arguments,"
                    " which was not the case in", exp_dims, expr, element))
            base_dims = self._flatten_dims(base, element)
            if base_dims != 1:
                if not isinstance(exponent, (sympy.Integer, int,
                                             sympy.numbers.NegativeOne)):
                    raise NineMLDimensionError(self._construct_error_message(
                        "Integer exponents are required for non-dimensionless "
                        "bases, which was not the case in", exp_dims, expr,
                        element))
            dims = (self._flatten_dims(base, element) ** exponent)
        elif isinstance(expr, sympy.Add):
            dims = None
            for arg in expr.args:
                arg_dims = self._flatten_dims(arg, element)
                if dims is None:
                    dims = arg_dims
                elif arg_dims - dims != 0:
                    raise NineMLDimensionError(self._construct_error_message(
                        "Dimensions do not match within",
                        ' + '.join(str(self._flatten_dims(a, element))
                                   for a in expr.args), expr, element))
        elif isinstance(expr, (sympy.GreaterThan, sympy.LessThan,
                               sympy.StrictGreaterThan, sympy.StrictLessThan)):
            lhs_dims = self._flatten_dims(expr.args[0], element)
            rhs_dims = self._flatten_dims(expr.args[1], element)
            if lhs_dims - rhs_dims != 0:
        """

        dimensionalitycomponentvalidator = next(instances_of_all_types['DimensionalityComponentValidator'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            dimensionalitycomponentvalidator._flatten_dims,
            expr=None,
            element=None)

    def test__flatten_dims_ninemldimensionerror5(self):
        """
        line #: 289
        message: self

        context:
        --------
    def _flatten_dims(self, expr, element):
        if isinstance(expr, (sympy.Integer, sympy.Float, int, float)):
            dims = 1
        elif isinstance(expr, (BooleanTrue, BooleanFalse)):
            dims = 0
        elif isinstance(expr, sympy.Symbol):
            dims = self._get_dimensions(expr)
        elif isinstance(expr, sympy.Mul):
            dims = reduce(operator.mul,
                          (self._flatten_dims(a, element) for a in expr.args))
            if isinstance(dims, sympy.Basic):
                dims = dims.powsimp()
        elif isinstance(expr, sympy.Pow):
            base = expr.args[0]
            exponent = expr.args[1]
            exp_dims = self._flatten_dims(exponent, element)
            if exp_dims != 1:
                raise NineMLDimensionError(self._construct_error_message(
                    "Exponents are required to be dimensionless arguments,"
                    " which was not the case in", exp_dims, expr, element))
            base_dims = self._flatten_dims(base, element)
            if base_dims != 1:
                if not isinstance(exponent, (sympy.Integer, int,
                                             sympy.numbers.NegativeOne)):
                    raise NineMLDimensionError(self._construct_error_message(
                        "Integer exponents are required for non-dimensionless "
                        "bases, which was not the case in", exp_dims, expr,
                        element))
            dims = (self._flatten_dims(base, element) ** exponent)
        elif isinstance(expr, sympy.Add):
            dims = None
            for arg in expr.args:
                arg_dims = self._flatten_dims(arg, element)
                if dims is None:
                    dims = arg_dims
                elif arg_dims - dims != 0:
                    raise NineMLDimensionError(self._construct_error_message(
                        "Dimensions do not match within",
                        ' + '.join(str(self._flatten_dims(a, element))
                                   for a in expr.args), expr, element))
        elif isinstance(expr, (sympy.GreaterThan, sympy.LessThan,
                               sympy.StrictGreaterThan, sympy.StrictLessThan)):
            lhs_dims = self._flatten_dims(expr.args[0], element)
            rhs_dims = self._flatten_dims(expr.args[1], element)
            if lhs_dims - rhs_dims != 0:
                raise NineMLDimensionError(self._construct_error_message(
                    "LHS/RHS dimensions of boolean expression",
                    lhs_dims - rhs_dims, expr, postamble="do not match"))
            dims = 0  # boolean expression
        elif isinstance(expr, (sympy.And, sympy.Or, sympy.Not)):
            for arg in expr.args:
                dims = self._flatten_dims(arg, element)
                # boolean expression == 0
                if dims != 0 and dims != 1:  # FIXME: allow dimless until bool params @IgnorePep8
        """

        dimensionalitycomponentvalidator = next(instances_of_all_types['DimensionalityComponentValidator'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            dimensionalitycomponentvalidator._flatten_dims,
            expr=None,
            element=None)

    def test__flatten_dims_ninemldimensionerror6(self):
        """
        line #: 296
        message: self

        context:
        --------
    def _flatten_dims(self, expr, element):
        if isinstance(expr, (sympy.Integer, sympy.Float, int, float)):
            dims = 1
        elif isinstance(expr, (BooleanTrue, BooleanFalse)):
            dims = 0
        elif isinstance(expr, sympy.Symbol):
            dims = self._get_dimensions(expr)
        elif isinstance(expr, sympy.Mul):
            dims = reduce(operator.mul,
                          (self._flatten_dims(a, element) for a in expr.args))
            if isinstance(dims, sympy.Basic):
                dims = dims.powsimp()
        elif isinstance(expr, sympy.Pow):
            base = expr.args[0]
            exponent = expr.args[1]
            exp_dims = self._flatten_dims(exponent, element)
            if exp_dims != 1:
                raise NineMLDimensionError(self._construct_error_message(
                    "Exponents are required to be dimensionless arguments,"
                    " which was not the case in", exp_dims, expr, element))
            base_dims = self._flatten_dims(base, element)
            if base_dims != 1:
                if not isinstance(exponent, (sympy.Integer, int,
                                             sympy.numbers.NegativeOne)):
                    raise NineMLDimensionError(self._construct_error_message(
                        "Integer exponents are required for non-dimensionless "
                        "bases, which was not the case in", exp_dims, expr,
                        element))
            dims = (self._flatten_dims(base, element) ** exponent)
        elif isinstance(expr, sympy.Add):
            dims = None
            for arg in expr.args:
                arg_dims = self._flatten_dims(arg, element)
                if dims is None:
                    dims = arg_dims
                elif arg_dims - dims != 0:
                    raise NineMLDimensionError(self._construct_error_message(
                        "Dimensions do not match within",
                        ' + '.join(str(self._flatten_dims(a, element))
                                   for a in expr.args), expr, element))
        elif isinstance(expr, (sympy.GreaterThan, sympy.LessThan,
                               sympy.StrictGreaterThan, sympy.StrictLessThan)):
            lhs_dims = self._flatten_dims(expr.args[0], element)
            rhs_dims = self._flatten_dims(expr.args[1], element)
            if lhs_dims - rhs_dims != 0:
                raise NineMLDimensionError(self._construct_error_message(
                    "LHS/RHS dimensions of boolean expression",
                    lhs_dims - rhs_dims, expr, postamble="do not match"))
            dims = 0  # boolean expression
        elif isinstance(expr, (sympy.And, sympy.Or, sympy.Not)):
            for arg in expr.args:
                dims = self._flatten_dims(arg, element)
                # boolean expression == 0
                if dims != 0 and dims != 1:  # FIXME: allow dimless until bool params @IgnorePep8
                    raise NineMLDimensionError(self._construct_error_message(
                        "Logical expression provided non-boolean argument '{}'"
                        .format(arg), dims, expr))
        elif isinstance(type(expr), sympy.FunctionClass):
            for arg in expr.args:
                arg_dims = self._flatten_dims(arg, element)
                if arg_dims != 1:
        """

        dimensionalitycomponentvalidator = next(instances_of_all_types['DimensionalityComponentValidator'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            dimensionalitycomponentvalidator._flatten_dims,
            expr=None,
            element=None)

    def test__flatten_dims_notimplementederror(self):
        """
        line #: 307
        message: Unrecognised type {} of expression '{}'

        context:
        --------
    def _flatten_dims(self, expr, element):
        if isinstance(expr, (sympy.Integer, sympy.Float, int, float)):
            dims = 1
        elif isinstance(expr, (BooleanTrue, BooleanFalse)):
            dims = 0
        elif isinstance(expr, sympy.Symbol):
            dims = self._get_dimensions(expr)
        elif isinstance(expr, sympy.Mul):
            dims = reduce(operator.mul,
                          (self._flatten_dims(a, element) for a in expr.args))
            if isinstance(dims, sympy.Basic):
                dims = dims.powsimp()
        elif isinstance(expr, sympy.Pow):
            base = expr.args[0]
            exponent = expr.args[1]
            exp_dims = self._flatten_dims(exponent, element)
            if exp_dims != 1:
                raise NineMLDimensionError(self._construct_error_message(
                    "Exponents are required to be dimensionless arguments,"
                    " which was not the case in", exp_dims, expr, element))
            base_dims = self._flatten_dims(base, element)
            if base_dims != 1:
                if not isinstance(exponent, (sympy.Integer, int,
                                             sympy.numbers.NegativeOne)):
                    raise NineMLDimensionError(self._construct_error_message(
                        "Integer exponents are required for non-dimensionless "
                        "bases, which was not the case in", exp_dims, expr,
                        element))
            dims = (self._flatten_dims(base, element) ** exponent)
        elif isinstance(expr, sympy.Add):
            dims = None
            for arg in expr.args:
                arg_dims = self._flatten_dims(arg, element)
                if dims is None:
                    dims = arg_dims
                elif arg_dims - dims != 0:
                    raise NineMLDimensionError(self._construct_error_message(
                        "Dimensions do not match within",
                        ' + '.join(str(self._flatten_dims(a, element))
                                   for a in expr.args), expr, element))
        elif isinstance(expr, (sympy.GreaterThan, sympy.LessThan,
                               sympy.StrictGreaterThan, sympy.StrictLessThan)):
            lhs_dims = self._flatten_dims(expr.args[0], element)
            rhs_dims = self._flatten_dims(expr.args[1], element)
            if lhs_dims - rhs_dims != 0:
                raise NineMLDimensionError(self._construct_error_message(
                    "LHS/RHS dimensions of boolean expression",
                    lhs_dims - rhs_dims, expr, postamble="do not match"))
            dims = 0  # boolean expression
        elif isinstance(expr, (sympy.And, sympy.Or, sympy.Not)):
            for arg in expr.args:
                dims = self._flatten_dims(arg, element)
                # boolean expression == 0
                if dims != 0 and dims != 1:  # FIXME: allow dimless until bool params @IgnorePep8
                    raise NineMLDimensionError(self._construct_error_message(
                        "Logical expression provided non-boolean argument '{}'"
                        .format(arg), dims, expr))
        elif isinstance(type(expr), sympy.FunctionClass):
            for arg in expr.args:
                arg_dims = self._flatten_dims(arg, element)
                if arg_dims != 1:
                    raise NineMLDimensionError(self._construct_error_message(
                        "Dimensionless arguments required for function",
                        arg_dims, element=element, expr=arg))
            dims = 1
        elif (type(expr).__name__ in ('Pi',) or
              isinstance(expr, sympy.Rational)):
            dims = 1
        elif isinstance(element, BaseNineMLObject):
            assert False, ("{} was not added to pre-determined dimensions"
                           .format(element))
        else:
        """

        dimensionalitycomponentvalidator = next(instances_of_all_types['DimensionalityComponentValidator'].itervalues())
        self.assertRaises(
            NotImplementedError,
            dimensionalitycomponentvalidator._flatten_dims,
            expr=None,
            element=None)

    def test__compare_dimensionality_ninemldimensionerror(self):
        """
        line #: 314
        message: self

        context:
        --------
    def _compare_dimensionality(self, dimension, reference, element, ref_name):
        if dimension - sympify(reference) != 0:
        """

        dimensionalitycomponentvalidator = next(instances_of_all_types['DimensionalityComponentValidator'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            dimensionalitycomponentvalidator._compare_dimensionality,
            dimension=None,
            reference=None,
            element=None,
            ref_name=None)

    def test__check_send_port_ninemldimensionerror(self):
        """
        line #: 326
        message: self

        context:
        --------
    def _check_send_port(self, port):
        # Get the state variable or alias associated with the analog send
        # port
        element = self.component_class.element(
            port.name, self.class_to_visit.class_to_member)
        try:
            if element.dimension != port.dimension:
        """

        dimensionalitycomponentvalidator = next(instances_of_all_types['DimensionalityComponentValidator'].itervalues())
        self.assertRaises(
            NineMLDimensionError,
            dimensionalitycomponentvalidator._check_send_port,
            port=None)


class TestCheckNoLHSAssignmentsToMathsNamespaceComponentValidatorExceptions(unittest.TestCase):

    def test_check_lhssymbol_is_valid_ninemlruntimeerror(self):
        """
        line #: 157
        message: err

        context:
        --------
    def check_lhssymbol_is_valid(self, symbol):
        assert isinstance(symbol, basestring)

        if not is_valid_lhs_target(symbol):
            err = 'Symbol: %s found on left-hand-side of an equation'
        """

        checknolhsassignmentstomathsnamespacecomponentvalidator = next(instances_of_all_types['CheckNoLHSAssignmentsToMathsNamespaceComponentValidator'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            checknolhsassignmentstomathsnamespacecomponentvalidator.check_lhssymbol_is_valid,
            symbol=None)


class TestAliasesAreNotRecursiveComponentValidatorExceptions(unittest.TestCase):

    def test_action_componentclass_ninemlruntimeerror(self):
        """
        line #: 49
        message: Unable to resolve all aliases, you may have a recursion issue. Remaining Aliases: {}

        context:
        --------
    def action_componentclass(self, component_class):

        unresolved_aliases = dict((a.lhs, a) for a in component_class.aliases)

        def alias_contains_unresolved_symbols(alias):
            unresolved = [sym for sym in alias.rhs_symbol_names
                          if sym in unresolved_aliases]
            return len(unresolved) != 0

        def get_resolved_aliases():
            return [alias for alias in unresolved_aliases.values()
                    if not alias_contains_unresolved_symbols(alias)]

        while(unresolved_aliases):
            resolved_aliases = get_resolved_aliases()
            if resolved_aliases:
                for r in resolved_aliases:
                    del unresolved_aliases[r.lhs]

            else:
        """

        aliasesarenotrecursivecomponentvalidator = next(instances_of_all_types['AliasesAreNotRecursiveComponentValidator'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            aliasesarenotrecursivecomponentvalidator.action_componentclass,
            component_class=None)


class TestNoUnresolvedSymbolsComponentValidatorExceptions(unittest.TestCase):

    def test___init___ninemlruntimeerror(self):
        """
        line #: 78
        message: Unresolved Symbol in Alias: {} [{}]

        context:
        --------
    def __init__(self, component_class, **kwargs):  # @UnusedVariable @IgnorePep8
        BaseValidator.__init__(
            self, require_explicit_overrides=False)

        self.available_symbols = []
        self.aliases = []
        self.time_derivatives = []
        self.state_assignments = []
        self.component_class = component_class
        self.visit(component_class)

        # Check Aliases:
        for alias in self.aliases:
            for rhs_atom in alias.rhs_symbol_names:
                if rhs_atom in reserved_identifiers:
                    continue
                if rhs_atom not in self.available_symbols:
        """

        nounresolvedsymbolscomponentvalidator = next(instances_of_all_types['NoUnresolvedSymbolsComponentValidator'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            nounresolvedsymbolscomponentvalidator.__init__,
            component_class=None)

    def test___init___ninemlruntimeerror2(self):
        """
        line #: 87
        message: Unresolved Symbol in Time Derivative: {} [{}]

        context:
        --------
    def __init__(self, component_class, **kwargs):  # @UnusedVariable @IgnorePep8
        BaseValidator.__init__(
            self, require_explicit_overrides=False)

        self.available_symbols = []
        self.aliases = []
        self.time_derivatives = []
        self.state_assignments = []
        self.component_class = component_class
        self.visit(component_class)

        # Check Aliases:
        for alias in self.aliases:
            for rhs_atom in alias.rhs_symbol_names:
                if rhs_atom in reserved_identifiers:
                    continue
                if rhs_atom not in self.available_symbols:
                    raise NineMLRuntimeError(
                        "Unresolved Symbol in Alias: {} [{}]"
                        .format(rhs_atom, alias))

        # Check TimeDerivatives:
        for timederivative in self.time_derivatives:
            for rhs_atom in timederivative.rhs_symbol_names:
                if (rhs_atom not in self.available_symbols and
                        rhs_atom not in reserved_identifiers):
        """

        nounresolvedsymbolscomponentvalidator = next(instances_of_all_types['NoUnresolvedSymbolsComponentValidator'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            nounresolvedsymbolscomponentvalidator.__init__,
            component_class=None)

    def test___init___ninemlruntimeerror3(self):
        """
        line #: 96
        message: Unresolved Symbol in Assignment: {} [{}]

        context:
        --------
    def __init__(self, component_class, **kwargs):  # @UnusedVariable @IgnorePep8
        BaseValidator.__init__(
            self, require_explicit_overrides=False)

        self.available_symbols = []
        self.aliases = []
        self.time_derivatives = []
        self.state_assignments = []
        self.component_class = component_class
        self.visit(component_class)

        # Check Aliases:
        for alias in self.aliases:
            for rhs_atom in alias.rhs_symbol_names:
                if rhs_atom in reserved_identifiers:
                    continue
                if rhs_atom not in self.available_symbols:
                    raise NineMLRuntimeError(
                        "Unresolved Symbol in Alias: {} [{}]"
                        .format(rhs_atom, alias))

        # Check TimeDerivatives:
        for timederivative in self.time_derivatives:
            for rhs_atom in timederivative.rhs_symbol_names:
                if (rhs_atom not in self.available_symbols and
                        rhs_atom not in reserved_identifiers):
                    raise NineMLRuntimeError(
                        "Unresolved Symbol in Time Derivative: {} [{}]"
                        .format(rhs_atom, timederivative))

        # Check StateAssignments
        for state_assignment in self.state_assignments:
            for rhs_atom in state_assignment.rhs_symbol_names:
                if (rhs_atom not in self.available_symbols and
                        rhs_atom not in reserved_identifiers):
        """

        nounresolvedsymbolscomponentvalidator = next(instances_of_all_types['NoUnresolvedSymbolsComponentValidator'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            nounresolvedsymbolscomponentvalidator.__init__,
            component_class=None)

    def test_add_symbol_ninemlruntimeerror(self):
        """
        line #: 102
        message: Duplicate Symbol '{}' found

        context:
        --------
    def add_symbol(self, symbol):
        if symbol in self.available_symbols:
        """

        nounresolvedsymbolscomponentvalidator = next(instances_of_all_types['NoUnresolvedSymbolsComponentValidator'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            nounresolvedsymbolscomponentvalidator.add_symbol,
            symbol=None)

