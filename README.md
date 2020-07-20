# Covid Watch

Covid Watch is a PyPip module that can be used to monitor new cases reported in countries. All data is pulled from [disease.sh](https://disease.sh), checking every 5 minutes to see if there is any new cases.

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install covidwatch
```

### Usage

```python
import covidwatch

watch = covid.Watcher("Australia")
watch.start("discord or slack url") 
# slack is not supported but can be used as they both use the same method for webhooks
```

### Sample Output
![image](https://discord.photos/CIro7/JE6DI.png)
![image](https://discord.photos/CIro7/2MZQ4.png)

###### Obviously new cases would only be shown if a new case is reported this was just for demo purposes

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### License
[MIT](https://choosealicense.com/licenses/mit/)
