# Description
Python plugin for Albert launcher. Shows the color queried.

# Install
Clone the repository into
`$HOME/.local/share/albert/org.albert.extension.python/modules`
```bash
git clone https://github.com/scmanjarrez/albert-plugin-colors.git $HOME/.local/share/albert/org.albert.extension.python/modules/colors
````

Enable **_colors_** plugin in `albert settings - Extensions - Python`

# Usage
**_colors_** can be called using **col** and **c** triggers. In addition,
it accepts 3 color formats:
- HEX
  - `col #ff00ff`
  - `col #FF00FF`
  - `c #ff00ff`
- RGB
  - `col (212, 231, 122)`
  - `col (212,231,122)`
  - `col 212, 231, 122`
  - `col 212,231,122`
  - `col 212 231 122`

**_colors_** has 3 actions that can be accessed using `Alt` key.
- Copy HEX (lower case) to clipboard
- Copy HEX (upper case) to clipboard
- Copy RGB to clipboard

<details>
<summary><b>Images</b></summary>
    <a href="http://i.imgur.com/Ddw1txs.png">
        <img src="http://imgur.com/Ddw1txsl.png" />
    </a>
    <a href="http://i.imgur.com/udkWJ9Z.png">
        <img src="http://imgur.com/udkWJ9Zl.png" />
    </a>
</details>


# License
    albert-plugin-colors  Copyright (C) 2021-2023 scmanjarrez.
    This program comes with ABSOLUTELY NO WARRANTY; for details check below.
    This is free software, and you are welcome to redistribute it
    under certain conditions; check below for details.

[LICENSE](https://github.com/scmanjarrez/albert-plugin-colors/blob/master/LICENSE)
