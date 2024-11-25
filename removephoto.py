import os


photo_path = 'https://github.com/studentAutomations/cs-aor1/blob/main/cs-aor1-nova-obavestenja.png' 


if os.path.exists(photo_path):
    os.remove(photo_path)  
