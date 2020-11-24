# NFL Play Predictor

### By: Jon Hickey

![alt text](/figures/football_field.jpg)

## Summary
The goal of this project is to use machine learning algorithms to predict whether an offensive play will be a run or pass based on in-game features. I will look at which features are most important when predicting a run or pass play, which can be valuable information for a defensive coordinator when it comes to schematics defensive packages.

## Table of Contents

<!--ts-->
 * [Data Understanding](https://github.com/howen7/Time-series-zillow#general-setup-instructions)
 * [Data Preparation](https://github.com/howen7/Time-series-zillow#Context)
 * [Modeling & Evaluation](https://github.com/howen7/Time-series-zillow#Definitions)
 * [Explosive Play Analysis](https://github.com/howen7/Time-series-zillow#Data)
 * [Presentation & Sources](https://github.com/howen7/Time-series-zillow#models-used--methodology)
<!--te-->

## Repository Navigation

```
.
├── README.md
|
├── environment.txt
|
├── notebooks
|   |__ DataFrame.ipynb
|   |__ EDA.ipynb
|   |__ Models.ipynb
|   |__ Pickle_Test.ipynb
|
├── reports
│   └── Presentation_deck
└── figures
    ├── data
    │   ├── zillow_data_lf.csv
    │   ├── zillow_data.csv
    │   └── zip_data.npy
    └── mymods.py
    

```

## Data Understanding
I used a package called nflfastR to source my data, which is based off of the nflscrapR package, but it speeds up the process of scraping new play-by-play data. This package was created so its users could analyze data from the National Football League API in a more reproducible way for the continued growth of football analytics. It allowed me to perform analysis on about 90,000 plays between the seasons of 2018 and 2020. Having chosen recent seasons to perform analysis on, I should be able to pick up on play calling trends to allow for better extrapolation into the future.

The play-by-play features that I felt would have most impact on a play being run or pass were things associated with how much time was left in the game or half, what down it was, the score of the game, the yards to gain for a first down or touchdown, how many timeouts a team had left, the winning probability before the snap, and the formation an offense lined up in.

## Data Preparation
Once I attained the initial dataset, I performed typical data preparation steps such as dropping NaN values and determining which features I deemed relevant for modeling and which ones were droppable. I then separated the regular season data from the postseason data, for in this context I was only concerned with predictablility in the regular season context. The next thing I did was create a column for my target variables of run/pass using the 'play_type' column. Once I had a target variable column created, the final thing I needed to check before the modeling process was the balance of my target variables. I determined that my pass plays outweighed my run plays by about 2:1, thus I used SMOTE to upsample my data when it came to the preprocessing steps before running models.

## Modeling & Evaluation
The models I chose to perform predictive analysis on included LogisticRegression, DecisionTrees, RandomForest, ExtraTrees, and K-Nearest Neighbors. I used cross validation for the evaluation process of my models and ultimately chose the ExtraTrees model based on its performance in F1 score and accuracy.

## Explosive Play Analysis
I performed additional analysis on a concept called explosive plays, which was created by a gentleman named Mike Eayrs in the 1970s and 1980s. I used his findings to create separate dataframes consisting of only 'explosive plays' from the years 2018 to 2020 to see if they showed correlations with wins and losses of a football team.

The original purpose of this concept of explosive plays was to give a coach a goal to shoot for in terms of yards gained in order to increase its probability of scoring on that drive. This information is very applicable to an offensive coordinator by giving them 'benchmarks' to hit, which should in turn influence their play calling to maximize scoring potential.

In order to create each dataframe for its respective year (2018-2020), I turned the 'game_date' column into a datetime object to simplify the grouping process. I proceeded to use the date as criteria for forming data dataframes of each season to find explosive plays on both offense and defense. The allowed me to find the NET explosive plays for each team which were plotted against the number of wins to see how they correlate.

## Future Improvements
I would like to continue my exploration using other models to see if I'm able to boost performance in cross validation metrics. Another goal is to perhaps seek out other feature combinations to optimize its performance.

I am currently learning how to work with Flask in order to deploy this model. My goal is to allow an individual the ability to plug in real-time features of a play and have my model predict whether it thinks the play will be a run or pass. This capability would be extremely useful in the context of coaching.

## Reproduction Instructions
#### Logos
I had issues with logos not being sized correctly on my visualizations. If you also run into this problem make sure to adjust logo sizes to your preference. I used a width of 1.39 to fix this issue.

## Presentation & Sources
 * [Presentation](https://github.com/howen7/Time-series-zillow#general-setup-instructions)
 
 * [Data Retrieval Using Python](https://gist.github.com/Deryck97/dff8d33e9f841568201a2a0d5519ac5e)
 * [Data Documentation](https://www.rdocumentation.org/packages/nflscrapR/versions/1.8.1/topics/scrape_json_play_by_play)
 * [Explosive Plays](https://thepowersweep.com/blog/how-explosive-plays-affect-the-packers-aaron-rodgers)
 
 * [README Image](https://www.google.com/url?sa=i&url=https%3A%2F%2Ftimclayton.photoshelter.com%2Fimage%2FI0000._zO6_SzdaA&psig=AOvVaw03X-RmgL2oQkZI6t_zc1-I&ust=1606322270096000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJDrs_jOm-0CFQAAAAAdAAAAABAO)
 
