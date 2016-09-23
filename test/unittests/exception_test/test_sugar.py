import unittest
from nineml.sugar import (On)
from nineml.utils.testing.comprehensive import instances_of_all_types
from nineml.exceptions import (NineMLRuntimeError)


class TestExceptions(unittest.TestCase):

    def test_On_ninemlruntimeerror(self):
        """
        line #: 44
        message: Unexpected Type for On() trigger: {} {}

        context:
        --------
def On(trigger, do=None, to=None):

    if isinstance(do, (OutputEvent, basestring)):
        do = [do]
    elif do is None:
        do = []
    if isinstance(trigger, basestring):
        if is_single_symbol(trigger):
            return DoOnEvent(input_event=trigger, do=do, to=to)
        else:
            return DoOnCondition(condition=trigger, do=do, to=to)

    elif isinstance(trigger, Trigger):
        return DoOnCondition(condition=trigger, do=do, to=to)
    else:
        """

        self.assertRaises(
            NineMLRuntimeError,
            On,
            trigger=None,
            do=None,
            to=None)

