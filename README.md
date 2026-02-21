# ubuntu-namer

Generates random Ubuntu-style names like "Bamboozling Barnacle" and "Xenial Xenops". Over 15,000 unique combinations.

## CLI

```bash
$ uvx ubuntu-namer
Cosmic Cow

$ uvx ubuntu-namer --letter k
Kinetic Kittiwake

$ uvx ubuntu-namer --style snake
keen_kittiwake

$ uvx ubuntu-namer --letter g --style dot
galloping.gannet
```

## Library

```python
from ubuntu_namer import generate_name

generate_name()                    # "Haughty Humpback"
generate_name("u")                 # "Unassailable Uakari"
generate_name("s", style="camel")  # "sarcasticStarfish"
generate_name(style="kebab")       # "ultimate-uguisu"
```

## Styles

```
title    Zen Zebu
lower    giggling gecko
upper    DILIGENT DRAKE
camel    remarkableRedbird
pascal   EvangelizingEagle
snake    idyllic_inosaurus
kebab    furious-fieldmouse
dot      quick.quahog
```
