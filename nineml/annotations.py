from copy import copy
from nineml.xml import E, extract_xmlns, strip_xmlns
from nineml.base import DocumentLevelObject, BaseNineMLObject
import re


class AnnotationsBase(BaseNineMLObject):

    def __init__(self, branches=None):
        if branches is None:
            branches = {}
        self._branches = branches

    @property
    def branches(self):
        return self._branches.itervalues()

    def __getitem__(self, key):
        try:
            val = self._branches[key]
        except KeyError:
            # Create a new annotations branch next level of annotations
            val = self._branches[key] = _AnnotationsBranch(key)
        return val


class _AnnotationsBranch(AnnotationsBase):

    nineml_type = '_AnnotationsBranch'
    defining_attributes = ('_branches', '_attr')

    def __init__(self, name, attr=None, branches=None):
        super(_AnnotationsBranch, self).__init__(branches)
        if attr is None:
            attr = {}
        self._name = name
        self._attr = {}

    @property
    def name(self):
        return self._name

    def __iter__(self):
        return self.keys()

    def values(self):
        return self._attr.itervalues()

    def keys(self):
        return self._attr.iterkeys()

    def items(self):
        return self._attr.iteritems()

    def get(self, key, default=None):
        """Like getitem but doesn't create a new branch if one isn't present"""
        try:
            val = self._attr[key]
        except KeyError:
            val = default
        return val

    def __setitem__(self, key, val):
        self._attr[key] = str(val)

    def to_xml(self, **kwargs):  # @UnusedVariable
        return E(self.name,
                 *(sb.to_xml(**kwargs) for sb in self._branches),
                 **self._attr)

    @classmethod
    def from_xml(cls, element, **kwargs):  # @UnusedVariable
        name = strip_xmlns(element.tag)
        branches = {}
        for child in element.getchildren():
            branches[
                strip_xmlns(child.tag)] = _AnnotationsBranch.from_xml(child)
        attr = dict(element.attrib)
        return cls(name, attr, branches)

    def _copy_to_clone(self, clone, memo, **kwargs):
        self._clone_defining_attr(clone, memo, **kwargs)


class Annotations(DocumentLevelObject, AnnotationsBase):
    """
    Defines the dimension used for quantity units
    """

    nineml_type = 'Annotations'
    defining_attributes = ('_branches',)

    def __init__(self, branches=None):
        AnnotationsBase.__init__(self, branches)

    def __repr__(self):
        return "Annotations('{}')".format("', '".join(self._branches.keys()))

    def to_xml(self, **kwargs):  # @UnusedVariable
        return E(self.nineml_type,
                 *(b.to_xml(**kwargs) for b in self.branches))

    @classmethod
    def from_xml(cls, element, **kwargs):  # @UnusedVariable
        assert strip_xmlns(element.tag) == cls.nineml_type
        branches = {}
        for child in element.getchildren():
            branches[
                strip_xmlns(child.tag)] = _AnnotationsBranch.from_xml(child)
        return cls(**kwargs)

    def _copy_to_clone(self, clone, memo, **kwargs):
        self._clone_defining_attr(clone, memo, **kwargs)


def read_annotations(from_xml):
    def annotate_from_xml(cls, element, *args, **kwargs):
        nineml_xmlns = extract_xmlns(element.tag)
        annot_elem = expect_none_or_single(
            element.findall(nineml_xmlns + Annotations.nineml_type))
        if annot_elem is not None:
            # Extract the annotations
            annotations = Annotations.from_xml(annot_elem)
            # Get a copy of the element with the annotations stripped
            element = copy(element)
            element.remove(element.find(nineml_xmlns +
                                        Annotations.nineml_type))
        else:
            annotations = Annotations()
        if (cls.__class__.__name__ == 'DynamicsXMLLoader' and
                VALIDATE_DIMENSIONS in annotations[nineml_xmlns]):
            # FIXME: Hack until I work out the best way to let other 9ML
            #        objects ignore this kwarg TGC 6/15
            kwargs['validate_dimensions'] = (
                annotations[nineml_xmlns][VALIDATE_DIMENSIONS] == 'True')
        nineml_object = from_xml(cls, element, *args, **kwargs)
        nineml_object.annotations.update(annotations.iteritems())
        return nineml_object
    return annotate_from_xml


def annotate_xml(to_xml):
    def annotate_to_xml(self, document_or_obj, **kwargs):
        # If Abstraction Layer class
        if xml_visitor_module_re.match(type(self).__module__):
            obj = document_or_obj
            options = self.options
        # If User Layer class
        else:
            obj = self
            options = kwargs
        elem = to_xml(self, document_or_obj, **kwargs)
        if (not options.get('no_annotations', False) and
                any(a for a in obj.annotations.itervalues())):
            elem.append(obj.annotations.to_xml(**kwargs))
        return elem
    return annotate_to_xml


VALIDATE_DIMENSIONS = 'ValidateDimensions'

xml_visitor_module_re = re.compile(r'nineml\.abstraction\.\w+\.visitors\.xml')

from nineml.utils import expect_none_or_single
