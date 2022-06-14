import numpy as np
#Monster Stat Functions

def monster_stat_gathering(soup, monster_dict):
    '''
    uses sub-functions to append a dictionary with each monster stat scraped from using 
    input:
            soup:  BeautifulSoup object parsed from XML data pulled from page source using Selenium
            monster_dict: an empty dictionary with just keys created in 1.0_ASI_Data_Scraping
    output:
            monster_dict: an appended dictionary cointaining all the scraped data from the BeautifulSoup XML data 
    '''

    stat_block = soup.find('div',{'class':'mon-stat-block'}) 
    tags = soup.find('footer')
    
    monster_name_gather(stat_block, monster_dict)
    
    monster_size_alignment_type_gather(stat_block, monster_dict)
    
    stat_gather(stat_block, monster_dict)

    monster_tidbit_gather(stat_block, monster_dict)
   
    ability_score_gather(stat_block, monster_dict)

    trait_gather(stat_block,monster_dict)

    action_type_gather(stat_block, monster_dict)

    tag_gather(tags, monster_dict)


def monster_name_gather(stat_block, monster_dict):
    '''
    append the monster_dict so to include the monster_name searched from the stat_block 

    input:
            stat_block: a portion of the beautiful soup object that was searched to contain "mon-stat-block"
            monster_dict: a monster dictionary that contains all the keys for each stats
    output:
            monster_dict: monster_dict that has the monster name key filled in.
    '''
    monster_name = stat_block.find('div', {'class':'mon-stat-block__name'}).text
    monster_dict['Monster Name'].append(' '.join(str(monster_name).split()))
    

def monster_size_alignment_type_gather(stat_block, monster_dict):
    '''
    Size, Alignment, and Type will split the single meta text using split() and replace() functions. 

    The function will find size and alignment, appending them into the monster dictionary.
    
    The sublist will remove Size and Alignment from the subtext, as well as the loose comma.

    It will also create a list for the type, as sometimes there are sub-types associated with monsters (e.g Titan)

    It will then append the monster dictionary for the type key.

    input:
            stat_block: a portion of the beautiful soup object that was searched to contain "mon-stat-block"
            monster_dict: a monster dictionary that contains all the keys for each stats

    output:
            monster_dict: an appended dictionary with the size, alignment, and type data filled in with a value
    '''

    monster_subinfo = stat_block.find('div', {'class':'mon-stat-block__meta'})
    monster_subinfo=monster_subinfo.text

    monster_size = monster_subinfo.split()[0]
    monster_dict['Size'].append(monster_size) 

    monster_alignment = monster_subinfo.split(', ')[-1]
    monster_dict['Alignment'].append(monster_alignment) 

    sub_list=(monster_size,monster_alignment, ', ')
    monster_type = monster_subinfo
    for substring in sub_list:
        monster_type = monster_type.replace(substring,'')
    monster_type=monster_type.split()
    monster_dict['Type'].append(monster_type) 


