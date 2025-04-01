---
title: Built-in Types — Python 3.13.2 documentation
source: https://docs.python.org/3/library/stdtypes.html
captured: 2025-03-31 20:24:10
---

[ ![Python logo](../_static/py.svg) ](https://www.python.org/)

Theme  Auto Light Dark

### [Table of Contents](../contents.html)

  * Built-in Types
    * Truth Value Testing
    * Boolean Operations â `and`, `or`, `not`
    * Comparisons
    * Numeric Types â `int`, `float`, `complex`
      * Bitwise Operations on Integer Types
      * Additional Methods on Integer Types
      * Additional Methods on Float
      * Hashing of numeric types
    * Boolean Type - `bool`
    * Iterator Types
      * Generator Types
    * Sequence Types â `list`, `tuple`, `range`
      * Common Sequence Operations
      * Immutable Sequence Types
      * Mutable Sequence Types
      * Lists
      * Tuples
      * Ranges
    * Text Sequence Type â `str`
      * String Methods
      * `printf`-style String Formatting
    * Binary Sequence Types â `bytes`, `bytearray`, `memoryview`
      * Bytes Objects
      * Bytearray Objects
      * Bytes and Bytearray Operations
      * `printf`-style Bytes Formatting
      * Memory Views
    * Set Types â `set`, `frozenset`
    * Mapping Types â `dict`
      * Dictionary view objects
    * Context Manager Types
    * Type Annotation Types â Generic Alias, Union
      * Generic Alias Type
        * Standard Generic Classes
        * Special Attributes of `GenericAlias` objects
      * Union Type
    * Other Built-in Types
      * Modules
      * Classes and Class Instances
      * Functions
      * Methods
      * Code Objects
      * Type Objects
      * The Null Object
      * The Ellipsis Object
      * The NotImplemented Object
      * Internal Objects
    * Special Attributes
    * Integer string conversion length limitation
      * Affected APIs
      * Configuring the limit
      * Recommended configuration



#### Previous topic

[Built-in Constants](constants.html "previous chapter")

#### Next topic

[Built-in Exceptions](exceptions.html "next chapter")

### This Page

  * [Report a Bug](../bugs.html)
  * [Show Source ](https://github.com/python/cpython/blob/main/Doc/library/stdtypes.rst)



### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](exceptions.html "Built-in Exceptions") |
  * [previous](constants.html "Built-in Constants") |
  * ![Python logo](../_static/py.svg)
  * [Python](https://www.python.org/) »
  *   *   * [3.13.2 Documentation](../index.html) » 
  * [The Python Standard Library](index.html) »
  * [Built-in Types]()
  * | 
  * Theme  Auto Light Dark |



# Built-in TypesÂ¶

The following sections describe the standard types that are built into the interpreter.

The principal built-in types are numerics, sequences, mappings, classes, instances and exceptions.

Some collection classes are mutable. The methods that add, subtract, or rearrange their members in place, and donât return a specific item, never return the collection instance itself but `None`.

Some operations are supported by several object types; in particular, practically all objects can be compared for equality, tested for truth value, and converted to a string (with the [`repr()`](functions.html#repr "repr") function or the slightly different `str()` function). The latter function is implicitly used when an object is written by the [`print()`](functions.html#print "print") function.

## Truth Value TestingÂ¶

Any object can be tested for truth value, for use in an [`if`](../reference/compound_stmts.html#if) or [`while`](../reference/compound_stmts.html#while) condition or as operand of the Boolean operations below.

By default, an object is considered true unless its class defines either a [`__bool__()`](../reference/datamodel.html#object.__bool__ "object.__bool__") method that returns `False` or a [`__len__()`](../reference/datamodel.html#object.__len__ "object.__len__") method that returns zero, when called with the object. [1] Here are most of the built-in objects considered false:

  * constants defined to be false: `None` and `False`

  * zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`

  * empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`




Operations and built-in functions that have a Boolean result always return `0` or `False` for false and `1` or `True` for true, unless otherwise stated. (Important exception: the Boolean operations `or` and `and` always return one of their operands.)

## Boolean Operations â `and`, `or`, `not`Â¶

These are the Boolean operations, ordered by ascending priority:

Operation | Result | Notes  
---|---|---  
`x or y` | if _x_ is true, then _x_ , else _y_ | (1)  
`x and y` | if _x_ is false, then _x_ , else _y_ | (2)  
`not x` | if _x_ is false, then `True`, else `False` | (3)  
  
Notes:

  1. This is a short-circuit operator, so it only evaluates the second argument if the first one is false.

  2. This is a short-circuit operator, so it only evaluates the second argument if the first one is true.

  3. `not` has a lower priority than non-Boolean operators, so `not a == b` is interpreted as `not (a == b)`, and `a == not b` is a syntax error.




## ComparisonsÂ¶

There are eight comparison operations in Python. They all have the same priority (which is higher than that of the Boolean operations). Comparisons can be chained arbitrarily; for example, `x < y <= z` is equivalent to `x < y and y <= z`, except that _y_ is evaluated only once (but in both cases _z_ is not evaluated at all when `x < y` is found to be false).

This table summarizes the comparison operations:

Operation | Meaning  
---|---  
`<` | strictly less than  
`<=` | less than or equal  
`>` | strictly greater than  
`>=` | greater than or equal  
`==` | equal  
`!=` | not equal  
`is` | object identity  
`is not` | negated object identity  
  
Objects of different types, except different numeric types, never compare equal. The `==` operator is always defined but for some object types (for example, class objects) is equivalent to [`is`](../reference/expressions.html#is). The `<`, `<=`, `>` and `>=` operators are only defined where they make sense; for example, they raise a [`TypeError`](exceptions.html#TypeError "TypeError") exception when one of the arguments is a complex number.

Non-identical instances of a class normally compare as non-equal unless the class defines the [`__eq__()`](../reference/datamodel.html#object.__eq__ "object.__eq__") method.

Instances of a class cannot be ordered with respect to other instances of the same class, or other types of object, unless the class defines enough of the methods [`__lt__()`](../reference/datamodel.html#object.__lt__ "object.__lt__"), [`__le__()`](../reference/datamodel.html#object.__le__ "object.__le__"), [`__gt__()`](../reference/datamodel.html#object.__gt__ "object.__gt__"), and [`__ge__()`](../reference/datamodel.html#object.__ge__ "object.__ge__") (in general, [`__lt__()`](../reference/datamodel.html#object.__lt__ "object.__lt__") and [`__eq__()`](../reference/datamodel.html#object.__eq__ "object.__eq__") are sufficient, if you want the conventional meanings of the comparison operators).

The behavior of the [`is`](../reference/expressions.html#is) and [`is not`](../reference/expressions.html#is-not) operators cannot be customized; also they can be applied to any two objects and never raise an exception.

Two more operations with the same syntactic priority, [`in`](../reference/expressions.html#in) and [`not in`](../reference/expressions.html#not-in), are supported by types that are [iterable](../glossary.html#term-iterable) or implement the [`__contains__()`](../reference/datamodel.html#object.__contains__ "object.__contains__") method.

## Numeric Types â [`int`](functions.html#int "int"), [`float`](functions.html#float "float"), [`complex`](functions.html#complex "complex")Â¶

There are three distinct numeric types: _integers_ , _floating-point numbers_ , and _complex numbers_. In addition, Booleans are a subtype of integers. Integers have unlimited precision. Floating-point numbers are usually implemented using double in C; information about the precision and internal representation of floating-point numbers for the machine on which your program is running is available in [`sys.float_info`](sys.html#sys.float_info "sys.float_info"). Complex numbers have a real and imaginary part, which are each a floating-point number. To extract these parts from a complex number _z_ , use `z.real` and `z.imag`. (The standard library includes the additional numeric types [`fractions.Fraction`](fractions.html#fractions.Fraction "fractions.Fraction"), for rationals, and [`decimal.Decimal`](decimal.html#decimal.Decimal "decimal.Decimal"), for floating-point numbers with user-definable precision.)

Numbers are created by numeric literals or as the result of built-in functions and operators. Unadorned integer literals (including hex, octal and binary numbers) yield integers. Numeric literals containing a decimal point or an exponent sign yield floating-point numbers. Appending `'j'` or `'J'` to a numeric literal yields an imaginary number (a complex number with a zero real part) which you can add to an integer or float to get a complex number with real and imaginary parts.

Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the ânarrowerâ type is widened to that of the other, where integer is narrower than floating point, which is narrower than complex. A comparison between numbers of different types behaves as though the exact values of those numbers were being compared. [2]

The constructors [`int()`](functions.html#int "int"), [`float()`](functions.html#float "float"), and [`complex()`](functions.html#complex "complex") can be used to produce numbers of a specific type.

All numeric types (except complex) support the following operations (for priorities of the operations, see [Operator precedence](../reference/expressions.html#operator-summary)):

Operation | Result | Notes | Full documentation  
---|---|---|---  
`x + y` | sum of _x_ and _y_ |  |   
`x - y` | difference of _x_ and _y_ |  |   
`x * y` | product of _x_ and _y_ |  |   
`x / y` | quotient of _x_ and _y_ |  |   
`x // y` | floored quotient of _x_ and _y_ | (1)(2) |   
`x % y` | remainder of `x / y` | (2) |   
`-x` | _x_ negated |  |   
`+x` | _x_ unchanged |  |   
`abs(x)` | absolute value or magnitude of _x_ |  | [`abs()`](functions.html#abs "abs")  
`int(x)` | _x_ converted to integer | (3)(6) | [`int()`](functions.html#int "int")  
`float(x)` | _x_ converted to floating point | (4)(6) | [`float()`](functions.html#float "float")  
`complex(re, im)` | a complex number with real part _re_ , imaginary part _im_. _im_ defaults to zero. | (6) | [`complex()`](functions.html#complex "complex")  
`c.conjugate()` | conjugate of the complex number _c_ |  |   
`divmod(x, y)` | the pair `(x // y, x % y)` | (2) | [`divmod()`](functions.html#divmod "divmod")  
`pow(x, y)` | _x_ to the power _y_ | (5) | [`pow()`](functions.html#pow "pow")  
`x ** y` | _x_ to the power _y_ | (5) |   
  
Notes:

  1. Also referred to as integer division. For operands of type [`int`](functions.html#int "int"), the result has type [`int`](functions.html#int "int"). For operands of type [`float`](functions.html#float "float"), the result has type [`float`](functions.html#float "float"). In general, the result is a whole integer, though the resultâs type is not necessarily [`int`](functions.html#int "int"). The result is always rounded towards minus infinity: `1//2` is `0`, `(-1)//2` is `-1`, `1//(-2)` is `-1`, and `(-1)//(-2)` is `0`.

  2. Not for complex numbers. Instead convert to floats using [`abs()`](functions.html#abs "abs") if appropriate.

  3. Conversion from [`float`](functions.html#float "float") to [`int`](functions.html#int "int") truncates, discarding the fractional part. See functions [`math.floor()`](math.html#math.floor "math.floor") and [`math.ceil()`](math.html#math.ceil "math.ceil") for alternative conversions.

  4. float also accepts the strings ânanâ and âinfâ with an optional prefix â+â or â-â for Not a Number (NaN) and positive or negative infinity.

  5. Python defines `pow(0, 0)` and `0 ** 0` to be `1`, as is common for programming languages.

  6. The numeric literals accepted include the digits `0` to `9` or any Unicode equivalent (code points with the `Nd` property).

See [the Unicode Standard](https://unicode.org/Public/UNIDATA/extracted/DerivedNumericType.txt) for a complete list of code points with the `Nd` property.




All [`numbers.Real`](numbers.html#numbers.Real "numbers.Real") types ([`int`](functions.html#int "int") and [`float`](functions.html#float "float")) also include the following operations:

Operation | Result  
---|---  
[`math.trunc(x)`](math.html#math.trunc "math.trunc") | _x_ truncated to [`Integral`](numbers.html#numbers.Integral "numbers.Integral")  
[`round(x[, n])`](functions.html#round "round") | _x_ rounded to _n_ digits, rounding half to even. If _n_ is omitted, it defaults to 0.  
[`math.floor(x)`](math.html#math.floor "math.floor") | the greatest [`Integral`](numbers.html#numbers.Integral "numbers.Integral") <= _x_  
[`math.ceil(x)`](math.html#math.ceil "math.ceil") | the least [`Integral`](numbers.html#numbers.Integral "numbers.Integral") >= _x_  
  
For additional numeric operations see the [`math`](math.html#module-math "math: Mathematical functions \(sin\(\) etc.\).") and [`cmath`](cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.") modules.

### Bitwise Operations on Integer TypesÂ¶

Bitwise operations only make sense for integers. The result of bitwise operations is calculated as though carried out in twoâs complement with an infinite number of sign bits.

The priorities of the binary bitwise operations are all lower than the numeric operations and higher than the comparisons; the unary operation `~` has the same priority as the other unary numeric operations (`+` and `-`).

This table lists the bitwise operations sorted in ascending priority:

Operation | Result | Notes  
---|---|---  
`x | y` | bitwise _or_ of _x_ and _y_ | (4)  
`x ^ y` | bitwise _exclusive or_ of _x_ and _y_ | (4)  
`x & y` | bitwise _and_ of _x_ and _y_ | (4)  
`x << n` | _x_ shifted left by _n_ bits | (1)(2)  
`x >> n` | _x_ shifted right by _n_ bits | (1)(3)  
`~x` | the bits of _x_ inverted |   
  
Notes:

  1. Negative shift counts are illegal and cause a [`ValueError`](exceptions.html#ValueError "ValueError") to be raised.

  2. A left shift by _n_ bits is equivalent to multiplication by `pow(2, n)`.

  3. A right shift by _n_ bits is equivalent to floor division by `pow(2, n)`.

  4. Performing these calculations with at least one extra sign extension bit in a finite twoâs complement representation (a working bit-width of `1 + max(x.bit_length(), y.bit_length())` or more) is sufficient to get the same result as if there were an infinite number of sign bits.




### Additional Methods on Integer TypesÂ¶

The int type implements the [`numbers.Integral`](numbers.html#numbers.Integral "numbers.Integral") [abstract base class](../glossary.html#term-abstract-base-class). In addition, it provides a few more methods:

int.bit_length()Â¶
    

Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros:
    
    
    >>> n = -37
    >>> bin(n)
    '-0b100101'
    >>> n.bit_length()
    6
    

More precisely, if `x` is nonzero, then `x.bit_length()` is the unique positive integer `k` such that `2**(k-1) <= abs(x) < 2**k`. Equivalently, when `abs(x)` is small enough to have a correctly rounded logarithm, then `k = 1 + int(log(abs(x), 2))`. If `x` is zero, then `x.bit_length()` returns `0`.

Equivalent to:
    
    
    def bit_length(self):
        s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
        s = s.lstrip('-0b') # remove leading zeros and minus sign
        return len(s)       # len('100101') --> 6
    

Added in version 3.1.

int.bit_count()Â¶
    

Return the number of ones in the binary representation of the absolute value of the integer. This is also known as the population count. Example:
    
    
    >>> n = 19
    >>> bin(n)
    '0b10011'
    >>> n.bit_count()
    3
    >>> (-n).bit_count()
    3
    

Equivalent to:
    
    
    def bit_count(self):
        return bin(self).count("1")
    

Added in version 3.10.

int.to_bytes(_length =1_, _byteorder ='big'_, _*_ , _signed =False_)Â¶
    

Return an array of bytes representing an integer.
    
    
    >>> (1024).to_bytes(2, byteorder='big')
    b'\x04\x00'
    >>> (1024).to_bytes(10, byteorder='big')
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
    >>> (-1024).to_bytes(10, byteorder='big', signed=True)
    b'\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00'
    >>> x = 1000
    >>> x.to_bytes((x.bit_length() + 7) // 8, byteorder='little')
    b'\xe8\x03'
    

The integer is represented using _length_ bytes, and defaults to 1. An [`OverflowError`](exceptions.html#OverflowError "OverflowError") is raised if the integer is not representable with the given number of bytes.

The _byteorder_ argument determines the byte order used to represent the integer, and defaults to `"big"`. If _byteorder_ is `"big"`, the most significant byte is at the beginning of the byte array. If _byteorder_ is `"little"`, the most significant byte is at the end of the byte array.

The _signed_ argument determines whether twoâs complement is used to represent the integer. If _signed_ is `False` and a negative integer is given, an [`OverflowError`](exceptions.html#OverflowError "OverflowError") is raised. The default value for _signed_ is `False`.

The default values can be used to conveniently turn an integer into a single byte object:
    
    
    >>> (65).to_bytes()
    b'A'
    

However, when using the default arguments, donât try to convert a value greater than 255 or youâll get an [`OverflowError`](exceptions.html#OverflowError "OverflowError").

Equivalent to:
    
    
    def to_bytes(n, length=1, byteorder='big', signed=False):
        if byteorder == 'little':
            order = range(length)
        elif byteorder == 'big':
            order = reversed(range(length))
        else:
            raise ValueError("byteorder must be either 'little' or 'big'")
    
        return bytes((n >> i*8) & 0xff for i in order)
    

Added in version 3.2.

Changed in version 3.11: Added default argument values for `length` and `byteorder`.

_classmethod _int.from_bytes(_bytes_ , _byteorder ='big'_, _*_ , _signed =False_)Â¶
    

Return the integer represented by the given array of bytes.
    
    
    >>> int.from_bytes(b'\x00\x10', byteorder='big')
    16
    >>> int.from_bytes(b'\x00\x10', byteorder='little')
    4096
    >>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=True)
    -1024
    >>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=False)
    64512
    >>> int.from_bytes([255, 0, 0], byteorder='big')
    16711680
    

The argument _bytes_ must either be a [bytes-like object](../glossary.html#term-bytes-like-object) or an iterable producing bytes.

The _byteorder_ argument determines the byte order used to represent the integer, and defaults to `"big"`. If _byteorder_ is `"big"`, the most significant byte is at the beginning of the byte array. If _byteorder_ is `"little"`, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use [`sys.byteorder`](sys.html#sys.byteorder "sys.byteorder") as the byte order value.

The _signed_ argument indicates whether twoâs complement is used to represent the integer.

Equivalent to:
    
    
    def from_bytes(bytes, byteorder='big', signed=False):
        if byteorder == 'little':
            little_ordered = list(bytes)
        elif byteorder == 'big':
            little_ordered = list(reversed(bytes))
        else:
            raise ValueError("byteorder must be either 'little' or 'big'")
    
        n = sum(b << i*8 for i, b in enumerate(little_ordered))
        if signed and little_ordered and (little_ordered[-1] & 0x80):
            n -= 1 << 8*len(little_ordered)
    
        return n
    

Added in version 3.2.

Changed in version 3.11: Added default argument value for `byteorder`.

int.as_integer_ratio()Â¶
    

Return a pair of integers whose ratio is equal to the original integer and has a positive denominator. The integer ratio of integers (whole numbers) is always the integer as the numerator and `1` as the denominator.

Added in version 3.8.

int.is_integer()Â¶
    

Returns `True`. Exists for duck type compatibility with `float.is_integer()`.

Added in version 3.12.

### Additional Methods on FloatÂ¶

The float type implements the [`numbers.Real`](numbers.html#numbers.Real "numbers.Real") [abstract base class](../glossary.html#term-abstract-base-class). float also has the following additional methods.

float.as_integer_ratio()Â¶
    

Return a pair of integers whose ratio is exactly equal to the original float. The ratio is in lowest terms and has a positive denominator. Raises [`OverflowError`](exceptions.html#OverflowError "OverflowError") on infinities and a [`ValueError`](exceptions.html#ValueError "ValueError") on NaNs.

float.is_integer()Â¶
    

Return `True` if the float instance is finite with integral value, and `False` otherwise:
    
    
    >>> (-2.0).is_integer()
    True
    >>> (3.2).is_integer()
    False
    

Two methods support conversion to and from hexadecimal strings. Since Pythonâs floats are stored internally as binary numbers, converting a float to or from a _decimal_ string usually involves a small rounding error. In contrast, hexadecimal strings allow exact representation and specification of floating-point numbers. This can be useful when debugging, and in numerical work.

float.hex()Â¶
    

Return a representation of a floating-point number as a hexadecimal string. For finite floating-point numbers, this representation will always include a leading `0x` and a trailing `p` and exponent.

_classmethod _float.fromhex(_s_)Â¶
    

Class method to return the float represented by a hexadecimal string _s_. The string _s_ may have leading and trailing whitespace.

Note that `float.hex()` is an instance method, while `float.fromhex()` is a class method.

A hexadecimal string takes the form:
    
    
    [sign] ['0x'] integer ['.' fraction] ['p' exponent]
    

where the optional `sign` may by either `+` or `-`, `integer` and `fraction` are strings of hexadecimal digits, and `exponent` is a decimal integer with an optional leading sign. Case is not significant, and there must be at least one hexadecimal digit in either the integer or the fraction. This syntax is similar to the syntax specified in section 6.4.4.2 of the C99 standard, and also to the syntax used in Java 1.5 onwards. In particular, the output of `float.hex()` is usable as a hexadecimal floating-point literal in C or Java code, and hexadecimal strings produced by Câs `%a` format character or Javaâs `Double.toHexString` are accepted by `float.fromhex()`.

Note that the exponent is written in decimal rather than hexadecimal, and that it gives the power of 2 by which to multiply the coefficient. For example, the hexadecimal string `0x3.a7p10` represents the floating-point number `(3 + 10./16 + 7./16**2) * 2.0**10`, or `3740.0`:
    
    
    >>> float.fromhex('0x3.a7p10')
    3740.0
    

Applying the reverse conversion to `3740.0` gives a different hexadecimal string representing the same number:
    
    
    >>> float.hex(3740.0)
    '0x1.d380000000000p+11'
    

### Hashing of numeric typesÂ¶

For numbers `x` and `y`, possibly of different types, itâs a requirement that `hash(x) == hash(y)` whenever `x == y` (see the [`__hash__()`](../reference/datamodel.html#object.__hash__ "object.__hash__") method documentation for more details). For ease of implementation and efficiency across a variety of numeric types (including [`int`](functions.html#int "int"), [`float`](functions.html#float "float"), [`decimal.Decimal`](decimal.html#decimal.Decimal "decimal.Decimal") and [`fractions.Fraction`](fractions.html#fractions.Fraction "fractions.Fraction")) Pythonâs hash for numeric types is based on a single mathematical function thatâs defined for any rational number, and hence applies to all instances of [`int`](functions.html#int "int") and [`fractions.Fraction`](fractions.html#fractions.Fraction "fractions.Fraction"), and all finite instances of [`float`](functions.html#float "float") and [`decimal.Decimal`](decimal.html#decimal.Decimal "decimal.Decimal"). Essentially, this function is given by reduction modulo `P` for a fixed prime `P`. The value of `P` is made available to Python as the [`modulus`](sys.html#sys.hash_info.modulus "sys.hash_info.modulus") attribute of [`sys.hash_info`](sys.html#sys.hash_info "sys.hash_info").

**CPython implementation detail:** Currently, the prime used is `P = 2**31 - 1` on machines with 32-bit C longs and `P = 2**61 - 1` on machines with 64-bit C longs.

Here are the rules in detail:

  * If `x = m / n` is a nonnegative rational number and `n` is not divisible by `P`, define `hash(x)` as `m * invmod(n, P) % P`, where `invmod(n, P)` gives the inverse of `n` modulo `P`.

  * If `x = m / n` is a nonnegative rational number and `n` is divisible by `P` (but `m` is not) then `n` has no inverse modulo `P` and the rule above doesnât apply; in this case define `hash(x)` to be the constant value `sys.hash_info.inf`.

  * If `x = m / n` is a negative rational number define `hash(x)` as `-hash(-x)`. If the resulting hash is `-1`, replace it with `-2`.

  * The particular values `sys.hash_info.inf` and `-sys.hash_info.inf` are used as hash values for positive infinity or negative infinity (respectively).

  * For a [`complex`](functions.html#complex "complex") number `z`, the hash values of the real and imaginary parts are combined by computing `hash(z.real) + sys.hash_info.imag * hash(z.imag)`, reduced modulo `2**sys.hash_info.width` so that it lies in `range(-2**(sys.hash_info.width - 1), 2**(sys.hash_info.width - 1))`. Again, if the result is `-1`, itâs replaced with `-2`.




To clarify the above rules, hereâs some example Python code, equivalent to the built-in hash, for computing the hash of a rational number, [`float`](functions.html#float "float"), or [`complex`](functions.html#complex "complex"):
    
    
    import sys, math
    
    def hash_fraction(m, n):
        """Compute the hash of a rational number m / n.
    
        Assumes m and n are integers, with n positive.
        Equivalent to hash(fractions.Fraction(m, n)).
    
        """
        P = sys.hash_info.modulus
        # Remove common factors of P.  (Unnecessary if m and n already coprime.)
        while m % P == n % P == 0:
            m, n = m // P, n // P
    
        if n % P == 0:
            hash_value = sys.hash_info.inf
        else:
            # Fermat's Little Theorem: pow(n, P-1, P) is 1, so
            # pow(n, P-2, P) gives the inverse of n modulo P.
            hash_value = (abs(m) % P) * pow(n, P - 2, P) % P
        if m < 0:
            hash_value = -hash_value
        if hash_value == -1:
            hash_value = -2
        return hash_value
    
    def hash_float(x):
        """Compute the hash of a float x."""
    
        if math.isnan(x):
            return object.__hash__(x)
        elif math.isinf(x):
            return sys.hash_info.inf if x > 0 else -sys.hash_info.inf
        else:
            return hash_fraction(*x.as_integer_ratio())
    
    def hash_complex(z):
        """Compute the hash of a complex number z."""
    
        hash_value = hash_float(z.real) + sys.hash_info.imag * hash_float(z.imag)
        # do a signed reduction modulo 2**sys.hash_info.width
        M = 2**(sys.hash_info.width - 1)
        hash_value = (hash_value & (M - 1)) - (hash_value & M)
        if hash_value == -1:
            hash_value = -2
        return hash_value
    

## Boolean Type - [`bool`](functions.html#bool "bool")Â¶

Booleans represent truth values. The [`bool`](functions.html#bool "bool") type has exactly two constant instances: `True` and `False`.

The built-in function [`bool()`](functions.html#bool "bool") converts any value to a boolean, if the value can be interpreted as a truth value (see section Truth Value Testing above).

For logical operations, use the boolean operators `and`, `or` and `not`. When applying the bitwise operators `&`, `|`, `^` to two booleans, they return a bool equivalent to the logical operations âandâ, âorâ, âxorâ. However, the logical operators `and`, `or` and `!=` should be preferred over `&`, `|` and `^`.

Deprecated since version 3.12: The use of the bitwise inversion operator `~` is deprecated and will raise an error in Python 3.16.

[`bool`](functions.html#bool "bool") is a subclass of [`int`](functions.html#int "int") (see Numeric Types â int, float, complex). In many numeric contexts, `False` and `True` behave like the integers 0 and 1, respectively. However, relying on this is discouraged; explicitly convert using [`int()`](functions.html#int "int") instead.

## Iterator TypesÂ¶

Python supports a concept of iteration over containers. This is implemented using two distinct methods; these are used to allow user-defined classes to support iteration. Sequences, described below in more detail, always support the iteration methods.

One method needs to be defined for container objects to provide [iterable](../glossary.html#term-iterable) support:

container.__iter__()Â¶
    

Return an [iterator](../glossary.html#term-iterator) object. The object is required to support the iterator protocol described below. If a container supports different types of iteration, additional methods can be provided to specifically request iterators for those iteration types. (An example of an object supporting multiple forms of iteration would be a tree structure which supports both breadth-first and depth-first traversal.) This method corresponds to the [`tp_iter`](../c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter") slot of the type structure for Python objects in the Python/C API.

The iterator objects themselves are required to support the following two methods, which together form the _iterator protocol_ :

iterator.__iter__()Â¶
    

Return the [iterator](../glossary.html#term-iterator) object itself. This is required to allow both containers and iterators to be used with the [`for`](../reference/compound_stmts.html#for) and [`in`](../reference/expressions.html#in) statements. This method corresponds to the [`tp_iter`](../c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter") slot of the type structure for Python objects in the Python/C API.

iterator.__next__()Â¶
    

Return the next item from the [iterator](../glossary.html#term-iterator). If there are no further items, raise the [`StopIteration`](exceptions.html#StopIteration "StopIteration") exception. This method corresponds to the [`tp_iternext`](../c-api/typeobj.html#c.PyTypeObject.tp_iternext "PyTypeObject.tp_iternext") slot of the type structure for Python objects in the Python/C API.

Python defines several iterator objects to support iteration over general and specific sequence types, dictionaries, and other more specialized forms. The specific types are not important beyond their implementation of the iterator protocol.

Once an iteratorâs `__next__()` method raises [`StopIteration`](exceptions.html#StopIteration "StopIteration"), it must continue to do so on subsequent calls. Implementations that do not obey this property are deemed broken.

### Generator TypesÂ¶

Pythonâs [generator](../glossary.html#term-generator)s provide a convenient way to implement the iterator protocol. If a container objectâs [`__iter__()`](../reference/datamodel.html#object.__iter__ "object.__iter__") method is implemented as a generator, it will automatically return an iterator object (technically, a generator object) supplying the `__iter__()` and [`__next__()`](../reference/expressions.html#generator.__next__ "generator.__next__") methods. More information about generators can be found in [the documentation for the yield expression](../reference/expressions.html#yieldexpr).

## Sequence Types â `list`, `tuple`, `range`Â¶

There are three basic sequence types: lists, tuples, and range objects. Additional sequence types tailored for processing of binary data and text strings are described in dedicated sections.

### Common Sequence OperationsÂ¶

The operations in the following table are supported by most sequence types, both mutable and immutable. The [`collections.abc.Sequence`](collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") ABC is provided to make it easier to correctly implement these operations on custom sequence types.

This table lists the sequence operations sorted in ascending priority. In the table, _s_ and _t_ are sequences of the same type, _n_ , _i_ , _j_ and _k_ are integers and _x_ is an arbitrary object that meets any type and value restrictions imposed by _s_.

The `in` and `not in` operations have the same priorities as the comparison operations. The `+` (concatenation) and `*` (repetition) operations have the same priority as the corresponding numeric operations. [3]

Operation | Result | Notes  
---|---|---  
`x in s` | `True` if an item of _s_ is equal to _x_ , else `False` | (1)  
`x not in s` | `False` if an item of _s_ is equal to _x_ , else `True` | (1)  
`s + t` | the concatenation of _s_ and _t_ | (6)(7)  
`s * n` or `n * s` | equivalent to adding _s_ to itself _n_ times | (2)(7)  
`s[i]` | _i_ th item of _s_ , origin 0 | (3)  
`s[i:j]` | slice of _s_ from _i_ to _j_ | (3)(4)  
`s[i:j:k]` | slice of _s_ from _i_ to _j_ with step _k_ | (3)(5)  
`len(s)` | length of _s_ |   
`min(s)` | smallest item of _s_ |   
`max(s)` | largest item of _s_ |   
`s.index(x[, i[, j]])` | index of the first occurrence of _x_ in _s_ (at or after index _i_ and before index _j_) | (8)  
`s.count(x)` | total number of occurrences of _x_ in _s_ |   
  
Sequences of the same type also support comparisons. In particular, tuples and lists are compared lexicographically by comparing corresponding elements. This means that to compare equal, every element must compare equal and the two sequences must be of the same type and have the same length. (For full details see [Comparisons](../reference/expressions.html#comparisons) in the language reference.)

Forward and reversed iterators over mutable sequences access values using an index. That index will continue to march forward (or backward) even if the underlying sequence is mutated. The iterator terminates only when an [`IndexError`](exceptions.html#IndexError "IndexError") or a [`StopIteration`](exceptions.html#StopIteration "StopIteration") is encountered (or when the index drops below zero).

Notes:

  1. While the `in` and `not in` operations are used only for simple containment testing in the general case, some specialised sequences (such as `str`, `bytes` and `bytearray`) also use them for subsequence testing:
    
        >>> "gg" in "eggs"
    True
    

  2. Values of _n_ less than `0` are treated as `0` (which yields an empty sequence of the same type as _s_). Note that items in the sequence _s_ are not copied; they are referenced multiple times. This often haunts new Python programmers; consider:
    
        >>> lists = [[]] * 3
    >>> lists
    [[], [], []]
    >>> lists[0].append(3)
    >>> lists
    [[3], [3], [3]]
    

What has happened is that `[[]]` is a one-element list containing an empty list, so all three elements of `[[]] * 3` are references to this single empty list. Modifying any of the elements of `lists` modifies this single list. You can create a list of different lists this way:
    
        >>> lists = [[] for i in range(3)]
    >>> lists[0].append(3)
    >>> lists[1].append(5)
    >>> lists[2].append(7)
    >>> lists
    [[3], [5], [7]]
    

Further explanation is available in the FAQ entry [How do I create a multidimensional list?](../faq/programming.html#faq-multidimensional-list).

  3. If _i_ or _j_ is negative, the index is relative to the end of sequence _s_ : `len(s) + i` or `len(s) + j` is substituted. But note that `-0` is still `0`.

  4. The slice of _s_ from _i_ to _j_ is defined as the sequence of items with index _k_ such that `i <= k < j`. If _i_ or _j_ is greater than `len(s)`, use `len(s)`. If _i_ is omitted or `None`, use `0`. If _j_ is omitted or `None`, use `len(s)`. If _i_ is greater than or equal to _j_ , the slice is empty.

  5. The slice of _s_ from _i_ to _j_ with step _k_ is defined as the sequence of items with index `x = i + n*k` such that `0 <= n < (j-i)/k`. In other words, the indices are `i`, `i+k`, `i+2*k`, `i+3*k` and so on, stopping when _j_ is reached (but never including _j_). When _k_ is positive, _i_ and _j_ are reduced to `len(s)` if they are greater. When _k_ is negative, _i_ and _j_ are reduced to `len(s) - 1` if they are greater. If _i_ or _j_ are omitted or `None`, they become âendâ values (which end depends on the sign of _k_). Note, _k_ cannot be zero. If _k_ is `None`, it is treated like `1`.

  6. Concatenating immutable sequences always results in a new object. This means that building up a sequence by repeated concatenation will have a quadratic runtime cost in the total sequence length. To get a linear runtime cost, you must switch to one of the alternatives below:

     * if concatenating `str` objects, you can build a list and use `str.join()` at the end or else write to an [`io.StringIO`](io.html#io.StringIO "io.StringIO") instance and retrieve its value when complete

     * if concatenating `bytes` objects, you can similarly use `bytes.join()` or [`io.BytesIO`](io.html#io.BytesIO "io.BytesIO"), or you can do in-place concatenation with a `bytearray` object. `bytearray` objects are mutable and have an efficient overallocation mechanism

     * if concatenating `tuple` objects, extend a `list` instead

     * for other types, investigate the relevant class documentation

  7. Some sequence types (such as `range`) only support item sequences that follow specific patterns, and hence donât support sequence concatenation or repetition.

  8. `index` raises [`ValueError`](exceptions.html#ValueError "ValueError") when _x_ is not found in _s_. Not all implementations support passing the additional arguments _i_ and _j_. These arguments allow efficient searching of subsections of the sequence. Passing the extra arguments is roughly equivalent to using `s[i:j].index(x)`, only without copying any data and with the returned index being relative to the start of the sequence rather than the start of the slice.




### Immutable Sequence TypesÂ¶

The only operation that immutable sequence types generally implement that is not also implemented by mutable sequence types is support for the [`hash()`](functions.html#hash "hash") built-in.

This support allows immutable sequences, such as `tuple` instances, to be used as `dict` keys and stored in `set` and `frozenset` instances.

Attempting to hash an immutable sequence that contains unhashable values will result in [`TypeError`](exceptions.html#TypeError "TypeError").

### Mutable Sequence TypesÂ¶

The operations in the following table are defined on mutable sequence types. The [`collections.abc.MutableSequence`](collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence") ABC is provided to make it easier to correctly implement these operations on custom sequence types.

In the table _s_ is an instance of a mutable sequence type, _t_ is any iterable object and _x_ is an arbitrary object that meets any type and value restrictions imposed by _s_ (for example, `bytearray` only accepts integers that meet the value restriction `0 <= x <= 255`).

Operation | Result | Notes  
---|---|---  
`s[i] = x` | item _i_ of _s_ is replaced by _x_ |   
`s[i:j] = t` | slice of _s_ from _i_ to _j_ is replaced by the contents of the iterable _t_ |   
`del s[i:j]` | same as `s[i:j] = []` |   
`s[i:j:k] = t` | the elements of `s[i:j:k]` are replaced by those of _t_ | (1)  
`del s[i:j:k]` | removes the elements of `s[i:j:k]` from the list |   
`s.append(x)` | appends _x_ to the end of the sequence (same as `s[len(s):len(s)] = [x]`) |   
`s.clear()` | removes all items from _s_ (same as `del s[:]`) | (5)  
`s.copy()` | creates a shallow copy of _s_ (same as `s[:]`) | (5)  
`s.extend(t)` or `s += t` | extends _s_ with the contents of _t_ (for the most part the same as `s[len(s):len(s)] = t`) |   
`s *= n` | updates _s_ with its contents repeated _n_ times | (6)  
`s.insert(i, x)` | inserts _x_ into _s_ at the index given by _i_ (same as `s[i:i] = [x]`) |   
`s.pop()` or `s.pop(i)` | retrieves the item at _i_ and also removes it from _s_ | (2)  
`s.remove(x)` | removes the first item from _s_ where `s[i]` is equal to _x_ | (3)  
`s.reverse()` | reverses the items of _s_ in place | (4)  
  
Notes:

  1. If _k_ is not equal to `1`, _t_ must have the same length as the slice it is replacing.

  2. The optional argument _i_ defaults to `-1`, so that by default the last item is removed and returned.

  3. `remove()` raises [`ValueError`](exceptions.html#ValueError "ValueError") when _x_ is not found in _s_.

  4. The `reverse()` method modifies the sequence in place for economy of space when reversing a large sequence. To remind users that it operates by side effect, it does not return the reversed sequence.

  5. `clear()` and `copy()` are included for consistency with the interfaces of mutable containers that donât support slicing operations (such as `dict` and `set`). `copy()` is not part of the [`collections.abc.MutableSequence`](collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence") ABC, but most concrete mutable sequence classes provide it.

Added in version 3.3: `clear()` and `copy()` methods.

  6. The value _n_ is an integer, or an object implementing [`__index__()`](../reference/datamodel.html#object.__index__ "object.__index__"). Zero and negative values of _n_ clear the sequence. Items in the sequence are not copied; they are referenced multiple times, as explained for `s * n` under Common Sequence Operations.




### ListsÂ¶

Lists are mutable sequences, typically used to store collections of homogeneous items (where the precise degree of similarity will vary by application).

_class _list([_iterable_])Â¶
    

Lists may be constructed in several ways:

  * Using a pair of square brackets to denote the empty list: `[]`

  * Using square brackets, separating items with commas: `[a]`, `[a, b, c]`

  * Using a list comprehension: `[x for x in iterable]`

  * Using the type constructor: `list()` or `list(iterable)`




The constructor builds a list whose items are the same and in the same order as _iterable_ âs items. _iterable_ may be either a sequence, a container that supports iteration, or an iterator object. If _iterable_ is already a list, a copy is made and returned, similar to `iterable[:]`. For example, `list('abc')` returns `['a', 'b', 'c']` and `list( (1, 2, 3) )` returns `[1, 2, 3]`. If no argument is given, the constructor creates a new empty list, `[]`.

Many other operations also produce lists, including the [`sorted()`](functions.html#sorted "sorted") built-in.

Lists implement all of the common and mutable sequence operations. Lists also provide the following additional method:

sort(_*_ , _key =None_, _reverse =False_)Â¶
    

This method sorts the list in place, using only `<` comparisons between items. Exceptions are not suppressed - if any comparison operations fail, the entire sort operation will fail (and the list will likely be left in a partially modified state).

`sort()` accepts two arguments that can only be passed by keyword ([keyword-only arguments](../glossary.html#keyword-only-parameter)):

_key_ specifies a function of one argument that is used to extract a comparison key from each list element (for example, `key=str.lower`). The key corresponding to each item in the list is calculated once and then used for the entire sorting process. The default value of `None` means that list items are sorted directly without calculating a separate key value.

The [`functools.cmp_to_key()`](functools.html#functools.cmp_to_key "functools.cmp_to_key") utility is available to convert a 2.x style _cmp_ function to a _key_ function.

_reverse_ is a boolean value. If set to `True`, then the list elements are sorted as if each comparison were reversed.

This method modifies the sequence in place for economy of space when sorting a large sequence. To remind users that it operates by side effect, it does not return the sorted sequence (use [`sorted()`](functions.html#sorted "sorted") to explicitly request a new sorted list instance).

The `sort()` method is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal â this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).

For sorting examples and a brief sorting tutorial, see [Sorting Techniques](../howto/sorting.html#sortinghowto).

**CPython implementation detail:** While a list is being sorted, the effect of attempting to mutate, or even inspect, the list is undefined. The C implementation of Python makes the list appear empty for the duration, and raises [`ValueError`](exceptions.html#ValueError "ValueError") if it can detect that the list has been mutated during a sort.

### TuplesÂ¶

Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the [`enumerate()`](functions.html#enumerate "enumerate") built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a `set` or `dict` instance).

_class _tuple([_iterable_])Â¶
    

Tuples may be constructed in a number of ways:

  * Using a pair of parentheses to denote the empty tuple: `()`

  * Using a trailing comma for a singleton tuple: `a,` or `(a,)`

  * Separating items with commas: `a, b, c` or `(a, b, c)`

  * Using the `tuple()` built-in: `tuple()` or `tuple(iterable)`




The constructor builds a tuple whose items are the same and in the same order as _iterable_ âs items. _iterable_ may be either a sequence, a container that supports iteration, or an iterator object. If _iterable_ is already a tuple, it is returned unchanged. For example, `tuple('abc')` returns `('a', 'b', 'c')` and `tuple( [1, 2, 3] )` returns `(1, 2, 3)`. If no argument is given, the constructor creates a new empty tuple, `()`.

Note that it is actually the comma which makes a tuple, not the parentheses. The parentheses are optional, except in the empty tuple case, or when they are needed to avoid syntactic ambiguity. For example, `f(a, b, c)` is a function call with three arguments, while `f((a, b, c))` is a function call with a 3-tuple as the sole argument.

Tuples implement all of the common sequence operations.

For heterogeneous collections of data where access by name is clearer than access by index, [`collections.namedtuple()`](collections.html#collections.namedtuple "collections.namedtuple") may be a more appropriate choice than a simple tuple object.

### RangesÂ¶

The `range` type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in [`for`](../reference/compound_stmts.html#for) loops.

_class _range(_stop_)Â¶
_class _range(_start_ , _stop_[, _step_])
    

The arguments to the range constructor must be integers (either built-in [`int`](functions.html#int "int") or any object that implements the [`__index__()`](../reference/datamodel.html#object.__index__ "object.__index__") special method). If the _step_ argument is omitted, it defaults to `1`. If the _start_ argument is omitted, it defaults to `0`. If _step_ is zero, [`ValueError`](exceptions.html#ValueError "ValueError") is raised.

For a positive _step_ , the contents of a range `r` are determined by the formula `r[i] = start + step*i` where `i >= 0` and `r[i] < stop`.

For a negative _step_ , the contents of the range are still determined by the formula `r[i] = start + step*i`, but the constraints are `i >= 0` and `r[i] > stop`.

A range object will be empty if `r[0]` does not meet the value constraint. Ranges do support negative indices, but these are interpreted as indexing from the end of the sequence determined by the positive indices.

Ranges containing absolute values larger than [`sys.maxsize`](sys.html#sys.maxsize "sys.maxsize") are permitted but some features (such as [`len()`](functions.html#len "len")) may raise [`OverflowError`](exceptions.html#OverflowError "OverflowError").

Range examples:
    
    
    >>> list(range(10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(range(1, 11))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> list(range(0, 30, 5))
    [0, 5, 10, 15, 20, 25]
    >>> list(range(0, 10, 3))
    [0, 3, 6, 9]
    >>> list(range(0, -10, -1))
    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    >>> list(range(0))
    []
    >>> list(range(1, 0))
    []
    

Ranges implement all of the common sequence operations except concatenation and repetition (due to the fact that range objects can only represent sequences that follow a strict pattern and repetition and concatenation will usually violate that pattern).

startÂ¶
    

The value of the _start_ parameter (or `0` if the parameter was not supplied)

stopÂ¶
    

The value of the _stop_ parameter

stepÂ¶
    

The value of the _step_ parameter (or `1` if the parameter was not supplied)

The advantage of the `range` type over a regular `list` or `tuple` is that a `range` object will always take the same (small) amount of memory, no matter the size of the range it represents (as it only stores the `start`, `stop` and `step` values, calculating individual items and subranges as needed).

Range objects implement the [`collections.abc.Sequence`](collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") ABC, and provide features such as containment tests, element index lookup, slicing and support for negative indices (see Sequence Types â list, tuple, range):
    
    
    >>> r = range(0, 20, 2)
    >>> r
    range(0, 20, 2)
    >>> 11 in r
    False
    >>> 10 in r
    True
    >>> r.index(10)
    5
    >>> r[5]
    10
    >>> r[:5]
    range(0, 10, 2)
    >>> r[-1]
    18
    

Testing range objects for equality with `==` and `!=` compares them as sequences. That is, two range objects are considered equal if they represent the same sequence of values. (Note that two range objects that compare equal might have different `start`, `stop` and `step` attributes, for example `range(0) == range(2, 1, 3)` or `range(0, 3, 2) == range(0, 4, 2)`.)

Changed in version 3.2: Implement the Sequence ABC. Support slicing and negative indices. Test [`int`](functions.html#int "int") objects for membership in constant time instead of iterating through all items.

Changed in version 3.3: Define â==â and â!=â to compare range objects based on the sequence of values they define (instead of comparing based on object identity).

Added the `start`, `stop` and `step` attributes.

See also

  * The [linspace recipe](https://code.activestate.com/recipes/579000-equally-spaced-numbers-linspace/) shows how to implement a lazy version of range suitable for floating-point applications.




## Text Sequence Type â `str`Â¶

Textual data in Python is handled with `str` objects, or _strings_. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways:

  * Single quotes: `'allows embedded "double" quotes'`

  * Double quotes: `"allows embedded 'single' quotes"`

  * Triple quoted: `'''Three single quotes'''`, `"""Three double quotes"""`




Triple quoted strings may span multiple lines - all associated whitespace will be included in the string literal.

String literals that are part of a single expression and have only whitespace between them will be implicitly converted to a single string literal. That is, `("spam " "eggs") == "spam eggs"`.

See [String and Bytes literals](../reference/lexical_analysis.html#strings) for more about the various forms of string literal, including supported [escape sequences](../reference/lexical_analysis.html#escape-sequences), and the `r` (ârawâ) prefix that disables most escape sequence processing.

Strings may also be created from other objects using the `str` constructor.

Since there is no separate âcharacterâ type, indexing a string produces strings of length 1. That is, for a non-empty string _s_ , `s[0] == s[0:1]`.

There is also no mutable string type, but `str.join()` or [`io.StringIO`](io.html#io.StringIO "io.StringIO") can be used to efficiently construct strings from multiple fragments.

Changed in version 3.3: For backwards compatibility with the Python 2 series, the `u` prefix is once again permitted on string literals. It has no effect on the meaning of string literals and cannot be combined with the `r` prefix.

_class _str(_object =''_)Â¶
_class _str(_object =b''_, _encoding ='utf-8'_, _errors ='strict'_)
    

Return a string version of _object_. If _object_ is not provided, returns the empty string. Otherwise, the behavior of `str()` depends on whether _encoding_ or _errors_ is given, as follows.

If neither _encoding_ nor _errors_ is given, `str(object)` returns [`type(object).__str__(object)`](../reference/datamodel.html#object.__str__ "object.__str__"), which is the âinformalâ or nicely printable string representation of _object_. For string objects, this is the string itself. If _object_ does not have a [`__str__()`](../reference/datamodel.html#object.__str__ "object.__str__") method, then `str()` falls back to returning [`repr(object)`](functions.html#repr "repr").

If at least one of _encoding_ or _errors_ is given, _object_ should be a [bytes-like object](../glossary.html#term-bytes-like-object) (e.g. `bytes` or `bytearray`). In this case, if _object_ is a `bytes` (or `bytearray`) object, then `str(bytes, encoding, errors)` is equivalent to `bytes.decode(encoding, errors)`. Otherwise, the bytes object underlying the buffer object is obtained before calling `bytes.decode()`. See Binary Sequence Types â bytes, bytearray, memoryview and [Buffer Protocol](../c-api/buffer.html#bufferobjects) for information on buffer objects.

Passing a `bytes` object to `str()` without the _encoding_ or _errors_ arguments falls under the first case of returning the informal string representation (see also the [`-b`](../using/cmdline.html#cmdoption-b) command-line option to Python). For example:
    
    
    >>> str(b'Zoot!')
    "b'Zoot!'"
    

For more information on the `str` class and its methods, see Text Sequence Type â str and the String Methods section below. To output formatted strings, see the [f-strings](../reference/lexical_analysis.html#f-strings) and [Format String Syntax](string.html#formatstrings) sections. In addition, see the [Text Processing Services](text.html#stringservices) section.

### String MethodsÂ¶

Strings implement all of the common sequence operations, along with the additional methods described below.

Strings also support two styles of string formatting, one providing a large degree of flexibility and customization (see `str.format()`, [Format String Syntax](string.html#formatstrings) and [Custom String Formatting](string.html#string-formatting)) and the other based on C `printf` style formatting that handles a narrower range of types and is slightly harder to use correctly, but is often faster for the cases it can handle (printf-style String Formatting).

The [Text Processing Services](text.html#textservices) section of the standard library covers a number of other modules that provide various text related utilities (including regular expression support in the [`re`](re.html#module-re "re: Regular expression operations.") module).

str.capitalize()Â¶
    

Return a copy of the string with its first character capitalized and the rest lowercased.

Changed in version 3.8: The first character is now put into titlecase rather than uppercase. This means that characters like digraphs will only have their first letter capitalized, instead of the full character.

str.casefold()Â¶
    

Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.

Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. For example, the German lowercase letter `'Ã'` is equivalent to `"ss"`. Since it is already lowercase, `lower()` would do nothing to `'Ã'`; `casefold()` converts it to `"ss"`.

The casefolding algorithm is [described in section 3.13 âDefault Case Foldingâ of the Unicode Standard](https://www.unicode.org/versions/Unicode15.1.0/ch03.pdf).

Added in version 3.3.

str.center(_width_[, _fillchar_])Â¶
    

Return centered in a string of length _width_. Padding is done using the specified _fillchar_ (default is an ASCII space). The original string is returned if _width_ is less than or equal to `len(s)`.

str.count(_sub_[, _start_[, _end_]])Â¶
    

Return the number of non-overlapping occurrences of substring _sub_ in the range [_start_ , _end_]. Optional arguments _start_ and _end_ are interpreted as in slice notation.

If _sub_ is empty, returns the number of empty strings between characters which is the length of the string plus one.

str.encode(_encoding ='utf-8'_, _errors ='strict'_)Â¶
    

Return the string encoded to `bytes`.

_encoding_ defaults to `'utf-8'`; see [Standard Encodings](codecs.html#standard-encodings) for possible values.

_errors_ controls how encoding errors are handled. If `'strict'` (the default), a [`UnicodeError`](exceptions.html#UnicodeError "UnicodeError") exception is raised. Other possible values are `'ignore'`, `'replace'`, `'xmlcharrefreplace'`, `'backslashreplace'` and any other name registered via [`codecs.register_error()`](codecs.html#codecs.register_error "codecs.register_error"). See [Error Handlers](codecs.html#error-handlers) for details.

For performance reasons, the value of _errors_ is not checked for validity unless an encoding error actually occurs, [Python Development Mode](devmode.html#devmode) is enabled or a [debug build](../using/configure.html#debug-build) is used.

Changed in version 3.1: Added support for keyword arguments.

Changed in version 3.9: The value of the _errors_ argument is now checked in [Python Development Mode](devmode.html#devmode) and in [debug mode](../using/configure.html#debug-build).

str.endswith(_suffix_[, _start_[, _end_]])Â¶
    

Return `True` if the string ends with the specified _suffix_ , otherwise return `False`. _suffix_ can also be a tuple of suffixes to look for. With optional _start_ , test beginning at that position. With optional _end_ , stop comparing at that position.

str.expandtabs(_tabsize =8_)Â¶
    

Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size. Tab positions occur every _tabsize_ characters (default is 8, giving tab positions at columns 0, 8, 16 and so on). To expand the string, the current column is set to zero and the string is examined character by character. If the character is a tab (`\t`), one or more space characters are inserted in the result until the current column is equal to the next tab position. (The tab character itself is not copied.) If the character is a newline (`\n`) or return (`\r`), it is copied and the current column is reset to zero. Any other character is copied unchanged and the current column is incremented by one regardless of how the character is represented when printed.
    
    
    >>> '01\t012\t0123\t01234'.expandtabs()
    '01      012     0123    01234'
    >>> '01\t012\t0123\t01234'.expandtabs(4)
    '01  012 0123    01234'
    

str.find(_sub_[, _start_[, _end_]])Â¶
    

Return the lowest index in the string where substring _sub_ is found within the slice `s[start:end]`. Optional arguments _start_ and _end_ are interpreted as in slice notation. Return `-1` if _sub_ is not found.

Note

The `find()` method should be used only if you need to know the position of _sub_. To check if _sub_ is a substring or not, use the [`in`](../reference/expressions.html#in) operator:
    
    
    >>> 'Py' in 'Python'
    True
    

str.format(_* args_, _** kwargs_)Â¶
    

Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces `{}`. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.
    
    
    >>> "The sum of 1 + 2 is {0}".format(1+2)
    'The sum of 1 + 2 is 3'
    

See [Format String Syntax](string.html#formatstrings) for a description of the various formatting options that can be specified in format strings.

Note

When formatting a number ([`int`](functions.html#int "int"), [`float`](functions.html#float "float"), [`complex`](functions.html#complex "complex"), [`decimal.Decimal`](decimal.html#decimal.Decimal "decimal.Decimal") and subclasses) with the `n` type (ex: `'{:n}'.format(1234)`), the function temporarily sets the `LC_CTYPE` locale to the `LC_NUMERIC` locale to decode `decimal_point` and `thousands_sep` fields of `localeconv()` if they are non-ASCII or longer than 1 byte, and the `LC_NUMERIC` locale is different than the `LC_CTYPE` locale. This temporary change affects other threads.

Changed in version 3.7: When formatting a number with the `n` type, the function sets temporarily the `LC_CTYPE` locale to the `LC_NUMERIC` locale in some cases.

str.format_map(_mapping_ , _/_)Â¶
    

Similar to `str.format(**mapping)`, except that `mapping` is used directly and not copied to a `dict`. This is useful if for example `mapping` is a dict subclass:
    
    
    >>> class Default(dict):
    ...     def __missing__(self, key):
    ...         return key
    ...
    >>> '{name} was born in {country}'.format_map(Default(name='Guido'))
    'Guido was born in country'
    

Added in version 3.2.

str.index(_sub_[, _start_[, _end_]])Â¶
    

Like `find()`, but raise [`ValueError`](exceptions.html#ValueError "ValueError") when the substring is not found.

str.isalnum()Â¶
    

Return `True` if all characters in the string are alphanumeric and there is at least one character, `False` otherwise. A character `c` is alphanumeric if one of the following returns `True`: `c.isalpha()`, `c.isdecimal()`, `c.isdigit()`, or `c.isnumeric()`.

str.isalpha()Â¶
    

Return `True` if all characters in the string are alphabetic and there is at least one character, `False` otherwise. Alphabetic characters are those characters defined in the Unicode character database as âLetterâ, i.e., those with general category property being one of âLmâ, âLtâ, âLuâ, âLlâ, or âLoâ. Note that this is different from the [Alphabetic property defined in the section 4.10 âLetters, Alphabetic, and Ideographicâ of the Unicode Standard](https://www.unicode.org/versions/Unicode15.1.0/ch04.pdf).

str.isascii()Â¶
    

Return `True` if the string is empty or all characters in the string are ASCII, `False` otherwise. ASCII characters have code points in the range U+0000-U+007F.

Added in version 3.7.

str.isdecimal()Â¶
    

Return `True` if all characters in the string are decimal characters and there is at least one character, `False` otherwise. Decimal characters are those that can be used to form numbers in base 10, e.g. U+0660, ARABIC-INDIC DIGIT ZERO. Formally a decimal character is a character in the Unicode General Category âNdâ.

str.isdigit()Â¶
    

Return `True` if all characters in the string are digits and there is at least one character, `False` otherwise. Digits include decimal characters and digits that need special handling, such as the compatibility superscript digits. This covers digits which cannot be used to form numbers in base 10, like the Kharosthi numbers. Formally, a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.

str.isidentifier()Â¶
    

Return `True` if the string is a valid identifier according to the language definition, section [Identifiers and keywords](../reference/lexical_analysis.html#identifiers).

[`keyword.iskeyword()`](keyword.html#keyword.iskeyword "keyword.iskeyword") can be used to test whether string `s` is a reserved identifier, such as [`def`](../reference/compound_stmts.html#def) and [`class`](../reference/compound_stmts.html#class).

Example:
    
    
    >>> from keyword import iskeyword
    
    >>> 'hello'.isidentifier(), iskeyword('hello')
    (True, False)
    >>> 'def'.isidentifier(), iskeyword('def')
    (True, True)
    

str.islower()Â¶
    

Return `True` if all cased characters [4] in the string are lowercase and there is at least one cased character, `False` otherwise.

str.isnumeric()Â¶
    

Return `True` if all characters in the string are numeric characters, and there is at least one character, `False` otherwise. Numeric characters include digit characters, and all characters that have the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH. Formally, numeric characters are those with the property value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric.

str.isprintable()Â¶
    

Return true if all characters in the string are printable, false if it contains at least one non-printable character.

Here âprintableâ means the character is suitable for [`repr()`](functions.html#repr "repr") to use in its output; ânon-printableâ means that [`repr()`](functions.html#repr "repr") on built-in types will hex-escape the character. It has no bearing on the handling of strings written to [`sys.stdout`](sys.html#sys.stdout "sys.stdout") or [`sys.stderr`](sys.html#sys.stderr "sys.stderr").

The printable characters are those which in the Unicode character database (see [`unicodedata`](unicodedata.html#module-unicodedata "unicodedata: Access the Unicode Database.")) have a general category in group Letter, Mark, Number, Punctuation, or Symbol (L, M, N, P, or S); plus the ASCII space 0x20. Nonprintable characters are those in group Separator or Other (Z or C), except the ASCII space.

str.isspace()Â¶
    

Return `True` if there are only whitespace characters in the string and there is at least one character, `False` otherwise.

A character is _whitespace_ if in the Unicode character database (see [`unicodedata`](unicodedata.html#module-unicodedata "unicodedata: Access the Unicode Database.")), either its general category is `Zs` (âSeparator, spaceâ), or its bidirectional class is one of `WS`, `B`, or `S`.

str.istitle()Â¶
    

Return `True` if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return `False` otherwise.

str.isupper()Â¶
    

Return `True` if all cased characters [4] in the string are uppercase and there is at least one cased character, `False` otherwise.
    
    
    >>> 'BANANA'.isupper()
    True
    >>> 'banana'.isupper()
    False
    >>> 'baNana'.isupper()
    False
    >>> ' '.isupper()
    False
    

str.join(_iterable_)Â¶
    

Return a string which is the concatenation of the strings in _iterable_. A [`TypeError`](exceptions.html#TypeError "TypeError") will be raised if there are any non-string values in _iterable_ , including `bytes` objects. The separator between elements is the string providing this method.

str.ljust(_width_[, _fillchar_])Â¶
    

Return the string left justified in a string of length _width_. Padding is done using the specified _fillchar_ (default is an ASCII space). The original string is returned if _width_ is less than or equal to `len(s)`.

str.lower()Â¶
    

Return a copy of the string with all the cased characters [4] converted to lowercase.

The lowercasing algorithm used is [described in section 3.13 âDefault Case Foldingâ of the Unicode Standard](https://www.unicode.org/versions/Unicode15.1.0/ch03.pdf).

str.lstrip([_chars_])Â¶
    

Return a copy of the string with leading characters removed. The _chars_ argument is a string specifying the set of characters to be removed. If omitted or `None`, the _chars_ argument defaults to removing whitespace. The _chars_ argument is not a prefix; rather, all combinations of its values are stripped:
    
    
    >>> '   spacious   '.lstrip()
    'spacious   '
    >>> 'www.example.com'.lstrip('cmowz.')
    'example.com'
    

See `str.removeprefix()` for a method that will remove a single prefix string rather than all of a set of characters. For example:
    
    
    >>> 'Arthur: three!'.lstrip('Arthur: ')
    'ee!'
    >>> 'Arthur: three!'.removeprefix('Arthur: ')
    'three!'
    

_static _str.maketrans(_x_[, _y_[, _z_]])Â¶
    

This static method returns a translation table usable for `str.translate()`.

If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters (strings of length 1) to Unicode ordinals, strings (of arbitrary lengths) or `None`. Character keys will then be converted to ordinals.

If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to `None` in the result.

str.partition(_sep_)Â¶
    

Split the string at the first occurrence of _sep_ , and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.

str.removeprefix(_prefix_ , _/_)Â¶
    

If the string starts with the _prefix_ string, return `string[len(prefix):]`. Otherwise, return a copy of the original string:
    
    
    >>> 'TestHook'.removeprefix('Test')
    'Hook'
    >>> 'BaseTestCase'.removeprefix('Test')
    'BaseTestCase'
    

Added in version 3.9.

str.removesuffix(_suffix_ , _/_)Â¶
    

If the string ends with the _suffix_ string and that _suffix_ is not empty, return `string[:-len(suffix)]`. Otherwise, return a copy of the original string:
    
    
    >>> 'MiscTests'.removesuffix('Tests')
    'Misc'
    >>> 'TmpDirMixin'.removesuffix('Tests')
    'TmpDirMixin'
    

Added in version 3.9.

str.replace(_old_ , _new_ , _count =-1_)Â¶
    

Return a copy of the string with all occurrences of substring _old_ replaced by _new_. If _count_ is given, only the first _count_ occurrences are replaced. If _count_ is not specified or `-1`, then all occurrences are replaced.

Changed in version 3.13: _count_ is now supported as a keyword argument.

str.rfind(_sub_[, _start_[, _end_]])Â¶
    

Return the highest index in the string where substring _sub_ is found, such that _sub_ is contained within `s[start:end]`. Optional arguments _start_ and _end_ are interpreted as in slice notation. Return `-1` on failure.

str.rindex(_sub_[, _start_[, _end_]])Â¶
    

Like `rfind()` but raises [`ValueError`](exceptions.html#ValueError "ValueError") when the substring _sub_ is not found.

str.rjust(_width_[, _fillchar_])Â¶
    

Return the string right justified in a string of length _width_. Padding is done using the specified _fillchar_ (default is an ASCII space). The original string is returned if _width_ is less than or equal to `len(s)`.

str.rpartition(_sep_)Â¶
    

Split the string at the last occurrence of _sep_ , and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself.

str.rsplit(_sep =None_, _maxsplit =-1_)Â¶
    

Return a list of the words in the string, using _sep_ as the delimiter string. If _maxsplit_ is given, at most _maxsplit_ splits are done, the _rightmost_ ones. If _sep_ is not specified or `None`, any whitespace string is a separator. Except for splitting from the right, `rsplit()` behaves like `split()` which is described in detail below.

str.rstrip([_chars_])Â¶
    

Return a copy of the string with trailing characters removed. The _chars_ argument is a string specifying the set of characters to be removed. If omitted or `None`, the _chars_ argument defaults to removing whitespace. The _chars_ argument is not a suffix; rather, all combinations of its values are stripped:
    
    
    >>> '   spacious   '.rstrip()
    '   spacious'
    >>> 'mississippi'.rstrip('ipz')
    'mississ'
    

See `str.removesuffix()` for a method that will remove a single suffix string rather than all of a set of characters. For example:
    
    
    >>> 'Monty Python'.rstrip(' Python')
    'M'
    >>> 'Monty Python'.removesuffix(' Python')
    'Monty'
    

str.split(_sep =None_, _maxsplit =-1_)Â¶
    

Return a list of the words in the string, using _sep_ as the delimiter string. If _maxsplit_ is given, at most _maxsplit_ splits are done (thus, the list will have at most `maxsplit+1` elements). If _maxsplit_ is not specified or `-1`, then there is no limit on the number of splits (all possible splits are made).

If _sep_ is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, `'1,,2'.split(',')` returns `['1', '', '2']`). The _sep_ argument may consist of multiple characters as a single delimiter (to split with multiple delimiters, use [`re.split()`](re.html#re.split "re.split")). Splitting an empty string with a specified separator returns `['']`.

For example:
    
    
    >>> '1,2,3'.split(',')
    ['1', '2', '3']
    >>> '1,2,3'.split(',', maxsplit=1)
    ['1', '2,3']
    >>> '1,2,,3,'.split(',')
    ['1', '2', '', '3', '']
    >>> '1<>2<>3<4'.split('<>')
    ['1', '2', '3<4']
    

If _sep_ is not specified or is `None`, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a `None` separator returns `[]`.

For example:
    
    
    >>> '1 2 3'.split()
    ['1', '2', '3']
    >>> '1 2 3'.split(maxsplit=1)
    ['1', '2 3']
    >>> '   1   2   3   '.split()
    ['1', '2', '3']
    

str.splitlines(_keepends =False_)Â¶
    

Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless _keepends_ is given and true.

This method splits on the following line boundaries. In particular, the boundaries are a superset of [universal newlines](../glossary.html#term-universal-newlines).

Representation | Description  
---|---  
`\n` | Line Feed  
`\r` | Carriage Return  
`\r\n` | Carriage Return + Line Feed  
`\v` or `\x0b` | Line Tabulation  
`\f` or `\x0c` | Form Feed  
`\x1c` | File Separator  
`\x1d` | Group Separator  
`\x1e` | Record Separator  
`\x85` | Next Line (C1 Control Code)  
`\u2028` | Line Separator  
`\u2029` | Paragraph Separator  
  
Changed in version 3.2: `\v` and `\f` added to list of line boundaries.

For example:
    
    
    >>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
    ['ab c', '', 'de fg', 'kl']
    >>> 'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
    ['ab c\n', '\n', 'de fg\r', 'kl\r\n']
    

Unlike `split()` when a delimiter string _sep_ is given, this method returns an empty list for the empty string, and a terminal line break does not result in an extra line:
    
    
    >>> "".splitlines()
    []
    >>> "One line\n".splitlines()
    ['One line']
    

For comparison, `split('\n')` gives:
    
    
    >>> ''.split('\n')
    ['']
    >>> 'Two lines\n'.split('\n')
    ['Two lines', '']
    

str.startswith(_prefix_[, _start_[, _end_]])Â¶
    

Return `True` if string starts with the _prefix_ , otherwise return `False`. _prefix_ can also be a tuple of prefixes to look for. With optional _start_ , test string beginning at that position. With optional _end_ , stop comparing string at that position.

str.strip([_chars_])Â¶
    

Return a copy of the string with the leading and trailing characters removed. The _chars_ argument is a string specifying the set of characters to be removed. If omitted or `None`, the _chars_ argument defaults to removing whitespace. The _chars_ argument is not a prefix or suffix; rather, all combinations of its values are stripped:
    
    
    >>> '   spacious   '.strip()
    'spacious'
    >>> 'www.example.com'.strip('cmowz.')
    'example'
    

The outermost leading and trailing _chars_ argument values are stripped from the string. Characters are removed from the leading end until reaching a string character that is not contained in the set of characters in _chars_. A similar action takes place on the trailing end. For example:
    
    
    >>> comment_string = '#....... Section 3.2.1 Issue #32 .......'
    >>> comment_string.strip('.#! ')
    'Section 3.2.1 Issue #32'
    

str.swapcase()Â¶
    

Return a copy of the string with uppercase characters converted to lowercase and vice versa. Note that it is not necessarily true that `s.swapcase().swapcase() == s`.

str.title()Â¶
    

Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.

For example:
    
    
    >>> 'Hello world'.title()
    'Hello World'
    

The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions and possessives form word boundaries, which may not be the desired result:
    
    
    >>> "they're bill's friends from the UK".title()
    "They'Re Bill'S Friends From The Uk"
    

The [`string.capwords()`](string.html#string.capwords "string.capwords") function does not have this problem, as it splits words on spaces only.

Alternatively, a workaround for apostrophes can be constructed using regular expressions:
    
    
    >>> import re
    >>> def titlecase(s):
    ...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
    ...                   lambda mo: mo.group(0).capitalize(),
    ...                   s)
    ...
    >>> titlecase("they're bill's friends.")
    "They're Bill's Friends."
    

str.translate(_table_)Â¶
    

Return a copy of the string in which each character has been mapped through the given translation table. The table must be an object that implements indexing via [`__getitem__()`](../reference/datamodel.html#object.__getitem__ "object.__getitem__"), typically a [mapping](../glossary.html#term-mapping) or [sequence](../glossary.html#term-sequence). When indexed by a Unicode ordinal (an integer), the table object can do any of the following: return a Unicode ordinal or a string, to map the character to one or more other characters; return `None`, to delete the character from the return string; or raise a [`LookupError`](exceptions.html#LookupError "LookupError") exception, to map the character to itself.

You can use `str.maketrans()` to create a translation map from character-to-character mappings in different formats.

See also the [`codecs`](codecs.html#module-codecs "codecs: Encode and decode data and streams.") module for a more flexible approach to custom character mappings.

str.upper()Â¶
    

Return a copy of the string with all the cased characters [4] converted to uppercase. Note that `s.upper().isupper()` might be `False` if `s` contains uncased characters or if the Unicode category of the resulting character(s) is not âLuâ (Letter, uppercase), but e.g. âLtâ (Letter, titlecase).

The uppercasing algorithm used is [described in section 3.13 âDefault Case Foldingâ of the Unicode Standard](https://www.unicode.org/versions/Unicode15.1.0/ch03.pdf).

str.zfill(_width_)Â¶
    

Return a copy of the string left filled with ASCII `'0'` digits to make a string of length _width_. A leading sign prefix (`'+'`/`'-'`) is handled by inserting the padding _after_ the sign character rather than before. The original string is returned if _width_ is less than or equal to `len(s)`.

For example:
    
    
    >>> "42".zfill(5)
    '00042'
    >>> "-42".zfill(5)
    '-0042'
    

### `printf`-style String FormattingÂ¶

Note

The formatting operations described here exhibit a variety of quirks that lead to a number of common errors (such as failing to display tuples and dictionaries correctly). Using the newer [formatted string literals](../reference/lexical_analysis.html#f-strings), the `str.format()` interface, or [template strings](string.html#template-strings) may help avoid these errors. Each of these alternatives provides their own trade-offs and benefits of simplicity, flexibility, and/or extensibility.

String objects have one unique built-in operation: the `%` operator (modulo). This is also known as the string _formatting_ or _interpolation_ operator. Given `format % values` (where _format_ is a string), `%` conversion specifications in _format_ are replaced with zero or more elements of _values_. The effect is similar to using the `sprintf()` function in the C language. For example:
    
    
    >>> print('%s has %d quote types.' % ('Python', 2))
    Python has 2 quote types.
    

If _format_ requires a single argument, _values_ may be a single non-tuple object. [5] Otherwise, _values_ must be a tuple with exactly the number of items specified by the format string, or a single mapping object (for example, a dictionary).

A conversion specifier contains two or more characters and has the following components, which must occur in this order:

  1. The `'%'` character, which marks the start of the specifier.

  2. Mapping key (optional), consisting of a parenthesised sequence of characters (for example, `(somename)`).

  3. Conversion flags (optional), which affect the result of some conversion types.

  4. Minimum field width (optional). If specified as an `'*'` (asterisk), the actual width is read from the next element of the tuple in _values_ , and the object to convert comes after the minimum field width and optional precision.

  5. Precision (optional), given as a `'.'` (dot) followed by the precision. If specified as `'*'` (an asterisk), the actual precision is read from the next element of the tuple in _values_ , and the value to convert comes after the precision.

  6. Length modifier (optional).

  7. Conversion type.




When the right argument is a dictionary (or other mapping type), then the formats in the string _must_ include a parenthesised mapping key into that dictionary inserted immediately after the `'%'` character. The mapping key selects the value to be formatted from the mapping. For example:
    
    
    >>> print('%(language)s has %(number)03d quote types.' %
    ...       {'language': "Python", "number": 2})
    Python has 002 quote types.
    

In this case no `*` specifiers may occur in a format (since they require a sequential parameter list).

The conversion flag characters are:

Flag | Meaning  
---|---  
`'#'` | The value conversion will use the âalternate formâ (where defined below).  
`'0'` | The conversion will be zero padded for numeric values.  
`'-'` | The converted value is left adjusted (overrides the `'0'` conversion if both are given).  
`' '` | (a space) A blank should be left before a positive number (or empty string) produced by a signed conversion.  
`'+'` | A sign character (`'+'` or `'-'`) will precede the conversion (overrides a âspaceâ flag).  
  
A length modifier (`h`, `l`, or `L`) may be present, but is ignored as it is not necessary for Python â so e.g. `%ld` is identical to `%d`.

The conversion types are:

Conversion | Meaning | Notes  
---|---|---  
`'d'` | Signed integer decimal. |   
`'i'` | Signed integer decimal. |   
`'o'` | Signed octal value. | (1)  
`'u'` | Obsolete type â it is identical to `'d'`. | (6)  
`'x'` | Signed hexadecimal (lowercase). | (2)  
`'X'` | Signed hexadecimal (uppercase). | (2)  
`'e'` | Floating-point exponential format (lowercase). | (3)  
`'E'` | Floating-point exponential format (uppercase). | (3)  
`'f'` | Floating-point decimal format. | (3)  
`'F'` | Floating-point decimal format. | (3)  
`'g'` | Floating-point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. | (4)  
`'G'` | Floating-point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. | (4)  
`'c'` | Single character (accepts integer or single character string). |   
`'r'` | String (converts any Python object using [`repr()`](functions.html#repr "repr")). | (5)  
`'s'` | String (converts any Python object using `str()`). | (5)  
`'a'` | String (converts any Python object using [`ascii()`](functions.html#ascii "ascii")). | (5)  
`'%'` | No argument is converted, results in a `'%'` character in the result. |   
  
Notes:

  1. The alternate form causes a leading octal specifier (`'0o'`) to be inserted before the first digit.

  2. The alternate form causes a leading `'0x'` or `'0X'` (depending on whether the `'x'` or `'X'` format was used) to be inserted before the first digit.

  3. The alternate form causes the result to always contain a decimal point, even if no digits follow it.

The precision determines the number of digits after the decimal point and defaults to 6.

  4. The alternate form causes the result to always contain a decimal point, and trailing zeroes are not removed as they would otherwise be.

The precision determines the number of significant digits before and after the decimal point and defaults to 6.

  5. If precision is `N`, the output is truncated to `N` characters.

  6. See [**PEP 237**](https://peps.python.org/pep-0237/).




Since Python strings have an explicit length, `%s` conversions do not assume that `'\0'` is the end of the string.

Changed in version 3.1: `%f` conversions for numbers whose absolute value is over 1e50 are no longer replaced by `%g` conversions.

## Binary Sequence Types â `bytes`, `bytearray`, `memoryview`Â¶

The core built-in types for manipulating binary data are `bytes` and `bytearray`. They are supported by `memoryview` which uses the [buffer protocol](../c-api/buffer.html#bufferobjects) to access the memory of other binary objects without needing to make a copy.

The [`array`](array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") module supports efficient storage of basic data types like 32-bit integers and IEEE754 double-precision floating values.

### Bytes ObjectsÂ¶

Bytes objects are immutable sequences of single bytes. Since many major binary protocols are based on the ASCII text encoding, bytes objects offer several methods that are only valid when working with ASCII compatible data and are closely related to string objects in a variety of other ways.

_class _bytes([_source_[, _encoding_[, _errors_]]])Â¶
    

Firstly, the syntax for bytes literals is largely the same as that for string literals, except that a `b` prefix is added:

  * Single quotes: `b'still allows embedded "double" quotes'`

  * Double quotes: `b"still allows embedded 'single' quotes"`

  * Triple quoted: `b'''3 single quotes'''`, `b"""3 double quotes"""`




Only ASCII characters are permitted in bytes literals (regardless of the declared source code encoding). Any binary values over 127 must be entered into bytes literals using the appropriate escape sequence.

As with string literals, bytes literals may also use a `r` prefix to disable processing of escape sequences. See [String and Bytes literals](../reference/lexical_analysis.html#strings) for more about the various forms of bytes literal, including supported escape sequences.

While bytes literals and representations are based on ASCII text, bytes objects actually behave like immutable sequences of integers, with each value in the sequence restricted such that `0 <= x < 256` (attempts to violate this restriction will trigger [`ValueError`](exceptions.html#ValueError "ValueError")). This is done deliberately to emphasise that while many binary formats include ASCII based elements and can be usefully manipulated with some text-oriented algorithms, this is not generally the case for arbitrary binary data (blindly applying text processing algorithms to binary data formats that are not ASCII compatible will usually lead to data corruption).

In addition to the literal forms, bytes objects can be created in a number of other ways:

  * A zero-filled bytes object of a specified length: `bytes(10)`

  * From an iterable of integers: `bytes(range(20))`

  * Copying existing binary data via the buffer protocol: `bytes(obj)`




Also see the [bytes](functions.html#func-bytes) built-in.

Since 2 hexadecimal digits correspond precisely to a single byte, hexadecimal numbers are a commonly used format for describing binary data. Accordingly, the bytes type has an additional class method to read data in that format:

_classmethod _fromhex(_string_)Â¶
    

This `bytes` class method returns a bytes object, decoding the given string object. The string must contain two hexadecimal digits per byte, with ASCII whitespace being ignored.
    
    
    >>> bytes.fromhex('2Ef0 F1f2  ')
    b'.\xf0\xf1\xf2'
    

Changed in version 3.7: `bytes.fromhex()` now skips all ASCII whitespace in the string, not just spaces.

A reverse conversion function exists to transform a bytes object into its hexadecimal representation.

hex([_sep_[, _bytes_per_sep_]])Â¶
    

Return a string object containing two hexadecimal digits for each byte in the instance.
    
    
    >>> b'\xf0\xf1\xf2'.hex()
    'f0f1f2'
    

If you want to make the hex string easier to read, you can specify a single character separator _sep_ parameter to include in the output. By default, this separator will be included between each byte. A second optional _bytes_per_sep_ parameter controls the spacing. Positive values calculate the separator position from the right, negative values from the left.
    
    
    >>> value = b'\xf0\xf1\xf2'
    >>> value.hex('-')
    'f0-f1-f2'
    >>> value.hex('_', 2)
    'f0_f1f2'
    >>> b'UUDDLRLRAB'.hex(' ', -4)
    '55554444 4c524c52 4142'
    

Added in version 3.5.

Changed in version 3.8: `bytes.hex()` now supports optional _sep_ and _bytes_per_sep_ parameters to insert separators between bytes in the hex output.

Since bytes objects are sequences of integers (akin to a tuple), for a bytes object _b_ , `b[0]` will be an integer, while `b[0:1]` will be a bytes object of length 1. (This contrasts with text strings, where both indexing and slicing will produce a string of length 1)

The representation of bytes objects uses the literal format (`b'...'`) since it is often more useful than e.g. `bytes([46, 46, 46])`. You can always convert a bytes object into a list of integers using `list(b)`.

### Bytearray ObjectsÂ¶

`bytearray` objects are a mutable counterpart to `bytes` objects.

_class _bytearray([_source_[, _encoding_[, _errors_]]])Â¶
    

There is no dedicated literal syntax for bytearray objects, instead they are always created by calling the constructor:

  * Creating an empty instance: `bytearray()`

  * Creating a zero-filled instance with a given length: `bytearray(10)`

  * From an iterable of integers: `bytearray(range(20))`

  * Copying existing binary data via the buffer protocol: `bytearray(b'Hi!')`




As bytearray objects are mutable, they support the mutable sequence operations in addition to the common bytes and bytearray operations described in Bytes and Bytearray Operations.

Also see the [bytearray](functions.html#func-bytearray) built-in.

Since 2 hexadecimal digits correspond precisely to a single byte, hexadecimal numbers are a commonly used format for describing binary data. Accordingly, the bytearray type has an additional class method to read data in that format:

_classmethod _fromhex(_string_)Â¶
    

This `bytearray` class method returns bytearray object, decoding the given string object. The string must contain two hexadecimal digits per byte, with ASCII whitespace being ignored.
    
    
    >>> bytearray.fromhex('2Ef0 F1f2  ')
    bytearray(b'.\xf0\xf1\xf2')
    

Changed in version 3.7: `bytearray.fromhex()` now skips all ASCII whitespace in the string, not just spaces.

A reverse conversion function exists to transform a bytearray object into its hexadecimal representation.

hex([_sep_[, _bytes_per_sep_]])Â¶
    

Return a string object containing two hexadecimal digits for each byte in the instance.
    
    
    >>> bytearray(b'\xf0\xf1\xf2').hex()
    'f0f1f2'
    

Added in version 3.5.

Changed in version 3.8: Similar to `bytes.hex()`, `bytearray.hex()` now supports optional _sep_ and _bytes_per_sep_ parameters to insert separators between bytes in the hex output.

Since bytearray objects are sequences of integers (akin to a list), for a bytearray object _b_ , `b[0]` will be an integer, while `b[0:1]` will be a bytearray object of length 1. (This contrasts with text strings, where both indexing and slicing will produce a string of length 1)

The representation of bytearray objects uses the bytes literal format (`bytearray(b'...')`) since it is often more useful than e.g. `bytearray([46, 46, 46])`. You can always convert a bytearray object into a list of integers using `list(b)`.

### Bytes and Bytearray OperationsÂ¶

Both bytes and bytearray objects support the common sequence operations. They interoperate not just with operands of the same type, but with any [bytes-like object](../glossary.html#term-bytes-like-object). Due to this flexibility, they can be freely mixed in operations without causing errors. However, the return type of the result may depend on the order of operands.

Note

The methods on bytes and bytearray objects donât accept strings as their arguments, just as the methods on strings donât accept bytes as their arguments. For example, you have to write:
    
    
    a = "abc"
    b = a.replace("a", "f")
    

and:
    
    
    a = b"abc"
    b = a.replace(b"a", b"f")
    

Some bytes and bytearray operations assume the use of ASCII compatible binary formats, and hence should be avoided when working with arbitrary binary data. These restrictions are covered below.

Note

Using these ASCII based operations to manipulate binary data that is not stored in an ASCII based format may lead to data corruption.

The following methods on bytes and bytearray objects can be used with arbitrary binary data.

bytes.count(_sub_[, _start_[, _end_]])Â¶
bytearray.count(_sub_[, _start_[, _end_]])Â¶
    

Return the number of non-overlapping occurrences of subsequence _sub_ in the range [_start_ , _end_]. Optional arguments _start_ and _end_ are interpreted as in slice notation.

The subsequence to search for may be any [bytes-like object](../glossary.html#term-bytes-like-object) or an integer in the range 0 to 255.

If _sub_ is empty, returns the number of empty slices between characters which is the length of the bytes object plus one.

Changed in version 3.3: Also accept an integer in the range 0 to 255 as the subsequence.

bytes.removeprefix(_prefix_ , _/_)Â¶
bytearray.removeprefix(_prefix_ , _/_)Â¶
    

If the binary data starts with the _prefix_ string, return `bytes[len(prefix):]`. Otherwise, return a copy of the original binary data:
    
    
    >>> b'TestHook'.removeprefix(b'Test')
    b'Hook'
    >>> b'BaseTestCase'.removeprefix(b'Test')
    b'BaseTestCase'
    

The _prefix_ may be any [bytes-like object](../glossary.html#term-bytes-like-object).

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

Added in version 3.9.

bytes.removesuffix(_suffix_ , _/_)Â¶
bytearray.removesuffix(_suffix_ , _/_)Â¶
    

If the binary data ends with the _suffix_ string and that _suffix_ is not empty, return `bytes[:-len(suffix)]`. Otherwise, return a copy of the original binary data:
    
    
    >>> b'MiscTests'.removesuffix(b'Tests')
    b'Misc'
    >>> b'TmpDirMixin'.removesuffix(b'Tests')
    b'TmpDirMixin'
    

The _suffix_ may be any [bytes-like object](../glossary.html#term-bytes-like-object).

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

Added in version 3.9.

bytes.decode(_encoding ='utf-8'_, _errors ='strict'_)Â¶
bytearray.decode(_encoding ='utf-8'_, _errors ='strict'_)Â¶
    

Return the bytes decoded to a `str`.

_encoding_ defaults to `'utf-8'`; see [Standard Encodings](codecs.html#standard-encodings) for possible values.

_errors_ controls how decoding errors are handled. If `'strict'` (the default), a [`UnicodeError`](exceptions.html#UnicodeError "UnicodeError") exception is raised. Other possible values are `'ignore'`, `'replace'`, and any other name registered via [`codecs.register_error()`](codecs.html#codecs.register_error "codecs.register_error"). See [Error Handlers](codecs.html#error-handlers) for details.

For performance reasons, the value of _errors_ is not checked for validity unless a decoding error actually occurs, [Python Development Mode](devmode.html#devmode) is enabled or a [debug build](../using/configure.html#debug-build) is used.

Note

Passing the _encoding_ argument to `str` allows decoding any [bytes-like object](../glossary.html#term-bytes-like-object) directly, without needing to make a temporary `bytes` or `bytearray` object.

Changed in version 3.1: Added support for keyword arguments.

Changed in version 3.9: The value of the _errors_ argument is now checked in [Python Development Mode](devmode.html#devmode) and in [debug mode](../using/configure.html#debug-build).

bytes.endswith(_suffix_[, _start_[, _end_]])Â¶
bytearray.endswith(_suffix_[, _start_[, _end_]])Â¶
    

Return `True` if the binary data ends with the specified _suffix_ , otherwise return `False`. _suffix_ can also be a tuple of suffixes to look for. With optional _start_ , test beginning at that position. With optional _end_ , stop comparing at that position.

The suffix(es) to search for may be any [bytes-like object](../glossary.html#term-bytes-like-object).

bytes.find(_sub_[, _start_[, _end_]])Â¶
bytearray.find(_sub_[, _start_[, _end_]])Â¶
    

Return the lowest index in the data where the subsequence _sub_ is found, such that _sub_ is contained in the slice `s[start:end]`. Optional arguments _start_ and _end_ are interpreted as in slice notation. Return `-1` if _sub_ is not found.

The subsequence to search for may be any [bytes-like object](../glossary.html#term-bytes-like-object) or an integer in the range 0 to 255.

Note

The `find()` method should be used only if you need to know the position of _sub_. To check if _sub_ is a substring or not, use the [`in`](../reference/expressions.html#in) operator:
    
    
    >>> b'Py' in b'Python'
    True
    

Changed in version 3.3: Also accept an integer in the range 0 to 255 as the subsequence.

bytes.index(_sub_[, _start_[, _end_]])Â¶
bytearray.index(_sub_[, _start_[, _end_]])Â¶
    

Like `find()`, but raise [`ValueError`](exceptions.html#ValueError "ValueError") when the subsequence is not found.

The subsequence to search for may be any [bytes-like object](../glossary.html#term-bytes-like-object) or an integer in the range 0 to 255.

Changed in version 3.3: Also accept an integer in the range 0 to 255 as the subsequence.

bytes.join(_iterable_)Â¶
bytearray.join(_iterable_)Â¶
    

Return a bytes or bytearray object which is the concatenation of the binary data sequences in _iterable_. A [`TypeError`](exceptions.html#TypeError "TypeError") will be raised if there are any values in _iterable_ that are not [bytes-like objects](../glossary.html#term-bytes-like-object), including `str` objects. The separator between elements is the contents of the bytes or bytearray object providing this method.

_static _bytes.maketrans(_from_ , _to_)Â¶
_static _bytearray.maketrans(_from_ , _to_)Â¶
    

This static method returns a translation table usable for `bytes.translate()` that will map each character in _from_ into the character at the same position in _to_ ; _from_ and _to_ must both be [bytes-like objects](../glossary.html#term-bytes-like-object) and have the same length.

Added in version 3.1.

bytes.partition(_sep_)Â¶
bytearray.partition(_sep_)Â¶
    

Split the sequence at the first occurrence of _sep_ , and return a 3-tuple containing the part before the separator, the separator itself or its bytearray copy, and the part after the separator. If the separator is not found, return a 3-tuple containing a copy of the original sequence, followed by two empty bytes or bytearray objects.

The separator to search for may be any [bytes-like object](../glossary.html#term-bytes-like-object).

bytes.replace(_old_ , _new_[, _count_])Â¶
bytearray.replace(_old_ , _new_[, _count_])Â¶
    

Return a copy of the sequence with all occurrences of subsequence _old_ replaced by _new_. If the optional argument _count_ is given, only the first _count_ occurrences are replaced.

The subsequence to search for and its replacement may be any [bytes-like object](../glossary.html#term-bytes-like-object).

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.rfind(_sub_[, _start_[, _end_]])Â¶
bytearray.rfind(_sub_[, _start_[, _end_]])Â¶
    

Return the highest index in the sequence where the subsequence _sub_ is found, such that _sub_ is contained within `s[start:end]`. Optional arguments _start_ and _end_ are interpreted as in slice notation. Return `-1` on failure.

The subsequence to search for may be any [bytes-like object](../glossary.html#term-bytes-like-object) or an integer in the range 0 to 255.

Changed in version 3.3: Also accept an integer in the range 0 to 255 as the subsequence.

bytes.rindex(_sub_[, _start_[, _end_]])Â¶
bytearray.rindex(_sub_[, _start_[, _end_]])Â¶
    

Like `rfind()` but raises [`ValueError`](exceptions.html#ValueError "ValueError") when the subsequence _sub_ is not found.

The subsequence to search for may be any [bytes-like object](../glossary.html#term-bytes-like-object) or an integer in the range 0 to 255.

Changed in version 3.3: Also accept an integer in the range 0 to 255 as the subsequence.

bytes.rpartition(_sep_)Â¶
bytearray.rpartition(_sep_)Â¶
    

Split the sequence at the last occurrence of _sep_ , and return a 3-tuple containing the part before the separator, the separator itself or its bytearray copy, and the part after the separator. If the separator is not found, return a 3-tuple containing two empty bytes or bytearray objects, followed by a copy of the original sequence.

The separator to search for may be any [bytes-like object](../glossary.html#term-bytes-like-object).

bytes.startswith(_prefix_[, _start_[, _end_]])Â¶
bytearray.startswith(_prefix_[, _start_[, _end_]])Â¶
    

Return `True` if the binary data starts with the specified _prefix_ , otherwise return `False`. _prefix_ can also be a tuple of prefixes to look for. With optional _start_ , test beginning at that position. With optional _end_ , stop comparing at that position.

The prefix(es) to search for may be any [bytes-like object](../glossary.html#term-bytes-like-object).

bytes.translate(_table_ , _/_ , _delete =b''_)Â¶
bytearray.translate(_table_ , _/_ , _delete =b''_)Â¶
    

Return a copy of the bytes or bytearray object where all bytes occurring in the optional argument _delete_ are removed, and the remaining bytes have been mapped through the given translation table, which must be a bytes object of length 256.

You can use the `bytes.maketrans()` method to create a translation table.

Set the _table_ argument to `None` for translations that only delete characters:
    
    
    >>> b'read this short text'.translate(None, b'aeiou')
    b'rd ths shrt txt'
    

Changed in version 3.6: _delete_ is now supported as a keyword argument.

The following methods on bytes and bytearray objects have default behaviours that assume the use of ASCII compatible binary formats, but can still be used with arbitrary binary data by passing appropriate arguments. Note that all of the bytearray methods in this section do _not_ operate in place, and instead produce new objects.

bytes.center(_width_[, _fillbyte_])Â¶
bytearray.center(_width_[, _fillbyte_])Â¶
    

Return a copy of the object centered in a sequence of length _width_. Padding is done using the specified _fillbyte_ (default is an ASCII space). For `bytes` objects, the original sequence is returned if _width_ is less than or equal to `len(s)`.

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.ljust(_width_[, _fillbyte_])Â¶
bytearray.ljust(_width_[, _fillbyte_])Â¶
    

Return a copy of the object left justified in a sequence of length _width_. Padding is done using the specified _fillbyte_ (default is an ASCII space). For `bytes` objects, the original sequence is returned if _width_ is less than or equal to `len(s)`.

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.lstrip([_chars_])Â¶
bytearray.lstrip([_chars_])Â¶
    

Return a copy of the sequence with specified leading bytes removed. The _chars_ argument is a binary sequence specifying the set of byte values to be removed - the name refers to the fact this method is usually used with ASCII characters. If omitted or `None`, the _chars_ argument defaults to removing ASCII whitespace. The _chars_ argument is not a prefix; rather, all combinations of its values are stripped:
    
    
    >>> b'   spacious   '.lstrip()
    b'spacious   '
    >>> b'www.example.com'.lstrip(b'cmowz.')
    b'example.com'
    

The binary sequence of byte values to remove may be any [bytes-like object](../glossary.html#term-bytes-like-object). See `removeprefix()` for a method that will remove a single prefix string rather than all of a set of characters. For example:
    
    
    >>> b'Arthur: three!'.lstrip(b'Arthur: ')
    b'ee!'
    >>> b'Arthur: three!'.removeprefix(b'Arthur: ')
    b'three!'
    

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.rjust(_width_[, _fillbyte_])Â¶
bytearray.rjust(_width_[, _fillbyte_])Â¶
    

Return a copy of the object right justified in a sequence of length _width_. Padding is done using the specified _fillbyte_ (default is an ASCII space). For `bytes` objects, the original sequence is returned if _width_ is less than or equal to `len(s)`.

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.rsplit(_sep =None_, _maxsplit =-1_)Â¶
bytearray.rsplit(_sep =None_, _maxsplit =-1_)Â¶
    

Split the binary sequence into subsequences of the same type, using _sep_ as the delimiter string. If _maxsplit_ is given, at most _maxsplit_ splits are done, the _rightmost_ ones. If _sep_ is not specified or `None`, any subsequence consisting solely of ASCII whitespace is a separator. Except for splitting from the right, `rsplit()` behaves like `split()` which is described in detail below.

bytes.rstrip([_chars_])Â¶
bytearray.rstrip([_chars_])Â¶
    

Return a copy of the sequence with specified trailing bytes removed. The _chars_ argument is a binary sequence specifying the set of byte values to be removed - the name refers to the fact this method is usually used with ASCII characters. If omitted or `None`, the _chars_ argument defaults to removing ASCII whitespace. The _chars_ argument is not a suffix; rather, all combinations of its values are stripped:
    
    
    >>> b'   spacious   '.rstrip()
    b'   spacious'
    >>> b'mississippi'.rstrip(b'ipz')
    b'mississ'
    

The binary sequence of byte values to remove may be any [bytes-like object](../glossary.html#term-bytes-like-object). See `removesuffix()` for a method that will remove a single suffix string rather than all of a set of characters. For example:
    
    
    >>> b'Monty Python'.rstrip(b' Python')
    b'M'
    >>> b'Monty Python'.removesuffix(b' Python')
    b'Monty'
    

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.split(_sep =None_, _maxsplit =-1_)Â¶
bytearray.split(_sep =None_, _maxsplit =-1_)Â¶
    

Split the binary sequence into subsequences of the same type, using _sep_ as the delimiter string. If _maxsplit_ is given and non-negative, at most _maxsplit_ splits are done (thus, the list will have at most `maxsplit+1` elements). If _maxsplit_ is not specified or is `-1`, then there is no limit on the number of splits (all possible splits are made).

If _sep_ is given, consecutive delimiters are not grouped together and are deemed to delimit empty subsequences (for example, `b'1,,2'.split(b',')` returns `[b'1', b'', b'2']`). The _sep_ argument may consist of a multibyte sequence as a single delimiter. Splitting an empty sequence with a specified separator returns `[b'']` or `[bytearray(b'')]` depending on the type of object being split. The _sep_ argument may be any [bytes-like object](../glossary.html#term-bytes-like-object).

For example:
    
    
    >>> b'1,2,3'.split(b',')
    [b'1', b'2', b'3']
    >>> b'1,2,3'.split(b',', maxsplit=1)
    [b'1', b'2,3']
    >>> b'1,2,,3,'.split(b',')
    [b'1', b'2', b'', b'3', b'']
    >>> b'1<>2<>3<4'.split(b'<>')
    [b'1', b'2', b'3<4']
    

If _sep_ is not specified or is `None`, a different splitting algorithm is applied: runs of consecutive ASCII whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the sequence has leading or trailing whitespace. Consequently, splitting an empty sequence or a sequence consisting solely of ASCII whitespace without a specified separator returns `[]`.

For example:
    
    
    >>> b'1 2 3'.split()
    [b'1', b'2', b'3']
    >>> b'1 2 3'.split(maxsplit=1)
    [b'1', b'2 3']
    >>> b'   1   2   3   '.split()
    [b'1', b'2', b'3']
    

bytes.strip([_chars_])Â¶
bytearray.strip([_chars_])Â¶
    

Return a copy of the sequence with specified leading and trailing bytes removed. The _chars_ argument is a binary sequence specifying the set of byte values to be removed - the name refers to the fact this method is usually used with ASCII characters. If omitted or `None`, the _chars_ argument defaults to removing ASCII whitespace. The _chars_ argument is not a prefix or suffix; rather, all combinations of its values are stripped:
    
    
    >>> b'   spacious   '.strip()
    b'spacious'
    >>> b'www.example.com'.strip(b'cmowz.')
    b'example'
    

The binary sequence of byte values to remove may be any [bytes-like object](../glossary.html#term-bytes-like-object).

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

The following methods on bytes and bytearray objects assume the use of ASCII compatible binary formats and should not be applied to arbitrary binary data. Note that all of the bytearray methods in this section do _not_ operate in place, and instead produce new objects.

bytes.capitalize()Â¶
bytearray.capitalize()Â¶
    

Return a copy of the sequence with each byte interpreted as an ASCII character, and the first byte capitalized and the rest lowercased. Non-ASCII byte values are passed through unchanged.

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.expandtabs(_tabsize =8_)Â¶
bytearray.expandtabs(_tabsize =8_)Â¶
    

Return a copy of the sequence where all ASCII tab characters are replaced by one or more ASCII spaces, depending on the current column and the given tab size. Tab positions occur every _tabsize_ bytes (default is 8, giving tab positions at columns 0, 8, 16 and so on). To expand the sequence, the current column is set to zero and the sequence is examined byte by byte. If the byte is an ASCII tab character (`b'\t'`), one or more space characters are inserted in the result until the current column is equal to the next tab position. (The tab character itself is not copied.) If the current byte is an ASCII newline (`b'\n'`) or carriage return (`b'\r'`), it is copied and the current column is reset to zero. Any other byte value is copied unchanged and the current column is incremented by one regardless of how the byte value is represented when printed:
    
    
    >>> b'01\t012\t0123\t01234'.expandtabs()
    b'01      012     0123    01234'
    >>> b'01\t012\t0123\t01234'.expandtabs(4)
    b'01  012 0123    01234'
    

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.isalnum()Â¶
bytearray.isalnum()Â¶
    

Return `True` if all bytes in the sequence are alphabetical ASCII characters or ASCII decimal digits and the sequence is not empty, `False` otherwise. Alphabetic ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`. ASCII decimal digits are those byte values in the sequence `b'0123456789'`.

For example:
    
    
    >>> b'ABCabc1'.isalnum()
    True
    >>> b'ABC abc1'.isalnum()
    False
    

bytes.isalpha()Â¶
bytearray.isalpha()Â¶
    

Return `True` if all bytes in the sequence are alphabetic ASCII characters and the sequence is not empty, `False` otherwise. Alphabetic ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

For example:
    
    
    >>> b'ABCabc'.isalpha()
    True
    >>> b'ABCabc1'.isalpha()
    False
    

bytes.isascii()Â¶
bytearray.isascii()Â¶
    

Return `True` if the sequence is empty or all bytes in the sequence are ASCII, `False` otherwise. ASCII bytes are in the range 0-0x7F.

Added in version 3.7.

bytes.isdigit()Â¶
bytearray.isdigit()Â¶
    

Return `True` if all bytes in the sequence are ASCII decimal digits and the sequence is not empty, `False` otherwise. ASCII decimal digits are those byte values in the sequence `b'0123456789'`.

For example:
    
    
    >>> b'1234'.isdigit()
    True
    >>> b'1.23'.isdigit()
    False
    

bytes.islower()Â¶
bytearray.islower()Â¶
    

Return `True` if there is at least one lowercase ASCII character in the sequence and no uppercase ASCII characters, `False` otherwise.

For example:
    
    
    >>> b'hello world'.islower()
    True
    >>> b'Hello world'.islower()
    False
    

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

bytes.isspace()Â¶
bytearray.isspace()Â¶
    

Return `True` if all bytes in the sequence are ASCII whitespace and the sequence is not empty, `False` otherwise. ASCII whitespace characters are those byte values in the sequence `b' \t\n\r\x0b\f'` (space, tab, newline, carriage return, vertical tab, form feed).

bytes.istitle()Â¶
bytearray.istitle()Â¶
    

Return `True` if the sequence is ASCII titlecase and the sequence is not empty, `False` otherwise. See `bytes.title()` for more details on the definition of âtitlecaseâ.

For example:
    
    
    >>> b'Hello World'.istitle()
    True
    >>> b'Hello world'.istitle()
    False
    

bytes.isupper()Â¶
bytearray.isupper()Â¶
    

Return `True` if there is at least one uppercase alphabetic ASCII character in the sequence and no lowercase ASCII characters, `False` otherwise.

For example:
    
    
    >>> b'HELLO WORLD'.isupper()
    True
    >>> b'Hello world'.isupper()
    False
    

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

bytes.lower()Â¶
bytearray.lower()Â¶
    

Return a copy of the sequence with all the uppercase ASCII characters converted to their corresponding lowercase counterpart.

For example:
    
    
    >>> b'Hello World'.lower()
    b'hello world'
    

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.splitlines(_keepends =False_)Â¶
bytearray.splitlines(_keepends =False_)Â¶
    

Return a list of the lines in the binary sequence, breaking at ASCII line boundaries. This method uses the [universal newlines](../glossary.html#term-universal-newlines) approach to splitting lines. Line breaks are not included in the resulting list unless _keepends_ is given and true.

For example:
    
    
    >>> b'ab c\n\nde fg\rkl\r\n'.splitlines()
    [b'ab c', b'', b'de fg', b'kl']
    >>> b'ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)
    [b'ab c\n', b'\n', b'de fg\r', b'kl\r\n']
    

Unlike `split()` when a delimiter string _sep_ is given, this method returns an empty list for the empty string, and a terminal line break does not result in an extra line:
    
    
    >>> b"".split(b'\n'), b"Two lines\n".split(b'\n')
    ([b''], [b'Two lines', b''])
    >>> b"".splitlines(), b"One line\n".splitlines()
    ([], [b'One line'])
    

bytes.swapcase()Â¶
bytearray.swapcase()Â¶
    

Return a copy of the sequence with all the lowercase ASCII characters converted to their corresponding uppercase counterpart and vice-versa.

For example:
    
    
    >>> b'Hello World'.swapcase()
    b'hELLO wORLD'
    

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

Unlike `str.swapcase()`, it is always the case that `bin.swapcase().swapcase() == bin` for the binary versions. Case conversions are symmetrical in ASCII, even though that is not generally true for arbitrary Unicode code points.

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.title()Â¶
bytearray.title()Â¶
    

Return a titlecased version of the binary sequence where words start with an uppercase ASCII character and the remaining characters are lowercase. Uncased byte values are left unmodified.

For example:
    
    
    >>> b'Hello world'.title()
    b'Hello World'
    

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`. All other byte values are uncased.

The algorithm uses a simple language-independent definition of a word as groups of consecutive letters. The definition works in many contexts but it means that apostrophes in contractions and possessives form word boundaries, which may not be the desired result:
    
    
    >>> b"they're bill's friends from the UK".title()
    b"They'Re Bill'S Friends From The Uk"
    

A workaround for apostrophes can be constructed using regular expressions:
    
    
    >>> import re
    >>> def titlecase(s):
    ...     return re.sub(rb"[A-Za-z]+('[A-Za-z]+)?",
    ...                   lambda mo: mo.group(0)[0:1].upper() +
    ...                              mo.group(0)[1:].lower(),
    ...                   s)
    ...
    >>> titlecase(b"they're bill's friends.")
    b"They're Bill's Friends."
    

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.upper()Â¶
bytearray.upper()Â¶
    

Return a copy of the sequence with all the lowercase ASCII characters converted to their corresponding uppercase counterpart.

For example:
    
    
    >>> b'Hello World'.upper()
    b'HELLO WORLD'
    

Lowercase ASCII characters are those byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are those byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

bytes.zfill(_width_)Â¶
bytearray.zfill(_width_)Â¶
    

Return a copy of the sequence left filled with ASCII `b'0'` digits to make a sequence of length _width_. A leading sign prefix (`b'+'`/ `b'-'`) is handled by inserting the padding _after_ the sign character rather than before. For `bytes` objects, the original sequence is returned if _width_ is less than or equal to `len(seq)`.

For example:
    
    
    >>> b"42".zfill(5)
    b'00042'
    >>> b"-42".zfill(5)
    b'-0042'
    

Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

### `printf`-style Bytes FormattingÂ¶

Note

The formatting operations described here exhibit a variety of quirks that lead to a number of common errors (such as failing to display tuples and dictionaries correctly). If the value being printed may be a tuple or dictionary, wrap it in a tuple.

Bytes objects (`bytes`/`bytearray`) have one unique built-in operation: the `%` operator (modulo). This is also known as the bytes _formatting_ or _interpolation_ operator. Given `format % values` (where _format_ is a bytes object), `%` conversion specifications in _format_ are replaced with zero or more elements of _values_. The effect is similar to using the `sprintf()` in the C language.

If _format_ requires a single argument, _values_ may be a single non-tuple object. [5] Otherwise, _values_ must be a tuple with exactly the number of items specified by the format bytes object, or a single mapping object (for example, a dictionary).

A conversion specifier contains two or more characters and has the following components, which must occur in this order:

  1. The `'%'` character, which marks the start of the specifier.

  2. Mapping key (optional), consisting of a parenthesised sequence of characters (for example, `(somename)`).

  3. Conversion flags (optional), which affect the result of some conversion types.

  4. Minimum field width (optional). If specified as an `'*'` (asterisk), the actual width is read from the next element of the tuple in _values_ , and the object to convert comes after the minimum field width and optional precision.

  5. Precision (optional), given as a `'.'` (dot) followed by the precision. If specified as `'*'` (an asterisk), the actual precision is read from the next element of the tuple in _values_ , and the value to convert comes after the precision.

  6. Length modifier (optional).

  7. Conversion type.




When the right argument is a dictionary (or other mapping type), then the formats in the bytes object _must_ include a parenthesised mapping key into that dictionary inserted immediately after the `'%'` character. The mapping key selects the value to be formatted from the mapping. For example:
    
    
    >>> print(b'%(language)s has %(number)03d quote types.' %
    ...       {b'language': b"Python", b"number": 2})
    b'Python has 002 quote types.'
    

In this case no `*` specifiers may occur in a format (since they require a sequential parameter list).

The conversion flag characters are:

Flag | Meaning  
---|---  
`'#'` | The value conversion will use the âalternate formâ (where defined below).  
`'0'` | The conversion will be zero padded for numeric values.  
`'-'` | The converted value is left adjusted (overrides the `'0'` conversion if both are given).  
`' '` | (a space) A blank should be left before a positive number (or empty string) produced by a signed conversion.  
`'+'` | A sign character (`'+'` or `'-'`) will precede the conversion (overrides a âspaceâ flag).  
  
A length modifier (`h`, `l`, or `L`) may be present, but is ignored as it is not necessary for Python â so e.g. `%ld` is identical to `%d`.

The conversion types are:

Conversion | Meaning | Notes  
---|---|---  
`'d'` | Signed integer decimal. |   
`'i'` | Signed integer decimal. |   
`'o'` | Signed octal value. | (1)  
`'u'` | Obsolete type â it is identical to `'d'`. | (8)  
`'x'` | Signed hexadecimal (lowercase). | (2)  
`'X'` | Signed hexadecimal (uppercase). | (2)  
`'e'` | Floating-point exponential format (lowercase). | (3)  
`'E'` | Floating-point exponential format (uppercase). | (3)  
`'f'` | Floating-point decimal format. | (3)  
`'F'` | Floating-point decimal format. | (3)  
`'g'` | Floating-point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. | (4)  
`'G'` | Floating-point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. | (4)  
`'c'` | Single byte (accepts integer or single byte objects). |   
`'b'` | Bytes (any object that follows the [buffer protocol](../c-api/buffer.html#bufferobjects) or has [`__bytes__()`](../reference/datamodel.html#object.__bytes__ "object.__bytes__")). | (5)  
`'s'` | `'s'` is an alias for `'b'` and should only be used for Python2/3 code bases. | (6)  
`'a'` | Bytes (converts any Python object using `repr(obj).encode('ascii', 'backslashreplace')`). | (5)  
`'r'` | `'r'` is an alias for `'a'` and should only be used for Python2/3 code bases. | (7)  
`'%'` | No argument is converted, results in a `'%'` character in the result. |   
  
Notes:

  1. The alternate form causes a leading octal specifier (`'0o'`) to be inserted before the first digit.

  2. The alternate form causes a leading `'0x'` or `'0X'` (depending on whether the `'x'` or `'X'` format was used) to be inserted before the first digit.

  3. The alternate form causes the result to always contain a decimal point, even if no digits follow it.

The precision determines the number of digits after the decimal point and defaults to 6.

  4. The alternate form causes the result to always contain a decimal point, and trailing zeroes are not removed as they would otherwise be.

The precision determines the number of significant digits before and after the decimal point and defaults to 6.

  5. If precision is `N`, the output is truncated to `N` characters.

  6. `b'%s'` is deprecated, but will not be removed during the 3.x series.

  7. `b'%r'` is deprecated, but will not be removed during the 3.x series.

  8. See [**PEP 237**](https://peps.python.org/pep-0237/).




Note

The bytearray version of this method does _not_ operate in place - it always produces a new object, even if no changes were made.

See also

[**PEP 461**](https://peps.python.org/pep-0461/) \- Adding % formatting to bytes and bytearray

Added in version 3.5.

### Memory ViewsÂ¶

`memoryview` objects allow Python code to access the internal data of an object that supports the [buffer protocol](../c-api/buffer.html#bufferobjects) without copying.

_class _memoryview(_object_)Â¶
    

Create a `memoryview` that references _object_. _object_ must support the buffer protocol. Built-in objects that support the buffer protocol include `bytes` and `bytearray`.

A `memoryview` has the notion of an _element_ , which is the atomic memory unit handled by the originating _object_. For many simple types such as `bytes` and `bytearray`, an element is a single byte, but other types such as [`array.array`](array.html#array.array "array.array") may have bigger elements.

`len(view)` is equal to the length of `tolist`, which is the nested list representation of the view. If `view.ndim = 1`, this is equal to the number of elements in the view.

Changed in version 3.12: If `view.ndim == 0`, `len(view)` now raises [`TypeError`](exceptions.html#TypeError "TypeError") instead of returning 1.

The `itemsize` attribute will give you the number of bytes in a single element.

A `memoryview` supports slicing and indexing to expose its data. One-dimensional slicing will result in a subview:
    
    
    >>> v = memoryview(b'abcefg')
    >>> v[1]
    98
    >>> v[-1]
    103
    >>> v[1:4]
    <memory at 0x7f3ddc9f4350>
    >>> bytes(v[1:4])
    b'bce'
    

If `format` is one of the native format specifiers from the [`struct`](struct.html#module-struct "struct: Interpret bytes as packed binary data.") module, indexing with an integer or a tuple of integers is also supported and returns a single _element_ with the correct type. One-dimensional memoryviews can be indexed with an integer or a one-integer tuple. Multi-dimensional memoryviews can be indexed with tuples of exactly _ndim_ integers where _ndim_ is the number of dimensions. Zero-dimensional memoryviews can be indexed with the empty tuple.

Here is an example with a non-byte format:
    
    
    >>> import array
    >>> a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
    >>> m = memoryview(a)
    >>> m[0]
    -11111111
    >>> m[-1]
    44444444
    >>> m[::2].tolist()
    [-11111111, -33333333]
    

If the underlying object is writable, the memoryview supports one-dimensional slice assignment. Resizing is not allowed:
    
    
    >>> data = bytearray(b'abcefg')
    >>> v = memoryview(data)
    >>> v.readonly
    False
    >>> v[0] = ord(b'z')
    >>> data
    bytearray(b'zbcefg')
    >>> v[1:4] = b'123'
    >>> data
    bytearray(b'z123fg')
    >>> v[2:3] = b'spam'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: memoryview assignment: lvalue and rvalue have different structures
    >>> v[2:6] = b'spam'
    >>> data
    bytearray(b'z1spam')
    

One-dimensional memoryviews of [hashable](../glossary.html#term-hashable) (read-only) types with formats âBâ, âbâ or âcâ are also hashable. The hash is defined as `hash(m) == hash(m.tobytes())`:
    
    
    >>> v = memoryview(b'abcefg')
    >>> hash(v) == hash(b'abcefg')
    True
    >>> hash(v[2:4]) == hash(b'ce')
    True
    >>> hash(v[::-2]) == hash(b'abcefg'[::-2])
    True
    

Changed in version 3.3: One-dimensional memoryviews can now be sliced. One-dimensional memoryviews with formats âBâ, âbâ or âcâ are now [hashable](../glossary.html#term-hashable).

Changed in version 3.4: memoryview is now registered automatically with [`collections.abc.Sequence`](collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")

Changed in version 3.5: memoryviews can now be indexed with tuple of integers.

`memoryview` has several methods:

__eq__(_exporter_)Â¶
    

A memoryview and a [**PEP 3118**](https://peps.python.org/pep-3118/) exporter are equal if their shapes are equivalent and if all corresponding values are equal when the operandsâ respective format codes are interpreted using [`struct`](struct.html#module-struct "struct: Interpret bytes as packed binary data.") syntax.

For the subset of [`struct`](struct.html#module-struct "struct: Interpret bytes as packed binary data.") format strings currently supported by `tolist()`, `v` and `w` are equal if `v.tolist() == w.tolist()`:
    
    
    >>> import array
    >>> a = array.array('I', [1, 2, 3, 4, 5])
    >>> b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
    >>> c = array.array('b', [5, 3, 1])
    >>> x = memoryview(a)
    >>> y = memoryview(b)
    >>> x == a == y == b
    True
    >>> x.tolist() == a.tolist() == y.tolist() == b.tolist()
    True
    >>> z = y[::-2]
    >>> z == c
    True
    >>> z.tolist() == c.tolist()
    True
    

If either format string is not supported by the [`struct`](struct.html#module-struct "struct: Interpret bytes as packed binary data.") module, then the objects will always compare as unequal (even if the format strings and buffer contents are identical):
    
    
    >>> from ctypes import BigEndianStructure, c_long
    >>> class BEPoint(BigEndianStructure):
    ...     _fields_ = [("x", c_long), ("y", c_long)]
    ...
    >>> point = BEPoint(100, 200)
    >>> a = memoryview(point)
    >>> b = memoryview(point)
    >>> a == point
    False
    >>> a == b
    False
    

Note that, as with floating-point numbers, `v is w` does _not_ imply `v == w` for memoryview objects.

Changed in version 3.3: Previous versions compared the raw memory disregarding the item format and the logical array structure.

tobytes(_order ='C'_)Â¶
    

Return the data in the buffer as a bytestring. This is equivalent to calling the `bytes` constructor on the memoryview.
    
    
    >>> m = memoryview(b"abc")
    >>> m.tobytes()
    b'abc'
    >>> bytes(m)
    b'abc'
    

For non-contiguous arrays the result is equal to the flattened list representation with all elements converted to bytes. `tobytes()` supports all format strings, including those that are not in [`struct`](struct.html#module-struct "struct: Interpret bytes as packed binary data.") module syntax.

Added in version 3.8: _order_ can be {âCâ, âFâ, âAâ}. When _order_ is âCâ or âFâ, the data of the original array is converted to C or Fortran order. For contiguous views, âAâ returns an exact copy of the physical memory. In particular, in-memory Fortran order is preserved. For non-contiguous views, the data is converted to C first. _order=None_ is the same as _order=âCâ_.

hex([_sep_[, _bytes_per_sep_]])Â¶
    

Return a string object containing two hexadecimal digits for each byte in the buffer.
    
    
    >>> m = memoryview(b"abc")
    >>> m.hex()
    '616263'
    

Added in version 3.5.

Changed in version 3.8: Similar to `bytes.hex()`, `memoryview.hex()` now supports optional _sep_ and _bytes_per_sep_ parameters to insert separators between bytes in the hex output.

tolist()Â¶
    

Return the data in the buffer as a list of elements.
    
    
    >>> memoryview(b'abc').tolist()
    [97, 98, 99]
    >>> import array
    >>> a = array.array('d', [1.1, 2.2, 3.3])
    >>> m = memoryview(a)
    >>> m.tolist()
    [1.1, 2.2, 3.3]
    

Changed in version 3.3: `tolist()` now supports all single character native formats in [`struct`](struct.html#module-struct "struct: Interpret bytes as packed binary data.") module syntax as well as multi-dimensional representations.

toreadonly()Â¶
    

Return a readonly version of the memoryview object. The original memoryview object is unchanged.
    
    
    >>> m = memoryview(bytearray(b'abc'))
    >>> mm = m.toreadonly()
    >>> mm.tolist()
    [97, 98, 99]
    >>> mm[0] = 42
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: cannot modify read-only memory
    >>> m[0] = 43
    >>> mm.tolist()
    [43, 98, 99]
    

Added in version 3.8.

release()Â¶
    

Release the underlying buffer exposed by the memoryview object. Many objects take special actions when a view is held on them (for example, a `bytearray` would temporarily forbid resizing); therefore, calling release() is handy to remove these restrictions (and free any dangling resources) as soon as possible.

After this method has been called, any further operation on the view raises a [`ValueError`](exceptions.html#ValueError "ValueError") (except `release()` itself which can be called multiple times):
    
    
    >>> m = memoryview(b'abc')
    >>> m.release()
    >>> m[0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: operation forbidden on released memoryview object
    

The context management protocol can be used for a similar effect, using the `with` statement:
    
    
    >>> with memoryview(b'abc') as m:
    ...     m[0]
    ...
    97
    >>> m[0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: operation forbidden on released memoryview object
    

Added in version 3.2.

cast(_format_[, _shape_])Â¶
    

Cast a memoryview to a new format or shape. _shape_ defaults to `[byte_length//new_itemsize]`, which means that the result view will be one-dimensional. The return value is a new memoryview, but the buffer itself is not copied. Supported casts are 1D -> C-[contiguous](../glossary.html#term-contiguous) and C-contiguous -> 1D.

The destination format is restricted to a single element native format in [`struct`](struct.html#module-struct "struct: Interpret bytes as packed binary data.") syntax. One of the formats must be a byte format (âBâ, âbâ or âcâ). The byte length of the result must be the same as the original length. Note that all byte lengths may depend on the operating system.

Cast 1D/long to 1D/unsigned bytes:
    
    
    >>> import array
    >>> a = array.array('l', [1,2,3])
    >>> x = memoryview(a)
    >>> x.format
    'l'
    >>> x.itemsize
    8
    >>> len(x)
    3
    >>> x.nbytes
    24
    >>> y = x.cast('B')
    >>> y.format
    'B'
    >>> y.itemsize
    1
    >>> len(y)
    24
    >>> y.nbytes
    24
    

Cast 1D/unsigned bytes to 1D/char:
    
    
    >>> b = bytearray(b'zyz')
    >>> x = memoryview(b)
    >>> x[0] = b'a'
    Traceback (most recent call last):
      ...
    TypeError: memoryview: invalid type for format 'B'
    >>> y = x.cast('c')
    >>> y[0] = b'a'
    >>> b
    bytearray(b'ayz')
    

Cast 1D/bytes to 3D/ints to 1D/signed char:
    
    
    >>> import struct
    >>> buf = struct.pack("i"*12, *list(range(12)))
    >>> x = memoryview(buf)
    >>> y = x.cast('i', shape=[2,2,3])
    >>> y.tolist()
    [[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
    >>> y.format
    'i'
    >>> y.itemsize
    4
    >>> len(y)
    2
    >>> y.nbytes
    48
    >>> z = y.cast('b')
    >>> z.format
    'b'
    >>> z.itemsize
    1
    >>> len(z)
    48
    >>> z.nbytes
    48
    

Cast 1D/unsigned long to 2D/unsigned long:
    
    
    >>> buf = struct.pack("L"*6, *list(range(6)))
    >>> x = memoryview(buf)
    >>> y = x.cast('L', shape=[2,3])
    >>> len(y)
    2
    >>> y.nbytes
    48
    >>> y.tolist()
    [[0, 1, 2], [3, 4, 5]]
    

Added in version 3.3.

Changed in version 3.5: The source format is no longer restricted when casting to a byte view.

There are also several readonly attributes available:

objÂ¶
    

The underlying object of the memoryview:
    
    
    >>> b  = bytearray(b'xyz')
    >>> m = memoryview(b)
    >>> m.obj is b
    True
    

Added in version 3.3.

nbytesÂ¶
    

`nbytes == product(shape) * itemsize == len(m.tobytes())`. This is the amount of space in bytes that the array would use in a contiguous representation. It is not necessarily equal to `len(m)`:
    
    
    >>> import array
    >>> a = array.array('i', [1,2,3,4,5])
    >>> m = memoryview(a)
    >>> len(m)
    5
    >>> m.nbytes
    20
    >>> y = m[::2]
    >>> len(y)
    3
    >>> y.nbytes
    12
    >>> len(y.tobytes())
    12
    

Multi-dimensional arrays:
    
    
    >>> import struct
    >>> buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
    >>> x = memoryview(buf)
    >>> y = x.cast('d', shape=[3,4])
    >>> y.tolist()
    [[0.0, 1.5, 3.0, 4.5], [6.0, 7.5, 9.0, 10.5], [12.0, 13.5, 15.0, 16.5]]
    >>> len(y)
    3
    >>> y.nbytes
    96
    

Added in version 3.3.

readonlyÂ¶
    

A bool indicating whether the memory is read only.

formatÂ¶
    

A string containing the format (in [`struct`](struct.html#module-struct "struct: Interpret bytes as packed binary data.") module style) for each element in the view. A memoryview can be created from exporters with arbitrary format strings, but some methods (e.g. `tolist()`) are restricted to native single element formats.

Changed in version 3.3: format `'B'` is now handled according to the struct module syntax. This means that `memoryview(b'abc')[0] == b'abc'[0] == 97`.

itemsizeÂ¶
    

The size in bytes of each element of the memoryview:
    
    
    >>> import array, struct
    >>> m = memoryview(array.array('H', [32000, 32001, 32002]))
    >>> m.itemsize
    2
    >>> m[0]
    32000
    >>> struct.calcsize('H') == m.itemsize
    True
    

ndimÂ¶
    

An integer indicating how many dimensions of a multi-dimensional array the memory represents.

shapeÂ¶
    

A tuple of integers the length of `ndim` giving the shape of the memory as an N-dimensional array.

Changed in version 3.3: An empty tuple instead of `None` when ndim = 0.

stridesÂ¶
    

A tuple of integers the length of `ndim` giving the size in bytes to access each element for each dimension of the array.

Changed in version 3.3: An empty tuple instead of `None` when ndim = 0.

suboffsetsÂ¶
    

Used internally for PIL-style arrays. The value is informational only.

c_contiguousÂ¶
    

A bool indicating whether the memory is C-[contiguous](../glossary.html#term-contiguous).

Added in version 3.3.

f_contiguousÂ¶
    

A bool indicating whether the memory is Fortran [contiguous](../glossary.html#term-contiguous).

Added in version 3.3.

contiguousÂ¶
    

A bool indicating whether the memory is [contiguous](../glossary.html#term-contiguous).

Added in version 3.3.

## Set Types â `set`, `frozenset`Â¶

A _set_ object is an unordered collection of distinct [hashable](../glossary.html#term-hashable) objects. Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference. (For other containers see the built-in `dict`, `list`, and `tuple` classes, and the [`collections`](collections.html#module-collections "collections: Container datatypes") module.)

Like other collections, sets support `x in set`, `len(set)`, and `for x in set`. Being an unordered collection, sets do not record element position or order of insertion. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.

There are currently two built-in set types, `set` and `frozenset`. The `set` type is mutable â the contents can be changed using methods like `add()` and `remove()`. Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set. The `frozenset` type is immutable and [hashable](../glossary.html#term-hashable) â its contents cannot be altered after it is created; it can therefore be used as a dictionary key or as an element of another set.

Non-empty sets (not frozensets) can be created by placing a comma-separated list of elements within braces, for example: `{'jack', 'sjoerd'}`, in addition to the `set` constructor.

The constructors for both classes work the same:

_class _set([_iterable_])Â¶
_class _frozenset([_iterable_])Â¶
    

Return a new set or frozenset object whose elements are taken from _iterable_. The elements of a set must be [hashable](../glossary.html#term-hashable). To represent sets of sets, the inner sets must be `frozenset` objects. If _iterable_ is not specified, a new empty set is returned.

Sets can be created by several means:

  * Use a comma-separated list of elements within braces: `{'jack', 'sjoerd'}`

  * Use a set comprehension: `{c for c in 'abracadabra' if c not in 'abc'}`

  * Use the type constructor: `set()`, `set('foobar')`, `set(['a', 'b', 'foo'])`




Instances of `set` and `frozenset` provide the following operations:

len(s)
    

Return the number of elements in set _s_ (cardinality of _s_).

x in s
    

Test _x_ for membership in _s_.

x not in s
    

Test _x_ for non-membership in _s_.

isdisjoint(_other_)Â¶
    

Return `True` if the set has no elements in common with _other_. Sets are disjoint if and only if their intersection is the empty set.

issubset(_other_)Â¶
set <= other
    

Test whether every element in the set is in _other_.

set < other
    

Test whether the set is a proper subset of _other_ , that is, `set <= other and set != other`.

issuperset(_other_)Â¶
set >= other
    

Test whether every element in _other_ is in the set.

set > other
    

Test whether the set is a proper superset of _other_ , that is, `set >= other and set != other`.

union(_* others_)Â¶
set | other | ...
    

Return a new set with elements from the set and all others.

intersection(_* others_)Â¶
set & other & ...
    

Return a new set with elements common to the set and all others.

difference(_* others_)Â¶
set - other - ...
    

Return a new set with elements in the set that are not in the others.

symmetric_difference(_other_)Â¶
set ^ other
    

Return a new set with elements in either the set or _other_ but not both.

copy()Â¶
    

Return a shallow copy of the set.

Note, the non-operator versions of `union()`, `intersection()`, `difference()`, `symmetric_difference()`, `issubset()`, and `issuperset()` methods will accept any iterable as an argument. In contrast, their operator based counterparts require their arguments to be sets. This precludes error-prone constructions like `set('abc') & 'cbs'` in favor of the more readable `set('abc').intersection('cbs')`.

Both `set` and `frozenset` support set to set comparisons. Two sets are equal if and only if every element of each set is contained in the other (each is a subset of the other). A set is less than another set if and only if the first set is a proper subset of the second set (is a subset, but is not equal). A set is greater than another set if and only if the first set is a proper superset of the second set (is a superset, but is not equal).

Instances of `set` are compared to instances of `frozenset` based on their members. For example, `set('abc') == frozenset('abc')` returns `True` and so does `set('abc') in set([frozenset('abc')])`.

The subset and equality comparisons do not generalize to a total ordering function. For example, any two nonempty disjoint sets are not equal and are not subsets of each other, so _all_ of the following return `False`: `a<b`, `a==b`, or `a>b`.

Since sets only define partial ordering (subset relationships), the output of the `list.sort()` method is undefined for lists of sets.

Set elements, like dictionary keys, must be [hashable](../glossary.html#term-hashable).

Binary operations that mix `set` instances with `frozenset` return the type of the first operand. For example: `frozenset('ab') | set('bc')` returns an instance of `frozenset`.

The following table lists operations available for `set` that do not apply to immutable instances of `frozenset`:

update(_* others_)Â¶
set |= other | ...
    

Update the set, adding elements from all others.

intersection_update(_* others_)Â¶
set &= other & ...
    

Update the set, keeping only elements found in it and all others.

difference_update(_* others_)Â¶
set -= other | ...
    

Update the set, removing elements found in others.

symmetric_difference_update(_other_)Â¶
set ^= other
    

Update the set, keeping only elements found in either set, but not in both.

add(_elem_)Â¶
    

Add element _elem_ to the set.

remove(_elem_)Â¶
    

Remove element _elem_ from the set. Raises [`KeyError`](exceptions.html#KeyError "KeyError") if _elem_ is not contained in the set.

discard(_elem_)Â¶
    

Remove element _elem_ from the set if it is present.

pop()Â¶
    

Remove and return an arbitrary element from the set. Raises [`KeyError`](exceptions.html#KeyError "KeyError") if the set is empty.

clear()Â¶
    

Remove all elements from the set.

Note, the non-operator versions of the `update()`, `intersection_update()`, `difference_update()`, and `symmetric_difference_update()` methods will accept any iterable as an argument.

Note, the _elem_ argument to the [`__contains__()`](../reference/datamodel.html#object.__contains__ "object.__contains__"), `remove()`, and `discard()` methods may be a set. To support searching for an equivalent frozenset, a temporary one is created from _elem_.

## Mapping Types â `dict`Â¶

A [mapping](../glossary.html#term-mapping) object maps [hashable](../glossary.html#term-hashable) values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the _dictionary_. (For other containers see the built-in `list`, `set`, and `tuple` classes, and the [`collections`](collections.html#module-collections "collections: Container datatypes") module.)

A dictionaryâs keys are _almost_ arbitrary values. Values that are not [hashable](../glossary.html#term-hashable), that is, values containing lists, dictionaries or other mutable types (that are compared by value rather than by object identity) may not be used as keys. Values that compare equal (such as `1`, `1.0`, and `True`) can be used interchangeably to index the same dictionary entry.

_class _dict(_** kwargs_)Â¶
_class _dict(_mapping_ , _** kwargs_)
_class _dict(_iterable_ , _** kwargs_)
    

Return a new dictionary initialized from an optional positional argument and a possibly empty set of keyword arguments.

Dictionaries can be created by several means:

  * Use a comma-separated list of `key: value` pairs within braces: `{'jack': 4098, 'sjoerd': 4127}` or `{4098: 'jack', 4127: 'sjoerd'}`

  * Use a dict comprehension: `{}`, `{x: x ** 2 for x in range(10)}`

  * Use the type constructor: `dict()`, `dict([('foo', 100), ('bar', 200)])`, `dict(foo=100, bar=200)`




If no positional argument is given, an empty dictionary is created. If a positional argument is given and it defines a `keys()` method, a dictionary is created by calling [`__getitem__()`](../reference/datamodel.html#object.__getitem__ "object.__getitem__") on the argument with each returned key from the method. Otherwise, the positional argument must be an [iterable](../glossary.html#term-iterable) object. Each item in the iterable must itself be an iterable with exactly two elements. The first element of each item becomes a key in the new dictionary, and the second element the corresponding value. If a key occurs more than once, the last value for that key becomes the corresponding value in the new dictionary.

If keyword arguments are given, the keyword arguments and their values are added to the dictionary created from the positional argument. If a key being added is already present, the value from the keyword argument replaces the value from the positional argument.

To illustrate, the following examples all return a dictionary equal to `{"one": 1, "two": 2, "three": 3}`:
    
    
    >>> a = dict(one=1, two=2, three=3)
    >>> b = {'one': 1, 'two': 2, 'three': 3}
    >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
    >>> e = dict({'three': 3, 'one': 1, 'two': 2})
    >>> f = dict({'one': 1, 'three': 3}, two=2)
    >>> a == b == c == d == e == f
    True
    

Providing keyword arguments as in the first example only works for keys that are valid Python identifiers. Otherwise, any valid keys can be used.

These are the operations that dictionaries support (and therefore, custom mapping types should support too):

list(d)
    

Return a list of all the keys used in the dictionary _d_.

len(d)
    

Return the number of items in the dictionary _d_.

d[key]
    

Return the item of _d_ with key _key_. Raises a [`KeyError`](exceptions.html#KeyError "KeyError") if _key_ is not in the map.

If a subclass of dict defines a method `__missing__()` and _key_ is not present, the `d[key]` operation calls that method with the key _key_ as argument. The `d[key]` operation then returns or raises whatever is returned or raised by the `__missing__(key)` call. No other operations or methods invoke `__missing__()`. If `__missing__()` is not defined, [`KeyError`](exceptions.html#KeyError "KeyError") is raised. `__missing__()` must be a method; it cannot be an instance variable:
    
    
    >>> class Counter(dict):
    ...     def __missing__(self, key):
    ...         return 0
    ...
    >>> c = Counter()
    >>> c['red']
    0
    >>> c['red'] += 1
    >>> c['red']
    1
    

The example above shows part of the implementation of [`collections.Counter`](collections.html#collections.Counter "collections.Counter"). A different `__missing__` method is used by [`collections.defaultdict`](collections.html#collections.defaultdict "collections.defaultdict").

d[key] = value
    

Set `d[key]` to _value_.

del d[key]
    

Remove `d[key]` from _d_. Raises a [`KeyError`](exceptions.html#KeyError "KeyError") if _key_ is not in the map.

key in d
    

Return `True` if _d_ has a key _key_ , else `False`.

key not in d
    

Equivalent to `not key in d`.

iter(d)
    

Return an iterator over the keys of the dictionary. This is a shortcut for `iter(d.keys())`.

clear()Â¶
    

Remove all items from the dictionary.

copy()Â¶
    

Return a shallow copy of the dictionary.

_classmethod _fromkeys(_iterable_ , _value =None_, _/_)Â¶
    

Create a new dictionary with keys from _iterable_ and values set to _value_.

`fromkeys()` is a class method that returns a new dictionary. _value_ defaults to `None`. All of the values refer to just a single instance, so it generally doesnât make sense for _value_ to be a mutable object such as an empty list. To get distinct values, use a [dict comprehension](../reference/expressions.html#dict) instead.

get(_key_ , _default =None_, _/_)Â¶
    

Return the value for _key_ if _key_ is in the dictionary, else _default_. If _default_ is not given, it defaults to `None`, so that this method never raises a [`KeyError`](exceptions.html#KeyError "KeyError").

items()Â¶
    

Return a new view of the dictionaryâs items (`(key, value)` pairs). See the documentation of view objects.

keys()Â¶
    

Return a new view of the dictionaryâs keys. See the documentation of view objects.

pop(_key_[, _default_])Â¶
    

If _key_ is in the dictionary, remove it and return its value, else return _default_. If _default_ is not given and _key_ is not in the dictionary, a [`KeyError`](exceptions.html#KeyError "KeyError") is raised.

popitem()Â¶
    

Remove and return a `(key, value)` pair from the dictionary. Pairs are returned in LIFO order.

`popitem()` is useful to destructively iterate over a dictionary, as often used in set algorithms. If the dictionary is empty, calling `popitem()` raises a [`KeyError`](exceptions.html#KeyError "KeyError").

Changed in version 3.7: LIFO order is now guaranteed. In prior versions, `popitem()` would return an arbitrary key/value pair.

reversed(d)
    

Return a reverse iterator over the keys of the dictionary. This is a shortcut for `reversed(d.keys())`.

Added in version 3.8.

setdefault(_key_ , _default =None_, _/_)Â¶
    

If _key_ is in the dictionary, return its value. If not, insert _key_ with a value of _default_ and return _default_. _default_ defaults to `None`.

update([_other_])Â¶
    

Update the dictionary with the key/value pairs from _other_ , overwriting existing keys. Return `None`.

`update()` accepts either another object with a `keys()` method (in which case [`__getitem__()`](../reference/datamodel.html#object.__getitem__ "object.__getitem__") is called with every key returned from the method) or an iterable of key/value pairs (as tuples or other iterables of length two). If keyword arguments are specified, the dictionary is then updated with those key/value pairs: `d.update(red=1, blue=2)`.

values()Â¶
    

Return a new view of the dictionaryâs values. See the documentation of view objects.

An equality comparison between one `dict.values()` view and another will always return `False`. This also applies when comparing `dict.values()` to itself:
    
    
    >>> d = {'a': 1}
    >>> d.values() == d.values()
    False
    

d | other
    

Create a new dictionary with the merged keys and values of _d_ and _other_ , which must both be dictionaries. The values of _other_ take priority when _d_ and _other_ share keys.

Added in version 3.9.

d |= other
    

Update the dictionary _d_ with keys and values from _other_ , which may be either a [mapping](../glossary.html#term-mapping) or an [iterable](../glossary.html#term-iterable) of key/value pairs. The values of _other_ take priority when _d_ and _other_ share keys.

Added in version 3.9.

Dictionaries compare equal if and only if they have the same `(key, value)` pairs (regardless of ordering). Order comparisons (â<â, â<=â, â>=â, â>â) raise [`TypeError`](exceptions.html#TypeError "TypeError").

Dictionaries preserve insertion order. Note that updating a key does not affect the order. Keys added after deletion are inserted at the end.
    
    
    >>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
    >>> d
    {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    >>> list(d)
    ['one', 'two', 'three', 'four']
    >>> list(d.values())
    [1, 2, 3, 4]
    >>> d["one"] = 42
    >>> d
    {'one': 42, 'two': 2, 'three': 3, 'four': 4}
    >>> del d["two"]
    >>> d["two"] = None
    >>> d
    {'one': 42, 'three': 3, 'four': 4, 'two': None}
    

Changed in version 3.7: Dictionary order is guaranteed to be insertion order. This behavior was an implementation detail of CPython from 3.6.

Dictionaries and dictionary views are reversible.
    
    
    >>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
    >>> d
    {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    >>> list(reversed(d))
    ['four', 'three', 'two', 'one']
    >>> list(reversed(d.values()))
    [4, 3, 2, 1]
    >>> list(reversed(d.items()))
    [('four', 4), ('three', 3), ('two', 2), ('one', 1)]
    

Changed in version 3.8: Dictionaries are now reversible.

See also

[`types.MappingProxyType`](types.html#types.MappingProxyType "types.MappingProxyType") can be used to create a read-only view of a `dict`.

### Dictionary view objectsÂ¶

The objects returned by `dict.keys()`, `dict.values()` and `dict.items()` are _view objects_. They provide a dynamic view on the dictionaryâs entries, which means that when the dictionary changes, the view reflects these changes.

Dictionary views can be iterated over to yield their respective data, and support membership tests:

len(dictview)
    

Return the number of entries in the dictionary.

iter(dictview)
    

Return an iterator over the keys, values or items (represented as tuples of `(key, value)`) in the dictionary.

Keys and values are iterated over in insertion order. This allows the creation of `(value, key)` pairs using [`zip()`](functions.html#zip "zip"): `pairs = zip(d.values(), d.keys())`. Another way to create the same list is `pairs = [(v, k) for (k, v) in d.items()]`.

Iterating views while adding or deleting entries in the dictionary may raise a [`RuntimeError`](exceptions.html#RuntimeError "RuntimeError") or fail to iterate over all entries.

Changed in version 3.7: Dictionary order is guaranteed to be insertion order.

x in dictview
    

Return `True` if _x_ is in the underlying dictionaryâs keys, values or items (in the latter case, _x_ should be a `(key, value)` tuple).

reversed(dictview)
    

Return a reverse iterator over the keys, values or items of the dictionary. The view will be iterated in reverse order of the insertion.

Changed in version 3.8: Dictionary views are now reversible.

dictview.mapping
    

Return a [`types.MappingProxyType`](types.html#types.MappingProxyType "types.MappingProxyType") that wraps the original dictionary to which the view refers.

Added in version 3.10.

Keys views are set-like since their entries are unique and [hashable](../glossary.html#term-hashable). Items views also have set-like operations since the (key, value) pairs are unique and the keys are hashable. If all values in an items view are hashable as well, then the items view can interoperate with other sets. (Values views are not treated as set-like since the entries are generally not unique.) For set-like views, all of the operations defined for the abstract base class [`collections.abc.Set`](collections.abc.html#collections.abc.Set "collections.abc.Set") are available (for example, `==`, `<`, or `^`). While using set operators, set-like views accept any iterable as the other operand, unlike sets which only accept sets as the input.

An example of dictionary view usage:
    
    
    >>> dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
    >>> keys = dishes.keys()
    >>> values = dishes.values()
    
    >>> # iteration
    >>> n = 0
    >>> for val in values:
    ...     n += val
    ...
    >>> print(n)
    504
    
    >>> # keys and values are iterated over in the same order (insertion order)
    >>> list(keys)
    ['eggs', 'sausage', 'bacon', 'spam']
    >>> list(values)
    [2, 1, 1, 500]
    
    >>> # view objects are dynamic and reflect dict changes
    >>> del dishes['eggs']
    >>> del dishes['sausage']
    >>> list(keys)
    ['bacon', 'spam']
    
    >>> # set operations
    >>> keys & {'eggs', 'bacon', 'salad'}
    {'bacon'}
    >>> keys ^ {'sausage', 'juice'} == {'juice', 'sausage', 'bacon', 'spam'}
    True
    >>> keys | ['juice', 'juice', 'juice'] == {'bacon', 'spam', 'juice'}
    True
    
    >>> # get back a read-only proxy for the original dictionary
    >>> values.mapping
    mappingproxy({'bacon': 1, 'spam': 500})
    >>> values.mapping['spam']
    500
    

## Context Manager TypesÂ¶

Pythonâs [`with`](../reference/compound_stmts.html#with) statement supports the concept of a runtime context defined by a context manager. This is implemented using a pair of methods that allow user-defined classes to define a runtime context that is entered before the statement body is executed and exited when the statement ends:

contextmanager.__enter__()Â¶
    

Enter the runtime context and return either this object or another object related to the runtime context. The value returned by this method is bound to the identifier in the `as` clause of [`with`](../reference/compound_stmts.html#with) statements using this context manager.

An example of a context manager that returns itself is a [file object](../glossary.html#term-file-object). File objects return themselves from __enter__() to allow [`open()`](functions.html#open "open") to be used as the context expression in a [`with`](../reference/compound_stmts.html#with) statement.

An example of a context manager that returns a related object is the one returned by [`decimal.localcontext()`](decimal.html#decimal.localcontext "decimal.localcontext"). These managers set the active decimal context to a copy of the original decimal context and then return the copy. This allows changes to be made to the current decimal context in the body of the [`with`](../reference/compound_stmts.html#with) statement without affecting code outside the `with` statement.

contextmanager.__exit__(_exc_type_ , _exc_val_ , _exc_tb_)Â¶
    

Exit the runtime context and return a Boolean flag indicating if any exception that occurred should be suppressed. If an exception occurred while executing the body of the [`with`](../reference/compound_stmts.html#with) statement, the arguments contain the exception type, value and traceback information. Otherwise, all three arguments are `None`.

Returning a true value from this method will cause the [`with`](../reference/compound_stmts.html#with) statement to suppress the exception and continue execution with the statement immediately following the `with` statement. Otherwise the exception continues propagating after this method has finished executing. Exceptions that occur during execution of this method will replace any exception that occurred in the body of the `with` statement.

The exception passed in should never be reraised explicitly - instead, this method should return a false value to indicate that the method completed successfully and does not want to suppress the raised exception. This allows context management code to easily detect whether or not an [`__exit__()`](../reference/datamodel.html#object.__exit__ "object.__exit__") method has actually failed.

Python defines several context managers to support easy thread synchronisation, prompt closure of files or other objects, and simpler manipulation of the active decimal arithmetic context. The specific types are not treated specially beyond their implementation of the context management protocol. See the [`contextlib`](contextlib.html#module-contextlib "contextlib: Utilities for with-statement contexts.") module for some examples.

Pythonâs [generator](../glossary.html#term-generator)s and the [`contextlib.contextmanager`](contextlib.html#contextlib.contextmanager "contextlib.contextmanager") decorator provide a convenient way to implement these protocols. If a generator function is decorated with the [`contextlib.contextmanager`](contextlib.html#contextlib.contextmanager "contextlib.contextmanager") decorator, it will return a context manager implementing the necessary `__enter__()` and `__exit__()` methods, rather than the iterator produced by an undecorated generator function.

Note that there is no specific slot for any of these methods in the type structure for Python objects in the Python/C API. Extension types wanting to define these methods must provide them as a normal Python accessible method. Compared to the overhead of setting up the runtime context, the overhead of a single class dictionary lookup is negligible.

## Type Annotation Types â Generic Alias, UnionÂ¶

The core built-in types for [type annotations](../glossary.html#term-annotation) are Generic Alias and Union.

### Generic Alias TypeÂ¶

`GenericAlias` objects are generally created by [subscripting](../reference/expressions.html#subscriptions) a class. They are most often used with [container classes](../reference/datamodel.html#sequence-types), such as `list` or `dict`. For example, `list[int]` is a `GenericAlias` object created by subscripting the `list` class with the argument [`int`](functions.html#int "int"). `GenericAlias` objects are intended primarily for use with [type annotations](../glossary.html#term-annotation).

Note

It is generally only possible to subscript a class if the class implements the special method [`__class_getitem__()`](../reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__").

A `GenericAlias` object acts as a proxy for a [generic type](../glossary.html#term-generic-type), implementing _parameterized generics_.

For a container class, the argument(s) supplied to a [subscription](../reference/expressions.html#subscriptions) of the class may indicate the type(s) of the elements an object contains. For example, `set[bytes]` can be used in type annotations to signify a `set` in which all the elements are of type `bytes`.

For a class which defines [`__class_getitem__()`](../reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__") but is not a container, the argument(s) supplied to a subscription of the class will often indicate the return type(s) of one or more methods defined on an object. For example, [`regular expressions`](re.html#module-re "re: Regular expression operations.") can be used on both the `str` data type and the `bytes` data type:

  * If `x = re.search('foo', 'foo')`, `x` will be a [re.Match](re.html#match-objects) object where the return values of `x.group(0)` and `x[0]` will both be of type `str`. We can represent this kind of object in type annotations with the `GenericAlias` `re.Match[str]`.

  * If `y = re.search(b'bar', b'bar')`, (note the `b` for `bytes`), `y` will also be an instance of `re.Match`, but the return values of `y.group(0)` and `y[0]` will both be of type `bytes`. In type annotations, we would represent this variety of [re.Match](re.html#match-objects) objects with `re.Match[bytes]`.




`GenericAlias` objects are instances of the class [`types.GenericAlias`](types.html#types.GenericAlias "types.GenericAlias"), which can also be used to create `GenericAlias` objects directly.

T[X, Y, ...]
    

Creates a `GenericAlias` representing a type `T` parameterized by types _X_ , _Y_ , and more depending on the `T` used. For example, a function expecting a `list` containing [`float`](functions.html#float "float") elements:
    
    
    def average(values: list[float]) -> float:
        return sum(values) / len(values)
    

Another example for [mapping](../glossary.html#term-mapping) objects, using a `dict`, which is a generic type expecting two type parameters representing the key type and the value type. In this example, the function expects a `dict` with keys of type `str` and values of type [`int`](functions.html#int "int"):
    
    
    def send_post_request(url: str, body: dict[str, int]) -> None:
        ...
    

The builtin functions [`isinstance()`](functions.html#isinstance "isinstance") and [`issubclass()`](functions.html#issubclass "issubclass") do not accept `GenericAlias` types for their second argument:
    
    
    >>> isinstance([1, 2], list[str])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: isinstance() argument 2 cannot be a parameterized generic
    

The Python runtime does not enforce [type annotations](../glossary.html#term-annotation). This extends to generic types and their type parameters. When creating a container object from a `GenericAlias`, the elements in the container are not checked against their type. For example, the following code is discouraged, but will run without errors:
    
    
    >>> t = list[str]
    >>> t([1, 2, 3])
    [1, 2, 3]
    

Furthermore, parameterized generics erase type parameters during object creation:
    
    
    >>> t = list[str]
    >>> type(t)
    <class 'types.GenericAlias'>
    
    >>> l = t()
    >>> type(l)
    <class 'list'>
    

Calling [`repr()`](functions.html#repr "repr") or `str()` on a generic shows the parameterized type:
    
    
    >>> repr(list[int])
    'list[int]'
    
    >>> str(list[int])
    'list[int]'
    

The [`__getitem__()`](../reference/datamodel.html#object.__getitem__ "object.__getitem__") method of generic containers will raise an exception to disallow mistakes like `dict[str][str]`:
    
    
    >>> dict[str][str]
    Traceback (most recent call last):
      ...
    TypeError: dict[str] is not a generic class
    

However, such expressions are valid when [type variables](typing.html#generics) are used. The index must have as many elements as there are type variable items in the `GenericAlias` objectâs `__args__`.
    
    
    >>> from typing import TypeVar
    >>> Y = TypeVar('Y')
    >>> dict[str, Y][int]
    dict[str, int]
    

#### Standard Generic ClassesÂ¶

The following standard library classes support parameterized generics. This list is non-exhaustive.

  * `tuple`

  * `list`

  * `dict`

  * `set`

  * `frozenset`

  * [`type`](functions.html#type "type")

  * [`asyncio.Future`](asyncio-future.html#asyncio.Future "asyncio.Future")

  * [`asyncio.Task`](asyncio-task.html#asyncio.Task "asyncio.Task")

  * [`collections.deque`](collections.html#collections.deque "collections.deque")

  * [`collections.defaultdict`](collections.html#collections.defaultdict "collections.defaultdict")

  * [`collections.OrderedDict`](collections.html#collections.OrderedDict "collections.OrderedDict")

  * [`collections.Counter`](collections.html#collections.Counter "collections.Counter")

  * [`collections.ChainMap`](collections.html#collections.ChainMap "collections.ChainMap")

  * [`collections.abc.Awaitable`](collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable")

  * [`collections.abc.Coroutine`](collections.abc.html#collections.abc.Coroutine "collections.abc.Coroutine")

  * [`collections.abc.AsyncIterable`](collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable")

  * [`collections.abc.AsyncIterator`](collections.abc.html#collections.abc.AsyncIterator "collections.abc.AsyncIterator")

  * [`collections.abc.AsyncGenerator`](collections.abc.html#collections.abc.AsyncGenerator "collections.abc.AsyncGenerator")

  * [`collections.abc.Iterable`](collections.abc.html#collections.abc.Iterable "collections.abc.Iterable")

  * [`collections.abc.Iterator`](collections.abc.html#collections.abc.Iterator "collections.abc.Iterator")

  * [`collections.abc.Generator`](collections.abc.html#collections.abc.Generator "collections.abc.Generator")

  * [`collections.abc.Reversible`](collections.abc.html#collections.abc.Reversible "collections.abc.Reversible")

  * [`collections.abc.Container`](collections.abc.html#collections.abc.Container "collections.abc.Container")

  * [`collections.abc.Collection`](collections.abc.html#collections.abc.Collection "collections.abc.Collection")

  * [`collections.abc.Callable`](collections.abc.html#collections.abc.Callable "collections.abc.Callable")

  * [`collections.abc.Set`](collections.abc.html#collections.abc.Set "collections.abc.Set")

  * [`collections.abc.MutableSet`](collections.abc.html#collections.abc.MutableSet "collections.abc.MutableSet")

  * [`collections.abc.Mapping`](collections.abc.html#collections.abc.Mapping "collections.abc.Mapping")

  * [`collections.abc.MutableMapping`](collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping")

  * [`collections.abc.Sequence`](collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")

  * [`collections.abc.MutableSequence`](collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence")

  * [`collections.abc.ByteString`](collections.abc.html#collections.abc.ByteString "collections.abc.ByteString")

  * [`collections.abc.MappingView`](collections.abc.html#collections.abc.MappingView "collections.abc.MappingView")

  * [`collections.abc.KeysView`](collections.abc.html#collections.abc.KeysView "collections.abc.KeysView")

  * [`collections.abc.ItemsView`](collections.abc.html#collections.abc.ItemsView "collections.abc.ItemsView")

  * [`collections.abc.ValuesView`](collections.abc.html#collections.abc.ValuesView "collections.abc.ValuesView")

  * [`contextlib.AbstractContextManager`](contextlib.html#contextlib.AbstractContextManager "contextlib.AbstractContextManager")

  * [`contextlib.AbstractAsyncContextManager`](contextlib.html#contextlib.AbstractAsyncContextManager "contextlib.AbstractAsyncContextManager")

  * [`dataclasses.Field`](dataclasses.html#dataclasses.Field "dataclasses.Field")

  * [`functools.cached_property`](functools.html#functools.cached_property "functools.cached_property")

  * [`functools.partialmethod`](functools.html#functools.partialmethod "functools.partialmethod")

  * [`os.PathLike`](os.html#os.PathLike "os.PathLike")

  * [`queue.LifoQueue`](queue.html#queue.LifoQueue "queue.LifoQueue")

  * [`queue.Queue`](queue.html#queue.Queue "queue.Queue")

  * [`queue.PriorityQueue`](queue.html#queue.PriorityQueue "queue.PriorityQueue")

  * [`queue.SimpleQueue`](queue.html#queue.SimpleQueue "queue.SimpleQueue")

  * [re.Pattern](re.html#re-objects)

  * [re.Match](re.html#match-objects)

  * [`shelve.BsdDbShelf`](shelve.html#shelve.BsdDbShelf "shelve.BsdDbShelf")

  * [`shelve.DbfilenameShelf`](shelve.html#shelve.DbfilenameShelf "shelve.DbfilenameShelf")

  * [`shelve.Shelf`](shelve.html#shelve.Shelf "shelve.Shelf")

  * [`types.MappingProxyType`](types.html#types.MappingProxyType "types.MappingProxyType")

  * [`weakref.WeakKeyDictionary`](weakref.html#weakref.WeakKeyDictionary "weakref.WeakKeyDictionary")

  * [`weakref.WeakMethod`](weakref.html#weakref.WeakMethod "weakref.WeakMethod")

  * [`weakref.WeakSet`](weakref.html#weakref.WeakSet "weakref.WeakSet")

  * [`weakref.WeakValueDictionary`](weakref.html#weakref.WeakValueDictionary "weakref.WeakValueDictionary")




#### Special Attributes of `GenericAlias` objectsÂ¶

All parameterized generics implement special read-only attributes.

genericalias.__origin__Â¶
    

This attribute points at the non-parameterized generic class:
    
    
    >>> list[int].__origin__
    <class 'list'>
    

genericalias.__args__Â¶
    

This attribute is a `tuple` (possibly of length 1) of generic types passed to the original [`__class_getitem__()`](../reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__") of the generic class:
    
    
    >>> dict[str, list[int]].__args__
    (<class 'str'>, list[int])
    

genericalias.__parameters__Â¶
    

This attribute is a lazily computed tuple (possibly empty) of unique type variables found in `__args__`:
    
    
    >>> from typing import TypeVar
    
    >>> T = TypeVar('T')
    >>> list[T].__parameters__
    (~T,)
    

Note

A `GenericAlias` object with [`typing.ParamSpec`](typing.html#typing.ParamSpec "typing.ParamSpec") parameters may not have correct `__parameters__` after substitution because [`typing.ParamSpec`](typing.html#typing.ParamSpec "typing.ParamSpec") is intended primarily for static type checking.

genericalias.__unpacked__Â¶
    

A boolean that is true if the alias has been unpacked using the `*` operator (see [`TypeVarTuple`](typing.html#typing.TypeVarTuple "typing.TypeVarTuple")).

Added in version 3.11.

See also

[**PEP 484**](https://peps.python.org/pep-0484/) \- Type Hints
    

Introducing Pythonâs framework for type annotations.

[**PEP 585**](https://peps.python.org/pep-0585/) \- Type Hinting Generics In Standard Collections
    

Introducing the ability to natively parameterize standard-library classes, provided they implement the special class method [`__class_getitem__()`](../reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__").

[Generics](typing.html#generics), [user-defined generics](typing.html#user-defined-generics) and [`typing.Generic`](typing.html#typing.Generic "typing.Generic")
    

Documentation on how to implement generic classes that can be parameterized at runtime and understood by static type-checkers.

Added in version 3.9.

### Union TypeÂ¶

A union object holds the value of the `|` (bitwise or) operation on multiple type objects. These types are intended primarily for [type annotations](../glossary.html#term-annotation). The union type expression enables cleaner type hinting syntax compared to [`typing.Union`](typing.html#typing.Union "typing.Union").

X | Y | ...
    

Defines a union object which holds types _X_ , _Y_ , and so forth. `X | Y` means either X or Y. It is equivalent to `typing.Union[X, Y]`. For example, the following function expects an argument of type [`int`](functions.html#int "int") or [`float`](functions.html#float "float"):
    
    
    def square(number: int | float) -> int | float:
        return number ** 2
    

Note

The `|` operand cannot be used at runtime to define unions where one or more members is a forward reference. For example, `int | "Foo"`, where `"Foo"` is a reference to a class not yet defined, will fail at runtime. For unions which include forward references, present the whole expression as a string, e.g. `"int | Foo"`.

union_object == other
    

Union objects can be tested for equality with other union objects. Details:

  * Unions of unions are flattened:
    
        (int | str) | float == int | str | float
    

  * Redundant types are removed:
    
        int | str | int == int | str
    

  * When comparing unions, the order is ignored:
    
        int | str == str | int
    

  * It is compatible with [`typing.Union`](typing.html#typing.Union "typing.Union"):
    
        int | str == typing.Union[int, str]
    

  * Optional types can be spelled as a union with `None`:
    
        str | None == typing.Optional[str]
    




isinstance(obj, union_object)
    

issubclass(obj, union_object)
    

Calls to [`isinstance()`](functions.html#isinstance "isinstance") and [`issubclass()`](functions.html#issubclass "issubclass") are also supported with a union object:
    
    
    >>> isinstance("", int | str)
    True
    

However, parameterized generics in union objects cannot be checked:
    
    
    >>> isinstance(1, int | list[int])  # short-circuit evaluation
    True
    >>> isinstance([1], int | list[int])
    Traceback (most recent call last):
      ...
    TypeError: isinstance() argument 2 cannot be a parameterized generic
    

The user-exposed type for the union object can be accessed from [`types.UnionType`](types.html#types.UnionType "types.UnionType") and used for [`isinstance()`](functions.html#isinstance "isinstance") checks. An object cannot be instantiated from the type:
    
    
    >>> import types
    >>> isinstance(int | str, types.UnionType)
    True
    >>> types.UnionType()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: cannot create 'types.UnionType' instances
    

Note

The `__or__()` method for type objects was added to support the syntax `X | Y`. If a metaclass implements `__or__()`, the Union may override it:
    
    
    >>> class M(type):
    ...     def __or__(self, other):
    ...         return "Hello"
    ...
    >>> class C(metaclass=M):
    ...     pass
    ...
    >>> C | int
    'Hello'
    >>> int | C
    int | C
    

See also

[**PEP 604**](https://peps.python.org/pep-0604/) â PEP proposing the `X | Y` syntax and the Union type.

Added in version 3.10.

## Other Built-in TypesÂ¶

The interpreter supports several other kinds of objects. Most of these support only one or two operations.

### ModulesÂ¶

The only special operation on a module is attribute access: `m.name`, where _m_ is a module and _name_ accesses a name defined in _m_ âs symbol table. Module attributes can be assigned to. (Note that the [`import`](../reference/simple_stmts.html#import) statement is not, strictly speaking, an operation on a module object; `import foo` does not require a module object named _foo_ to exist, rather it requires an (external) _definition_ for a module named _foo_ somewhere.)

A special attribute of every module is [`__dict__`](../reference/datamodel.html#object.__dict__ "object.__dict__"). This is the dictionary containing the moduleâs symbol table. Modifying this dictionary will actually change the moduleâs symbol table, but direct assignment to the [`__dict__`](../reference/datamodel.html#object.__dict__ "object.__dict__") attribute is not possible (you can write `m.__dict__['a'] = 1`, which defines `m.a` to be `1`, but you canât write `m.__dict__ = {}`). Modifying [`__dict__`](../reference/datamodel.html#object.__dict__ "object.__dict__") directly is not recommended.

Modules built into the interpreter are written like this: `<module 'sys' (built-in)>`. If loaded from a file, they are written as `<module 'os' from '/usr/local/lib/pythonX.Y/os.pyc'>`.

### Classes and Class InstancesÂ¶

See [Objects, values and types](../reference/datamodel.html#objects) and [Class definitions](../reference/compound_stmts.html#class) for these.

### FunctionsÂ¶

Function objects are created by function definitions. The only operation on a function object is to call it: `func(argument-list)`.

There are really two flavors of function objects: built-in functions and user-defined functions. Both support the same operation (to call the function), but the implementation is different, hence the different object types.

See [Function definitions](../reference/compound_stmts.html#function) for more information.

### MethodsÂ¶

Methods are functions that are called using the attribute notation. There are two flavors: [built-in methods](../reference/datamodel.html#builtin-methods) (such as `append()` on lists) and [class instance method](../reference/datamodel.html#instance-methods). Built-in methods are described with the types that support them.

If you access a method (a function defined in a class namespace) through an instance, you get a special object: a _bound method_ (also called [instance method](../reference/datamodel.html#instance-methods)) object. When called, it will add the `self` argument to the argument list. Bound methods have two special read-only attributes: [`m.__self__`](../reference/datamodel.html#method.__self__ "method.__self__") is the object on which the method operates, and [`m.__func__`](../reference/datamodel.html#method.__func__ "method.__func__") is the function implementing the method. Calling `m(arg-1, arg-2, ..., arg-n)` is completely equivalent to calling `m.__func__(m.__self__, arg-1, arg-2, ..., arg-n)`.

Like [function objects](../reference/datamodel.html#user-defined-funcs), bound method objects support getting arbitrary attributes. However, since method attributes are actually stored on the underlying function object ([`method.__func__`](../reference/datamodel.html#method.__func__ "method.__func__")), setting method attributes on bound methods is disallowed. Attempting to set an attribute on a method results in an [`AttributeError`](exceptions.html#AttributeError "AttributeError") being raised. In order to set a method attribute, you need to explicitly set it on the underlying function object:
    
    
    >>> class C:
    ...     def method(self):
    ...         pass
    ...
    >>> c = C()
    >>> c.method.whoami = 'my name is method'  # can't set on the method
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'method' object has no attribute 'whoami'
    >>> c.method.__func__.whoami = 'my name is method'
    >>> c.method.whoami
    'my name is method'
    

See [Instance methods](../reference/datamodel.html#instance-methods) for more information.

### Code ObjectsÂ¶

Code objects are used by the implementation to represent âpseudo-compiledâ executable Python code such as a function body. They differ from function objects because they donât contain a reference to their global execution environment. Code objects are returned by the built-in [`compile()`](functions.html#compile "compile") function and can be extracted from function objects through their [`__code__`](../reference/datamodel.html#function.__code__ "function.__code__") attribute. See also the [`code`](code.html#module-code "code: Facilities to implement read-eval-print loops.") module.

Accessing [`__code__`](../reference/datamodel.html#function.__code__ "function.__code__") raises an [auditing event](sys.html#auditing) `object.__getattr__` with arguments `obj` and `"__code__"`.

A code object can be executed or evaluated by passing it (instead of a source string) to the [`exec()`](functions.html#exec "exec") or [`eval()`](functions.html#eval "eval") built-in functions.

See [The standard type hierarchy](../reference/datamodel.html#types) for more information.

### Type ObjectsÂ¶

Type objects represent the various object types. An objectâs type is accessed by the built-in function [`type()`](functions.html#type "type"). There are no special operations on types. The standard module [`types`](types.html#module-types "types: Names for built-in types.") defines names for all standard built-in types.

Types are written like this: `<class 'int'>`.

### The Null ObjectÂ¶

This object is returned by functions that donât explicitly return a value. It supports no special operations. There is exactly one null object, named `None` (a built-in name). `type(None)()` produces the same singleton.

It is written as `None`.

### The Ellipsis ObjectÂ¶

This object is commonly used by slicing (see [Slicings](../reference/expressions.html#slicings)). It supports no special operations. There is exactly one ellipsis object, named [`Ellipsis`](constants.html#Ellipsis "Ellipsis") (a built-in name). `type(Ellipsis)()` produces the [`Ellipsis`](constants.html#Ellipsis "Ellipsis") singleton.

It is written as `Ellipsis` or `...`.

### The NotImplemented ObjectÂ¶

This object is returned from comparisons and binary operations when they are asked to operate on types they donât support. See [Comparisons](../reference/expressions.html#comparisons) for more information. There is exactly one [`NotImplemented`](constants.html#NotImplemented "NotImplemented") object. `type(NotImplemented)()` produces the singleton instance.

It is written as `NotImplemented`.

### Internal ObjectsÂ¶

See [The standard type hierarchy](../reference/datamodel.html#types) for this information. It describes [stack frame objects](../reference/datamodel.html#frame-objects), [traceback objects](../reference/datamodel.html#traceback-objects), and slice objects.

## Special AttributesÂ¶

The implementation adds a few special read-only attributes to several object types, where they are relevant. Some of these are not reported by the [`dir()`](functions.html#dir "dir") built-in function.

definition.__name__Â¶
    

The name of the class, function, method, descriptor, or generator instance.

definition.__qualname__Â¶
    

The [qualified name](../glossary.html#term-qualified-name) of the class, function, method, descriptor, or generator instance.

Added in version 3.3.

definition.__module__Â¶
    

The name of the module in which a class or function was defined.

definition.__doc__Â¶
    

The documentation string of a class or function, or `None` if undefined.

definition.__type_params__Â¶
    

The [type parameters](../reference/compound_stmts.html#type-params) of generic classes, functions, and [type aliases](typing.html#type-aliases). For classes and functions that are not generic, this will be an empty tuple.

Added in version 3.12.

## Integer string conversion length limitationÂ¶

CPython has a global limit for converting between [`int`](functions.html#int "int") and `str` to mitigate denial of service attacks. This limit _only_ applies to decimal or other non-power-of-two number bases. Hexadecimal, octal, and binary conversions are unlimited. The limit can be configured.

The [`int`](functions.html#int "int") type in CPython is an arbitrary length number stored in binary form (commonly known as a âbignumâ). There exists no algorithm that can convert a string to a binary integer or a binary integer to a string in linear time, _unless_ the base is a power of 2. Even the best known algorithms for base 10 have sub-quadratic complexity. Converting a large value such as `int('1' * 500_000)` can take over a second on a fast CPU.

Limiting conversion size offers a practical way to avoid [**CVE 2020-10735**](https://www.cve.org/CVERecord?id=CVE-2020-10735).

The limit is applied to the number of digit characters in the input or output string when a non-linear conversion algorithm would be involved. Underscores and the sign are not counted towards the limit.

When an operation would exceed the limit, a [`ValueError`](exceptions.html#ValueError "ValueError") is raised:
    
    
    >>> import sys
    >>> sys.set_int_max_str_digits(4300)  # Illustrative, this is the default.
    >>> _ = int('2' * 5432)
    Traceback (most recent call last):
    ...
    ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5432 digits; use sys.set_int_max_str_digits() to increase the limit
    >>> i = int('2' * 4300)
    >>> len(str(i))
    4300
    >>> i_squared = i*i
    >>> len(str(i_squared))
    Traceback (most recent call last):
    ...
    ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
    >>> len(hex(i_squared))
    7144
    >>> assert int(hex(i_squared), base=16) == i*i  # Hexadecimal is unlimited.
    

The default limit is 4300 digits as provided in [`sys.int_info.default_max_str_digits`](sys.html#sys.int_info "sys.int_info"). The lowest limit that can be configured is 640 digits as provided in [`sys.int_info.str_digits_check_threshold`](sys.html#sys.int_info "sys.int_info").

Verification:
    
    
    >>> import sys
    >>> assert sys.int_info.default_max_str_digits == 4300, sys.int_info
    >>> assert sys.int_info.str_digits_check_threshold == 640, sys.int_info
    >>> msg = int('578966293710682886880994035146873798396722250538762761564'
    ...           '9252925514383915483333812743580549779436104706260696366600'
    ...           '571186405732').to_bytes(53, 'big')
    ...
    

Added in version 3.11.

### Affected APIsÂ¶

The limitation only applies to potentially slow conversions between [`int`](functions.html#int "int") and `str` or `bytes`:

  * `int(string)` with default base 10.

  * `int(string, base)` for all bases that are not a power of 2.

  * `str(integer)`.

  * `repr(integer)`.

  * any other string conversion to base 10, for example `f"{integer}"`, `"{}".format(integer)`, or `b"%d" % integer`.




The limitations do not apply to functions with a linear algorithm:

  * `int(string, base)` with base 2, 4, 8, 16, or 32.

  * `int.from_bytes()` and `int.to_bytes()`.

  * [`hex()`](functions.html#hex "hex"), [`oct()`](functions.html#oct "oct"), [`bin()`](functions.html#bin "bin").

  * [Format Specification Mini-Language](string.html#formatspec) for hex, octal, and binary numbers.

  * `str` to [`float`](functions.html#float "float").

  * `str` to [`decimal.Decimal`](decimal.html#decimal.Decimal "decimal.Decimal").




### Configuring the limitÂ¶

Before Python starts up you can use an environment variable or an interpreter command line flag to configure the limit:

  * [`PYTHONINTMAXSTRDIGITS`](../using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS), e.g. `PYTHONINTMAXSTRDIGITS=640 python3` to set the limit to 640 or `PYTHONINTMAXSTRDIGITS=0 python3` to disable the limitation.

  * [`-X int_max_str_digits`](../using/cmdline.html#cmdoption-X), e.g. `python3 -X int_max_str_digits=640`

  * [`sys.flags.int_max_str_digits`](sys.html#sys.flags.int_max_str_digits "sys.flags.int_max_str_digits") contains the value of [`PYTHONINTMAXSTRDIGITS`](../using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS) or [`-X int_max_str_digits`](../using/cmdline.html#cmdoption-X). If both the env var and the `-X` option are set, the `-X` option takes precedence. A value of _-1_ indicates that both were unset, thus a value of [`sys.int_info.default_max_str_digits`](sys.html#sys.int_info.default_max_str_digits "sys.int_info.default_max_str_digits") was used during initialization.




From code, you can inspect the current limit and set a new one using these [`sys`](sys.html#module-sys "sys: Access system-specific parameters and functions.") APIs:

  * [`sys.get_int_max_str_digits()`](sys.html#sys.get_int_max_str_digits "sys.get_int_max_str_digits") and [`sys.set_int_max_str_digits()`](sys.html#sys.set_int_max_str_digits "sys.set_int_max_str_digits") are a getter and setter for the interpreter-wide limit. Subinterpreters have their own limit.




Information about the default and minimum can be found in [`sys.int_info`](sys.html#sys.int_info "sys.int_info"):

  * [`sys.int_info.default_max_str_digits`](sys.html#sys.int_info "sys.int_info") is the compiled-in default limit.

  * [`sys.int_info.str_digits_check_threshold`](sys.html#sys.int_info "sys.int_info") is the lowest accepted value for the limit (other than 0 which disables it).




Added in version 3.11.

Caution

Setting a low limit _can_ lead to problems. While rare, code exists that contains integer constants in decimal in their source that exceed the minimum threshold. A consequence of setting the limit is that Python source code containing decimal integer literals longer than the limit will encounter an error during parsing, usually at startup time or import time or even at installation time - anytime an up to date `.pyc` does not already exist for the code. A workaround for source that contains such large constants is to convert them to `0x` hexadecimal form as it has no limit.

Test your application thoroughly if you use a low limit. Ensure your tests run with the limit set early via the environment or flag so that it applies during startup and even during any installation step that may invoke Python to precompile `.py` sources to `.pyc` files.

### Recommended configurationÂ¶

The default [`sys.int_info.default_max_str_digits`](sys.html#sys.int_info.default_max_str_digits "sys.int_info.default_max_str_digits") is expected to be reasonable for most applications. If your application requires a different limit, set it from your main entry point using Python version agnostic code as these APIs were added in security patch releases in versions before 3.12.

Example:
    
    
    >>> import sys
    >>> if hasattr(sys, "set_int_max_str_digits"):
    ...     upper_bound = 68000
    ...     lower_bound = 4004
    ...     current_limit = sys.get_int_max_str_digits()
    ...     if current_limit == 0 or current_limit > upper_bound:
    ...         sys.set_int_max_str_digits(upper_bound)
    ...     elif current_limit < lower_bound:
    ...         sys.set_int_max_str_digits(lower_bound)
    

If you need to disable it entirely, set it to `0`.

Footnotes

[1]

Additional information on these special methods may be found in the Python Reference Manual ([Basic customization](../reference/datamodel.html#customization)).

[2]

As a consequence, the list `[1, 2]` is considered equal to `[1.0, 2.0]`, and similarly for tuples.

[3]

They must have since the parser canât tell the type of the operands.

[4] (1,2,3,4)

Cased characters are those with general category property being one of âLuâ (Letter, uppercase), âLlâ (Letter, lowercase), or âLtâ (Letter, titlecase).

[5] (1,2)

To format only a tuple you should therefore provide a singleton tuple whose only element is the tuple to be formatted.

### [Table of Contents](../contents.html)

  * Built-in Types
    * Truth Value Testing
    * Boolean Operations â `and`, `or`, `not`
    * Comparisons
    * Numeric Types â `int`, `float`, `complex`
      * Bitwise Operations on Integer Types
      * Additional Methods on Integer Types
      * Additional Methods on Float
      * Hashing of numeric types
    * Boolean Type - `bool`
    * Iterator Types
      * Generator Types
    * Sequence Types â `list`, `tuple`, `range`
      * Common Sequence Operations
      * Immutable Sequence Types
      * Mutable Sequence Types
      * Lists
      * Tuples
      * Ranges
    * Text Sequence Type â `str`
      * String Methods
      * `printf`-style String Formatting
    * Binary Sequence Types â `bytes`, `bytearray`, `memoryview`
      * Bytes Objects
      * Bytearray Objects
      * Bytes and Bytearray Operations
      * `printf`-style Bytes Formatting
      * Memory Views
    * Set Types â `set`, `frozenset`
    * Mapping Types â `dict`
      * Dictionary view objects
    * Context Manager Types
    * Type Annotation Types â Generic Alias, Union
      * Generic Alias Type
        * Standard Generic Classes
        * Special Attributes of `GenericAlias` objects
      * Union Type
    * Other Built-in Types
      * Modules
      * Classes and Class Instances
      * Functions
      * Methods
      * Code Objects
      * Type Objects
      * The Null Object
      * The Ellipsis Object
      * The NotImplemented Object
      * Internal Objects
    * Special Attributes
    * Integer string conversion length limitation
      * Affected APIs
      * Configuring the limit
      * Recommended configuration



#### Previous topic

[Built-in Constants](constants.html "previous chapter")

#### Next topic

[Built-in Exceptions](exceptions.html "next chapter")

### This Page

  * [Report a Bug](../bugs.html)
  * [Show Source ](https://github.com/python/cpython/blob/main/Doc/library/stdtypes.rst)



Â«

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](exceptions.html "Built-in Exceptions") |
  * [previous](constants.html "Built-in Constants") |
  * ![Python logo](../_static/py.svg)
  * [Python](https://www.python.org/) »
  *   *   * [3.13.2 Documentation](../index.html) » 
  * [The Python Standard Library](index.html) »
  * [Built-in Types]()
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
  *[LIFO]: last-in, first-out
