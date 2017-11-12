# IPK NTNU Table Tennis ELO Ladder

TODO: Make this README.md complete!
NB! This is not just a template I have yet to fill out.

## How to update the ladder
1. Gather all new "Match history" sheets
2. Open "matches.csv" and fill out the newly played matches
3. go to "pyCharm" directory
4. Run calculate the new ELO scores for everyone
```
python main.py
```
5. Plot the ELO temporal score of every player
```
python plot_temporal_elo.py
```
6. Make new PDF of the leaderboard by generating LaTeX files
```
python make_leaderboard_pdf.py
```
7. Go to "latex_leaderboard" directory and the current date to get the newly generated LaTeX files
```
cd latex_leaderboard
cd <current-date>
```
8. Open main.tex in sublime
```
subl main.tex
```
9. Generate new PDF from .tex files in current folder
- If you have install LaTeXTools in sublime, you can simply press "<ctrl> + b" and a new PDF will be created
NB! I bugg has been spoted where you need to compile the LaTeX file several times before the table is nice-looking in the PDF. Simply press "<ctrl> + b" a couple of times.
```
<ctrl> + b
```









One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
