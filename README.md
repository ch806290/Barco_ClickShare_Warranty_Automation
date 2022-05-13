# Barco_ClickShare_Assignment
This is for testing Barco web page > ClickShare Warranty input feature in web. And for all automation test cases could seperate different part as below and reference `Test Plan` folder:
1. **End 2 End Testing**
2. **Function Testing**
3. **L10N Testing**
4. **Browser Testing - Firefox**
5. **Browser Testing - Edge**

***Automation methodology***:
I use the **python selenium** + **browser driver** + **beautifulReport**, so if you would like to run the automation case, please follow below steps to accomplish. Finally, I also put the `result report` and `recording` of running case process, if any question, please contact with me, thank you!

<h4 align="center">
  <img alt="Barco fature scope" src="Barco_feature.jpg">
</h4>

## Demo - recording



https://user-images.githubusercontent.com/6802038/168200312-d1426b1d-89e0-48cb-a4d7-4cd6ef9fdc2a.mp4


### Table of Contents
**[Pre-requirement](#pre-requirement)**<br>
**[Installation steps - python selenium](#installation-steps---python-selenium)**<br>
**[Installation steps - browser driver](#installation-steps---browser-driver)**<br>
**[Installation steps - beautifulReport](#installation-steps---beautifulreport)**<br>
**[Usage - how to run my test case](#usage---how-to-run-my-test-case)**<br>
**[Reference](#reference)**<br>



## Pre-requirement
1. [Python 3.10.4](https://www.python.org/downloads/)
2. [Python Selenium](https://selenium-python.readthedocs.io/installation.html)
3. [Web driver (Chrome, Firefox, Edge)](https://selenium-python.readthedocs.io/installation.html#drivers)
4. [BeautifulReport](https://github.com/TesterlifeRaymond/BeautifulReport)

Or you could see also [Python Selenium with VSCODE 教學筆記](https://hackmd.io/@FortesHuang/S1V6jrvet)
## Installation steps - python selenium
**My environment : win10**
So I would introduce how to install in win10 env.

Make sure your env installed `Python 3.9 or above` version, and open **cmd** and run
    $ pip install selenium

![image](https://user-images.githubusercontent.com/6802038/168201379-9374506c-3c07-4753-845a-6a847b5dd347.png)

And after see "Successfully installed selenium" means you install already!

## Installation steps - browser driver
#####Chrome driver#####

## Installation steps - beautifulReport
## Usage - how to run my test case



## Reference
---

## Usage

With [npm](https://npmjs.org/) installed, run

    $ npm install -g common-readme

`common-readme` is a command line program. You run it when you've started a new
module that has a `package.json` set up.

When run, a brand new README is generated and written to your terminal. You can
redirect this to `README.md` and use it as a basis for your new module.

    $ common-readme > README.md

This brand new readme will be automatically populated with values from
`package.json` such as `name`, `description`, and `license`. Stub sections will
be created for everything else (Usage, API, etc), ready for you to fill in.

## Why?

This isn't a crazy new idea. Other ecosystems like [Perl's
CPAN](http://perldoc.perl.org/perlmodstyle.html) have been benefiting from a
common readme format for years. Furthermore:

1. The node community is powered by us people and the modules we share. It's our
   documentation that links us together. Our README is the first thing
   developers see and it should be maximally effective at communicating its
   purpose and function.

2. There is much wisdom to be found from the many developers who have written
   many many modules. Common readme aims to distill that experience into a
   common format that stands to benefit us all; especially newer developers!

3. Writing the same boilerplate is a waste of every author's time -- we might as
   well generate the common pieces and let the author focus on the content.

4. Scanning through modules on npm is a part of every node developer's regular
   development cycle. Having a consistent format lets the brain focus on content
   instead of structure.

## The Art of README

For even more background, wisdom, and ideas, take a look at the article that
inspired common-readme:

- [*Art of README*](https://github.com/noffle/art-of-readme).

## Install

With [npm](https://npmjs.org/) installed, run

```shell
npm install -g common-readme
```

You can now execute the `common-readme` command.

## Acknowledgments

A standard readme format for the Node community isn't a new idea. Inspiration
came from many conversations and unrealized efforts in the community:

- <https://github.com/feross/standard/issues/141>
- [richardlitt/standard-readme](https://github.com/RichardLitt/readme-standard)
- [zwei/standard-readme](https://github.com/zcei/standard-readme)

This, in addition to my own experiences evaluating hundreds of node modules and
their READMEs.

I was partly inspired by the audacity of the honey-badger-don't-care efforts of
[standard](https://github.com/feross/standard).

I also did a great deal of Perl archaeology -- it turns out the monks of the
Perl community already did much of the hard work of [figuring out great
READMEs](http://perldoc.perl.org/perlmodstyle.html) and the wisdom around small
module development well over a decade ago.

Thanks to @mafintosh, @andrewosh, and @feross for many long conversations about
readmes and Node.

## See Also

READMEs love [`readme`](https://www.npmjs.com/package/readme)!

## License

ISC
