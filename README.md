# alias-cd
This tool is meant to help developers create aliases for directories on their local machines. It is configured through a simple yaml file.

## Install
Neither of these are implimented yet...
TODO host this on PyPI
TODO make it work with brew or pipx?
```bash
# With pipbased tools
pip install alias-cd
```

```bash
# homebrew
brew install alias-cd
```

## Configure
The following is an example configuration file. Which you can drop into `~/.config/alias_cd`
```yaml
---
"~":
  # _alias with no value is used as the default directory
  _alias:
  # Used a nested tree structure 
  Documents:
    # Uses _alias tags to set shorter names for directories
    _alias: docs
    repos:
      _alias: repos
      open-source: # Aliases are optional
        my-repo:
          _alias: fun
      public:
        my-organizations-repo:
          _alias: work
```

## Usage
```
# navigate to the docs directory
alias_cd docs

# display the version of the tool
alias_cd version

# validate that all directories exist
alias_cd validate
```