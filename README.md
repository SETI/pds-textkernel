| PyPI Release | Test Status | Code Coverage |
| ------------ | ----------- | ------------- |
| [![PyPI version](https://badge.fury.io/py/rms-textkernel.svg)](https://badge.fury.io/py/rms-textkernel) | [![Build status](https://img.shields.io/github/actions/workflow/status/SETI/rms-textkernel/run-tests.yml?branch=master)](https://github.com/SETI/rms-textkernel/actions) | [![Code coverage](https://img.shields.io/codecov/c/github/SETI/rms-textkernel/main?logo=codecov)](https://codecov.io/gh/SETI/rms-textkernel) |

# rms-textkernel

Supported versions: Python >= 3.7

## PDS Ring-Moon Systems Node, SETI Institute
## TextKernel Library

This is a set of routines for parsing SPICE text kernels. The simplest use case is as
follows:
```
        import textkernel
        tkdict = textkernel.from_file('path/to/kernel/file')
```

The returned dictionary is keyed by all the parameter names (on the left side of an equal
sign) in the text kernel, and each associated dictionary value is that found on the right
side. Values are Python ints, floats, strings, datetime objects, or lists of one or more
of these.

This module implements the complete syntax specification as discussed in the SPICE Kernel
Required Reading document, "kernel.req":
        <https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/kernel.html>

For convenience, the returned dictionary adds additional, "hierarchical" keys that provide
alternative access to the same values. Hierarchical keys are substrings from the original
parameter name, which return a sub-dictionary keyed by part or all of the remainder of
that parameter name.

Parameter names with a slash are split apart as if they represented components of a file
directory tree, so these are equivalent:
```
        tkdict["DELTET/EB"] == tkdict["DELTET"]["EB"]
```

When a body or frame ID is embedded inside a parameter name, it is extracted, converted
to integer, and used as a piece of the hierarchy, making these equivalent:
```
        tkdict["BODY399_POLE_RA"] == tkdict["BODY"][399]["POLE_RA"]
        tkdict["SCLK01_MODULI_32"] == tkdict["SCLK"][-32]["01_MODULI"]
```

Leading and trailing underscores before and after the embedded numeric ID are stripped
from the hierarchical keys, as you can see in the examples above. Note also that the
components of the parameter name are re-ordered in the second example, so that the
second key is always the numeric ID.

When the name associated with a body or frame ID is known, that name can be used in the
place of the integer ID:
```
        tkdict["BODY"][399] == tkdict["BODY"]["EARTH"]
        tkdict["FRAME"][10013] == tkdict["FRAME"]["IAU_EARTH"]
        tkdict["SCLK"][-32] == tkdict["SCLK"]["VOYAGER 2"]
```

If a frame is uniquely or primarily associated with a particular central body, that
body's ID can also be used in place of the frame's ID:
```
        tkdict["FRAME"][399] == tkdict["FRAME"]["IAU_EARTH"]
```

Note that the "BODY" and "FRAME" dictionaries also have an additional entry keyed by "ID",
which returns the associated integer ID:
```
        tkdict["FRAME"][623]["ID"] = 623
        tkdict["FRAME"]["IAU_SUTTUNGR"]["ID"] = 623
```
This ensures that you can look up a body or frame by name and readily obtain its ID.
