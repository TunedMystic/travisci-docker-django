'''
The 'patterns' dictionary is used to store regex fragments that
are commonly used across url definitions.

Only raw strings should be stored (no compiled regex patterns).
'''

patterns = {
    'uuid': r'[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}'
}
