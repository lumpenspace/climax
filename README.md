# climax: **ᴄʟɪ**pboad **ᴍᴀx**imizer.

> 🐙🖥️🐍➕👮🏻☃️🔧4️⃣👯‍♀️*🫢📁*(🚫🗃️)⏭️📋

*(A* mͫuͧltͭiͥplaͣtͭfoͦrͬmͫ *python library and command line tool for copying 𝕬𝖈𝖙𝖚𝖆𝖑 𝕱𝖎𝖑𝖊𝖘* (ie, not their content) *to the clipboard.)*

## Status

[![PyPI version](https://badge.fury.io/py/clipboard-maximizer.svg)](https://badge.fury.io/py/clipboard-maximizer)

**macOS** and **Linux** are supported and tested; the latter via `xclip` (`apt-get install xclip`)

**Windows** should be supported (I can run it on mac Powershell via `pwsh`), but I don't have a Windows machine to test it on.

## Installation

Use pip, poetry, or your favorite python package manager to install the latest version of the clipboard maximiser.

```bash
pip install clipboard_maximizer
```

## Usage

### Command Line

```bash
climax --help # show help
climax file1 [file2] # copy file1 and file2 to the clipboard
climax file1 --clipboard xclip # use a specific clipboard.
            # xclip, powershell (custom script) and applescript 
            # are supported).
```

### Python API

```python
from clipboard_maximizer import copy_to_clipboard;

# copy file to clipboard
copy_to_clipboard("file1") 

# use a specific clipboard (see above)
copy_to_clipboard("file1", clipboard="xclip")
```

## Contributing

```bash
poetry install
poetry run pytest
```

Contributions, in particular windows-related, are welcome.

If you plan to turn this into a full multiplatform clipboard manager, please fork the project and do so; I'll happily transfer the name to you.

## Blah

License: MIT.