def monster_tidbit_gather(stat_block, monster_dict):
    '''
    Since the tidbits column changes based on the monster, we can't index the rows, as they are added or deleted based on the monster. 
    
    Instead, we will write a for-loop that iterates through the all possible monster tidbit headings (e.g. Skills, Saving Throws, etc.) and if they exist, it will take the sibling data (i.e. it will take the actual data corresponding to each heading) and deposit it into the dictionary. 
    
    Any heading not in the description will be given NaN values.

    input:
            stat_block: a portion of the beautiful soup object that was searched to contain "mon-stat-block"
            monster_dict: a monster dictionary that contains all the keys for each stats

    output:
            monster_dict: an appended dictionary with all the attribute data filled in with a value
    '''  
  #find all tidbit  metrics
    tidbit_label = stat_block.findAll('span', {'class':'mon-stat-block__tidbit-label'})
    tidbit_list = []
    for label in tidbit_label:    
        tidbit_list.append(label.text)
        if label.text == "Saving Throws":
            monster_saving_throw = ' '.join(str(label.find_next_sibling('span').text).split())
            monster_dict['Saving Throws'].append(monster_saving_throw)
        elif label.text == "Skills":
            monster_skills = ' '.join(str(label.find_next_sibling('span').text).split())
            monster_dict['Skills'].append(monster_skills)
        elif label.text == "Damage Vulnerabilities":    
            monster_damage_vulnerability = ' '.join(str(label.find_next_sibling('span').text).split())
            monster_dict['Damage Vulnerabilities'].append(monster_damage_vulnerability)
        elif label.text == "Damage Immunities":
            monster_damage_immunity = ' '.join(str(label.find_next_sibling('span').text).split())
            monster_dict['Damage Immunities'].append(monster_damage_immunity)
        elif label.text == 'Condition Immunities':
            monster_condition_immunity = ' '.join(str(label.find_next_sibling('span').text).split())
            monster_dict['Condition Immunities'].append(monster_condition_immunity)
        elif label.text == 'Senses':
            monster_senses = ' '.join(str(label.find_next_sibling('span').text).split())
            monster_dict['Senses'].append(monster_senses)
        elif label.text == 'Languages':
            monster_languages = ' '.join(str(label.find_next_sibling('span').text).split())
            monster_dict['Languages'].append(monster_languages)
        elif label.text == 'Challenge':
            monster_challenge= ' '.join(str(label.find_next_sibling('span').text).split())
            monster_dict['Challenge'].append(monster_challenge)
        elif label.text == 'Proficiency Bonus':
            monster_proficiency = ' '.join(str(label.find_next_sibling('span').text).split())
            monster_dict['Proficiency Bonus'].append(monster_proficiency)
        elif label.text == 'Damage Resistances':
            monster_damage_resistence = ' '.join(str(label.find_next_sibling('span').text).split())
            monster_dict['Damage Resistances'].append(monster_damage_resistence)

    #start with full list of tidbit, which will be removed for everyone that exists within the monster.
    missing_tidbit_list=["Saving Throws", "Skills", "Damage Vulnerabilities", "Damage Immunities", "Condition Immunities", "Senses", "Languages", "Challenge", "Proficiency Bonus", "Damage Resistances"]
    
    for tidbit in tidbit_list:
        missing_tidbit_list.remove(tidbit)

    #add NaN value to all missing tidbits for this monster
    for tidbit in missing_tidbit_list:
        monster_dict[tidbit].append(np.NaN)

def stat_gather(stat_block, monster_dict):
    '''
    append monster dictionary to include hit points, armor class, and speed

    input:
            stat_block: a portion of the beautiful soup object that was searched to contain "mon-stat-block"
            monster_dict: a monster dictionary that contains all the keys for each stats

    output:
            monster_dict: an appended dictionary with all the attribute data filled in with a value
    '''
    # find all attribute metrics
    attribute_data = stat_block.findAll('span',{'class':'mon-stat-block__attribute-data-value'})
    
    # Armor Class
    monster_ac = ' '.join(str(attribute_data[0].text).split())
    monster_dict['Armor Class'].append(monster_ac)
    # Hit Points
    monster_hp = ' '.join(str(attribute_data[1].text).split())
    monster_dict['Hit Points'].append(monster_hp)
    # Speed
    monster_speed = ' '.join(str(attribute_data[2].text).split())
    monster_dict['Speed'].append(monster_speed)


def ability_score_gather(stat_block, monster_dict):  
    '''
    append all ability scores into the monster dictionary at the respective key

    input:
            stat_block: a portion of the beautiful soup object that was searched to contain "mon-stat-block"
            monster_dict: a monster dictionary that contains all the keys for each stats

    output:
            monster_dict: an appended dictionary with all the ability scores filled in with a value 
    '''   
    #find all ability score metrics
    ability_scores = stat_block.findAll('span',{'class':'ability-block__score'})
        # STR Score
    monster_str = ability_scores[0].text
    monster_dict['STR'].append(monster_str)
        # DEX Score
    monster_dex = ability_scores[1].text
    monster_dict['DEX'].append(monster_dex)
        # CON Score
    monster_con = ability_scores[2].text
    monster_dict['CON'].append(monster_con)
        # INT Score
    monster_int = ability_scores[3].text
    monster_dict['INT'].append(monster_int)
        # WIS Score
    monster_wis = ability_scores[4].text
    monster_dict['WIS'].append(monster_wis)
        # CHA Score
    monster_cha = ability_scores[5].text
    monster_dict['CHA'].append(monster_cha) 


