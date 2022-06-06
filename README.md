DnD_Monsters
==============================

## Business Case
In 1974, Dungeons and Dragons was created by designers Gary Gygax and David Arneson. While I wasn’t alive, I can certainly guarantee some of the same problems that are discussed in the realm of DnD today, were discussed around the tables then as well. One of these issues, is the Dungeon Master’s (DM) struggle to create the perfectly balanced encounter. 

This issue has certainly come a long way. In the 1st and 2nd editions, DM’s had to decide just based on the stats of the monster as well as the experience, if these monsters could put up an adequate fight for the party level in question. In the 3rd edition, we received something known as the Challenge Rating (CR) and Encounter Levels (EL). This system was by no means perfect, but essentially monsters were given a number and the aggregate of the monsters in your fight should consume 20% of a party’s daily resources. In 4th edition, we moved into Encounter Levels and daily experience budgets. In 5e, Wizards of the Coast took us back to Challenge Ratings, but this time with a much more streamlined system.

All of this however assumes that the Dungeon Master only uses the 2,460 monsters that have been created through the 5e source books. While that looks like quite a bit of monsters, an inexperienced DM may not have access to all the books, and even further, those monsters span 20 player levels. If we are a brand new DM, we many only have access to around 300 monsters from the System Reference Document (SRD). Over 20 levels, that isn’t much variation. With a game that has always been about the freedom, exploration, and creativity of it’s players, you can almost guarantee DMs will want to create their own monstrosities. 

Luckly, Wizards of the Coast has always known this. Even in 3.5e, they provided a way for Dungeons Masters to become their own Dr. Frankensteins! This system has since been streamlined and in 5e Wizards of the Coast has brought us a Challenge Rating equation! A simple way to use hit points, armor class, attack bonus, and attack damage per round to start molding your own monster for whatever level you choose! Unfortunately, this process still takes a bit of effort and many DMs have even said it doesn’t provide the results they hoped for. 

I don’t know that we will ever get to a place that is both simple and all-encompasing for monster creation. That is because, to be honest, a lot of balancing an encounter does fall onto the DM, and a lot of it isn’t even monster related. What kind of resources do the players have left for the day? Are there any environmental hazards in this fight? Is there a secondary or primary goal other than kill the monster that the party will focus on? Is there a single monster, a boss with minions, or several semi-boss level characters to worry about? Not to mention…the rolls, one good or bad roll on either side could mean a huge swing in the favor of the monster or the players. These questions and others will sway the battle difficulty without even considering the level of the monster. This is why encounter building is considered such a nuanced art for DMs.
Frankly, I don’t know that it will ever be possible to create the perfect system for choosing monsters for players. There is so much variance just from table to table, that I believe you would have to restrict the game a considerable amount in order for something consistent to appear. And that certainly is not in the spirit of Dungeons and Dragons.
With all that being said, I am still curious if there is an easier way for dungeons masters to create a monster stat block on the fly. One that may be more in line with the monsters from our manual. While it may not be perfect, it may eventually allow us to create something very quickly that we can then spend time tweaking and turning into a beautiful encounter. Rather than spending the time trying to create the monster itself.
To that end, this project focused on three major questions:
1. How different is the Challenge Rating when used to calculate the CR of Monster Manual Monsters?
2. How does the monster’s non-stat oriented categories (type, environment, size, alignment) impact its stats?
3. Can we predict a monster stat block for inexperienced DMs that resembles SRC monsters?

## Table of Contents
<details open>
  <summary>Show/Hide</summary>
  <br>
  
1. [ File Descriptions ](#File_Description)
2. [ Technologies Used ](#Technologies_Used)    
3. [ Structure ](#Structure)
4. [ Evaluation ](#Evaluation)
5. [ Future Improvements ](#Future_Improvements)
</details>


## Project Organization

<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
 <br>
 ------------

    ├── LICENSE
    ├── .gitignore
    ├── README.md          <- The top-level README for developers using this project.
    ├──
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── deployment         <- Folder that contains all deployment needs
    │   ├── venv           <- Virtual Environment for just app deployment
    │   ├── app.py         <- Dashboard used to show off the model
    │   ├── monster_generator.h5         <- built final model
    │   ├── requirements.txt             <- library requirements for app to run
    │   ├── Dockerfile     <- containerize the app
    │   └── lc.json        <- Used in AWS lightsail
    │
    ├── env                <- Virtual Environment for the project
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        |   ├── selenium_scrape.py
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make              
        │   |                 predictions
        │   └── test_model.py    
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations

--------
  </details>   

## Technologies Used:
<details>
<a name="Technologies_Used"></a>
<summary>Show/Hide</summary>
<br>

 </details>

## Structure of Notebooks:
<details>
<a name="Structure"></a>
<summary>Show/Hide</summary>
<br>

 </details>

## Evaluation:
<a name="Evaluation"></a>
<details>
<summary>Show/Hide</summary>
<br>

</details>
  
## Future Improvements
 <a name="Future_Improvements"></a>
 <details>
<summary>Show/Hide</summary>
<br>
While I was able to create a deployed app for our model, it’s far from complete. Moving forward there will need to be a lot more testing, refining, and features built out to make this a stable and usable app for Dungeon Masters. The first step will be, using this app, discussing with other Dungeon Masters how useful this tool is to them and what kind of improvements they would like to see. <br>
From there, I can already see the following will need to be addressed:<br>
1. Fine tunning model further. I would like the stats to reflect the monster type shape more consistently
2. Finding a way to incorporate spells and spell damage into the inputs and/or outputs
3. Allow for more variety in inputs (spellcaster, player character magic items, flying traits)
4. Increase the number of traits available in output
5. Upgrade the UI of the model 

</details>

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
<p>README outline tailored from [awesomeahi95][]<p>
