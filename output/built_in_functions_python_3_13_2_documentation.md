---
title: Built-in Functions — Python 3.13.2 documentation
source: https://docs.python.org/3/library/functions.html
captured: 2025-03-31 20:24:08
---

[ ![Python logo](../_static/py.svg) ](https://www.python.org/)

Theme  Auto Light Dark

#### Previous topic

[Introduction](intro.html "previous chapter")

#### Next topic

[Built-in Constants](constants.html "next chapter")

### This Page

  * [Report a Bug](../bugs.html)
  * [Show Source ](https://github.com/python/cpython/blob/main/Doc/library/functions.rst)



### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](constants.html "Built-in Constants") |
  * [previous](intro.html "Introduction") |
  * ![Python logo](../_static/py.svg)
  * [Python](https://www.python.org/) »
  *   *   * [3.13.2 Documentation](../index.html) » 
  * [The Python Standard Library](index.html) »
  * [Built-in Functions]()
  * | 
  * Theme  Auto Light Dark |



# Built-in FunctionsÂ¶

The Python interpreter has a number of functions and types built into it that are always available. They are listed here in alphabetical order.

Built-in Functions  
---  
**A** `abs()` `aiter()` `all()` `anext()` `any()` `ascii()`   
**B** `bin()` `bool()` `breakpoint()` `bytearray()` `bytes()`   
**C** `callable()` `chr()` `classmethod()` `compile()` `complex()`   
**D** `delattr()` `dict()` `dir()` `divmod()`   
|  **E** `enumerate()` `eval()` `exec()`   
**F** `filter()` `float()` `format()` `frozenset()`   
**G** `getattr()` `globals()`   
**H** `hasattr()` `hash()` `help()` `hex()`   
**I** `id()` `input()` `int()` `isinstance()` `issubclass()` `iter()` |  **L** `len()` `list()` `locals()`   
**M** `map()` `max()` `memoryview()` `min()`   
**N** `next()`   
**O** `object()` `oct()` `open()` `ord()`   
**P** `pow()` `print()` `property()`   
  
  
  
|  **R** `range()` `repr()` `reversed()` `round()`   
**S** `set()` `setattr()` `slice()` `sorted()` `staticmethod()` `str()` `sum()` `super()`   
**T** `tuple()` `type()`   
**V** `vars()`   
**Z** `zip()`   
**_** `__import__()`  
  
abs(_x_)Â¶
    

Return the absolute value of a number. The argument may be an integer, a floating-point number, or an object implementing [`__abs__()`](../reference/datamodel.html#object.__abs__ "object.__abs__"). If the argument is a complex number, its magnitude is returned.

aiter(_async_iterable_)Â¶
    

Return an [asynchronous iterator](../glossary.html#term-asynchronous-iterator) for an [asynchronous iterable](../glossary.html#term-asynchronous-iterable). Equivalent to calling `x.__aiter__()`.

Note: Unlike `iter()`, `aiter()` has no 2-argument variant.

Added in version 3.10.

all(_iterable_)Â¶
    

Return `True` if all elements of the _iterable_ are true (or if the iterable is empty). Equivalent to:
    
    
    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True
    

_awaitable _anext(_async_iterator_)Â¶
_awaitable _anext(_async_iterator_ , _default_)
    

When awaited, return the next item from the given [asynchronous iterator](../glossary.html#term-asynchronous-iterator), or _default_ if given and the iterator is exhausted.

This is the async variant of the `next()` builtin, and behaves similarly.

This calls the [`__anext__()`](../reference/datamodel.html#object.__anext__ "object.__anext__") method of _async_iterator_ , returning an [awaitable](../glossary.html#term-awaitable). Awaiting this returns the next value of the iterator. If _default_ is given, it is returned if the iterator is exhausted, otherwise [`StopAsyncIteration`](exceptions.html#StopAsyncIteration "StopAsyncIteration") is raised.

Added in version 3.10.

any(_iterable_)Â¶
    

Return `True` if any element of the _iterable_ is true. If the iterable is empty, return `False`. Equivalent to:
    
    
    def any(iterable):
        for element in iterable:
            if element:
                return True
        return False
    

ascii(_object_)Â¶
    

As `repr()`, return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by `repr()` using `\x`, `\u`, or `\U` escapes. This generates a string similar to that returned by `repr()` in Python 2.

bin(_x_)Â¶
    

Convert an integer number to a binary string prefixed with â0bâ. The result is a valid Python expression. If _x_ is not a Python `int` object, it has to define an [`__index__()`](../reference/datamodel.html#object.__index__ "object.__index__") method that returns an integer. Some examples:
    
    
    >>> bin(3)
    '0b11'
    >>> bin(-10)
    '-0b1010'
    

If the prefix â0bâ is desired or not, you can use either of the following ways.
    
    
    >>> format(14, '#b'), format(14, 'b')
    ('0b1110', '1110')
    >>> f'{14:#b}', f'{14:b}'
    ('0b1110', '1110')
    

See also `format()` for more information.

_class _bool(_object =False_, _/_)Â¶
    

Return a Boolean value, i.e. one of `True` or `False`. The argument is converted using the standard [truth testing procedure](stdtypes.html#truth). If the argument is false or omitted, this returns `False`; otherwise, it returns `True`. The `bool` class is a subclass of `int` (see [Numeric Types â int, float, complex](stdtypes.html#typesnumeric)). It cannot be subclassed further. Its only instances are `False` and `True` (see [Boolean Type - bool](stdtypes.html#typebool)).

Changed in version 3.7: The parameter is now positional-only.

breakpoint(_* args_, _** kws_)Â¶
    

This function drops you into the debugger at the call site. Specifically, it calls [`sys.breakpointhook()`](sys.html#sys.breakpointhook "sys.breakpointhook"), passing `args` and `kws` straight through. By default, `sys.breakpointhook()` calls [`pdb.set_trace()`](pdb.html#pdb.set_trace "pdb.set_trace") expecting no arguments. In this case, it is purely a convenience function so you donât have to explicitly import [`pdb`](pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.") or type as much code to enter the debugger. However, [`sys.breakpointhook()`](sys.html#sys.breakpointhook "sys.breakpointhook") can be set to some other function and `breakpoint()` will automatically call that, allowing you to drop into the debugger of choice. If [`sys.breakpointhook()`](sys.html#sys.breakpointhook "sys.breakpointhook") is not accessible, this function will raise [`RuntimeError`](exceptions.html#RuntimeError "RuntimeError").

By default, the behavior of `breakpoint()` can be changed with the [`PYTHONBREAKPOINT`](../using/cmdline.html#envvar-PYTHONBREAKPOINT) environment variable. See [`sys.breakpointhook()`](sys.html#sys.breakpointhook "sys.breakpointhook") for usage details.

Note that this is not guaranteed if [`sys.breakpointhook()`](sys.html#sys.breakpointhook "sys.breakpointhook") has been replaced.

Raises an [auditing event](sys.html#auditing) `builtins.breakpoint` with argument `breakpointhook`.

Added in version 3.7.

_class _bytearray(_source =b''_)
_class _bytearray(_source_ , _encoding_)
_class _bytearray(_source_ , _encoding_ , _errors_)
    

Return a new array of bytes. The [`bytearray`](stdtypes.html#bytearray "bytearray") class is a mutable sequence of integers in the range 0 <= x < 256\. It has most of the usual methods of mutable sequences, described in [Mutable Sequence Types](stdtypes.html#typesseq-mutable), as well as most methods that the [`bytes`](stdtypes.html#bytes "bytes") type has, see [Bytes and Bytearray Operations](stdtypes.html#bytes-methods).

The optional _source_ parameter can be used to initialize the array in a few different ways:

  * If it is a _string_ , you must also give the _encoding_ (and optionally, _errors_) parameters; [`bytearray()`](stdtypes.html#bytearray "bytearray") then converts the string to bytes using [`str.encode()`](stdtypes.html#str.encode "str.encode").

  * If it is an _integer_ , the array will have that size and will be initialized with null bytes.

  * If it is an object conforming to the [buffer interface](../c-api/buffer.html#bufferobjects), a read-only buffer of the object will be used to initialize the bytes array.

  * If it is an _iterable_ , it must be an iterable of integers in the range `0 <= x < 256`, which are used as the initial contents of the array.




Without an argument, an array of size 0 is created.

See also [Binary Sequence Types â bytes, bytearray, memoryview](stdtypes.html#binaryseq) and [Bytearray Objects](stdtypes.html#typebytearray).

_class _bytes(_source =b''_)
_class _bytes(_source_ , _encoding_)
_class _bytes(_source_ , _encoding_ , _errors_)
    

Return a new âbytesâ object which is an immutable sequence of integers in the range `0 <= x < 256`. [`bytes`](stdtypes.html#bytes "bytes") is an immutable version of [`bytearray`](stdtypes.html#bytearray "bytearray") â it has the same non-mutating methods and the same indexing and slicing behavior.

Accordingly, constructor arguments are interpreted as for [`bytearray()`](stdtypes.html#bytearray "bytearray").

Bytes objects can also be created with literals, see [String and Bytes literals](../reference/lexical_analysis.html#strings).

See also [Binary Sequence Types â bytes, bytearray, memoryview](stdtypes.html#binaryseq), [Bytes Objects](stdtypes.html#typebytes), and [Bytes and Bytearray Operations](stdtypes.html#bytes-methods).

callable(_object_)Â¶
    

Return [`True`](constants.html#True "True") if the _object_ argument appears callable, [`False`](constants.html#False "False") if not. If this returns `True`, it is still possible that a call fails, but if it is `False`, calling _object_ will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a [`__call__()`](../reference/datamodel.html#object.__call__ "object.__call__") method.

Added in version 3.2: This function was first removed in Python 3.0 and then brought back in Python 3.2.

chr(_i_)Â¶
    

Return the string representing a character whose Unicode code point is the integer _i_. For example, `chr(97)` returns the string `'a'`, while `chr(8364)` returns the string `'â¬'`. This is the inverse of `ord()`.

The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). [`ValueError`](exceptions.html#ValueError "ValueError") will be raised if _i_ is outside that range.

@classmethodÂ¶
    

Transform a method into a class method.

A class method receives the class as an implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:
    
    
    class C:
        @classmethod
        def f(cls, arg1, arg2): ...
    

The `@classmethod` form is a function [decorator](../glossary.html#term-decorator) â see [Function definitions](../reference/compound_stmts.html#function) for details.

A class method can be called either on the class (such as `C.f()`) or on an instance (such as `C().f()`). The instance is ignored except for its class. If a class method is called for a derived class, the derived class object is passed as the implied first argument.

Class methods are different than C++ or Java static methods. If you want those, see `staticmethod()` in this section. For more information on class methods, see [The standard type hierarchy](../reference/datamodel.html#types).

Changed in version 3.9: Class methods can now wrap other [descriptors](../glossary.html#term-descriptor) such as `property()`.

Changed in version 3.10: Class methods now inherit the method attributes ([`__module__`](../reference/datamodel.html#function.__module__ "function.__module__"), [`__name__`](../reference/datamodel.html#function.__name__ "function.__name__"), [`__qualname__`](../reference/datamodel.html#function.__qualname__ "function.__qualname__"), [`__doc__`](../reference/datamodel.html#function.__doc__ "function.__doc__") and [`__annotations__`](../reference/datamodel.html#function.__annotations__ "function.__annotations__")) and have a new `__wrapped__` attribute.

Deprecated since version 3.11, removed in version 3.13: Class methods can no longer wrap other [descriptors](../glossary.html#term-descriptor) such as `property()`.

compile(_source_ , _filename_ , _mode_ , _flags =0_, _dont_inherit =False_, _optimize =-1_)Â¶
    

Compile the _source_ into a code or AST object. Code objects can be executed by `exec()` or `eval()`. _source_ can either be a normal string, a byte string, or an AST object. Refer to the [`ast`](ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") module documentation for information on how to work with AST objects.

The _filename_ argument should give the file from which the code was read; pass some recognizable value if it wasnât read from a file (`'<string>'` is commonly used).

The _mode_ argument specifies what kind of code must be compiled; it can be `'exec'` if _source_ consists of a sequence of statements, `'eval'` if it consists of a single expression, or `'single'` if it consists of a single interactive statement (in the latter case, expression statements that evaluate to something other than `None` will be printed).

The optional arguments _flags_ and _dont_inherit_ control which [compiler options](ast.html#ast-compiler-flags) should be activated and which [future features](../reference/simple_stmts.html#future) should be allowed. If neither is present (or both are zero) the code is compiled with the same flags that affect the code that is calling `compile()`. If the _flags_ argument is given and _dont_inherit_ is not (or is zero) then the compiler options and the future statements specified by the _flags_ argument are used in addition to those that would be used anyway. If _dont_inherit_ is a non-zero integer then the _flags_ argument is it â the flags (future features and compiler options) in the surrounding code are ignored.

Compiler options and future statements are specified by bits which can be bitwise ORed together to specify multiple options. The bitfield required to specify a given future feature can be found as the [`compiler_flag`](__future__.html#future__._Feature.compiler_flag "__future__._Feature.compiler_flag") attribute on the [`_Feature`](__future__.html#future__._Feature "__future__._Feature") instance in the [`__future__`](__future__.html#module-__future__ "__future__: Future statement definitions") module. [Compiler flags](ast.html#ast-compiler-flags) can be found in [`ast`](ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") module, with `PyCF_` prefix.

The argument _optimize_ specifies the optimization level of the compiler; the default value of `-1` selects the optimization level of the interpreter as given by [`-O`](../using/cmdline.html#cmdoption-O) options. Explicit levels are `0` (no optimization; `__debug__` is true), `1` (asserts are removed, `__debug__` is false) or `2` (docstrings are removed too).

This function raises [`SyntaxError`](exceptions.html#SyntaxError "SyntaxError") if the compiled source is invalid, and [`ValueError`](exceptions.html#ValueError "ValueError") if the source contains null bytes.

If you want to parse Python code into its AST representation, see [`ast.parse()`](ast.html#ast.parse "ast.parse").

Raises an [auditing event](sys.html#auditing) `compile` with arguments `source` and `filename`. This event may also be raised by implicit compilation.

Note

When compiling a string with multi-line code in `'single'` or `'eval'` mode, input must be terminated by at least one newline character. This is to facilitate detection of incomplete and complete statements in the [`code`](code.html#module-code "code: Facilities to implement read-eval-print loops.") module.

Warning

It is possible to crash the Python interpreter with a sufficiently large/complex string when compiling to an AST object due to stack depth limitations in Pythonâs AST compiler.

Changed in version 3.2: Allowed use of Windows and Mac newlines. Also, input in `'exec'` mode does not have to end in a newline anymore. Added the _optimize_ parameter.

Changed in version 3.5: Previously, [`TypeError`](exceptions.html#TypeError "TypeError") was raised when null bytes were encountered in _source_.

Added in version 3.8: `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` can now be passed in flags to enable support for top-level `await`, `async for`, and `async with`.

_class _complex(_number =0_, _/_)Â¶
_class _complex(_string_ , _/_)
_class _complex(_real =0_, _imag =0_)
    

Convert a single string or number to a complex number, or create a complex number from real and imaginary parts.

Examples:
    
    
    >>> complex('+1.23')
    (1.23+0j)
    >>> complex('-4.5j')
    -4.5j
    >>> complex('-1.23+4.5j')
    (-1.23+4.5j)
    >>> complex('\t( -1.23+4.5J )\n')
    (-1.23+4.5j)
    >>> complex('-Infinity+NaNj')
    (-inf+nanj)
    >>> complex(1.23)
    (1.23+0j)
    >>> complex(imag=-4.5)
    -4.5j
    >>> complex(-1.23, 4.5)
    (-1.23+4.5j)
    

If the argument is a string, it must contain either a real part (in the same format as for `float()`) or an imaginary part (in the same format but with a `'j'` or `'J'` suffix), or both real and imaginary parts (the sign of the imaginary part is mandatory in this case). The string can optionally be surrounded by whitespaces and the round parentheses `'('` and `')'`, which are ignored. The string must not contain whitespace between `'+'`, `'-'`, the `'j'` or `'J'` suffix, and the decimal number. For example, `complex('1+2j')` is fine, but `complex('1 + 2j')` raises [`ValueError`](exceptions.html#ValueError "ValueError"). More precisely, the input must conform to the `complexvalue` production rule in the following grammar, after parentheses and leading and trailing whitespace characters are removed:
    
    
    **complexvalue** ::= floatvalue |
                     floatvalue ("j" | "J") |
                     floatvalue sign absfloatvalue ("j" | "J")
    

If the argument is a number, the constructor serves as a numeric conversion like `int` and `float`. For a general Python object `x`, `complex(x)` delegates to `x.__complex__()`. If [`__complex__()`](../reference/datamodel.html#object.__complex__ "object.__complex__") is not defined then it falls back to [`__float__()`](../reference/datamodel.html#object.__float__ "object.__float__"). If `__float__()` is not defined then it falls back to [`__index__()`](../reference/datamodel.html#object.__index__ "object.__index__").

If two arguments are provided or keyword arguments are used, each argument may be any numeric type (including complex). If both arguments are real numbers, return a complex number with the real component _real_ and the imaginary component _imag_. If both arguments are complex numbers, return a complex number with the real component `real.real-imag.imag` and the imaginary component `real.imag+imag.real`. If one of arguments is a real number, only its real component is used in the above expressions.

If all arguments are omitted, returns `0j`.

The complex type is described in [Numeric Types â int, float, complex](stdtypes.html#typesnumeric).

Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.

Changed in version 3.8: Falls back to [`__index__()`](../reference/datamodel.html#object.__index__ "object.__index__") if [`__complex__()`](../reference/datamodel.html#object.__complex__ "object.__complex__") and [`__float__()`](../reference/datamodel.html#object.__float__ "object.__float__") are not defined.

delattr(_object_ , _name_)Â¶
    

This is a relative of `setattr()`. The arguments are an object and a string. The string must be the name of one of the objectâs attributes. The function deletes the named attribute, provided the object allows it. For example, `delattr(x, 'foobar')` is equivalent to `del x.foobar`. _name_ need not be a Python identifier (see `setattr()`).

_class _dict(_** kwarg_)
_class _dict(_mapping_ , _** kwarg_)
_class _dict(_iterable_ , _** kwarg_)
    

Create a new dictionary. The [`dict`](stdtypes.html#dict "dict") object is the dictionary class. See [`dict`](stdtypes.html#dict "dict") and [Mapping Types â dict](stdtypes.html#typesmapping) for documentation about this class.

For other containers see the built-in [`list`](stdtypes.html#list "list"), [`set`](stdtypes.html#set "set"), and [`tuple`](stdtypes.html#tuple "tuple") classes, as well as the [`collections`](collections.html#module-collections "collections: Container datatypes") module.

dir()Â¶
dir(_object_)
    

Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.

If the object has a method named [`__dir__()`](../reference/datamodel.html#object.__dir__ "object.__dir__"), this method will be called and must return the list of attributes. This allows objects that implement a custom [`__getattr__()`](../reference/datamodel.html#object.__getattr__ "object.__getattr__") or [`__getattribute__()`](../reference/datamodel.html#object.__getattribute__ "object.__getattribute__") function to customize the way `dir()` reports their attributes.

If the object does not provide [`__dir__()`](../reference/datamodel.html#object.__dir__ "object.__dir__"), the function tries its best to gather information from the objectâs [`__dict__`](../reference/datamodel.html#object.__dict__ "object.__dict__") attribute, if defined, and from its type object. The resulting list is not necessarily complete and may be inaccurate when the object has a custom [`__getattr__()`](../reference/datamodel.html#object.__getattr__ "object.__getattr__").

The default `dir()` mechanism behaves differently with different types of objects, as it attempts to produce the most relevant, rather than complete, information:

  * If the object is a module object, the list contains the names of the moduleâs attributes.

  * If the object is a type or class object, the list contains the names of its attributes, and recursively of the attributes of its bases.

  * Otherwise, the list contains the objectâs attributesâ names, the names of its classâs attributes, and recursively of the attributes of its classâs base classes.




The resulting list is sorted alphabetically. For example:
    
    
    >>> import struct
    >>> dir()   # show the names in the module namespace
    ['__builtins__', '__name__', 'struct']
    >>> dir(struct)   # show the names in the struct module
    ['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
     '__initializing__', '__loader__', '__name__', '__package__',
     '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
     'unpack', 'unpack_from']
    >>> class Shape:
    ...     def __dir__(self):
    ...         return ['area', 'perimeter', 'location']
    ...
    >>> s = Shape()
    >>> dir(s)
    ['area', 'location', 'perimeter']
    

Note

Because `dir()` is supplied primarily as a convenience for use at an interactive prompt, it tries to supply an interesting set of names more than it tries to supply a rigorously or consistently defined set of names, and its detailed behavior may change across releases. For example, metaclass attributes are not in the result list when the argument is a class.

divmod(_a_ , _b_)Â¶
    

Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division. With mixed operand types, the rules for binary arithmetic operators apply. For integers, the result is the same as `(a // b, a % b)`. For floating-point numbers the result is `(q, a % b)`, where _q_ is usually `math.floor(a / b)` but may be 1 less than that. In any case `q * b + a % b` is very close to _a_ , if `a % b` is non-zero it has the same sign as _b_ , and `0 <= abs(a % b) < abs(b)`.

enumerate(_iterable_ , _start =0_)Â¶
    

Return an enumerate object. _iterable_ must be a sequence, an [iterator](../glossary.html#term-iterator), or some other object which supports iteration. The [`__next__()`](stdtypes.html#iterator.__next__ "iterator.__next__") method of the iterator returned by `enumerate()` returns a tuple containing a count (from _start_ which defaults to 0) and the values obtained from iterating over _iterable_.
    
    
    >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    >>> list(enumerate(seasons, start=1))
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
    

Equivalent to:
    
    
    def enumerate(iterable, start=0):
        n = start
        for elem in iterable:
            yield n, elem
            n += 1
    

eval(_source_ , _/_ , _globals =None_, _locals =None_)Â¶
    

Parameters:
    

  * **source** ([`str`](stdtypes.html#str "str") | [code object](../reference/datamodel.html#code-objects)) â A Python expression.

  * **globals** ([`dict`](stdtypes.html#dict "dict") | `None`) â The global namespace (default: `None`).

  * **locals** ([mapping](../glossary.html#term-mapping) | `None`) â The local namespace (default: `None`).



Returns:
    

The result of the evaluated expression.

Raises:
    

Syntax errors are reported as exceptions.

Warning

This function executes arbitrary code. Calling it with user-supplied input may lead to security vulnerabilities.

The _expression_ argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the _globals_ and _locals_ mappings as global and local namespace. If the _globals_ dictionary is present and does not contain a value for the key `__builtins__`, a reference to the dictionary of the built-in module [`builtins`](builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") is inserted under that key before _expression_ is parsed. That way you can control what builtins are available to the executed code by inserting your own `__builtins__` dictionary into _globals_ before passing it to `eval()`. If the _locals_ mapping is omitted it defaults to the _globals_ dictionary. If both mappings are omitted, the expression is executed with the _globals_ and _locals_ in the environment where `eval()` is called. Note, _eval()_ will only have access to the [nested scopes](../glossary.html#term-nested-scope) (non-locals) in the enclosing environment if they are already referenced in the scope that is calling `eval()` (e.g. via a [`nonlocal`](../reference/simple_stmts.html#nonlocal) statement).

Example:
    
    
    >>> x = 1
    >>> eval('x+1')
    2
    

This function can also be used to execute arbitrary code objects (such as those created by `compile()`). In this case, pass a code object instead of a string. If the code object has been compiled with `'exec'` as the _mode_ argument, `eval()`'s return value will be `None`.

Hints: dynamic execution of statements is supported by the `exec()` function. The `globals()` and `locals()` functions return the current global and local dictionary, respectively, which may be useful to pass around for use by `eval()` or `exec()`.

If the given source is a string, then leading and trailing spaces and tabs are stripped.

See [`ast.literal_eval()`](ast.html#ast.literal_eval "ast.literal_eval") for a function that can safely evaluate strings with expressions containing only literals.

Raises an [auditing event](sys.html#auditing) `exec` with the code object as the argument. Code compilation events may also be raised.

Changed in version 3.13: The _globals_ and _locals_ arguments can now be passed as keywords.

Changed in version 3.13: The semantics of the default _locals_ namespace have been adjusted as described for the `locals()` builtin.

exec(_source_ , _/_ , _globals =None_, _locals =None_, _*_ , _closure =None_)Â¶
    

Warning

This function executes arbitrary code. Calling it with user-supplied input may lead to security vulnerabilities.

This function supports dynamic execution of Python code. _source_ must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). [1] If it is a code object, it is simply executed. In all cases, the code thatâs executed is expected to be valid as file input (see the section [File input](../reference/toplevel_components.html#file-input) in the Reference Manual). Be aware that the [`nonlocal`](../reference/simple_stmts.html#nonlocal), [`yield`](../reference/simple_stmts.html#yield), and [`return`](../reference/simple_stmts.html#return) statements may not be used outside of function definitions even within the context of code passed to the `exec()` function. The return value is `None`.

In all cases, if the optional parts are omitted, the code is executed in the current scope. If only _globals_ is provided, it must be a dictionary (and not a subclass of dictionary), which will be used for both the global and the local variables. If _globals_ and _locals_ are given, they are used for the global and local variables, respectively. If provided, _locals_ can be any mapping object. Remember that at the module level, globals and locals are the same dictionary.

Note

When `exec` gets two separate objects as _globals_ and _locals_ , the code will be executed as if it were embedded in a class definition. This means functions and classes defined in the executed code will not be able to access variables assigned at the top level (as the âtop levelâ variables are treated as class variables in a class definition).

If the _globals_ dictionary does not contain a value for the key `__builtins__`, a reference to the dictionary of the built-in module [`builtins`](builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") is inserted under that key. That way you can control what builtins are available to the executed code by inserting your own `__builtins__` dictionary into _globals_ before passing it to `exec()`.

The _closure_ argument specifies a closureâa tuple of cellvars. Itâs only valid when the _object_ is a code object containing [free (closure) variables](../glossary.html#term-closure-variable). The length of the tuple must exactly match the length of the code objectâs [`co_freevars`](../reference/datamodel.html#codeobject.co_freevars "codeobject.co_freevars") attribute.

Raises an [auditing event](sys.html#auditing) `exec` with the code object as the argument. Code compilation events may also be raised.

Note

The built-in functions `globals()` and `locals()` return the current global and local namespace, respectively, which may be useful to pass around for use as the second and third argument to `exec()`.

Note

The default _locals_ act as described for function `locals()` below. Pass an explicit _locals_ dictionary if you need to see effects of the code on _locals_ after function `exec()` returns.

Changed in version 3.11: Added the _closure_ parameter.

Changed in version 3.13: The _globals_ and _locals_ arguments can now be passed as keywords.

Changed in version 3.13: The semantics of the default _locals_ namespace have been adjusted as described for the `locals()` builtin.

filter(_function_ , _iterable_)Â¶
    

Construct an iterator from those elements of _iterable_ for which _function_ is true. _iterable_ may be either a sequence, a container which supports iteration, or an iterator. If _function_ is `None`, the identity function is assumed, that is, all elements of _iterable_ that are false are removed.

Note that `filter(function, iterable)` is equivalent to the generator expression `(item for item in iterable if function(item))` if function is not `None` and `(item for item in iterable if item)` if function is `None`.

See [`itertools.filterfalse()`](itertools.html#itertools.filterfalse "itertools.filterfalse") for the complementary function that returns elements of _iterable_ for which _function_ is false.

_class _float(_number =0.0_, _/_)Â¶
_class _float(_string_ , _/_)
    

Return a floating-point number constructed from a number or a string.

Examples:
    
    
    >>> float('+1.23')
    1.23
    >>> float('   -12345\n')
    -12345.0
    >>> float('1e-003')
    0.001
    >>> float('+1E6')
    1000000.0
    >>> float('-Infinity')
    -inf
    

If the argument is a string, it should contain a decimal number, optionally preceded by a sign, and optionally embedded in whitespace. The optional sign may be `'+'` or `'-'`; a `'+'` sign has no effect on the value produced. The argument may also be a string representing a NaN (not-a-number), or positive or negative infinity. More precisely, the input must conform to the `floatvalue` production rule in the following grammar, after leading and trailing whitespace characters are removed:
    
    
    **sign**          ::= "+" | "-"
    **infinity**      ::= "Infinity" | "inf"
    **nan**           ::= "nan"
    **digit**         ::= <a Unicode decimal digit, i.e. characters in Unicode general category Nd>
    **digitpart**     ::= digit (["_"] digit)*
    **number**        ::= [digitpart] "." digitpart | digitpart ["."]
    **exponent**      ::= ("e" | "E") [sign] digitpart
    **floatnumber**   ::= number [exponent]
    **absfloatvalue** ::= floatnumber | infinity | nan
    **floatvalue**    ::= [sign] absfloatvalue
    

Case is not significant, so, for example, âinfâ, âInfâ, âINFINITYâ, and âiNfINityâ are all acceptable spellings for positive infinity.

Otherwise, if the argument is an integer or a floating-point number, a floating-point number with the same value (within Pythonâs floating-point precision) is returned. If the argument is outside the range of a Python float, an [`OverflowError`](exceptions.html#OverflowError "OverflowError") will be raised.

For a general Python object `x`, `float(x)` delegates to `x.__float__()`. If [`__float__()`](../reference/datamodel.html#object.__float__ "object.__float__") is not defined then it falls back to [`__index__()`](../reference/datamodel.html#object.__index__ "object.__index__").

If no argument is given, `0.0` is returned.

The float type is described in [Numeric Types â int, float, complex](stdtypes.html#typesnumeric).

Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.

Changed in version 3.7: The parameter is now positional-only.

Changed in version 3.8: Falls back to [`__index__()`](../reference/datamodel.html#object.__index__ "object.__index__") if [`__float__()`](../reference/datamodel.html#object.__float__ "object.__float__") is not defined.

format(_value_ , _format_spec =''_)Â¶
    

Convert a _value_ to a âformattedâ representation, as controlled by _format_spec_. The interpretation of _format_spec_ will depend on the type of the _value_ argument; however, there is a standard formatting syntax that is used by most built-in types: [Format Specification Mini-Language](string.html#formatspec).

The default _format_spec_ is an empty string which usually gives the same effect as calling [`str(value)`](stdtypes.html#str "str").

A call to `format(value, format_spec)` is translated to `type(value).__format__(value, format_spec)` which bypasses the instance dictionary when searching for the valueâs [`__format__()`](../reference/datamodel.html#object.__format__ "object.__format__") method. A [`TypeError`](exceptions.html#TypeError "TypeError") exception is raised if the method search reaches `object` and the _format_spec_ is non-empty, or if either the _format_spec_ or the return value are not strings.

Changed in version 3.4: `object().__format__(format_spec)` raises [`TypeError`](exceptions.html#TypeError "TypeError") if _format_spec_ is not an empty string.

_class _frozenset(_iterable =set()_)
    

Return a new [`frozenset`](stdtypes.html#frozenset "frozenset") object, optionally with elements taken from _iterable_. `frozenset` is a built-in class. See [`frozenset`](stdtypes.html#frozenset "frozenset") and [Set Types â set, frozenset](stdtypes.html#types-set) for documentation about this class.

For other containers see the built-in [`set`](stdtypes.html#set "set"), [`list`](stdtypes.html#list "list"), [`tuple`](stdtypes.html#tuple "tuple"), and [`dict`](stdtypes.html#dict "dict") classes, as well as the [`collections`](collections.html#module-collections "collections: Container datatypes") module.

getattr(_object_ , _name_)Â¶
getattr(_object_ , _name_ , _default_)
    

Return the value of the named attribute of _object_. _name_ must be a string. If the string is the name of one of the objectâs attributes, the result is the value of that attribute. For example, `getattr(x, 'foobar')` is equivalent to `x.foobar`. If the named attribute does not exist, _default_ is returned if provided, otherwise [`AttributeError`](exceptions.html#AttributeError "AttributeError") is raised. _name_ need not be a Python identifier (see `setattr()`).

Note

Since [private name mangling](../reference/expressions.html#private-name-mangling) happens at compilation time, one must manually mangle a private attributeâs (attributes with two leading underscores) name in order to retrieve it with `getattr()`.

globals()Â¶
    

Return the dictionary implementing the current module namespace. For code within functions, this is set when the function is defined and remains the same regardless of where the function is called.

hasattr(_object_ , _name_)Â¶
    

The arguments are an object and a string. The result is `True` if the string is the name of one of the objectâs attributes, `False` if not. (This is implemented by calling `getattr(object, name)` and seeing whether it raises an [`AttributeError`](exceptions.html#AttributeError "AttributeError") or not.)

hash(_object_)Â¶
    

Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).

Note

For objects with custom [`__hash__()`](../reference/datamodel.html#object.__hash__ "object.__hash__") methods, note that `hash()` truncates the return value based on the bit width of the host machine.

help()Â¶
help(_request_)
    

Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object is generated.

Note that if a slash(/) appears in the parameter list of a function when invoking `help()`, it means that the parameters prior to the slash are positional-only. For more info, see [the FAQ entry on positional-only parameters](../faq/programming.html#faq-positional-only-arguments).

This function is added to the built-in namespace by the [`site`](site.html#module-site "site: Module responsible for site-specific configuration.") module.

Changed in version 3.4: Changes to [`pydoc`](pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.") and [`inspect`](inspect.html#module-inspect "inspect: Extract information and source code from live objects.") mean that the reported signatures for callables are now more comprehensive and consistent.

hex(_x_)Â¶
    

Convert an integer number to a lowercase hexadecimal string prefixed with â0xâ. If _x_ is not a Python `int` object, it has to define an [`__index__()`](../reference/datamodel.html#object.__index__ "object.__index__") method that returns an integer. Some examples:
    
    
    >>> hex(255)
    '0xff'
    >>> hex(-42)
    '-0x2a'
    

If you want to convert an integer number to an uppercase or lower hexadecimal string with prefix or not, you can use either of the following ways:
    
    
    >>> '%#x' % 255, '%x' % 255, '%X' % 255
    ('0xff', 'ff', 'FF')
    >>> format(255, '#x'), format(255, 'x'), format(255, 'X')
    ('0xff', 'ff', 'FF')
    >>> f'{255:#x}', f'{255:x}', f'{255:X}'
    ('0xff', 'ff', 'FF')
    

See also `format()` for more information.

See also `int()` for converting a hexadecimal string to an integer using a base of 16.

Note

To obtain a hexadecimal string representation for a float, use the [`float.hex()`](stdtypes.html#float.hex "float.hex") method.

id(_object_)Â¶
    

Return the âidentityâ of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same `id()` value.

**CPython implementation detail:** This is the address of the object in memory.

Raises an [auditing event](sys.html#auditing) `builtins.id` with argument `id`.

input()Â¶
input(_prompt_)
    

If the _prompt_ argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, [`EOFError`](exceptions.html#EOFError "EOFError") is raised. Example:
    
    
    >>> s = input('--> ')
    --> Monty Python's Flying Circus
    >>> s
    "Monty Python's Flying Circus"
    

If the [`readline`](readline.html#module-readline "readline: GNU readline support for Python. \(Unix\)") module was loaded, then `input()` will use it to provide elaborate line editing and history features.

Raises an [auditing event](sys.html#auditing) `builtins.input` with argument `prompt` before reading input

Raises an [auditing event](sys.html#auditing) `builtins.input/result` with the result after successfully reading input.

_class _int(_number =0_, _/_)Â¶
_class _int(_string_ , _/_ , _base =10_)
    

Return an integer object constructed from a number or a string, or return `0` if no arguments are given.

Examples:
    
    
    >>> int(123.45)
    123
    >>> int('123')
    123
    >>> int('   -12_345\n')
    -12345
    >>> int('FACE', 16)
    64206
    >>> int('0xface', 0)
    64206
    >>> int('01110011', base=2)
    115
    

If the argument defines [`__int__()`](../reference/datamodel.html#object.__int__ "object.__int__"), `int(x)` returns `x.__int__()`. If the argument defines [`__index__()`](../reference/datamodel.html#object.__index__ "object.__index__"), it returns `x.__index__()`. If the argument defines [`__trunc__()`](../reference/datamodel.html#object.__trunc__ "object.__trunc__"), it returns `x.__trunc__()`. For floating-point numbers, this truncates towards zero.

If the argument is not a number or if _base_ is given, then it must be a string, [`bytes`](stdtypes.html#bytes "bytes"), or [`bytearray`](stdtypes.html#bytearray "bytearray") instance representing an integer in radix _base_. Optionally, the string can be preceded by `+` or `-` (with no space in between), have leading zeros, be surrounded by whitespace, and have single underscores interspersed between digits.

A base-n integer string contains digits, each representing a value from 0 to n-1. The values 0â9 can be represented by any Unicode decimal digit. The values 10â35 can be represented by `a` to `z` (or `A` to `Z`). The default _base_ is 10. The allowed bases are 0 and 2â36. Base-2, -8, and -16 strings can be optionally prefixed with `0b`/`0B`, `0o`/`0O`, or `0x`/`0X`, as with integer literals in code. For base 0, the string is interpreted in a similar way to an [integer literal in code](../reference/lexical_analysis.html#integers), in that the actual base is 2, 8, 10, or 16 as determined by the prefix. Base 0 also disallows leading zeros: `int('010', 0)` is not legal, while `int('010')` and `int('010', 8)` are.

The integer type is described in [Numeric Types â int, float, complex](stdtypes.html#typesnumeric).

Changed in version 3.4: If _base_ is not an instance of `int` and the _base_ object has a [`base.__index__`](../reference/datamodel.html#object.__index__ "object.__index__") method, that method is called to obtain an integer for the base. Previous versions used [`base.__int__`](../reference/datamodel.html#object.__int__ "object.__int__") instead of [`base.__index__`](../reference/datamodel.html#object.__index__ "object.__index__").

Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.

Changed in version 3.7: The first parameter is now positional-only.

Changed in version 3.8: Falls back to [`__index__()`](../reference/datamodel.html#object.__index__ "object.__index__") if [`__int__()`](../reference/datamodel.html#object.__int__ "object.__int__") is not defined.

Changed in version 3.11: The delegation to [`__trunc__()`](../reference/datamodel.html#object.__trunc__ "object.__trunc__") is deprecated.

Changed in version 3.11: `int` string inputs and string representations can be limited to help avoid denial of service attacks. A [`ValueError`](exceptions.html#ValueError "ValueError") is raised when the limit is exceeded while converting a string to an `int` or when converting an `int` into a string would exceed the limit. See the [integer string conversion length limitation](stdtypes.html#int-max-str-digits) documentation.

isinstance(_object_ , _classinfo_)Â¶
    

Return `True` if the _object_ argument is an instance of the _classinfo_ argument, or of a (direct, indirect, or [virtual](../glossary.html#term-abstract-base-class)) subclass thereof. If _object_ is not an object of the given type, the function always returns `False`. If _classinfo_ is a tuple of type objects (or recursively, other such tuples) or a [Union Type](stdtypes.html#types-union) of multiple types, return `True` if _object_ is an instance of any of the types. If _classinfo_ is not a type or tuple of types and such tuples, a [`TypeError`](exceptions.html#TypeError "TypeError") exception is raised. [`TypeError`](exceptions.html#TypeError "TypeError") may not be raised for an invalid type if an earlier check succeeds.

Changed in version 3.10: _classinfo_ can be a [Union Type](stdtypes.html#types-union).

issubclass(_class_ , _classinfo_)Â¶
    

Return `True` if _class_ is a subclass (direct, indirect, or [virtual](../glossary.html#term-abstract-base-class)) of _classinfo_. A class is considered a subclass of itself. _classinfo_ may be a tuple of class objects (or recursively, other such tuples) or a [Union Type](stdtypes.html#types-union), in which case return `True` if _class_ is a subclass of any entry in _classinfo_. In any other case, a [`TypeError`](exceptions.html#TypeError "TypeError") exception is raised.

Changed in version 3.10: _classinfo_ can be a [Union Type](stdtypes.html#types-union).

iter(_object_)Â¶
iter(_object_ , _sentinel_)
    

Return an [iterator](../glossary.html#term-iterator) object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, _object_ must be a collection object which supports the [iterable](../glossary.html#term-iterable) protocol (the [`__iter__()`](../reference/datamodel.html#object.__iter__ "object.__iter__") method), or it must support the sequence protocol (the [`__getitem__()`](../reference/datamodel.html#object.__getitem__ "object.__getitem__") method with integer arguments starting at `0`). If it does not support either of those protocols, [`TypeError`](exceptions.html#TypeError "TypeError") is raised. If the second argument, _sentinel_ , is given, then _object_ must be a callable object. The iterator created in this case will call _object_ with no arguments for each call to its [`__next__()`](stdtypes.html#iterator.__next__ "iterator.__next__") method; if the value returned is equal to _sentinel_ , [`StopIteration`](exceptions.html#StopIteration "StopIteration") will be raised, otherwise the value will be returned.

See also [Iterator Types](stdtypes.html#typeiter).

One useful application of the second form of `iter()` is to build a block-reader. For example, reading fixed-width blocks from a binary database file until the end of file is reached:
    
    
    from functools import partial
    with open('mydata.db', 'rb') as f:
        for block in iter(partial(f.read, 64), b''):
            process_block(block)
    

len(_s_)Â¶
    

Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

**CPython implementation detail:** `len` raises [`OverflowError`](exceptions.html#OverflowError "OverflowError") on lengths larger than [`sys.maxsize`](sys.html#sys.maxsize "sys.maxsize"), such as [`range(2 ** 100)`](stdtypes.html#range "range").

_class _list
_class _list(_iterable_)
    

Rather than being a function, [`list`](stdtypes.html#list "list") is actually a mutable sequence type, as documented in [Lists](stdtypes.html#typesseq-list) and [Sequence Types â list, tuple, range](stdtypes.html#typesseq).

locals()Â¶
    

> Return a mapping object representing the current local symbol table, with variable names as the keys, and their currently bound references as the values.
> 
> At module scope, as well as when using `exec()` or `eval()` with a single namespace, this function returns the same namespace as `globals()`.
> 
> At class scope, it returns the namespace that will be passed to the metaclass constructor.
> 
> When using `exec()` or `eval()` with separate local and global arguments, it returns the local namespace passed in to the function call.
> 
> In all of the above cases, each call to `locals()` in a given frame of execution will return the _same_ mapping object. Changes made through the mapping object returned from `locals()` will be visible as assigned, reassigned, or deleted local variables, and assigning, reassigning, or deleting local variables will immediately affect the contents of the returned mapping object.
> 
> In an [optimized scope](../glossary.html#term-optimized-scope) (including functions, generators, and coroutines), each call to `locals()` instead returns a fresh dictionary containing the current bindings of the functionâs local variables and any nonlocal cell references. In this case, name binding changes made via the returned dict are _not_ written back to the corresponding local variables or nonlocal cell references, and assigning, reassigning, or deleting local variables and nonlocal cell references does _not_ affect the contents of previously returned dictionaries.
> 
> Calling `locals()` as part of a comprehension in a function, generator, or coroutine is equivalent to calling it in the containing scope, except that the comprehensionâs initialised iteration variables will be included. In other scopes, it behaves as if the comprehension were running as a nested function.
> 
> Calling `locals()` as part of a generator expression is equivalent to calling it in a nested generator function.

Changed in version 3.12: The behaviour of `locals()` in a comprehension has been updated as described in [**PEP 709**](https://peps.python.org/pep-0709/).

Changed in version 3.13: As part of [**PEP 667**](https://peps.python.org/pep-0667/), the semantics of mutating the mapping objects returned from this function are now defined. The behavior in [optimized scopes](../glossary.html#term-optimized-scope) is now as described above. Aside from being defined, the behaviour in other scopes remains unchanged from previous versions.

map(_function_ , _iterable_ , _* iterables_)Â¶
    

Return an iterator that applies _function_ to every item of _iterable_ , yielding the results. If additional _iterables_ arguments are passed, _function_ must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see [`itertools.starmap()`](itertools.html#itertools.starmap "itertools.starmap").

max(_iterable_ , _*_ , _key =None_)Â¶
max(_iterable_ , _*_ , _default_ , _key =None_)
max(_arg1_ , _arg2_ , _* args_, _key =None_)
    

Return the largest item in an iterable or the largest of two or more arguments.

If one positional argument is provided, it should be an [iterable](../glossary.html#term-iterable). The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.

There are two optional keyword-only arguments. The _key_ argument specifies a one-argument ordering function like that used for [`list.sort()`](stdtypes.html#list.sort "list.sort"). The _default_ argument specifies an object to return if the provided iterable is empty. If the iterable is empty and _default_ is not provided, a [`ValueError`](exceptions.html#ValueError "ValueError") is raised.

If multiple items are maximal, the function returns the first one encountered. This is consistent with other sort-stability preserving tools such as `sorted(iterable, key=keyfunc, reverse=True)[0]` and `heapq.nlargest(1, iterable, key=keyfunc)`.

Changed in version 3.4: Added the _default_ keyword-only parameter.

Changed in version 3.8: The _key_ can be `None`.

_class _memoryview(_object_)
    

Return a âmemory viewâ object created from the given argument. See [Memory Views](stdtypes.html#typememoryview) for more information.

min(_iterable_ , _*_ , _key =None_)Â¶
min(_iterable_ , _*_ , _default_ , _key =None_)
min(_arg1_ , _arg2_ , _* args_, _key =None_)
    

Return the smallest item in an iterable or the smallest of two or more arguments.

If one positional argument is provided, it should be an [iterable](../glossary.html#term-iterable). The smallest item in the iterable is returned. If two or more positional arguments are provided, the smallest of the positional arguments is returned.

There are two optional keyword-only arguments. The _key_ argument specifies a one-argument ordering function like that used for [`list.sort()`](stdtypes.html#list.sort "list.sort"). The _default_ argument specifies an object to return if the provided iterable is empty. If the iterable is empty and _default_ is not provided, a [`ValueError`](exceptions.html#ValueError "ValueError") is raised.

If multiple items are minimal, the function returns the first one encountered. This is consistent with other sort-stability preserving tools such as `sorted(iterable, key=keyfunc)[0]` and `heapq.nsmallest(1, iterable, key=keyfunc)`.

Changed in version 3.4: Added the _default_ keyword-only parameter.

Changed in version 3.8: The _key_ can be `None`.

next(_iterator_)Â¶
next(_iterator_ , _default_)
    

Retrieve the next item from the [iterator](../glossary.html#term-iterator) by calling its [`__next__()`](stdtypes.html#iterator.__next__ "iterator.__next__") method. If _default_ is given, it is returned if the iterator is exhausted, otherwise [`StopIteration`](exceptions.html#StopIteration "StopIteration") is raised.

_class _objectÂ¶
    

This is the ultimate base class of all other classes. It has methods that are common to all instances of Python classes. When the constructor is called, it returns a new featureless object. The constructor does not accept any arguments.

Note

`object` instances do _not_ have [`__dict__`](../reference/datamodel.html#object.__dict__ "object.__dict__") attributes, so you canât assign arbitrary attributes to an instance of `object`.

oct(_x_)Â¶
    

Convert an integer number to an octal string prefixed with â0oâ. The result is a valid Python expression. If _x_ is not a Python `int` object, it has to define an [`__index__()`](../reference/datamodel.html#object.__index__ "object.__index__") method that returns an integer. For example:
    
    
    >>> oct(8)
    '0o10'
    >>> oct(-56)
    '-0o70'
    

If you want to convert an integer number to an octal string either with the prefix â0oâ or not, you can use either of the following ways.
    
    
    >>> '%#o' % 10, '%o' % 10
    ('0o12', '12')
    >>> format(10, '#o'), format(10, 'o')
    ('0o12', '12')
    >>> f'{10:#o}', f'{10:o}'
    ('0o12', '12')
    

See also `format()` for more information.

open(_file_ , _mode ='r'_, _buffering =-1_, _encoding =None_, _errors =None_, _newline =None_, _closefd =True_, _opener =None_)Â¶
    

Open _file_ and return a corresponding [file object](../glossary.html#term-file-object). If the file cannot be opened, an [`OSError`](exceptions.html#OSError "OSError") is raised. See [Reading and Writing Files](../tutorial/inputoutput.html#tut-files) for more examples of how to use this function.

_file_ is a [path-like object](../glossary.html#term-path-like-object) giving the pathname (absolute or relative to the current working directory) of the file to be opened or an integer file descriptor of the file to be wrapped. (If a file descriptor is given, it is closed when the returned I/O object is closed unless _closefd_ is set to `False`.)

_mode_ is an optional string that specifies the mode in which the file is opened. It defaults to `'r'` which means open for reading in text mode. Other common values are `'w'` for writing (truncating the file if it already exists), `'x'` for exclusive creation, and `'a'` for appending (which on _some_ Unix systems, means that _all_ writes append to the end of the file regardless of the current seek position). In text mode, if _encoding_ is not specified the encoding used is platform-dependent: [`locale.getencoding()`](locale.html#locale.getencoding "locale.getencoding") is called to get the current locale encoding. (For reading and writing raw bytes use binary mode and leave _encoding_ unspecified.) The available modes are:

Character | Meaning  
---|---  
`'r'` | open for reading (default)  
`'w'` | open for writing, truncating the file first  
`'x'` | open for exclusive creation, failing if the file already exists  
`'a'` | open for writing, appending to the end of file if it exists  
`'b'` | binary mode  
`'t'` | text mode (default)  
`'+'` | open for updating (reading and writing)  
  
The default mode is `'r'` (open for reading text, a synonym of `'rt'`). Modes `'w+'` and `'w+b'` open and truncate the file. Modes `'r+'` and `'r+b'` open the file with no truncation.

As mentioned in the [Overview](io.html#io-overview), Python distinguishes between binary and text I/O. Files opened in binary mode (including `'b'` in the _mode_ argument) return contents as [`bytes`](stdtypes.html#bytes "bytes") objects without any decoding. In text mode (the default, or when `'t'` is included in the _mode_ argument), the contents of the file are returned as [`str`](stdtypes.html#str "str"), the bytes having been first decoded using a platform-dependent encoding or using the specified _encoding_ if given.

Note

Python doesnât depend on the underlying operating systemâs notion of text files; all the processing is done by Python itself, and is therefore platform-independent.

_buffering_ is an optional integer used to set the buffering policy. Pass 0 to switch buffering off (only allowed in binary mode), 1 to select line buffering (only usable when writing in text mode), and an integer > 1 to indicate the size in bytes of a fixed-size chunk buffer. Note that specifying a buffer size this way applies for binary buffered I/O, but `TextIOWrapper` (i.e., files opened with `mode='r+'`) would have another buffering. To disable buffering in `TextIOWrapper`, consider using the `write_through` flag for [`io.TextIOWrapper.reconfigure()`](io.html#io.TextIOWrapper.reconfigure "io.TextIOWrapper.reconfigure"). When no _buffering_ argument is given, the default buffering policy works as follows:

  * Binary files are buffered in fixed-size chunks; the size of the buffer is chosen using a heuristic trying to determine the underlying deviceâs âblock sizeâ and falling back on [`io.DEFAULT_BUFFER_SIZE`](io.html#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE"). On many systems, the buffer will typically be 4096 or 8192 bytes long.

  * âInteractiveâ text files (files for which [`isatty()`](io.html#io.IOBase.isatty "io.IOBase.isatty") returns `True`) use line buffering. Other text files use the policy described above for binary files.




_encoding_ is the name of the encoding used to decode or encode the file. This should only be used in text mode. The default encoding is platform dependent (whatever [`locale.getencoding()`](locale.html#locale.getencoding "locale.getencoding") returns), but any [text encoding](../glossary.html#term-text-encoding) supported by Python can be used. See the [`codecs`](codecs.html#module-codecs "codecs: Encode and decode data and streams.") module for the list of supported encodings.

_errors_ is an optional string that specifies how encoding and decoding errors are to be handledâthis cannot be used in binary mode. A variety of standard error handlers are available (listed under [Error Handlers](codecs.html#error-handlers)), though any error handling name that has been registered with [`codecs.register_error()`](codecs.html#codecs.register_error "codecs.register_error") is also valid. The standard names include:

  * `'strict'` to raise a [`ValueError`](exceptions.html#ValueError "ValueError") exception if there is an encoding error. The default value of `None` has the same effect.

  * `'ignore'` ignores errors. Note that ignoring encoding errors can lead to data loss.

  * `'replace'` causes a replacement marker (such as `'?'`) to be inserted where there is malformed data.

  * `'surrogateescape'` will represent any incorrect bytes as low surrogate code units ranging from U+DC80 to U+DCFF. These surrogate code units will then be turned back into the same bytes when the `surrogateescape` error handler is used when writing data. This is useful for processing files in an unknown encoding.

  * `'xmlcharrefreplace'` is only supported when writing to a file. Characters not supported by the encoding are replaced with the appropriate XML character reference `&#_nnn_ ;`.

  * `'backslashreplace'` replaces malformed data by Pythonâs backslashed escape sequences.

  * `'namereplace'` (also only supported when writing) replaces unsupported characters with `\N{...}` escape sequences.




_newline_ determines how to parse newline characters from the stream. It can be `None`, `''`, `'\n'`, `'\r'`, and `'\r\n'`. It works as follows:

  * When reading input from the stream, if _newline_ is `None`, universal newlines mode is enabled. Lines in the input can end in `'\n'`, `'\r'`, or `'\r\n'`, and these are translated into `'\n'` before being returned to the caller. If it is `''`, universal newlines mode is enabled, but line endings are returned to the caller untranslated. If it has any of the other legal values, input lines are only terminated by the given string, and the line ending is returned to the caller untranslated.

  * When writing output to the stream, if _newline_ is `None`, any `'\n'` characters written are translated to the system default line separator, [`os.linesep`](os.html#os.linesep "os.linesep"). If _newline_ is `''` or `'\n'`, no translation takes place. If _newline_ is any of the other legal values, any `'\n'` characters written are translated to the given string.




If _closefd_ is `False` and a file descriptor rather than a filename was given, the underlying file descriptor will be kept open when the file is closed. If a filename is given _closefd_ must be `True` (the default); otherwise, an error will be raised.

A custom opener can be used by passing a callable as _opener_. The underlying file descriptor for the file object is then obtained by calling _opener_ with (_file_ , _flags_). _opener_ must return an open file descriptor (passing [`os.open`](os.html#os.open "os.open") as _opener_ results in functionality similar to passing `None`).

The newly created file is [non-inheritable](os.html#fd-inheritance).

The following example uses the [dir_fd](os.html#dir-fd) parameter of the [`os.open()`](os.html#os.open "os.open") function to open a file relative to a given directory:
    
    
    >>> import os
    >>> dir_fd = os.open('somedir', os.O_RDONLY)
    >>> def opener(path, flags):
    ...     return os.open(path, flags, dir_fd=dir_fd)
    ...
    >>> with open('spamspam.txt', 'w', opener=opener) as f:
    ...     print('This will be written to somedir/spamspam.txt', file=f)
    ...
    >>> os.close(dir_fd)  # don't leak a file descriptor
    

The type of [file object](../glossary.html#term-file-object) returned by the `open()` function depends on the mode. When `open()` is used to open a file in a text mode (`'w'`, `'r'`, `'wt'`, `'rt'`, etc.), it returns a subclass of [`io.TextIOBase`](io.html#io.TextIOBase "io.TextIOBase") (specifically [`io.TextIOWrapper`](io.html#io.TextIOWrapper "io.TextIOWrapper")). When used to open a file in a binary mode with buffering, the returned class is a subclass of [`io.BufferedIOBase`](io.html#io.BufferedIOBase "io.BufferedIOBase"). The exact class varies: in read binary mode, it returns an [`io.BufferedReader`](io.html#io.BufferedReader "io.BufferedReader"); in write binary and append binary modes, it returns an [`io.BufferedWriter`](io.html#io.BufferedWriter "io.BufferedWriter"), and in read/write mode, it returns an [`io.BufferedRandom`](io.html#io.BufferedRandom "io.BufferedRandom"). When buffering is disabled, the raw stream, a subclass of [`io.RawIOBase`](io.html#io.RawIOBase "io.RawIOBase"), [`io.FileIO`](io.html#io.FileIO "io.FileIO"), is returned.

See also the file handling modules, such as [`fileinput`](fileinput.html#module-fileinput "fileinput: Loop over standard input or a list of files."), [`io`](io.html#module-io "io: Core tools for working with streams.") (where `open()` is declared), [`os`](os.html#module-os "os: Miscellaneous operating system interfaces."), [`os.path`](os.path.html#module-os.path "os.path: Operations on pathnames."), [`tempfile`](tempfile.html#module-tempfile "tempfile: Generate temporary files and directories."), and [`shutil`](shutil.html#module-shutil "shutil: High-level file operations, including copying.").

Raises an [auditing event](sys.html#auditing) `open` with arguments `path`, `mode`, `flags`.

The `mode` and `flags` arguments may have been modified or inferred from the original call.

Changed in version 3.3: 

  * The _opener_ parameter was added.

  * The `'x'` mode was added.

  * [`IOError`](exceptions.html#IOError "IOError") used to be raised, it is now an alias of [`OSError`](exceptions.html#OSError "OSError").

  * [`FileExistsError`](exceptions.html#FileExistsError "FileExistsError") is now raised if the file opened in exclusive creation mode (`'x'`) already exists.




Changed in version 3.4: 

  * The file is now non-inheritable.




Changed in version 3.5: 

  * If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an [`InterruptedError`](exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

  * The `'namereplace'` error handler was added.




Changed in version 3.6: 

  * Support added to accept objects implementing [`os.PathLike`](os.html#os.PathLike "os.PathLike").

  * On Windows, opening a console buffer may return a subclass of [`io.RawIOBase`](io.html#io.RawIOBase "io.RawIOBase") other than [`io.FileIO`](io.html#io.FileIO "io.FileIO").




Changed in version 3.11: The `'U'` mode has been removed.

ord(_c_)Â¶
    

Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, `ord('a')` returns the integer `97` and `ord('â¬')` (Euro sign) returns `8364`. This is the inverse of `chr()`.

pow(_base_ , _exp_ , _mod =None_)Â¶
    

Return _base_ to the power _exp_ ; if _mod_ is present, return _base_ to the power _exp_ , modulo _mod_ (computed more efficiently than `pow(base, exp) % mod`). The two-argument form `pow(base, exp)` is equivalent to using the power operator: `base**exp`.

The arguments must have numeric types. With mixed operand types, the coercion rules for binary arithmetic operators apply. For `int` operands, the result has the same type as the operands (after coercion) unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered. For example, `pow(10, 2)` returns `100`, but `pow(10, -2)` returns `0.01`. For a negative base of type `int` or `float` and a non-integral exponent, a complex result is delivered. For example, `pow(-9, 0.5)` returns a value close to `3j`. Whereas, for a negative base of type `int` or `float` with an integral exponent, a float result is delivered. For example, `pow(-9, 2.0)` returns `81.0`.

For `int` operands _base_ and _exp_ , if _mod_ is present, _mod_ must also be of integer type and _mod_ must be nonzero. If _mod_ is present and _exp_ is negative, _base_ must be relatively prime to _mod_. In that case, `pow(inv_base, -exp, mod)` is returned, where _inv_base_ is an inverse to _base_ modulo _mod_.

Hereâs an example of computing an inverse for `38` modulo `97`:
    
    
    >>> pow(38, -1, mod=97)
    23
    >>> 23 * 38 % 97 == 1
    True
    

Changed in version 3.8: For `int` operands, the three-argument form of `pow` now allows the second argument to be negative, permitting computation of modular inverses.

Changed in version 3.8: Allow keyword arguments. Formerly, only positional arguments were supported.

print(_* objects_, _sep =' '_, _end ='\n'_, _file =None_, _flush =False_)Â¶
    

Print _objects_ to the text stream _file_ , separated by _sep_ and followed by _end_. _sep_ , _end_ , _file_ , and _flush_ , if present, must be given as keyword arguments.

All non-keyword arguments are converted to strings like [`str()`](stdtypes.html#str "str") does and written to the stream, separated by _sep_ and followed by _end_. Both _sep_ and _end_ must be strings; they can also be `None`, which means to use the default values. If no _objects_ are given, `print()` will just write _end_.

The _file_ argument must be an object with a `write(string)` method; if it is not present or `None`, [`sys.stdout`](sys.html#sys.stdout "sys.stdout") will be used. Since printed arguments are converted to text strings, `print()` cannot be used with binary mode file objects. For these, use `file.write(...)` instead.

Output buffering is usually determined by _file_. However, if _flush_ is true, the stream is forcibly flushed.

Changed in version 3.3: Added the _flush_ keyword argument.

_class _property(_fget =None_, _fset =None_, _fdel =None_, _doc =None_)Â¶
    

Return a property attribute.

_fget_ is a function for getting an attribute value. _fset_ is a function for setting an attribute value. _fdel_ is a function for deleting an attribute value. And _doc_ creates a docstring for the attribute.

A typical use is to define a managed attribute `x`:
    
    
    class C:
        def __init__(self):
            self._x = None
    
        def getx(self):
            return self._x
    
        def setx(self, value):
            self._x = value
    
        def delx(self):
            del self._x
    
        x = property(getx, setx, delx, "I'm the 'x' property.")
    

If _c_ is an instance of _C_ , `c.x` will invoke the getter, `c.x = value` will invoke the setter, and `del c.x` the deleter.

If given, _doc_ will be the docstring of the property attribute. Otherwise, the property will copy _fget_ âs docstring (if it exists). This makes it possible to create read-only properties easily using `property()` as a [decorator](../glossary.html#term-decorator):
    
    
    class Parrot:
        def __init__(self):
            self._voltage = 100000
    
        @property
        def voltage(self):
            """Get the current voltage."""
            return self._voltage
    

The `@property` decorator turns the `voltage()` method into a âgetterâ for a read-only attribute with the same name, and it sets the docstring for _voltage_ to âGet the current voltage.â

@getterÂ¶
    

@setterÂ¶
    

@deleterÂ¶
    

A property object has `getter`, `setter`, and `deleter` methods usable as decorators that create a copy of the property with the corresponding accessor function set to the decorated function. This is best explained with an example:
    
    
    class C:
        def __init__(self):
            self._x = None
    
        @property
        def x(self):
            """I'm the 'x' property."""
            return self._x
    
        @x.setter
        def x(self, value):
            self._x = value
    
        @x.deleter
        def x(self):
            del self._x
    

This code is exactly equivalent to the first example. Be sure to give the additional functions the same name as the original property (`x` in this case.)

The returned property object also has the attributes `fget`, `fset`, and `fdel` corresponding to the constructor arguments.

Changed in version 3.5: The docstrings of property objects are now writeable.

__name__Â¶
    

Attribute holding the name of the property. The name of the property can be changed at runtime.

Added in version 3.13.

_class _range(_stop_)
_class _range(_start_ , _stop_ , _step =1_)
    

Rather than being a function, [`range`](stdtypes.html#range "range") is actually an immutable sequence type, as documented in [Ranges](stdtypes.html#typesseq-range) and [Sequence Types â list, tuple, range](stdtypes.html#typesseq).

repr(_object_)Â¶
    

Return a string containing a printable representation of an object. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to `eval()`; otherwise, the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a [`__repr__()`](../reference/datamodel.html#object.__repr__ "object.__repr__") method. If [`sys.displayhook()`](sys.html#sys.displayhook "sys.displayhook") is not accessible, this function will raise [`RuntimeError`](exceptions.html#RuntimeError "RuntimeError").

This class has a custom representation that can be evaluated:
    
    
    class Person:
       def __init__(self, name, age):
          self.name = name
          self.age = age
    
       def __repr__(self):
          return f"Person('{self.name}', {self.age})"
    

reversed(_seq_)Â¶
    

Return a reverse [iterator](../glossary.html#term-iterator). _seq_ must be an object which has a [`__reversed__()`](../reference/datamodel.html#object.__reversed__ "object.__reversed__") method or supports the sequence protocol (the [`__len__()`](../reference/datamodel.html#object.__len__ "object.__len__") method and the [`__getitem__()`](../reference/datamodel.html#object.__getitem__ "object.__getitem__") method with integer arguments starting at `0`).

round(_number_ , _ndigits =None_)Â¶
    

Return _number_ rounded to _ndigits_ precision after the decimal point. If _ndigits_ is omitted or is `None`, it returns the nearest integer to its input.

For the built-in types supporting `round()`, values are rounded to the closest multiple of 10 to the power minus _ndigits_ ; if two multiples are equally close, rounding is done toward the even choice (so, for example, both `round(0.5)` and `round(-0.5)` are `0`, and `round(1.5)` is `2`). Any integer value is valid for _ndigits_ (positive, zero, or negative). The return value is an integer if _ndigits_ is omitted or `None`. Otherwise, the return value has the same type as _number_.

For a general Python object `number`, `round` delegates to `number.__round__`.

Note

The behavior of `round()` for floats can be surprising: for example, `round(2.675, 2)` gives `2.67` instead of the expected `2.68`. This is not a bug: itâs a result of the fact that most decimal fractions canât be represented exactly as a float. See [Floating-Point Arithmetic: Issues and Limitations](../tutorial/floatingpoint.html#tut-fp-issues) for more information.

_class _set
_class _set(_iterable_)
    

Return a new [`set`](stdtypes.html#set "set") object, optionally with elements taken from _iterable_. `set` is a built-in class. See [`set`](stdtypes.html#set "set") and [Set Types â set, frozenset](stdtypes.html#types-set) for documentation about this class.

For other containers see the built-in [`frozenset`](stdtypes.html#frozenset "frozenset"), [`list`](stdtypes.html#list "list"), [`tuple`](stdtypes.html#tuple "tuple"), and [`dict`](stdtypes.html#dict "dict") classes, as well as the [`collections`](collections.html#module-collections "collections: Container datatypes") module.

setattr(_object_ , _name_ , _value_)Â¶
    

This is the counterpart of `getattr()`. The arguments are an object, a string, and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, `setattr(x, 'foobar', 123)` is equivalent to `x.foobar = 123`.

_name_ need not be a Python identifier as defined in [Identifiers and keywords](../reference/lexical_analysis.html#identifiers) unless the object chooses to enforce that, for example in a custom [`__getattribute__()`](../reference/datamodel.html#object.__getattribute__ "object.__getattribute__") or via [`__slots__`](../reference/datamodel.html#object.__slots__ "object.__slots__"). An attribute whose name is not an identifier will not be accessible using the dot notation, but is accessible through `getattr()` etc..

Note

Since [private name mangling](../reference/expressions.html#private-name-mangling) happens at compilation time, one must manually mangle a private attributeâs (attributes with two leading underscores) name in order to set it with `setattr()`.

_class _slice(_stop_)Â¶
_class _slice(_start_ , _stop_ , _step =None_)
    

Return a [slice](../glossary.html#term-slice) object representing the set of indices specified by `range(start, stop, step)`. The _start_ and _step_ arguments default to `None`.

startÂ¶
    

stopÂ¶
    

stepÂ¶
    

Slice objects have read-only data attributes `start`, `stop`, and `step` which merely return the argument values (or their default). They have no other explicit functionality; however, they are used by NumPy and other third-party packages.

Slice objects are also generated when extended indexing syntax is used. For example: `a[start:stop:step]` or `a[start:stop, i]`. See [`itertools.islice()`](itertools.html#itertools.islice "itertools.islice") for an alternate version that returns an [iterator](../glossary.html#term-iterator).

Changed in version 3.12: Slice objects are now [hashable](../glossary.html#term-hashable) (provided `start`, `stop`, and `step` are hashable).

sorted(_iterable_ , _/_ , _*_ , _key =None_, _reverse =False_)Â¶
    

Return a new sorted list from the items in _iterable_.

Has two optional arguments which must be specified as keyword arguments.

_key_ specifies a function of one argument that is used to extract a comparison key from each element in _iterable_ (for example, `key=str.lower`). The default value is `None` (compare the elements directly).

_reverse_ is a boolean value. If set to `True`, then the list elements are sorted as if each comparison were reversed.

Use [`functools.cmp_to_key()`](functools.html#functools.cmp_to_key "functools.cmp_to_key") to convert an old-style _cmp_ function to a _key_ function.

The built-in `sorted()` function is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal â this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).

The sort algorithm uses only `<` comparisons between items. While defining an [`__lt__()`](../reference/datamodel.html#object.__lt__ "object.__lt__") method will suffice for sorting, [**PEP 8**](https://peps.python.org/pep-0008/) recommends that all six [rich comparisons](../reference/expressions.html#comparisons) be implemented. This will help avoid bugs when using the same data with other ordering tools such as `max()` that rely on a different underlying method. Implementing all six comparisons also helps avoid confusion for mixed type comparisons which can call reflected the [`__gt__()`](../reference/datamodel.html#object.__gt__ "object.__gt__") method.

For sorting examples and a brief sorting tutorial, see [Sorting Techniques](../howto/sorting.html#sortinghowto).

@staticmethodÂ¶
    

Transform a method into a static method.

A static method does not receive an implicit first argument. To declare a static method, use this idiom:
    
    
    class C:
        @staticmethod
        def f(arg1, arg2, argN): ...
    

The `@staticmethod` form is a function [decorator](../glossary.html#term-decorator) â see [Function definitions](../reference/compound_stmts.html#function) for details.

A static method can be called either on the class (such as `C.f()`) or on an instance (such as `C().f()`). Moreover, the static method [descriptor](../glossary.html#term-descriptor) is also callable, so it can be used in the class definition (such as `f()`).

Static methods in Python are similar to those found in Java or C++. Also, see `classmethod()` for a variant that is useful for creating alternate class constructors.

Like all decorators, it is also possible to call `staticmethod` as a regular function and do something with its result. This is needed in some cases where you need a reference to a function from a class body and you want to avoid the automatic transformation to instance method. For these cases, use this idiom:
    
    
    def regular_function():
        ...
    
    class C:
        method = staticmethod(regular_function)
    

For more information on static methods, see [The standard type hierarchy](../reference/datamodel.html#types).

Changed in version 3.10: Static methods now inherit the method attributes ([`__module__`](../reference/datamodel.html#function.__module__ "function.__module__"), [`__name__`](../reference/datamodel.html#function.__name__ "function.__name__"), [`__qualname__`](../reference/datamodel.html#function.__qualname__ "function.__qualname__"), [`__doc__`](../reference/datamodel.html#function.__doc__ "function.__doc__") and [`__annotations__`](../reference/datamodel.html#function.__annotations__ "function.__annotations__")), have a new `__wrapped__` attribute, and are now callable as regular functions.

_class _str(_object =''_)
_class _str(_object =b''_, _encoding ='utf-8'_, _errors ='strict'_)
    

Return a [`str`](stdtypes.html#str "str") version of _object_. See [`str()`](stdtypes.html#str "str") for details.

`str` is the built-in string [class](../glossary.html#term-class). For general information about strings, see [Text Sequence Type â str](stdtypes.html#textseq).

sum(_iterable_ , _/_ , _start =0_)Â¶
    

Sums _start_ and the items of an _iterable_ from left to right and returns the total. The _iterable_ âs items are normally numbers, and the start value is not allowed to be a string.

For some use cases, there are good alternatives to `sum()`. The preferred, fast way to concatenate a sequence of strings is by calling `''.join(sequence)`. To add floating-point values with extended precision, see [`math.fsum()`](math.html#math.fsum "math.fsum"). To concatenate a series of iterables, consider using [`itertools.chain()`](itertools.html#itertools.chain "itertools.chain").

Changed in version 3.8: The _start_ parameter can be specified as a keyword argument.

Changed in version 3.12: Summation of floats switched to an algorithm that gives higher accuracy and better commutativity on most builds.

_class _superÂ¶
_class _super(_type_ , _object_or_type =None_)
    

Return a proxy object that delegates method calls to a parent or sibling class of _type_. This is useful for accessing inherited methods that have been overridden in a class.

The _object_or_type_ determines the [method resolution order](../glossary.html#term-method-resolution-order) to be searched. The search starts from the class right after the _type_.

For example, if [`__mro__`](../reference/datamodel.html#type.__mro__ "type.__mro__") of _object_or_type_ is `D -> B -> C -> A -> object` and the value of _type_ is `B`, then `super()` searches `C -> A -> object`.

The [`__mro__`](../reference/datamodel.html#type.__mro__ "type.__mro__") attribute of the class corresponding to _object_or_type_ lists the method resolution search order used by both `getattr()` and `super()`. The attribute is dynamic and can change whenever the inheritance hierarchy is updated.

If the second argument is omitted, the super object returned is unbound. If the second argument is an object, `isinstance(obj, type)` must be true. If the second argument is a type, `issubclass(type2, type)` must be true (this is useful for classmethods).

When called directly within an ordinary method of a class, both arguments may be omitted (âzero-argument `super()`â). In this case, _type_ will be the enclosing class, and _obj_ will be the first argument of the immediately enclosing function (typically `self`). (This means that zero-argument `super()` will not work as expected within nested functions, including generator expressions, which implicitly create nested functions.)

There are two typical use cases for _super_. In a class hierarchy with single inheritance, _super_ can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of _super_ in other programming languages.

The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case is unique to Python and is not found in statically compiled languages or languages that only support single inheritance. This makes it possible to implement âdiamond diagramsâ where multiple base classes implement the same method. Good design dictates that such implementations have the same calling signature in every case (because the order of calls is determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).

For both use cases, a typical superclass call looks like this:
    
    
    class C(B):
        def method(self, arg):
            super().method(arg)    # This does the same thing as:
                                   # super(C, self).method(arg)
    

In addition to method lookups, `super()` also works for attribute lookups. One possible use case for this is calling [descriptors](../glossary.html#term-descriptor) in a parent or sibling class.

Note that `super()` is implemented as part of the binding process for explicit dotted attribute lookups such as `super().__getitem__(name)`. It does so by implementing its own [`__getattribute__()`](../reference/datamodel.html#object.__getattribute__ "object.__getattribute__") method for searching classes in a predictable order that supports cooperative multiple inheritance. Accordingly, `super()` is undefined for implicit lookups using statements or operators such as `super()[name]`.

Also note that, aside from the zero argument form, `super()` is not limited to use inside methods. The two argument form specifies the arguments exactly and makes the appropriate references. The zero argument form only works inside a class definition, as the compiler fills in the necessary details to correctly retrieve the class being defined, as well as accessing the current instance for ordinary methods.

For practical suggestions on how to design cooperative classes using `super()`, see [guide to using super()](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/).

_class _tuple
_class _tuple(_iterable_)
    

Rather than being a function, [`tuple`](stdtypes.html#tuple "tuple") is actually an immutable sequence type, as documented in [Tuples](stdtypes.html#typesseq-tuple) and [Sequence Types â list, tuple, range](stdtypes.html#typesseq).

_class _type(_object_)Â¶
_class _type(_name_ , _bases_ , _dict_ , _** kwds_)
    

With one argument, return the type of an _object_. The return value is a type object and generally the same object as returned by [`object.__class__`](../reference/datamodel.html#object.__class__ "object.__class__").

The `isinstance()` built-in function is recommended for testing the type of an object, because it takes subclasses into account.

With three arguments, return a new type object. This is essentially a dynamic form of the [`class`](../reference/compound_stmts.html#class) statement. The _name_ string is the class name and becomes the [`__name__`](../reference/datamodel.html#type.__name__ "type.__name__") attribute. The _bases_ tuple contains the base classes and becomes the [`__bases__`](../reference/datamodel.html#type.__bases__ "type.__bases__") attribute; if empty, `object`, the ultimate base of all classes, is added. The _dict_ dictionary contains attribute and method definitions for the class body; it may be copied or wrapped before becoming the [`__dict__`](../reference/datamodel.html#type.__dict__ "type.__dict__") attribute. The following two statements create identical `type` objects:
    
    
    >>> class X:
    ...     a = 1
    ...
    >>> X = type('X', (), dict(a=1))
    

See also:

  * [Documentation on attributes and methods on classes](../reference/datamodel.html#class-attrs-and-methods).

  * [Type Objects](stdtypes.html#bltin-type-objects)




Keyword arguments provided to the three argument form are passed to the appropriate metaclass machinery (usually [`__init_subclass__()`](../reference/datamodel.html#object.__init_subclass__ "object.__init_subclass__")) in the same way that keywords in a class definition (besides _metaclass_) would.

See also [Customizing class creation](../reference/datamodel.html#class-customization).

Changed in version 3.6: Subclasses of `type` which donât override `type.__new__` may no longer use the one-argument form to get the type of an object.

vars()Â¶
vars(_object_)
    

Return the [`__dict__`](../reference/datamodel.html#object.__dict__ "object.__dict__") attribute for a module, class, instance, or any other object with a `__dict__` attribute.

Objects such as modules and instances have an updateable [`__dict__`](../reference/datamodel.html#object.__dict__ "object.__dict__") attribute; however, other objects may have write restrictions on their `__dict__` attributes (for example, classes use a [`types.MappingProxyType`](types.html#types.MappingProxyType "types.MappingProxyType") to prevent direct dictionary updates).

Without an argument, `vars()` acts like `locals()`.

A [`TypeError`](exceptions.html#TypeError "TypeError") exception is raised if an object is specified but it doesnât have a [`__dict__`](../reference/datamodel.html#object.__dict__ "object.__dict__") attribute (for example, if its class defines the [`__slots__`](../reference/datamodel.html#object.__slots__ "object.__slots__") attribute).

Changed in version 3.13: The result of calling this function without an argument has been updated as described for the `locals()` builtin.

zip(_* iterables_, _strict =False_)Â¶
    

Iterate over several iterables in parallel, producing tuples with an item from each one.

Example:
    
    
    >>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    ...     print(item)
    ...
    (1, 'sugar')
    (2, 'spice')
    (3, 'everything nice')
    

More formally: `zip()` returns an iterator of tuples, where the _i_ -th tuple contains the _i_ -th element from each of the argument iterables.

Another way to think of `zip()` is that it turns rows into columns, and columns into rows. This is similar to [transposing a matrix](https://en.wikipedia.org/wiki/Transpose).

`zip()` is lazy: The elements wonât be processed until the iterable is iterated on, e.g. by a `for` loop or by wrapping in a [`list`](stdtypes.html#list "list").

One thing to consider is that the iterables passed to `zip()` could have different lengths; sometimes by design, and sometimes because of a bug in the code that prepared these iterables. Python offers three different approaches to dealing with this issue:

  * By default, `zip()` stops when the shortest iterable is exhausted. It will ignore the remaining items in the longer iterables, cutting off the result to the length of the shortest iterable:
    
        >>> list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
    [(0, 'fee'), (1, 'fi'), (2, 'fo')]
    

  * `zip()` is often used in cases where the iterables are assumed to be of equal length. In such cases, itâs recommended to use the `strict=True` option. Its output is the same as regular `zip()`:
    
        >>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
    [('a', 1), ('b', 2), ('c', 3)]
    

Unlike the default behavior, it raises a [`ValueError`](exceptions.html#ValueError "ValueError") if one iterable is exhausted before the others:
    
        >>> for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):
    ...     print(item)
    ...
    (0, 'fee')
    (1, 'fi')
    (2, 'fo')
    Traceback (most recent call last):
      ...
    ValueError: zip() argument 2 is longer than argument 1
    

Without the `strict=True` argument, any bug that results in iterables of different lengths will be silenced, possibly manifesting as a hard-to-find bug in another part of the program.

  * Shorter iterables can be padded with a constant value to make all the iterables have the same length. This is done by [`itertools.zip_longest()`](itertools.html#itertools.zip_longest "itertools.zip_longest").




Edge cases: With a single iterable argument, `zip()` returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.

Tips and tricks:

  * The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering a data series into n-length groups using `zip(*[iter(s)]*n, strict=True)`. This repeats the _same_ iterator `n` times so that each output tuple has the result of `n` calls to the iterator. This has the effect of dividing the input into n-length chunks.

  * `zip()` in conjunction with the `*` operator can be used to unzip a list:
    
        >>> x = [1, 2, 3]
    >>> y = [4, 5, 6]
    >>> list(zip(x, y))
    [(1, 4), (2, 5), (3, 6)]
    >>> x2, y2 = zip(*zip(x, y))
    >>> x == list(x2) and y == list(y2)
    True
    




Changed in version 3.10: Added the `strict` argument.

__import__(_name_ , _globals =None_, _locals =None_, _fromlist =()_, _level =0_)Â¶
    

Note

This is an advanced function that is not needed in everyday Python programming, unlike [`importlib.import_module()`](importlib.html#importlib.import_module "importlib.import_module").

This function is invoked by the [`import`](../reference/simple_stmts.html#import) statement. It can be replaced (by importing the [`builtins`](builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") module and assigning to `builtins.__import__`) in order to change semantics of the `import` statement, but doing so is **strongly** discouraged as it is usually simpler to use import hooks (see [**PEP 302**](https://peps.python.org/pep-0302/)) to attain the same goals and does not cause issues with code which assumes the default import implementation is in use. Direct use of `__import__()` is also discouraged in favor of [`importlib.import_module()`](importlib.html#importlib.import_module "importlib.import_module").

The function imports the module _name_ , potentially using the given _globals_ and _locals_ to determine how to interpret the name in a package context. The _fromlist_ gives the names of objects or submodules that should be imported from the module given by _name_. The standard implementation does not use its _locals_ argument at all and uses its _globals_ only to determine the package context of the [`import`](../reference/simple_stmts.html#import) statement.

_level_ specifies whether to use absolute or relative imports. `0` (the default) means only perform absolute imports. Positive values for _level_ indicate the number of parent directories to search relative to the directory of the module calling `__import__()` (see [**PEP 328**](https://peps.python.org/pep-0328/) for the details).

When the _name_ variable is of the form `package.module`, normally, the top-level package (the name up till the first dot) is returned, _not_ the module named by _name_. However, when a non-empty _fromlist_ argument is given, the module named by _name_ is returned.

For example, the statement `import spam` results in bytecode resembling the following code:
    
    
    spam = __import__('spam', globals(), locals(), [], 0)
    

The statement `import spam.ham` results in this call:
    
    
    spam = __import__('spam.ham', globals(), locals(), [], 0)
    

Note how `__import__()` returns the toplevel module here because this is the object that is bound to a name by the [`import`](../reference/simple_stmts.html#import) statement.

On the other hand, the statement `from spam.ham import eggs, sausage as saus` results in
    
    
    _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
    eggs = _temp.eggs
    saus = _temp.sausage
    

Here, the `spam.ham` module is returned from `__import__()`. From this object, the names to import are retrieved and assigned to their respective names.

If you simply want to import a module (potentially within a package) by name, use [`importlib.import_module()`](importlib.html#importlib.import_module "importlib.import_module").

Changed in version 3.3: Negative values for _level_ are no longer supported (which also changes the default value to 0).

Changed in version 3.9: When the command line options [`-E`](../using/cmdline.html#cmdoption-E) or [`-I`](../using/cmdline.html#cmdoption-I) are being used, the environment variable [`PYTHONCASEOK`](../using/cmdline.html#envvar-PYTHONCASEOK) is now ignored.

Footnotes

[1]

Note that the parser only accepts the Unix-style end of line convention. If you are reading the code from a file, make sure to use newline conversion mode to convert Windows or Mac-style newlines.

#### Previous topic

[Introduction](intro.html "previous chapter")

#### Next topic

[Built-in Constants](constants.html "next chapter")

### This Page

  * [Report a Bug](../bugs.html)
  * [Show Source ](https://github.com/python/cpython/blob/main/Doc/library/functions.rst)



Â«

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](constants.html "Built-in Constants") |
  * [previous](intro.html "Introduction") |
  * ![Python logo](../_static/py.svg)
  * [Python](https://www.python.org/) »
  *   *   * [3.13.2 Documentation](../index.html) » 
  * [The Python Standard Library](index.html) »
  * [Built-in Functions]()
  * | 
  * Theme  Auto Light Dark |



© [ Copyright ](../copyright.html) 2001-2025, Python Software Foundation.   
This page is licensed under the Python Software Foundation License Version 2.   
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.   
See [History and License](/license.html) for more information.  
  
The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)   
  
Last updated on Apr 01, 2025 (02:17 UTC). [Found a bug](/bugs.html)?   
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)
