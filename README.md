# climax: **ᴄʟɪ**pboad **ᴍᴀx**imizer.

[![PyPI version](https://badge.fury.io/py/clipboard-maximizer.svg)](https://badge.fury.io/py/clipboard-maximizer)

> 🐙🖥️🐍➕👮🏻☃️🔧4️⃣👯‍♀️*🫢📁*(🚫🗃️)⏭️📋

*(A* mͫuͧltͭiͥplaͣtͭfoͦrͬmͫ *python library and command line tool for copying 𝕬𝖈𝖙𝖚𝖆𝖑 𝕱𝖎𝖑𝖊𝖘* (ie, not their content) *to the clipboard.)*

- [climax: **ᴄʟɪ**pboad **ᴍᴀx**imizer.](#climax-ᴄʟɪpboad-ᴍᴀximizer)
  - [1.1. Compatibility](#11-compatibility)
  - [1.2. Installation](#12-installation)
  - [1.3. Command Line](#13-command-line)
    - [1.3.1. Python API](#131-python-api)
  - [1.4. Contributing](#14-contributing)
  - [1.5. Blah](#15-blah)

![CLIPboard MAXimizer logo, courtesy of bing](logo.png)

## 1.1. Compatibility

| OS | 🍎 | 🐧 | 🪟 |
|--|--|--|--|
| Integration available | ✅ | ✅ | ✅ |
| Tested on device | ✅ | ✅ | 🙊[[1]](#14-contributing) |
|extra requirements| none |`xclip`|`pwsh`|

**macOS** and **Linux** are supported and tested; the latter via `xclip` (`apt-get install xclip`)

**Windows** should be supported (I can run it on mac Powershell via `pwsh`), but I don't have a Windows machine to test it on.

## 1.2. Installation

Use pip, poetry, or your favorite python package manager to install the latest version of the clipboard maximiser: `clipboard_maximizer`.

## 1.3. Command Line

Install with pipx:

```bash
pipx install clipboard_maximizer
```

The script is available as `climax`:

```bash
climax --help # show help
climax file1 [file2] # copy file1 and file2 to the clipboard
climax file1 --clipboard xclip # use a specific clipboard.
            # xclip, powershell (custom script) and applescript 
            # are supported).
```

### 1.3.1. Python API

Install:

```bash
pip install clipboard_maximizer
```

Or, if you use poetry:

```bash
poetry add clipboard_maximizer
```

Use:

```python
from clipboard_maximizer import copy_to_clipboard;

# copy file to clipboard
copy_to_clipboard("file1") 

# use a specific clipboard (see above)
copy_to_clipboard("file1", clipboard="xclip")
```

## 1.4. Contributing

```bash
poetry install
poetry run pytest
```

Contributions, in particular windows-related, are welcome.

If you plan to turn this into a full multiplatform clipboard manager, please fork the project and do so; I'll happily transfer the name to you.

![CLIPboard MAXimizer logo, courtesy of bing](logo.png)

## 1.5. Blah

License: MIT.
