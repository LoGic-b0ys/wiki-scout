![](https://i.ibb.co/G03129y/Artboard-1wiki-scout.png)
#### <p align="center">**Scout your keyword and formed a wiki**</p>
---
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#future-development">Future Development</a>
</p>

---
![](https://i.ibb.co/Vvg61sw/Screenshot-2019-05-26-22-53-01.png)

## Key Features

* Crawl as many as review you want
  - Just copy the Farnam URL and you will get the keyword linked to wikipedia
* Customizable
* Simple algorithm, you can tweak it easily
* Integrated with wikipedia huge database

![](https://i.ibb.co/Z85x8ns/Screenshot-2019-06-01-13-24-21.png)

## How to Use

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer and of course a pip. From your command line:

```bash
# Install required packages
$ pip install nltk
$ pip install rake-nltk
$ pip install selenium
$ pip install flask
$ pip install flask-bootstrap

# Clone the repository
$ git clone https://github.com/LoGic-b0ys/wiki-scout.git
```
* After that you need to get the [wikipedia title database](https://www.kaggle.com/residentmario/wikipedia-article-titles) to refer the keyword from wikipedia article.
* Move to the repository folder and extract the file
* After that open the terminal again

```bash
# Go into the repository
$ cd wiki-scout

# Execute the server
$ python main.py
```
* You can access your article with the default Flask URL and port at http://localhost:5000


## Future Development

* Still brainstorming

## Contribution

Contribute to this work by fork this repository. Don't forget to submit an issue first.

## Licence
GPL-3.0