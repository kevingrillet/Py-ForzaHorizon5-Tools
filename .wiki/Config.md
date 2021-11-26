Edit `config.ini` next to `main.py`. The file is created at first launch.

## Default values

```ini
[main]
car = pontiac
debug = 0
dev = False
language = fr
scale = 1
```

## Description

| Options    | Type    | Nullable | Description                                                         | Values            |
|------------|---------|----------|---------------------------------------------------------------------|-------------------|
| `car`      | `str`   | Yes      | Set the car to buy / master.                                        | `ford`, `pontiac` |
| `debug`    | `int`   | Yes      | Set the verbosity of the script. Higher values will have more text. | `0`-`4`           |
| `dev`      | `bool`  | Yes      | Set dev mode. Will save images in `.temp/` folder.                  | `True`, `False`   |
| `language` | `str`   | Yes      | Set language for the image folder.                                  | `en`, `fr`, ...   |
| `scale`    | `float` | Yes      | Set scale.                                                          | `1`, `0.75`       |


## More info

### Car

Car enum can be found here: <https://github.com/kevingrillet/Py-ForzaHorizon5-Tools/blob/main/game/constant.py>

| Name      | Value     |
|:---------:|:---------:|
| `FORD`    | `ford`    |
| `PONTIAC` | `pontiac` |
|           |           |

### Debug

Debug enum can be found here: <https://github.com/kevingrillet/Py-ForzaHorizon5-Tools/blob/main/utils/constant.py>

| Name        | Value |
|:-----------:|:-----:|
| `ALWAYS`    | `0`   |
| `INFO`      | `1`   |
| `CLASS`     | `2`   |
| `FUNCTIONS` | `3`   |
| `DEBUG`     | `4`   |
|             |       |

### Language

Lang enum can be found here: <https://github.com/kevingrillet/Py-ForzaHorizon5-Tools/blob/main/utils/constant.py>

| Name      | Value |
|:---------:|:-----:|
| `ENGLISH` | `en`  |
| `FRENCH`  | `fr`  |
|           |       |

### Scale

Scale is based on mine: `QHD` which is: `2560x1440`.

| Name                     | Resolution  | Scale  |
|:------------------------:|:-----------:|:------:|
| `WQHD` / `QHD` / `1440p` | `2560x1440` | `1`    |
| `HD 1080` / `1080p`      | `1920x1080` | `0.75` |

<hr>

<div align="center">
<a href="https://github.com/kevingrillet/Py-ForzaHorizon5-Tools/wiki/Home">Previous page</a>
|
<a href="https://github.com/kevingrillet/Py-ForzaHorizon5-Tools/wiki/Requirements">Next page</a>
</div>
