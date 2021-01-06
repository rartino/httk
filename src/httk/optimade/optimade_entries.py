#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This specific file is a mere re-formatting of information in
# the OPTIMaDe specification [http://www.optimade.org/].
#
# Formally, the author makes a Public Domain Dedication
# according to CC0 1.0 Universal (CC0 1.0)
#   https://creativecommons.org/publicdomain/zero/1.0/
#
# (Note, this only applies to this one specific file.)
#

entry_info = {
    'structures': {
        'descripion': 'A structures entry.',
        'properties': {
            'id': {
                'description': "The ID for the structures entry.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': True,
                'should_support': True,
                'required_query': True,
                'required_response': True,
                'default_response': True,
            },
            'type': {
                'description': "The name of the type of this entry, always 'structures'",
                'type': 'string',
                'fulltype': 'string',
                'required_support': True,
                'should_support': True,
                'required_query': True,
                'required_response': True,
                'default_response': True,
            },
            'immutable_id': {
                'description': "The entry's immutable ID (e.g., an UUID). This is important for databases having preferred IDs that point to \"the latest version\" of a record, but still offer access to older variants. This ID maps to the version-specific record, in case it changes in the future.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
            'last_modified': {
                'description': "A date representing when the entry was last modified.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': True,
                'required_query': True,
                'required_response': False,
                'default_response': True,
            },
            'elements': {
                'description': "Names of the different elements present in the structure.",
                'type': 'list',
                'fulltype': 'list of strings',
                'required_support': False,
                'should_support': True,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
            'nelements': {
                'description': "The number of elements found in a structure.",
                'type': 'integer',
                'fulltype': 'integer',
                'required_support': False,
                'should_support': True,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
            'elements_ratios': {
                'description': "Relative proportions of different elements in the structure.",
                'type': 'list',
                'fulltype': 'list of floats',
                'required_support': False,
                'should_support': True,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
            'chemical_formula_descriptive': {
                'description': "The chemical formula for a structure as a string in a form chosen by the API implementation.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': True,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
            'chemical_formula_reduced': {
                'description': "The reduced chemical formula for a structure as a string with element symbols and integer chemical proportion numbers. The proportion number MUST be omitted if it is 1.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': True,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
            'chemical_formula_hill': {
                'description': "The chemical formula for a structure in Hill form with element symbols followed by integer chemical proportion numbers. The proportion number MUST be omitted if it is 1.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
            'chemical_formula_anonymous': {
                'description': "The anonymous formula is the chemical_formula_reduced, but where the elements are instead first ordered by their chemical proportion number, and then, in order left to right, replaced by anonymous symbols A, B, C, ..., Z, Aa, Ba, ..., Za, Ab, Bb, ... and so on.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': True,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
            'dimension_types': {
                'description': "List of three integers. For each of the three directions indicated by the three lattice vectors (see property lattice_vectors), this list indicates if the direction is periodic (value 1) or non-periodic (value 0). Note: the elements in this list each refer to the direction of the corresponding entry in lattice_vectors and not the Cartesian x, y, z directions.",
                'type': 'list',
                'fulltype': 'list of integers',
                'required_support': False,
                'should_support': True,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'nperiodic_dimensions': {
                'description': "An integer specifying the number of periodic dimensions in the structure, equivalent to the number of non-zero entries in dimension_types.",
                'type': 'integer',
                'fulltype': 'integer',
                'required_support': False,
                'should_support': True,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
            'lattice_vectors': {
                'description': "The three lattice vectors in Cartesian coordinates, in ångström (Å).",
                'type': 'integer',
                'fulltype': 'list of list of floats',
                'required_support': False,
                'should_support': True,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'cartesian_site_positions': {
                'description': "Cartesian positions of each site in the structure. A site is usually used to describe positions of atoms; what atoms can be encountered at a given site is conveyed by the species_at_sites property, and the species themselves are described in the species property.",
                'type': 'list',
                'fulltype': 'list of list of floats',
                'required_support': False,
                'should_support': True,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'nsites': {
                'description': "An integer specifying the length of the cartesian_site_positions property.",
                'type': 'integer',
                'fulltype': 'integer',
                'required_support': False,
                'should_support': True,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'species_at_sites': {
                'description': "Name of the species at each site (where values for sites are specified with the same order of the property cartesian_site_positions). The properties of the species are found in the property species.",
                'type': 'list',
                'fulltype': 'list of strings',
                'required_support': False,
                'should_support': True,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'species': {
                'description': "A list describing the species of the sites of this structure. Species can represent pure chemical elements, virtual-crystal atoms representing a statistical occupation of a given site by multiple chemical elements, and/or a location to which there are attached atoms, i.e., atoms whose precise location are unknown beyond that they are attached to that position (frequently used to indicate hydrogen atoms attached to another element, e.g., a carbon with three attached hydrogens might represent a methyl group, -CH3).",
                'type': 'list',
                'fulltype': 'list of dict',
                'required_support': False,
                'should_support': True,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'assemblies': {
                'description': "A description of groups of sites that are statistically correlated.",
                'type': 'list',
                'fulltype': 'list of dict',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'structure_features': {
                'description': "A list of strings that flag which special features are used by the structure.",
                'type': 'list',
                'fulltype': 'list of string',
                'required_support': True,
                'should_support': True,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
        },
    },
    'calculations': {
        'descripion': 'a calculations entry',
        'properties': {
            'id': {
                'description': "The ID for the calculations entry.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': True,
                'should_support': True,
                'required_query': True,
                'required_response': True,
                'default_response': True,
            },
            'type': {
                'description': "The name of the type of this entry, always 'calculations'",
                'type': 'string',
                'fulltype': 'string',
                'required_support': True,
                'should_support': True,
                'required_query': True,
                'required_response': True,
                'default_response': True,
            },
            'immutable_id': {
                'description': "The entry's immutable ID (e.g., an UUID). This is important for databases having preferred IDs that point to \"the latest version\" of a record, but still offer access to older variants. This ID maps to the version-specific record, in case it changes in the future.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
            'last_modified': {
                'description': "A date representing when the entry was last modified.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': True,
                'required_query': True,
                'required_response': False,
                'default_response': True,
            },
        },
    },
    'references': {
        'descripion': 'a references entry',
        'properties': {
            'id': {
                'description': "The ID for the references entry.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': True,
                'should_support': True,
                'required_query': True,
                'required_response': True,
                'default_response': True,
            },
            'type': {
                'description': "The name of the type of this entry, always 'references'",
                'type': 'string',
                'fulltype': 'string',
                'required_support': True,
                'should_support': True,
                'required_query': True,
                'required_response': True,
                'default_response': True,
            },
            'immutable_id': {
                'description': "The entry's immutable ID (e.g., an UUID). This is important for databases having preferred IDs that point to \"the latest version\" of a record, but still offer access to older variants. This ID maps to the version-specific record, in case it changes in the future.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': True,
                'required_response': False,
                'default_response': False,
            },
            'last_modified': {
                'description': "A date representing when the entry was last modified.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': True,
                'required_query': True,
                'required_response': False,
                'default_response': True,
            },
            'address': {
                'description': "Usually the address of the publisher or other type of institution. For major publishing houses, van Leunen recommends omitting the information entirely. For small publishers, on the other hand, you can help the reader by giving the complete address.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'annote': {
                'description': "An annotation. It is not used by the standard bibliography styles, but may be used by others that produce an annotated bibliography.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'booktitle': {
                'description': "Title of a book, part of which is being cited. See the LATEX book for how to type titles. For book entries, use the title field instead.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'chapter': {
                'description': "A chapter (or section or whatever) number.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'crossref': {
                'description': "The database key of the entry being cross referenced.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'edition': {
                'description': "The edition of a book—for example, \"Second\". This should be an ordinal, and should have the first letter capitalized, as shown here; the standard styles convert to lower case when necessary.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'howpublished': {
                'description': "How something strange has been published. The first word should be capitalized.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'institution': {
                'description': "The sponsoring institution of a technical report.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'journal': {
                'description': "A journal name. Abbreviations are provided for many journals; see the BibTeX specification [http://bibtexml.sourceforge.net/btxdoc.pdf] \"Local Guide\".",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'key': {
                'description': "Used for alphabetizing, cross referencing, and creating a label when the \"author\" information (described in Section 4) is missing.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'month': {
                'description': "The month in which the work was published or, for an unpublished work, in which it was written. You should use the standard three-letter abbreviation, as described in Appendix B.1.3 of the LATEX book.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'note': {
                'description': "Any additional information that can help the reader. The first word should be capitalized.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'number': {
                'description': "The number of a journal, magazine, technical report, or of a work in a series. An issue of a journal or magazine is usually identified by its volume and number; the organization that issues a technical report usually gives it a number; and sometimes books are given numbers in a named series.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'organization': {
                'description': "The organization that sponsors a conference or that publishes a manual.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'pages': {
                'description': "One or more page numbers or range of numbers, such as 42--111 or 7,41,73--97 or 43+ (the ‘+’ in this last example indicates pages following that don’t form a simple range). To make it easier to maintain Scribecompatible databases, the standard styles convert a single dash (as in 7-33) to the double dash used in TEX to denote number ranges (as in 7--33).",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'publisher': {
                'description': "The publisher’s name.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'school': {
                'description': "The name of the school where a thesis was written.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'series': {
                'description': "The name of a series or set of books. When citing an entire book, the the title field gives its title and an optional series field gives the name of a series or multi-volume set in which the book is published.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'title': {
                'description': "The work’s title, typed as explained in the LATEX book.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'volume': {
                'description': "The volume of a journal or multivolume book.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'year': {
                'description': "The year of publication or, for an unpublished work, the year it was written. Generally it should consist of four numerals, such as 1984, although the standard styles can handle any year whose last four nonpunctuation characters are numerals, such as '(about 1984)'.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'bib_type': {
                'description': "The type of a technical report—for example, \"Research Note\", corresponding to type property in the BibTeX specification [http://bibtexml.sourceforge.net/btxdoc.pdf].",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'authors': {
                'description': "The name(s) of the author(s), in the format described in the LATEX book.",
                'type': 'list',
                'fulltype': 'list of dict',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'editors': {
                'description': "Name(s) of editor(s), typed as indicated in the LATEX book. If there is also an author field, then the editor field gives the editor of the book or collection in which the reference appears.",
                'type': 'list',
                'fulltype': 'list of dict',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'doi': {
                'description': "DOI of the reference.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            },
            'url': {
                'description': "URL to the reference.",
                'type': 'string',
                'fulltype': 'string',
                'required_support': False,
                'should_support': False,
                'required_query': False,
                'required_response': False,
                'default_response': False,
            }
        }
    }
}

all_entries = list(entry_info.keys())

properties_by_entry = dict([(x, entry_info[x]['properties'].keys()) for x in entry_info])

# In the future, not all properties may be valid response fields
valid_response_fields = properties_by_entry

valid_endpoints = list(['info', 'all'] + all_entries + [x+"/info" for x in all_entries] + [''])

