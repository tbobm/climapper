# <center>![Citymapper](https://lh6.ggpht.com/Imb9kzIzJPanYvoMhRzT04AemnqlYzS2RmU4rHX-Hoy3WONLzRhUo3j9bIJJi1N7we8F=w300)</center> Climapper <center>![Citymapper](https://lh6.ggpht.com/Imb9kzIzJPanYvoMhRzT04AemnqlYzS2RmU4rHX-Hoy3WONLzRhUo3j9bIJJi1N7we8F=w300)</center>

[![Build Status](https://travis-ci.org/massard-t/climapper.svg?branch=master)](https://travis-ci.org/massard-t/climapper)

Simple tool that for the Citymapper API made by a lazy person.
This project isn't related to Citymapper in any way, totally unofficial.

## Installation

### Prerequisites

#### Dependencies

Climapper works perfectly under python3. It uses 2 pip3 packages, `Unidecode` and `requests`.

```bash
sudo -H pip3 install -r requirements.txt
```

#### Installation

Simply run the installation script. It will create a `~/bin` directory, and a symbolic link to your climapper script.
This configuration allows you to update the script without having to run the installation script again.

```bash
./install
```

#### Configuration

In order to get climapper to work efficiently, you have to set a `home` variable, based on the LAT and LONG of your destination.

> Example:


```bash
# In your bash_profile (or bashrc)

export WORK="48.813896,2.392448"
export MY_HOME="48.928378,2.162200"
```


## Usage

```bash
$ climapper home
--------------------------------
| Rer C        |     5 min     |
|------------------------------|
| Bibliotheque Francois Mitt   |
|------------------------------|
| Rer A        |     19 min    |
|------------------------------|
|..............................|
|      Home in 89 min          |
|------------------------------|
```


## Todos

- [x] Collect destination and current location (ENV variables ?)
- [x] Make a call to the API
- [x] Parse the results
- [x] Display them gracefully
- [ ] Manage CLI args
- [ ] Manage configuration trough specific file (~/.config/climapper.json?)
- [ ] Maybe use [Fire](https://github.com/google/python-fire)



### Resources

[Citymapper Website](https://citymapper.com/)

[Citymapper for Directions](https://citymapper.com/tools/1053/launch-citymapper-for-directions)

[Citymapper for Robots](https://citymapper.3scale.net/docs)

[latlon.net](http://www.latlong.net/)
