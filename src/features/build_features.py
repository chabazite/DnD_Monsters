def monster_stat_gathering(soup):

    stat_block = soup.find('div',{'class':'mon-stat-block'}) 
    tags = soup.find('footer')

    # Monster Name
    monster_name = stat_block.find('div', {'class':'mon-stat-block__name'}).text
    monster_dict['Monster Name'].append(' '.join(str(monster_name).split())) 
    
    
    #This next set (Size,Alignment, and Type) will split the single meta text using split() and replace() functions
    monster_subinfo = stat_block.find('div', {'class':'mon-stat-block__meta'})
    monster_subinfo=monster_subinfo.text
    
    # Size (first word)
    monster_size = monster_subinfo.split()[0]
    monster_dict['Size'].append(monster_size) 
    # Alignment (after comma)
    monster_alignment = monster_subinfo.split(', ')[-1]
    monster_dict['Alignment'].append(monster_alignment) 
    # Type (remaining words). The sublist will remove the above two variables from the text, as well as the loose comma.
    #It will also create a list for the type, as sometimes there are sub-types associated with monsters (e.g Titan)
    sub_list=(monster_size,monster_alignment, ', ')
    monster_type = monster_subinfo
    for substring in sub_list:
        monster_type = monster_type.replace(substring,'')
    monster_type=monster_type.split()
    monster_dict['Type'].append(monster_type) 
    
    
    #find all attribute metrics
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
    
    
    #find all tidbit  metrics
    tidbit_label = stat_block.findAll('span', {'class':'mon-stat-block__tidbit-label'})
    
    for label in tidbit_label:    
        '''
        Because the tidbits column shifts based on the monster, we can't index the rows, as they
        are added or deleted based on the monster. So instead, we will write a for loop that loops through 
        the monsters tidbit headings (e.g. Skills, Saving Throws, etc.) and if they exits, it will take
        the sibling data (i.e. it will take the actual data corresponding to each heading) and deposit it into the dictionary.
        Any columns not in the monster data will be left blank for now. Each if statement is labeled with the corresponding tidbit.
        '''
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
        elif label.text == 'Damage Resistences':
            monster_damage_resistence = ' '.join(str(label.find_next_sibling('span').text).split())
            monster_dict['Damage Resistences'].append(monster_damage_resistence)
    
    
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
        
    # Traits: because traits doesn't contain any defining HTML or any headings such as Actions or Legendary Actions
    # I searched through all the description blocks of the text. If they don't contain the div 'heading' then we print
    # This allows us to only print the traits and to place them in a list if need be for later wrangling and analysis. 
                 
    trait_list = []
    description_block = stat_block.findAll('div', {'class':'mon-stat-block__description-block'})
    for block in description_block:
         if not block.findAll('div',{'class':'mon-stat-block__description-block-heading'}):
            for p in block.findAll('p'):
                trait_list.append(p.text)
    
    #Remaining descriptions that had headings
    description_heading = stat_block.findAll('div', {'class':'mon-stat-block__description-block-heading'})
    action_list=[]
    for heading in description_heading:    
        '''
        Because the description column shifts based on the monster, we can't index the rows, as they
        are added or deleted based on the monster. So instead, we will write a for loop that loops through 
        the monsters description headings (e.g. Actions, Legendary Actions, etc.) and if they exits, it will take
        the sibling data (i.e. it will take the actual data corresponding to each heading) and deposit it into the dictionary.
        Any columns not in the monster data will be left blank for now. Each if statement is labeled with the corresponding tidbit.
        '''
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
             
    #These final traits are either referring to the environment it lives in (can be multiple), the sub type its classified as,
    # or the source book it came from. all of these or none of these may be represented in the monster sheet.
    monster_tags = tags.findAll('span') 
    
    for tag in tags.find_all("p"):
           
        if (tag.contents[0].strip()) == "Environment:":
           monster_dict['Environment:'].append(monster_tags[0].text)
        elif (tag.contents[0].strip()) == "Monster Tags:":
            monster_dict['Monster Tags'].append(monster_tags[1].text)
        else:
            monster_dict['Source'].append(tag.contents[0].strip())
    