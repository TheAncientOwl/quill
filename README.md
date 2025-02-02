# 🪶 Quill

Quill is a lightweight yet powerful command-line interface (CLI) tool designed to streamline development workflows within the Feather ecosystem. It simplifies project management, plugin development, and various utility tasks related to Minecraft plugin development 🎮.

## ✨ Features

- 🏠 **Project Initialization**: Quickly scaffold new Feather-based projects.
- 🚀 **Build & Deploy**: Automate building and deploying your plugins.
- 📦 **Dependency Management**: Easily manage dependencies for your Feather projects.
- 🧬 **Plugin Testing**: Run and test plugins locally with minimal setup.

### 🔧 Prerequisites

Ensure you have the following installed:

- ☕ Java 21+ _(you can use any version though, but you'll have to manually update plugins Java version in `pom.xml` by yourself for now)_
- 🛠️ Maven
- 🖥️ Git (optional, but recommended)

## 💡 Installation

Quill release version tags can be found [here](https://github.com/TheAncientOwl/quill/releases).

```bash
$ git clone https://github.com/TheAncientOwl/quill.git
$ cd quill
# choose release version
$ git fetch && git checkout v1.0.0

# set your bash/zsh/etc profile file path
$ QUILL_HOME=$(pwd) && PROFILE_PATH=~/.zshrc && echo "
export QUILL_HOME=$QUILL_HOME
export PATH=\$PATH:\$QUILL_HOME:\$QUILL_HOME/src
alias quill=quill.py
alias quill_run=\$QUILL_HOME/src/quill_run_server.sh
alias quill_dev=\$QUILL_HOME/src/quill_dev.sh" >> $PROFILE_PATH && source $PROFILE_PATH
```

## 🚀 Usage example

Example of using Quill for developing feather-toolkit paper-spigot plugins can be found [here](https://github.com/TheAncientOwl/feather-toolkit)

## ⚙️ Arguments

| 📏 No. | ⚡ Short Flag   | 🏷️ Long Flag                  | 📖 Description                                                         |
| ------ | --------------- | ----------------------------- | ---------------------------------------------------------------------- |
| 1.     | `-h`            | `--help`                      | Show this help message and exit                                        |
| 2.     | `-v`            | `--version`                   | Show program's version number and exit                                 |
| 3.     | `-c`            | `--clean`                     | Remove the plugin files from the dev server location and target files  |
| 4.     | `-i`            | `--install`                   | Compile the plugin and install it to the dev server                    |
| 5.     | `-iv`           | `--install-verbose`           | Verbose output for install command                                     |
| 6.     | `-x`            | `--configure`                 | Configure Maven project                                                |
| 7.     | `-t [TEST/S]`   | `--test [TEST/S]`             | Run unit tests 🧬 (default test suite if no specific test is provided) |
| 8.     | `-k`            | `--coverage`                  | Run unit test coverage 📊                                              |
| 9.     | `-hh`           | `--headers`                   | Configure code files 📚                                                |
| 10.    | **---**         | `--pre-dev-server-run`        | Run pre-server-run configured commands                                 |
| 11.    | **---**         | `--post-dev-server-run`       | Run post-server-run configured commands                                |
| 12.    | `-it [VERSION]` | `--install-toolkit [VERSION]` | Install Feather toolkit lib 🛠️                                         |
| 13.    | `-rn`           | `--release-notes`             | Generate git history between last 2 tags 📚                            |
| 13.    | **---**         | `--init`                      | Initialize Feather Toolkit project                                     |

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](https://github.com/TheAncientOwl/quill/blob/main/LICENSE) file for details.

## 🔗 Related Projects

- [🪶 FeatherCore](https://github.com/TheAncientOwl/feather-core)
- [🪶 FeatherToolkit](https://github.com/TheAncientOwl/feather-toolkit)
- [🪶 FeatherShowcase](https://github.com/TheAncientOwl/feather-showcase)
