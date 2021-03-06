#this functions read in a list of
#[employee id, name, dob (year-month-day), ssn, state name]

#returns [employee id, first name, last name, dob (mm/dd/yyyy), ssn (***-**-1234), state abbrev.]

def convert_data(employee_data):

    emp_id = employee_data[0]
    name = employee_data[1]
    dob=employee_data[2]
    ssn=employee_data[3]
    state=employee_data[4]

    name_list= name.split()
    first_name = name_list[0]
    last_name = name_list[1]

    dob_list=dob.split("-")
    dob_conv=f'{dob_list[1]}/{dob_list[2]}/{dob_list[0]}'

    ssn_list=ssn.split("-")
    ssn_conv=f'***-**-{ssn_list[2]}'

    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }

    state_conv = us_state_abbrev[state]

    return_list = [emp_id, first_name, last_name, dob_conv, ssn_conv, state_conv]
    
    return return_list
