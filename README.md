  
# About watch_scope

Its a tool for watching grate bug bounty platforms if any scope is added into program scopes or not and if yes it'll let you know in your discord channel and there is no need to work with databases, it work by files.

## Installation
```
git clone https://github.com/mhossein1631/watch_scope.git
```

## Recommended Python Version:
-   The recommended version for Python 3 is  **3.6.x**

## Dependencies:
Sublist3r depends on the `requests`, `sys` and `discordwebhook` python modules.

-   Installation on Linux
```
pip install -r Requirements.txt
```


## Usage
-   Just write script file in your command line then paste your discord web hook url.
- Don't forget to add it to crontab on your server
### Example
```	
 crontab -e
 30 0 * * * main.py <discord webhook url>	
```
## Version

**Current version is 1.0**
