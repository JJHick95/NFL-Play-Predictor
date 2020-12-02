# NFL Play Predictor

![alt text](/figures/football_field.jpg)

## Business Understanding
Knowing what the next play is in any sport would be a huge advantage. The question I want to explore is whether or not data can accurately provide the defense with this advantage in the game of football.

With the help of machine learning, I've created a model that takes in play-by-play data before the snap occurs and predicts whether that play will be a run or pass. My hope is that this information can be beneficial to coaching staffs in the NFL when it comes to game preparation and live play calling.

## Table of Contents

<!--ts-->
 * [Data Understanding](https://github.com/JJHick95/NFL-Play-Predictor#Data-Understanding)
 * [Data Preparation](https://github.com/JJHick95/NFL-Play-Predictor#Data-Preparation)
 * [Modeling & Evaluation](https://github.com/JJHick95/NFL-Play-Predictor#Modeling-and-Evaluation)
 * [Explosive Play Analysis](https://github.com/JJHick95/NFL-Play-Predictor#Explosive-Play-Analysis)
 * [Presentation & Sources](https://github.com/JJHick95/NFL-Play-Predictor#Presentation-and-Sources)
<!--te-->

## Repository Navigation

```
.
├── README.md
├── requirements.txt
|__ .gitignore
|
├── notebooks
|   |__ DataFrame.ipynb
|   |__ EDA.ipynb
|   |__ Models.ipynb
|   |__ Pickle_Test.ipynb
|
├── reports
│   |── Presentation.pdf
|   |__ Capstone_Final_Notebook.ipynb
|
|-- deployment_material
|   |__ src
|   |   |__utils.py
|   |   |__ models
|   |       |__ final_pipeline.p
|   |       |__ predictor.py
|   |
|   |__ static
|   |   |__ index.html
|   |   |__ bootstrap.min.css
|   |   |__ football_field.jpg
|   |   |__ handoff.jpg
|   |   |__ pass.jpg
|   |
|   |__ templates
|   |   |__ results.html
|   |
|   |__ app.py
|
|
└── figures
    |__ football_field.jpg
    
```

## Data Understanding
I used a package called nflfastR to source my data, which is based off of the nflscrapR package, but it speeds up the process of scraping new play-by-play data. This package was created so its users could analyze data from the National Football League API in a more reproducible way for the continued growth of football analytics. It allowed me to perform analysis on roughly 90,000 plays from 2018 to 2020. Having chosen recent seasons to perform analysis on, I should be able to pick up on play calling trends to allow for better extrapolation into the future.

The play-by-play features that I felt would have most impact on a play being run or pass were things associated with how much time was left in the game or half, what down it was, the score of the game, the yards to gain for a first down or touchdown, how many timeouts a team had left, the winning probability before the snap occurred, and the formation an offense lined up in.

The reason I chose these features was due to the strategic approach many coaches take in certain game scenarios. In the rules of football, incomplete passes will stop the game clock and running the football keeps the clock moving unless the running back is forced out of bounds. Many coaches use this rule in a way that is beneficial to their team, as they should. For example, if your team is losing and there isn’t much time left, most coaches won’t want to run the football and risk letting the clock continue to tick away, as they are trying to preserve time and move the football in large chunks of yards in order to score. Vice versa, if you your team is winning by a large margin and there’s still a decent amount of time left, a coach might make the executive decision to change the play script and run the football, so the clock keeps moving.

## Data Preparation
Once I attained the initial dataset, I performed typical data preparation steps such as dropping NaN values and determining which features I deemed relevant for modeling and which ones were droppable. I then separated the regular season data from the postseason data, for in this context I was only concerned with predictablility in the regular season. The next thing I did was create a column for my target variables of run/pass using the 'play_type' column. Once I had a target variable column created, the final thing I needed to check before the modeling process was the balance of my target variables. I determined that my pass plays outweighed my run plays by about 2:1, thus I used SMOTE to create additional sythetic data points for the run play group to balance them out.

## Explosive Play Analysis
I performed additional analysis on a concept called explosive plays, which was created by Mike Eayrs in the 1970s and 1980s. I used his findings to create separate dataframes consisting of only 'explosive plays' from the years 2018 to 2020 to see if they showed correlations with wins and losses of a football team.

The original purpose of this concept of explosive plays was to give a coach a goal to shoot for in terms of yards gained in order to increase its probability of scoring on that drive. This information is very applicable to an offensive coordinator by giving them 'benchmarks' to hit, which should in turn influence their play calling to maximize scoring potential.

In order to create each dataframe for its respective year (2018-2020), I turned the 'game_date' column into a datetime object to simplify the grouping process. I proceeded to use the date as criteria for forming these dataframes of each season to find explosive plays on both offense and defense. This allowed me to come up with the NET explosive plays for each team which were then plotted against the number of wins a team had.

## Modeling and Evaluation
The models I chose to perform predictive analysis on included LogisticRegression, DecisionTrees, RandomForest, ExtraTrees, and K-Nearest Neighbors. I used cross validation for the evaluation process and ultimately chose the ExtraTrees model based on its performance in recall score.

I chose recall score as my metric because I believe its more detrimental to falsely predict a run play than a pass play, as more explosive plays occured in the air vs on the ground. We should want to minimize these false negative predictions so our defense isn't caught with run play personnel on the field when it needs pass play personnel, or they've decided to call a blitz when they actually need to be in prevent defense.

## Future Improvements
I would like to continue exploring other models and feature combinations to see if I'm able to boost performance in cross validation metrics.

I would like to complete the live deployment process of my ExtraTrees model on the web, as it currently runs in a developmental environment. My goal is to allow an individual the ability to plug in real-time features of a play and have my model predict whether it thinks the play will be a run or pass. Providing this capability to a coach would be an extremely useful addition and might even become how coaching is done in the future.

## Reproduction Instructions
Ensure that you have installed [Anaconda](https://docs.anaconda.com/anaconda/install/)

This project relies on you using the [`requirements.txt`](requirements.txt) file to recreate the NFL Predictor. To do so, please run the following commands in your terminal:
```bash
# using pip
pip install -r requirements.txt

# using Conda
conda create --name <env_name> --file requirements.txt
```
#### Logos
I had issues with logos not being sized correctly on my visualizations. If you also run into this problem make sure to adjust logo sizes to your preference. I used a width of 1.39 to fix this issue.

## Presentation and Sources
 * [Presentation](/reports/Presentation.pdf)
 * [Final Notebook](/reports/Capstone_Final_Notebook.pdf)
 
 * [Data Retrieval Using Python](https://gist.github.com/Deryck97/dff8d33e9f841568201a2a0d5519ac5e)
 * [Data Documentation](https://www.rdocumentation.org/packages/nflscrapR/versions/1.8.1/topics/scrape_json_play_by_play)
 * [Explosive Plays](https://thepowersweep.com/blog/how-explosive-plays-affect-the-packers-aaron-rodgers)
 
 * [README Image](https://www.google.com/url?sa=i&url=https%3A%2F%2Ftimclayton.photoshelter.com%2Fimage%2FI0000._zO6_SzdaA&psig=AOvVaw03X-RmgL2oQkZI6t_zc1-I&ust=1606322270096000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJDrs_jOm-0CFQAAAAAdAAAAABAO)
 
