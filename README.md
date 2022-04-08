## GDS Dash Starter Template

A starter template for building Dash visualization interfaces with the [GDS design system](https://design-system.service.gov.uk/) styling applied.

## Prerequisites

* An installation of [Python 3.6](https://www.python.org/downloads/) or above
* Admin access to the development machine

## Getting started

* Create a virtual environment using `python -m venv venv`
* Activate the virtual environment using `venv/Scripts/activate`
* Install packages using `python -m pip install -r requirements.txt`
* Run the app using `python index.py`

## Installing new packages

* Install the package using `python -m pip install <package-name>`
* Update the requirements file using `python -m pip freeze > requirements.txt`

## Steps to create a choropleth map 

The choropleth in the starter template map tab is an adapted version of the [dash-leaflet Choropleth map tutorial](https://dash-leaflet.herokuapp.com/).

* Download a shape map from [ONS GeoPortal](https://geoportal.statistics.gov.uk/datasets/ons::local-authority-districts-december-2021-gb-bfc/explore?location=54.111333%2C-1.754323%2C6.09)
* Upload to [mapshaper](https://mapshaper.org/) and download as CSV
* Join custom data i.e. population metrics to CSV
* Upload CSV back to mapshaper 
* In the mapshaper console use `-join dataset_two keys=<column_one>,<column_two>` to join the CSV data to the Shape file
* Simply the Shape file to less than 4%
* Set projection to World Geodetic System (WGS) using `-proj wgs84` in the mapshaper console
* Download as GeoJSON
* Adapt the code in section/map.py

## Documentation

* [Leaflet.js](https://leafletjs.com/)
* [Dash Leaflet](http://dash-leaflet.herokuapp.com/#)
* [Plotly layouts](https://plotly.com/python/reference/layout/)

## References

* [Dash tutorial for single page app](https://realpython.com/python-dash/)
* [Dash tutorial for multi page app](https://www.youtube.com/watch?v=RMBSQ6leon)
* [Approved colour pallete](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1060710/Research_reports_guidance_March_2022.pdf)
* [Setting global styles for Plotly charts](https://community.plotly.com/t/setting-global-styles-for-plotly-charts/14213)
* [Stylesheet reference](https://coronavirus.data.gov.uk/public/assets/summary/css/application.css)
* [Leaflet providers preview](https://leaflet-extras.github.io/leaflet-providers/preview/)