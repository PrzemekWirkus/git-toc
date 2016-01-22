#Table of content
* [Description](#description)
* [Installation](#installation)
* [Usage](#usage)
  * [Example](#example)

# Description
Generates super simple TOC (Table of Content) for git MD files. 

# Installation
```
$ git clone <repo>
```

```
$ cd git-toc
$ python setup.py install
```

# Usage
Below command will print TOC which you can embed to e.g. ```README.md```.
```
$ gittoc -f <file>
```

## Example
```
$ gittoc.exe -f TESTING.md
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
