import re

def extract_hashtags(text):
    pattern = r'#\w+'
    hashtags = re.findall(pattern, text)
    return hashtags

#text = 'Loving the new features in our product! #innovation #tech'
#print('Extracted hashtags:', extract_hashtags(text))

def remove_html_tags(text):
    pattern = r'<.*?>'
    return re.sub(pattern, '', text)

html_text = '<p>This is a <b>bold</b> paragraph.</p>'
#print('Text without HTML tags:', remove_html_tags(html_text))

def identify_sentiment(text):
    positive_pattern = r'\b(great|amazing|awesome|fantastic|good)\b'
    negative_pattern = r'\b(bad|terrible|awful|poor|worst)\b'

    positive_matches = re.findall(positive_pattern, text, re.IGNORECASE)
    negative_matches = re.findall(negative_pattern, text, re.IGNORECASE)

    if positive_matches:
        return 'Positive sentiment'
    elif negative_matches:
        return 'Negative sentiment'
    else:
        return 'Neutral sentiment'

text = 'The service was amazing and the product is fantastic!'
print('Sentiment:', identify_sentiment(text))

def normalize_whitespace(text):
    pattern = r'\s+'
    return re.sub(pattern, ' ', text)

text = 'This    is   a    text  with   irregular  spacing.'
#print('Normalized text:', normalize_whitespace(text))

def extract_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    emails = re.findall(pattern, text)
    return emails

text = 'Contact us at info@example.com or support@example.org.'
print('Extracted emails:', extract_emails(text))

def extract_urls(text):
    pattern = r'https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9._%-]*)*'
    urls = re.findall(pattern, text)
    return urls

text = 'Visit our website at https://example.com or follow us on http://twitter.com/example.'
print('Extracted URLs:', extract_urls(text))

def validate_dni(dni):
    pattern = r'^\d{8}[A-Z]$'
    if re.match(pattern, dni):
        return True
    else:
        return False

dni = '12345678A'
print('Valid DNI' if validate_dni(dni) else 'Invalid DNI')

def validate_phone(phone):
    pattern = r'^\+?1?\d{9,15}$'
    if re.match(pattern, phone):
        return True
    else:
        return False

phone = '01234567890'
print('Valid phone number' if validate_phone(phone) else 'Invalid phone number')

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email = 'user@example.com'
print('Valid email' if validate_email(email) else 'Invalid email')
