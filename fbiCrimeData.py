from urllib.request import urlopen
import json
import pandas as pd

#######################CRIME DATA#######################
# FBI DATA api key
API_KEY = "YsQEzTwMdMPRymtS4Fp7XYFBQmT5A6kSe62h5laI"

# assult category
all_categories_string = "aggravated-assault,all-other-larceny,all-other-offenses,animal-cruelty,arson,assisting-or-promoting-prostitution,bad-checks,betting,bribery,burglary-breaking-and-entering,counterfeiting-forgery,credit-card-automated-teller-machine-fraud,destruction-damage-vandalism-of-property,driving-under-the-influence,drug-equipment-violations,drug-violations,drunkenness,embezzlement,extortion-blackmail,false-pretenses-swindle-confidence-game,fondling,gambling-equipment-violation,hacking-computer-invasion,human-trafficking-commerical-sex-acts,human-trafficking-commerical-involuntary-servitude,identity-theft,impersonation,incest,intimidation,justifiable-homicide,kidnapping-abduction,motor-vehicle-theft,murder-and-nonnegligent-manslaughter,negligent-manslaughter,operating-promoting-assiting-gambling,curfew-loitering-vagrancy-violations,peeping-tom,pocket-picking,pornography-obscence-material,prostitution,purchasing-prostitution,purse-snatching,rape,robbery,sexual-assult-with-an-object,sex-offenses-non-forcible,shoplifting,simple-assault,sodomy,sports-tampering,statutory-rape,stolen-property-offenses,theft-from-building,theft-from-coin-operated-machine-or-device,theft-from-motor-vehicle,theft-of-motor-vehicle-parts-or-accessories,theft-from-motor-vehicle,weapon-law-violation,welfare-fraud,wire-fraud,not-specified,liquor-law-violations,crime-against-person,crime-against-property,crime-against-society,assault-offenses,homicide-offenses,human-trafficking-offenses,sex-offenses,sex-offenses-non-forcible, fraud-offenses,larceny-theft-offenses, drugs-narcotic-offenses,gambling-offenses,prostitution-offenses,all-offenses"
all_categories = [s.strip() for s in all_categories_string.split(",")]
selected_categories = all_categories[0:15]


# all states
all_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
              'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND',
              'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


categories_of_interest = ['murder-and-nonnegligent-manslaughter', 'rape', 'robbery', 'drug-violations']
def getCrimeDataOfInterest(assult_category, state):
    state_data_link = "https://api.usa.gov/crime/fbi/sapi/api/data/nibrs/" + categories_of_interest[
        assult_category] + "/victim/states/" + all_states[state] + "/count?API_KEY=" + API_KEY
    response = urlopen(state_data_link)
    if response is None:
        return pd.DataFrame(columns=['count', 'data_year'])
    else:
        data_json = json.loads(response.read())
        crimedf = pd.DataFrame(data_json["results"])
        return crimedf