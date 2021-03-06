# Web Scraping JavaScript Generated Pages with Python

The code shows how to do web scraping dynamic content pages generated from Javascript using Python and Selenium.

We use as data the ETHERSCAN site to extract transations of shinja token and generate a json file, to show on html table.

**Important: Educational Purposes Only**

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

What things you need to install the software and how to install them

- Python 3.x
- Geckodriver
- Firefox (you can use another browser)
- Some Python libraries following

## Installing

A step by step series of examples that tell you how to get a development env running

### Install the following Python libraries:

- **requests2** - Requests is the only Non-GMO HTTP library for Python, safe for human consumption;
- **pandas** - A great Python Data Analysis Library;
- **lxml** - Library for processing XML and HTML;
- **beautfulsoup4** - Library for pulling data out of HTML and XML files;
- **selenium** - An API to write functional/acceptance tests using Selenium WebDriver.

With:

```
pip install -r requirements.txt
```

### Geckodriver

[You can find install instructions in the official repository.](https://github.com/mozilla/geckodriver/releases)

## Running the code

```
python main.py
```

## Contributing

Feel free to submitting pull requests to us.

## Authors

- **Joaquim Peixoto**

## License

This project is licensed under the [GNU General Public License](https://opensource.org/licenses/GPL-3.0).
