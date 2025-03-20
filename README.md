# pypokemon

![Build Status](https://github.com/software-students-spring2025/3-python-package-ez-squad-3-0/actions/workflows/build.yaml/badge.svg)

---

## Project Description

**pypokemon** is a terminal-based **Pokémon battle game** featuring ASCII art, interactive gameplay, and a fun "Lucky Pokémon" feature. Players can select Pokémon and engage in simulated battles with simple commands.

---

## PyPI Package

 **[pypokemon on PyPI](https://pypi.org/project/pypokemon/)**

---

## Importing and Using pypokemon in Your Code

Developers can import and use `pypokemon` functions in their own projects.

### Available Functions & Examples

#### 1. `show_pokemon()`
Displays ASCII art and stats of all Pokémon.

```python
from pypokemon import show_pokemon
show_pokemon()
```

#### 2. `select_pokemon()`
Interactive Pokémon selector.

```python
from pypokemon import select_pokemon
p1, p2 = select_pokemon()
print(f"You selected {p1} and {p2}")
```

#### 3. `battle(pokemon1, pokemon2)`
Simulate a battle between two Pokémon.

```python
from pypokemon import battle
battle("Charizard", "Blastoise")
```

#### 4. `luckypokemon()`
Randomly selects and displays a lucky Pokémon.

```python
from pypokemon import luckypokemon
print(luckypokemon())
```

**[Example Program](./example.py)**

---
## Developer Setup Guide
Follow these steps to contribute to pypokemon:


1. **Clone this repository:**
```bash
git clone https://github.com/software-students-spring2025/3-python-package-ez-squad-3-0.git
cd 3-python-package-ez-squad-3-0
```
2. **Set Up a Virtual Environment:**
```bash
pipenv shell
```

3. **Install Dependencies:**
```bash
pip install -e .[dev]
```

4. **Run Tests:**
```bash
pytest
```

5. **Install Build Tools:**
```bash
pip install build twine
```

6. **Build Package:**
```bash
python -m build
```

---
##  Team Members

| Name           | NYU Email           | GitHub Profile                                           |
|----------------|---------------------|----------------------------------------------------------|
| Chen Jun Hsu   | ch4356@nyu.edu      | [Junpapadiamond](https://github.com/Junpapadiamond)     |
| Kenny Pan      | zp2165@nyu.edu      | [kenny-pan](https://github.com/kenny-pan)               |
| Shenrui Xue    | sx2218@nyu.edu      | [ShenruiXue666](https://github.com/ShenruiXue666)       |
| Eric Zhao      | zz4040@nyu.edu      | [Ericzzy675](https://github.com/Ericzzy675)             |

---

##  Setup Instructions for Any User Any Platform

This project is designed to run on **any operating system** (Windows, macOS, Linux) with **Python 3.7+**. Follow these exact steps to configure and run `pypokemon`:

1. **Install pypokemon:**
```bash
pipenv shell #Linux user
pip install pypokemon
```

2. **Run the Game:**
```bash
pypokemon
# or
python -m pypokemon
```

##  Environment Variables & Starter Data
This project does not require any environment variables or a database.
##  Secret Configuration Files
This project does not require any environment variables or a database.