def trait_gather(stat_block,monster_dict):
    '''
    Since traits doesn't contain any defining HTML or any headings such as Actions or Legendary Actions. I searched through all the description blocks of the text. 
    
    If they don't contain the div 'heading' then we print. This allows us to only print the trait text and to place them in a list if need be for later wrangling and analysis. 

    Any heading not in the description will be given NaN values.

    This is appended into the monster dictionary for the trait key.

    input:
            stat_block: a portion of the beautiful soup object that was searched to contain "mon-stat-block"
            monster_dict: a monster dictionary that contains all the keys for each stats

    output:
            monster_dict: an appended dictionary with all the traits filled in with a list of traits
    '''

                 
    trait_list = []
    description_block = stat_block.findAll('div', {'class':'mon-stat-block__description-block'})
    for block in description_block:
         if not block.findAll('div',{'class':'mon-stat-block__description-block-heading'}):
            for p in block.findAll('p'):
                trait_list.append(p.text)
    #if no traits are found, create a NaN value
    if not trait_list:
        trait_list.append(np.NaN)
    monster_dict["Traits"].append(trait_list)


def action_type_gather(stat_block, monster_dict):
    '''
    Because the description section changes based on the monster, we can't index the rows, since action types are added or deleted based on the monster. 
        
    Instead, a for-loop will iterate through the monsters description headings (e.g. Actions, Legendary Actions, etc.) and if they exits, it will take the sibling data (i.e. it will take the actual data corresponding to each heading) and deposit it into the dictionary.

    Any heading not in the description will be given NaN values.

    These will be appended into the monster dictionary at their respective keys.

    input:
            stat_block: a portion of the beautiful soup object that was searched to contain "mon-stat-block"
            monster_dict: a monster dictionary that contains all the keys for each stats

    output:
            monster_dict: an appended dictionary with all the action types filled in with a value or a NaN where no value exists 
    '''
    #Remaining descriptions that had headings
    description_heading = stat_block.findAll('div', {'class':'mon-stat-block__description-block-heading'})
    action_list=[]
    action_headings=[]
    for heading in description_heading:    
        #create a list of heading actions to use for missing actions 
        action_headings.append(heading.text)

        action_list=[]
        if heading.text == "Actions":
            monster_actions = heading.find_next_sibling('div')
            for p in monster_actions.findAll('p'):
               action_list.append(p.text.strip())
            monster_dict['Actions'].append(action_list)
        elif heading.text == "Legendary Actions":
            monster_legendary_actions = heading.find_next_sibling('div')
            for p in monster_legendary_actions.findAll('p'):
               action_list.append(p.text.strip())
            monster_dict['Legendary Actions'].append(action_list)
        elif heading.text == "Mythic Actions":
            monster_mythic_actions = heading.find_next_sibling('div')
            for p in monster_mythic_actions.findAll('p'):
               action_list.append(p.text.strip())
            monster_dict['Mythic Actions'].append(action_list)
        elif heading.text == "Reactions":
            monster_reactions = heading.find_next_sibling('div')
            for p in monster_reactions.findAll('p'):
               action_list.append(p.text.strip())
            monster_dict['Reactions'].append(action_list)

#like tidbits, we will create the full list of actions, that we will subtract away from to find the missing action categories for NaN
    missing_actions_list = ["Actions", "Legendary Actions", "Mythic Actions", "Reactions"]

    for action in action_headings:
        missing_actions_list.remove(action)

    #add NaN value to all missing tidbits for this monster
    for action in missing_actions_list:
        monster_dict[action].append(np.NaN)

       
def tag_gather(tags, monster_dict):
    '''
    Append tags like environment, monster sub-type tag, or source book tag into the monster dictionary

    input:
            tags: a portion of the beautiful soup object that was searched to contain "footer" where the tags are contained
            monster_dict: a monster dictionary that contains all the keys for each stats

    output:
            monster_dict: an appended dictionary with all the tags filled in with a value or a NaN where no value exists 
    '''
    monster_env_list=[]
    monster_tag_list=[]
    for tag in tags.find_all("p"): 
        if (tag.contents[0].strip()) == "Environment:":
            monster_env = tag.findChildren("span",recursive=False)
            for span in monster_env:
                monster_env_list.append(span.text)
            monster_dict['Environment:'].append(monster_env_list)
        elif (tag.contents[0].strip()) == "Monster Tags:":
            monster_tag = tag.findChildren("span",recursive=False)
            for span in monster_tag:
                monster_tag_list.append(span.text)
            monster_dict['Monster Tags:'].append(monster_tag_list)
        else:
            monster_dict['Source'].append(tag.contents[0].strip())
    
    #this will find out if either the two tags are missing in this monster and replace the value with NaN
    monster_tags=[]
    missing_tags=['Environment:',"Monster Tags:"]
    
    for tag in tags.find_all("p",{'class':'tags'}):
        monster_tags.append(tag.contents[0].strip())

    for tag in monster_tags:
        missing_tags.remove(tag)
    
    for tag in missing_tags:
        monster_dict[tag].append(np.NaN)


