# adobe-pdf-print
<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">adobe-pdf-print</h3>

  <p align="center">
    <br />
    <a href="https://github.com/hen0014/adobe-pdf-print"><strong>Explore the project »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hen0014/adobe-pdf-print">View Demo</a>
    ·
    <a href="https://github.com/hen0014/adobe-pdf-print/issues">Report Bug</a>
    ·
    <a href="https://github.com/hen0014/adobe-pdf-print/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#making-changes">Making changes</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I have to sometimes print a lot of PDFs at once, for example, 20+ documents at a time every blue moon. It takes a lot of time to open Adobe Reader> print > printer settings> print.

I am basing this script around Adobe Reader command line options, not because it is a good idea (you can't run Adobe Headless), but because it is a standard app a lot of workplaces have and trust to process their PDFs. there are additional Python libraries you can install with pip, or pdf printer binaries, but you are trusting a third-party bit of code from the internet which you might have to explain to someone. far easier to say it's just an automation script for the default pdf reader app than it's a program using another program or library set no one has heard of.


* [python](https://www.python3.org)

<!-- GETTING STARTED -->
## Getting Started

The script comes in two parts:
1. pdfprint.py -- file containing the class implementation for printing
2. pdf_print.py -- the file you run and uses the pdfprint.py class file

### Prerequisites

The following python libraries are required.

python
* N/A

software
* Adobe reader

## Installation

1. Open the project at **.insert local path of script here** with an editor. Preferrably [**vscode**](https://code.visualstudio.com/)
2. You could also clone the repo
   ```sh
   git clone https://github.com/hen0014/adobe-pdf-print.git

<!-- MAKING CHANGES -->
## Usage
command line options
./pdf_printer.py <directory> <printer> <--readOptions> <--debug> <--silent> <--options> <--all>
 
'directory', help='Directory to print PDFs from, specify "pwd" or directory', default='pwd'
'printer', help='Printer to print PDFs to', default='lexy=print'
'-ro', '--readOptions', help='Read options from file'
'-d', '--debug', help='Debug mode', action='store_true'
'-s', '--silent', help='Silent mode', action='store_true'
'-o', '--options', help='Options to print PDFs', nargs='+'
'-all', '--all', help='Print all PDFs in directory', action='store_true'

### Notes:
1. N/A

<!-- MAKING CHANGES -->
## Making Changes

<!-- ROADMAP -->
## Roadmap

1. tidy up the scripts
2. implement a read files to print from file
3. fix option names for the main script (change --readOptions to --file, --options to --printlist, etc)

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->

Project Link: [aodbe-pdf-print](https://github.com/hen0014/adobe-pdf-print.git)
