# Networking, a key to success in movie industry ?

___Study of the influence of actor's network on their carreer evolution___

## Abstract

How do actors become famous ? Is it only thanks to their talent, or did they follow a certain pattern ? Did their carreer exploded once they played with a well known actor ? In this study, we aim to assess wether there is a link between an actor's network and the quality of the movies he plays in, characterized by their ratings. By network, we mean the other actors one actor has played with, during the realization of a movie. For the purpose of our analysis, we will construct a graph that can change over time, where nodes are actors and edges movies. We use an additional dataset taken from IMDb, in order to get the ratings of those movies. Each actor will get a "success" number, that depends on the rates of the movies he has played in. The nodes' diameter will depend on this success number. We will explore the evolution of actors carreer through 126 years, from 1888 to 2014, with 300 185 actors and 44 929 movies. 
 

## Research questions

- Can we find a relation between networking and the evolution of an actor's carreer over time ? 
- Do the "speed" of the evolution of the actor's carreer change according to the number of famous actors he plays with ? 
- For actors with multiple occurencies, do the rate of the next movie they play in is influenced by the actor's "success" ? 

  
## Additional datasets

As we are interested in knowing how much a certain movie is appreciated by the public, we decided to add a dataset containing movies'rating. Two datasets were taken from [IMDb](https://datasets.imdbws.com/).

* **1: title.basics.tsv.gz **  : dataset that contains the following usefull informations for our study : 
    * tconst (string) : unique alphanumeric encoding of each movie title 
    * startYear (YYYY) : release year of the title/movie
    * originalTitle (string) : title of the movie, in its original language
* **2 : title.ratings.tsv.gz ** : dataset that contains the following usefull informations for our study : 
    * averageRating : weighted average of all the individual user ratings
    * tconst (string) : unique alphanumeric encoding of each movie title 
    
Both dataset were connected thanks to the tconst feature. Then, the movie name could be linked to the average rating of the movie. After having merged both dataset, we compared the resulting dataset to the one given from the course. It was found that 44 151 movies were in common, and could be used for our study. Furthermore, we got around 300 000 actors that could be linked to one of those rated movies from the 450 000 actors that were in the original dataset. Finally we created a dataset combining all the features that we will be needed for our study: "Actor Name", "startYear", "Movie name", and "averageRating".


## Methods

** 

* Dataset D1 : General dataset containing quotes of women authors
* Dataset D2 : MeToo dataset containing quotes linked to the movement, in which the movement is mentioned
  * D2.1 : Subsets by gender of speaker
  * D2.2 : Subsets by age of speaker
  * D2.3 : Subsets by political parties (for politician authors) of speaker\
    *These subsets are built later on during Step 4.*
* Dataset D3 : Dataset containing quotes in which a woman is mentioned
  * D3.1: Subset by gender of speaker

**Step 2: General preliminary analysis using Quotebank entire dataset**
Weekly percentage of quotes by author’s gender (men, women, other, unkown) from 2015 to 2020.

**Step 3: Generate annual word clouds based on dataset D1 with this [library.](https://github.com/amueller/word_cloud)**

**Step 4: Investigate gender, political and generational biases in MeToo coverage using NLP to answer question A).**
Train a [SpaCy NLP model](https://spacy.io/usage/training) with dataset AD3 to perform sentiment analysis. Classification thanks to trained model on the whole dataset D2. Subdivision of D2 into D2.1, D2.2 and D2.3 for biases investigation. Clustering trials with unsupervised different ML algorithms applied on the sentiment analysis classification probabilities.

**Step 5: Investigate general women perception via dataset D3 in medias to answer question B).**
Generate word clouds. Classification of quotes : Text Blob or Vader models for positive, negative or neutral. Train SpaCy model on AD2 for misogynistic or non misogynistic. Classification thanks to trained model on D3.

**Step 6: Correlate and investigate causation between MeToo general perception and women’s mediatic place to answer question C).**
Plot previously collected (step 5) data distributions according to time. Comparison with key turning points of MeToo. Investigation of the statistical significance of detected changes before and after MeToo.

**Step 7: Github site building and Datastory redaction.**

**Further details on the proposed data pipelines can be found in the notebook.**

## Proposed timeline

* Step 2: 22/11/21
* Step 3, 4: 29/11/21
* Step 5: 06/12/21
* Step 6, 7: 13/12/21

## Organization within the team

* SpaCy Training on AD2 and AD3: Teammate 1
* Datastory: Teammate 2
* Website: Teammate 3 and 4
* Steps: Teammate 1,2,3,4
