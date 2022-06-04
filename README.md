DnD_Monsters
==============================

Scrapping DnD Monsters for EDL and ML insights

Project Organization
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

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
