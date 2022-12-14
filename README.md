# Networking, a key to success in the movie industry ?

___Study of the influence of actor's network on their career evolution___

## Abstract

How do actors become famous? Is it only thanks to their talent, or did they follow a certain pattern? Did their career explode once they played with a well known actor? In this study, we aim to assess whether there is a link between an actor's network and the quality of the movies he plays in, characterized by their ratings. For the purpose of our analysis, we will construct a graph that can change over time, where nodes are actors and edges represent the fact that two actors play in a movie together. We use an additional dataset taken from IMDb, in order to get the ratings of those movies. We will explore the evolution of actors' careers through 126 years, from 1888 to 2014, with 300 185 actors and 44 129 movies. 
 

## Research questions

- Can we find a relation between networking and the evolution of an actor's career over time? 
- Are there actors that influence more than others? 
- Are actors with many edges better ? 
- For actors with multiple occurrences, is the rating of the next movie they play influenced by the actor's "success"? 
  
## Additional datasets

As we are interested in knowing how much a certain movie is appreciated by the public, we decided to add a dataset containing movies rating. Two datasets were taken from [IMDb](https://datasets.imdbws.com/).

* **1: title.basics.tsv.gz**  : dataset that contains the following useful informations for our study : 
    * tconst (string) : unique alphanumeric encoding of each movie title 
    * startYear (YYYY) : release year of the title/movie
    * originalTitle (string) : title of the movie, in its original language
* **2 : title.ratings.tsv.gz** : dataset that contains the following useful informations for our study : 
    * averageRating : weighted average of all the individual user ratings
    * tconst (string) : unique alphanumeric encoding of each movie title 
    
Both datasets were connected thanks to the tconst feature. Then, the movie name could be linked to the average rating of the movie. After having merged both dataset, we compared the resulting dataset to the one given from the course. It was found that 44 129 movies were in common, and could be used for our study. Furthermore, we got around 300 185 actors that could be linked to one of those rated movies from the 450 000 actors that were in the original dataset. Finally we created a dataset combining all the features that we will be needed for our study: "Actor Name", "startYear", "Movie name", and "averageRating".


## Methods
### Data preprocessing
The first step of data cleaning involved counting the percentage of missing values to determine what features could not be used. For instance, we concluded that box office revenue couldn???t be used to determine a movie revenue because the dataset is missing that information for more than 90% of its movies.
Then, we cleaned the data and normalized the date format, as described in the notebook.
At this point we included review information from additional sources, as described in the Additional datasets section.

### Data visualization
We got a better understanding of the data by drawing several plottings of it, such as the distribution of actors and movies across time to make sure we have enough data for our purpose, as time is a key factor in our project.
Finally, we plotted the average degree (number of edges) in our actor graph to make sure our proposal is feasible.

### Graph representation

We use the networkx library to implement the Actor Graph. This will be the fundamental object to work with for the third milestone.

We plan to annotate each vertex (i.e. each actor in a time window) quality score aggregating the ratings of the movies he played in during that specific time window. We can either work with multi edges or weighted edges between actors when they play together in several movies to strengthen his relationship in the graph. For mathematical details of the graph please see the jupyter notebook.

To measure the networking impact in an actor's career, we consider actors??? network - his k-neighborhood in Actor Graph, or his cluster in Actor Graph (find using DBSCAN algorithm). We treat an actor's career as a function - from time to quality (measured as quality of movies he plays in). We inspect how changes in this function relate to changes in average of this function for his environment. 

## Proposed timeline

We divide the workload in the five remaining weeks:
1. Week 1 (21st Nov): Indepth graph analysis.
1. Week 2 (28th Nov): Build graph clusters using DBSCAN and k-neighborhood. Compare both approaches 
1. Week 3 (5th Dec): Inspect correlation between actors career and his network.
1. Week 4 (12nd Dec): Aggregate results and build the website to tell the data story.
1. Week 5 (19th Dec): Nothing (free time in case of inconveniences).

## Organization within the team

| Team member | Task |
| :-: | :-: |
| Ale | Make graph visualization and inspect actors' careers. |
| Charlotte | Indepth graph analysis and inspection of actors??? careers. |
| Konrad | Implementing and testing cluster algorithms in the graph. Aggregate results. |
| Matthias | Develop the web interface and write the narrative for the data story. |
