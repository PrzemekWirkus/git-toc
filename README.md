#Table of Contents

* [Description](#description)
  * [Example usage](#example-usage)
* [Installation from PyPI (preferred)](#installation-from-pypi-preferred)
* [Installation from sources](#installation-from-sources)
* [Usage](#usage)
  * [Example](#example)

# Description
Generates super simple TOC (Table of Content) for [GitHub markdown language](https://guides.github.com/features/mastering-markdown/) documents.

## Example usage
```
$ gittoc -f README.md
```
```
* [greentea-client](#greentea-client)
  * [mbed-drivers dependencies](#mbed-drivers-dependencies)
  * [Greentea test tools](#greentea-test-tools)
  * [Compatibility](#compatibility)
    * [Greentea support](#greentea-support)
    * [utest support](#utest-support)
    * [greentea-client support in your module](#greentea-client-support-in-your-module)
  * [Terms](#terms)
    * [Test suite](#test-suite)
    * [Test case](#test-case)
    * [key-value protocol](#key-value-protocol)
  * [Where can I use it?](#where-can-i-use-it)
* [Test suite model](#test-suite-model)
  * [utest support template](#utest-support-template)
  * [No utest support template](#no-utest-support-template)
```

# Installation from PyPI (preferred)

This application is released with PyPI so you can use ```pip``` to install it on your host.

```
$ pip install git-toc --upgrade
```

# Installation from sources

```
$ git clone https://github.com/PrzemekWirkus/git-toc.git
```

```
$ cd git-toc
$ python setup.py install
```

# Usage
Below command will print on the screen TOC extracted from file specified with switch ```-f``` which you can embed to TOC section of your ```README.md``` document.
```
$ gittoc -f <file-name>
```

## Example
```
$ gittoc.exe -f TESTING.md
```
```
  * [Mbed SDK automated test suite](#mbed-sdk-automated-test-suite)
    * [Introduction](#introduction)
    * [What is host test?](#what-is-host-test)
    * [Test suite core: singletest.py script](#test-suite-core-singletestpy-script)
      * [Parameters of singletest.py](#parameters-of-singletestpy)
        * [MUTs Specification](#muts-specification)
        * [Peripherals testing](#peripherals-testing)
        * [Additional MUTs configuration file settings](#additional-muts-configuration-file-settings)
        * [Run your tests](#run-your-tests)
      * [Exmple of device configuration (one device connected to host computer)](#exmple-of-device-configuration-one-device-connected-to-host-computer)
  * [CppUTest unit test library support](#cpputest-unit-test-library-support)
    * [CppUTest in Mbed SDK testing introduction](#cpputest-in-mbed-sdk-testing-introduction)
    * [From where you can get more help about CppUTest library and unit testing](#from-where-you-can-get-more-help-about-cpputest-library-and-unit-testing)
    * [How to add CppUTest to your current Mbed SDK installation](#how-to-add-cpputest-to-your-current-mbed-sdk-installation)
      * [Do I need CppUTest port for Mbed SDK?](#do-i-need-cpputest-port-for-mbed-sdk)
      * [Prerequisites](#prerequisites)
      * [How / where to install](#how--where-to-install)
    * [New off-line mbed SDK project with CppUTest support](#new-offline-mbed-sdk-project-with-cpputest-support)
    * [CppUTest with mbed port ](#cpputest-with-mbed-port-)
    * [Unit test location](#unit-test-location)
    * [Define unit tests in mbed SDK test suite structure](#define-unit-tests-in-mbed-sdk-test-suite-structure)
      * [Tests are now divided into two types:](#tests-are-now-divided-into-two-types)
        * ['Hello world' tests ](#hello-world-tests-)
        * ['Unit test' test cases](#unit-test-test-cases)
    * [Example](#example)
      * [Example configuration](#example-configuration)
      * [Execute tests](#execute-tests)
```
